-- Database Schema Template
-- Database: PostgreSQL 14+
-- Created: YYYY-MM-DD
-- Description: [Brief description of the schema purpose]

-- Enable necessary extensions
CREATE EXTENSION IF NOT EXISTS "uuid-ossp";
CREATE EXTENSION IF NOT EXISTS "pg_trgm";  -- For fuzzy text search

-- =============================================================================
-- DROP TABLES (for development/reset only - comment out for production)
-- =============================================================================

-- DROP TABLE IF EXISTS table_name CASCADE;

-- =============================================================================
-- TABLES
-- =============================================================================

-- Users table
CREATE TABLE users (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    email VARCHAR(255) UNIQUE NOT NULL,
    name VARCHAR(100) NOT NULL,
    password_hash VARCHAR(255) NOT NULL,
    role VARCHAR(20) NOT NULL DEFAULT 'user' CHECK (role IN ('admin', 'user', 'guest')),
    is_active BOOLEAN DEFAULT TRUE,
    email_verified BOOLEAN DEFAULT FALSE,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    deleted_at TIMESTAMP WITH TIME ZONE  -- Soft delete
);

COMMENT ON TABLE users IS 'User accounts and authentication';
COMMENT ON COLUMN users.password_hash IS 'Bcrypt hashed password';
COMMENT ON COLUMN users.deleted_at IS 'Soft delete timestamp (NULL = not deleted)';

-- Posts table (example of one-to-many relationship)
CREATE TABLE posts (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    user_id UUID NOT NULL REFERENCES users(id) ON DELETE CASCADE,
    title VARCHAR(255) NOT NULL,
    slug VARCHAR(255) UNIQUE NOT NULL,
    content TEXT NOT NULL,
    excerpt VARCHAR(500),
    status VARCHAR(20) NOT NULL DEFAULT 'draft' CHECK (status IN ('draft', 'published', 'archived')),
    published_at TIMESTAMP WITH TIME ZONE,
    view_count INTEGER DEFAULT 0,
    metadata JSONB,  -- Flexible additional data
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    deleted_at TIMESTAMP WITH TIME ZONE
);

COMMENT ON TABLE posts IS 'Blog posts or articles';
COMMENT ON COLUMN posts.metadata IS 'JSON metadata (tags, categories, custom fields)';

-- Comments table (example of nested data)
CREATE TABLE comments (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    post_id UUID NOT NULL REFERENCES posts(id) ON DELETE CASCADE,
    user_id UUID NOT NULL REFERENCES users(id) ON DELETE CASCADE,
    parent_id UUID REFERENCES comments(id) ON DELETE CASCADE,  -- For nested comments
    content TEXT NOT NULL,
    is_approved BOOLEAN DEFAULT FALSE,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    deleted_at TIMESTAMP WITH TIME ZONE
);

COMMENT ON TABLE comments IS 'User comments on posts';
COMMENT ON COLUMN comments.parent_id IS 'Parent comment ID for nested/threaded comments';

-- Tags table
CREATE TABLE tags (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    name VARCHAR(50) UNIQUE NOT NULL,
    slug VARCHAR(50) UNIQUE NOT NULL,
    description TEXT,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

COMMENT ON TABLE tags IS 'Content tags or categories';

-- Post tags junction table (many-to-many)
CREATE TABLE post_tags (
    post_id UUID NOT NULL REFERENCES posts(id) ON DELETE CASCADE,
    tag_id UUID NOT NULL REFERENCES tags(id) ON DELETE CASCADE,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY (post_id, tag_id)
);

COMMENT ON TABLE post_tags IS 'Many-to-many relationship between posts and tags';

-- =============================================================================
-- INDEXES
-- =============================================================================

-- Users indexes
CREATE INDEX idx_users_email ON users(email);
CREATE INDEX idx_users_role ON users(role) WHERE deleted_at IS NULL;
CREATE INDEX idx_users_created_at ON users(created_at DESC);
CREATE INDEX idx_users_deleted_at ON users(deleted_at) WHERE deleted_at IS NOT NULL;

-- Posts indexes
CREATE INDEX idx_posts_user_id ON posts(user_id);
CREATE INDEX idx_posts_status ON posts(status) WHERE deleted_at IS NULL;
CREATE INDEX idx_posts_published_at ON posts(published_at DESC) WHERE status = 'published' AND deleted_at IS NULL;
CREATE INDEX idx_posts_slug ON posts(slug) WHERE deleted_at IS NULL;
CREATE INDEX idx_posts_created_at ON posts(created_at DESC);

-- Full-text search index on posts
CREATE INDEX idx_posts_search ON posts USING GIN (to_tsvector('english', title || ' ' || content));

-- JSONB index on metadata
CREATE INDEX idx_posts_metadata ON posts USING GIN (metadata);

-- Comments indexes
CREATE INDEX idx_comments_post_id ON comments(post_id) WHERE deleted_at IS NULL;
CREATE INDEX idx_comments_user_id ON comments(user_id) WHERE deleted_at IS NULL;
CREATE INDEX idx_comments_parent_id ON comments(parent_id) WHERE parent_id IS NOT NULL;
CREATE INDEX idx_comments_created_at ON comments(created_at DESC);

-- Tags indexes
CREATE INDEX idx_tags_slug ON tags(slug);
CREATE INDEX idx_tags_name ON tags USING GIN (name gin_trgm_ops);  -- Fuzzy search

-- Post tags indexes
CREATE INDEX idx_post_tags_tag_id ON post_tags(tag_id);
CREATE INDEX idx_post_tags_created_at ON post_tags(created_at);

-- =============================================================================
-- TRIGGERS
-- =============================================================================

-- Auto-update updated_at timestamp
CREATE OR REPLACE FUNCTION update_updated_at_column()
RETURNS TRIGGER AS $$
BEGIN
    NEW.updated_at = CURRENT_TIMESTAMP;
    RETURN NEW;
END;
$$ language 'plpgsql';

CREATE TRIGGER update_users_updated_at
    BEFORE UPDATE ON users
    FOR EACH ROW
    EXECUTE FUNCTION update_updated_at_column();

CREATE TRIGGER update_posts_updated_at
    BEFORE UPDATE ON posts
    FOR EACH ROW
    EXECUTE FUNCTION update_updated_at_column();

CREATE TRIGGER update_comments_updated_at
    BEFORE UPDATE ON comments
    FOR EACH ROW
    EXECUTE FUNCTION update_updated_at_column();

-- =============================================================================
-- FUNCTIONS
-- =============================================================================

-- Example: Increment post view count
CREATE OR REPLACE FUNCTION increment_post_views(post_uuid UUID)
RETURNS VOID AS $$
BEGIN
    UPDATE posts
    SET view_count = view_count + 1
    WHERE id = post_uuid AND deleted_at IS NULL;
END;
$$ LANGUAGE plpgsql;

-- Example: Get post with author details
CREATE OR REPLACE FUNCTION get_post_with_author(post_uuid UUID)
RETURNS TABLE (
    post_id UUID,
    post_title VARCHAR,
    post_content TEXT,
    author_name VARCHAR,
    author_email VARCHAR
) AS $$
BEGIN
    RETURN QUERY
    SELECT
        p.id,
        p.title,
        p.content,
        u.name,
        u.email
    FROM posts p
    JOIN users u ON p.user_id = u.id
    WHERE p.id = post_uuid
      AND p.deleted_at IS NULL
      AND u.deleted_at IS NULL;
END;
$$ LANGUAGE plpgsql;

-- =============================================================================
-- VIEWS
-- =============================================================================

-- Example: Published posts with author info
CREATE OR REPLACE VIEW published_posts AS
SELECT
    p.id,
    p.title,
    p.slug,
    p.excerpt,
    p.published_at,
    p.view_count,
    u.name as author_name,
    u.email as author_email,
    COUNT(c.id) as comment_count
FROM posts p
JOIN users u ON p.user_id = u.id
LEFT JOIN comments c ON c.post_id = p.id AND c.deleted_at IS NULL
WHERE p.status = 'published'
  AND p.deleted_at IS NULL
  AND u.deleted_at IS NULL
GROUP BY p.id, u.name, u.email;

COMMENT ON VIEW published_posts IS 'Published posts with author and comment counts';

-- =============================================================================
-- SEED DATA (for development/testing)
-- =============================================================================

-- Insert sample users
INSERT INTO users (email, name, password_hash, role, email_verified) VALUES
    ('admin@example.com', 'Admin User', '$2b$12$...', 'admin', TRUE),
    ('user@example.com', 'Regular User', '$2b$12$...', 'user', TRUE),
    ('guest@example.com', 'Guest User', '$2b$12$...', 'guest', FALSE)
ON CONFLICT (email) DO NOTHING;

-- Insert sample tags
INSERT INTO tags (name, slug, description) VALUES
    ('Technology', 'technology', 'Technology related posts'),
    ('Tutorial', 'tutorial', 'How-to guides and tutorials'),
    ('News', 'news', 'Latest news and updates')
ON CONFLICT (slug) DO NOTHING;

-- =============================================================================
-- GRANTS (adjust based on your user setup)
-- =============================================================================

-- Example: Grant permissions to application user
-- GRANT SELECT, INSERT, UPDATE, DELETE ON ALL TABLES IN SCHEMA public TO app_user;
-- GRANT USAGE, SELECT ON ALL SEQUENCES IN SCHEMA public TO app_user;

-- =============================================================================
-- ANALYTICS / MONITORING
-- =============================================================================

-- Check table sizes
-- SELECT
--     schemaname,
--     tablename,
--     pg_size_pretty(pg_total_relation_size(schemaname||'.'||tablename)) AS size,
--     pg_total_relation_size(schemaname||'.'||tablename) AS size_bytes
-- FROM pg_tables
-- WHERE schemaname = 'public'
-- ORDER BY size_bytes DESC;

-- Check index usage
-- SELECT
--     schemaname,
--     tablename,
--     indexname,
--     idx_scan,
--     pg_size_pretty(pg_relation_size(indexrelid)) AS size
-- FROM pg_stat_user_indexes
-- ORDER BY idx_scan ASC;
