# Technical Writing Skill

Comprehensive knowledge of technical writing principles, documentation types, structure, style, and best practices for creating clear, concise, and user-friendly technical content.

## Writing Principles

### Clarity and Conciseness

**Core Principle**: Say exactly what you mean, using as few words as necessary.

**Clarity Techniques**

1. **Use Simple Words**
   - ✅ "use" instead of "utilize"
   - ✅ "help" instead of "facilitate"
   - ✅ "end" instead of "terminate"
   - ✅ "before" instead of "prior to"
   - ✅ "about" instead of "approximately"

2. **Avoid Jargon (Unless Necessary)**
   - Define technical terms on first use
   - Provide context for abbreviations
   - Use glossaries for specialized terminology
   - Consider your audience's expertise level

3. **Be Specific**
   - ❌ "The process takes a while"
   - ✅ "The process takes 5-10 minutes"
   - ❌ "Click the button"
   - ✅ "Click the Submit button"
   - ❌ "The file is large"
   - ✅ "The file is 250 MB"

4. **One Idea Per Sentence**
   - ❌ "Click Save to save your changes and then click Exit to close the window, or you can click Cancel to discard changes."
   - ✅ "To save your changes, click Save. To close the window, click Exit. To discard changes, click Cancel."

5. **Short Sentences**
   - Aim for 15-20 words per sentence on average
   - Break complex sentences into multiple simple ones
   - Use bullet points for lists of items
   - Vary sentence length for readability

**Conciseness Techniques**

1. **Eliminate Redundancy**
   - ❌ "completely eliminate" → ✅ "eliminate"
   - ❌ "advance planning" → ✅ "planning"
   - ❌ "end result" → ✅ "result"
   - ❌ "past history" → ✅ "history"
   - ❌ "repeat again" → ✅ "repeat"

2. **Remove Filler Words**
   - ❌ "in order to" → ✅ "to"
   - ❌ "due to the fact that" → ✅ "because"
   - ❌ "at this point in time" → ✅ "now"
   - ❌ "for the purpose of" → ✅ "to"
   - ❌ "in the event that" → ✅ "if"

3. **Cut Unnecessary Phrases**
   - ❌ "It should be noted that..."
   - ❌ "As previously mentioned..."
   - ❌ "For all intents and purposes..."
   - ❌ "The fact of the matter is..."
   - ❌ "Needless to say..."

4. **Direct Expression**
   - ❌ "There is a function that allows you to..."
   - ✅ "You can..."
   - ❌ "It is possible to configure the system to..."
   - ✅ "You can configure the system to..."

### Active Voice vs Passive Voice

**Active Voice**: Subject performs the action (Subject + Verb + Object)
**Passive Voice**: Subject receives the action (Object + Verb + by Subject)

**When to Use Active Voice** (Preferred 90% of time)

1. **Clarity and Directness**
   - ❌ Passive: "The file was saved by the user"
   - ✅ Active: "The user saved the file"
   - ❌ Passive: "An error message is displayed by the system"
   - ✅ Active: "The system displays an error message"

2. **Instructions and Procedures**
   - ❌ Passive: "The configuration file should be edited"
   - ✅ Active: "Edit the configuration file"
   - ❌ Passive: "The button must be clicked"
   - ✅ Active: "Click the button"

3. **Responsibilities**
   - ❌ Passive: "The API key must be kept secure"
   - ✅ Active: "Keep your API key secure"
   - ❌ Passive: "Backups should be performed daily"
   - ✅ Active: "Perform backups daily"

**When to Use Passive Voice** (Strategic use)

1. **When Actor is Unknown or Irrelevant**
   - ✅ "The file was corrupted during transmission"
   - ✅ "The data was lost"
   - ✅ "The server was compromised"

2. **To Emphasize the Object**
   - ✅ "Your password is encrypted with AES-256"
   - ✅ "All transactions are logged for audit purposes"

3. **To Soften Blame or Criticism**
   - ✅ "An error was made in the configuration"
   - ✅ "The deadline was missed"

4. **Technical Descriptions**
   - ✅ "The data is stored in JSON format"
   - ✅ "Requests are processed asynchronously"

**Identifying Passive Voice**
- Look for "to be" verb + past participle (is done, was created, will be sent)
- Check if you can add "by zombies" after the verb (if it makes sense, it's passive)

### Parallel Structure

**Principle**: Items in a list or series should have the same grammatical structure.

**Lists and Bullet Points**

1. **Parallel Verbs**
   - ❌ Mixed structure:
     * Install the software
     * Configuration of settings
     * The database needs to be initialized

   - ✅ Parallel structure:
     * Install the software
     * Configure the settings
     * Initialize the database

2. **Parallel Nouns**
   - ❌ Mixed structure:
     * Speed
     * Being reliable
     * How secure it is

   - ✅ Parallel structure:
     * Speed
     * Reliability
     * Security

3. **Parallel Phrases**
   - ❌ Mixed structure:
     * Click File > Open
     * Select a file by clicking Browse
     * Then you should click OK

   - ✅ Parallel structure:
     * Click File > Open
     * Click Browse to select a file
     * Click OK

**Headings and Subheadings**

1. **Same Level, Same Structure**
   - ❌ Mixed structure:
     * Installing the Software
     * How to Configure
     * Troubleshoot

   - ✅ Parallel structure (Gerunds):
     * Installing the Software
     * Configuring the System
     * Troubleshooting Issues

   - ✅ Parallel structure (Imperatives):
     * Install the Software
     * Configure the System
     * Troubleshoot Issues

2. **Question Format**
   - ✅ Parallel questions:
     * What is the API?
     * How does authentication work?
     * When should I use caching?

**Comparisons and Contrasts**

- ❌ "The old version was slow, but the new one has improved speed"
- ✅ "The old version was slow, but the new version is fast"
- ❌ "Python is easy to learn and has readability"
- ✅ "Python is easy to learn and easy to read"

### Plain Language Guidelines

**Core Principles**

1. **Write for Your Audience**
   - Consider education level
   - Assume no prior knowledge (unless expert documentation)
   - Define specialized terms
   - Use familiar concepts and examples

2. **Front-Load Important Information**
   - ❌ "When the system encounters an error during processing, which can happen for various reasons including network issues, an error message is displayed"
   - ✅ "The system displays an error message when processing fails due to network issues or other problems"

3. **Use Pronouns to Engage Readers**
   - ✅ "You can configure the system..."
   - ✅ "Your data is encrypted..."
   - ✅ "We recommend updating regularly..."
   - ❌ "The user can configure the system..."
   - ❌ "One's data is encrypted..."

4. **Use Consistent Terminology**
   - Choose one term and stick with it
   - Don't alternate between "click" and "select"
   - Don't alternate between "dialog" and "window"
   - Don't alternate between "start" and "begin"

5. **Avoid Nominalizations**
   - ❌ "provide a description of" → ✅ "describe"
   - ❌ "make a decision" → ✅ "decide"
   - ❌ "perform an analysis" → ✅ "analyze"
   - ❌ "conduct an investigation" → ✅ "investigate"

**Readability Formulas**

Target readability scores:
- **General audience**: Flesch-Kincaid Grade 8-10
- **Technical audience**: Grade 10-12
- **Expert audience**: Grade 12+

**Tools**: Hemingway Editor, Grammarly, Microsoft Word readability statistics

### Audience Analysis

**Identify Your Audience**

1. **Expertise Level**
   - **Beginner**: No prior knowledge; needs step-by-step instructions
   - **Intermediate**: Some experience; needs reference and best practices
   - **Advanced**: Expert knowledge; needs technical details and edge cases
   - **Mixed**: Multiple skill levels; use progressive disclosure

2. **Job Role**
   - **End Users**: Focus on tasks and outcomes
   - **Administrators**: Focus on configuration and management
   - **Developers**: Focus on integration and technical details
   - **Decision Makers**: Focus on benefits and business value

3. **Goals and Tasks**
   - What are they trying to accomplish?
   - What problems are they solving?
   - What questions will they have?
   - What obstacles might they face?

**Tailoring Content**

1. **For Beginners**
   - Define all terms
   - Use lots of examples
   - Provide screenshots
   - Anticipate common mistakes
   - Link to related concepts
   - Use step-by-step procedures

2. **For Experts**
   - Use technical vocabulary
   - Provide reference tables
   - Include code samples
   - Document edge cases
   - Link to API documentation
   - Focus on efficiency

3. **For Mixed Audiences**
   - Use progressive disclosure (basic info first, then advanced)
   - Provide "Quick Start" and "Complete Guide" versions
   - Use expandable sections for advanced topics
   - Include skill level indicators
   - Offer multiple paths through content

**User Personas**

Create personas to represent your audience:

```
Persona: Sarah (System Administrator)
- Experience: 5 years IT administration
- Goals: Configure software efficiently, minimize downtime
- Pain points: Complex documentation, missing troubleshooting info
- Preferred format: Checklists, command references, troubleshooting guides
- Technical level: Intermediate to advanced
```

## Documentation Types

### User Guides and Manuals

**Purpose**: Help users understand and use a product effectively.

**Structure**

```markdown
# [Product Name] User Guide

## Table of Contents

## 1. Introduction
   - What is [Product]?
   - Who is this guide for?
   - What you'll learn
   - Conventions used in this guide

## 2. Getting Started
   - System requirements
   - Installation
   - Initial setup
   - First-time configuration
   - Quick start tutorial

## 3. Core Features
   - Feature 1: [Description]
     - How it works
     - How to use it
     - Examples
   - Feature 2: [Description]
   - Feature 3: [Description]

## 4. Advanced Features
   - Advanced configuration
   - Customization options
   - Integration with other tools
   - Power user tips

## 5. Common Tasks
   - How to [Task 1]
   - How to [Task 2]
   - How to [Task 3]

## 6. Troubleshooting
   - Common issues and solutions
   - Error messages
   - Getting help

## 7. FAQ
   - Frequently asked questions

## 8. Glossary
   - Key terms and definitions

## 9. Appendices
   - Keyboard shortcuts
   - Command reference
   - Configuration file reference
```

**Best Practices**

1. **Task-Oriented Organization**
   - Organize by what users want to accomplish
   - Use action-oriented headings ("Creating a Report" not "Reports")
   - Provide step-by-step procedures

2. **Logical Flow**
   - Start with basics, progress to advanced
   - Build on previous knowledge
   - Cross-reference related topics

3. **Visual Aids**
   - Screenshots with annotations
   - Diagrams showing workflows
   - Icons to indicate tips, warnings, notes
   - Videos for complex procedures

4. **Examples**
   - Realistic, relevant scenarios
   - Before and after comparisons
   - Sample data and output

**User Guide Template**

```markdown
## [Task Name]

**Purpose**: Brief description of what this accomplishes and why it's useful.

**Prerequisites**:
- Requirement 1
- Requirement 2

**Steps**:

1. Open the [Component] window by selecting File > New.

   ![Screenshot showing menu](path/to/image.png)

2. In the Name field, enter a name for your [item].

3. (Optional) To enable [feature], select the [checkbox].

4. Click Create.

**Result**: Description of what happens.

**What's Next**: Links to related tasks or next steps.

**Troubleshooting**:
- If [problem], [solution]
- If [problem], [solution]
```

### API Documentation

**Purpose**: Enable developers to integrate with and use your API effectively.

**Essential Components**

1. **Overview**
   - What the API does
   - Use cases
   - Authentication methods
   - Base URL
   - Rate limits
   - Versioning

2. **Authentication**
   ```markdown
   ## Authentication

   All API requests require authentication using an API key.

   **Getting an API Key**:
   1. Log in to your account
   2. Navigate to Settings > API Keys
   3. Click "Generate New Key"

   **Using Your API Key**:

   Include the key in the Authorization header:

   ```http
   Authorization: Bearer YOUR_API_KEY
   ```

   **Security**:
   - Keep your API key secret
   - Rotate keys regularly
   - Use different keys for different environments
   ```

3. **Endpoint Documentation Template**

   ```markdown
   ## [Endpoint Name]

   [Brief description of what this endpoint does]

   **Endpoint**: `[METHOD] /api/v1/resource`

   **Authentication**: Required

   **Rate Limit**: [X requests per minute]

   ### Request

   **HTTP Method**: GET | POST | PUT | PATCH | DELETE

   **URL**: `https://api.example.com/v1/resource`

   **Headers**:
   | Header | Type | Required | Description |
   |--------|------|----------|-------------|
   | Authorization | string | Yes | Bearer token |
   | Content-Type | string | Yes | application/json |

   **Path Parameters**:
   | Parameter | Type | Required | Description |
   |-----------|------|----------|-------------|
   | id | integer | Yes | Resource ID |

   **Query Parameters**:
   | Parameter | Type | Required | Default | Description |
   |-----------|------|----------|---------|-------------|
   | limit | integer | No | 10 | Number of results |
   | offset | integer | No | 0 | Pagination offset |
   | sort | string | No | created_at | Sort field |

   **Request Body**:
   ```json
   {
     "name": "string",
     "email": "string",
     "age": 25
   }
   ```

   **Field Descriptions**:
   | Field | Type | Required | Validation | Description |
   |-------|------|----------|------------|-------------|
   | name | string | Yes | 1-100 chars | User's full name |
   | email | string | Yes | Valid email | Email address |
   | age | integer | No | 0-120 | User's age |

   ### Response

   **Success Response** (200 OK):
   ```json
   {
     "id": 123,
     "name": "John Doe",
     "email": "john@example.com",
     "age": 25,
     "created_at": "2024-01-15T10:30:00Z",
     "updated_at": "2024-01-15T10:30:00Z"
   }
   ```

   **Error Responses**:

   **400 Bad Request**:
   ```json
   {
     "error": "validation_error",
     "message": "Invalid email format",
     "details": {
       "email": ["Must be a valid email address"]
     }
   }
   ```

   **401 Unauthorized**:
   ```json
   {
     "error": "unauthorized",
     "message": "Invalid or missing API key"
   }
   ```

   **404 Not Found**:
   ```json
   {
     "error": "not_found",
     "message": "Resource not found"
   }
   ```

   **429 Too Many Requests**:
   ```json
   {
     "error": "rate_limit_exceeded",
     "message": "Rate limit exceeded. Try again in 60 seconds"
   }
   ```

   **500 Internal Server Error**:
   ```json
   {
     "error": "internal_error",
     "message": "An unexpected error occurred"
   }
   ```

   ### Examples

   **cURL**:
   ```bash
   curl -X POST https://api.example.com/v1/users \
     -H "Authorization: Bearer YOUR_API_KEY" \
     -H "Content-Type: application/json" \
     -d '{
       "name": "John Doe",
       "email": "john@example.com",
       "age": 25
     }'
   ```

   **JavaScript (fetch)**:
   ```javascript
   const response = await fetch('https://api.example.com/v1/users', {
     method: 'POST',
     headers: {
       'Authorization': 'Bearer YOUR_API_KEY',
       'Content-Type': 'application/json'
     },
     body: JSON.stringify({
       name: 'John Doe',
       email: 'john@example.com',
       age: 25
     })
   });

   const data = await response.json();
   console.log(data);
   ```

   **Python (requests)**:
   ```python
   import requests

   url = 'https://api.example.com/v1/users'
   headers = {
       'Authorization': 'Bearer YOUR_API_KEY',
       'Content-Type': 'application/json'
   }
   data = {
       'name': 'John Doe',
       'email': 'john@example.com',
       'age': 25
   }

   response = requests.post(url, headers=headers, json=data)
   print(response.json())
   ```

   ### Notes

   - [Additional information]
   - [Known limitations]
   - [Related endpoints]
   ```

4. **Common Patterns**

   **Pagination**:
   ```markdown
   ## Pagination

   List endpoints support pagination using `limit` and `offset` parameters.

   **Response includes pagination metadata**:
   ```json
   {
     "data": [...],
     "pagination": {
       "total": 100,
       "limit": 10,
       "offset": 0,
       "has_more": true
     }
   }
   ```

   **Example**: Get items 11-20:
   ```
   GET /api/v1/items?limit=10&offset=10
   ```
   ```

   **Error Handling**:
   ```markdown
   ## Error Handling

   All errors follow a consistent format:

   ```json
   {
     "error": "error_code",
     "message": "Human-readable message",
     "details": {}  // Optional additional context
   }
   ```

   **Common Error Codes**:
   | Code | HTTP Status | Description |
   |------|-------------|-------------|
   | validation_error | 400 | Invalid input data |
   | unauthorized | 401 | Missing or invalid auth |
   | forbidden | 403 | Insufficient permissions |
   | not_found | 404 | Resource doesn't exist |
   | rate_limit_exceeded | 429 | Too many requests |
   | internal_error | 500 | Server error |
   ```

5. **API Reference Tools**
   - OpenAPI/Swagger specification
   - Postman collections
   - Interactive API explorers
   - SDKs and client libraries

### Installation Guides

**Purpose**: Help users install software correctly and efficiently.

**Structure**

```markdown
# Installation Guide

## System Requirements

**Minimum Requirements**:
- Operating System: [Specific versions]
- CPU: [Specifications]
- RAM: [Amount]
- Disk Space: [Amount]
- Network: [Requirements]
- Additional Software: [Dependencies]

**Recommended Requirements**:
- Operating System: [Specific versions]
- CPU: [Specifications]
- RAM: [Amount]
- Disk Space: [Amount]
- Network: [Requirements]

## Pre-Installation Checklist

Before you begin, ensure:
- [ ] You have administrator/root privileges
- [ ] You have downloaded the correct installer for your OS
- [ ] You have backed up existing data
- [ ] Required ports are available (list specific ports)
- [ ] Dependencies are installed

## Installation Methods

### Method 1: Quick Install (Recommended)

**For most users. Automated installation with default settings.**

[Platform-specific instructions]

### Method 2: Custom Install

**For advanced users. Full control over installation options.**

[Detailed instructions]

### Method 3: Docker/Container Install

**For containerized deployments.**

[Container-specific instructions]

## Platform-Specific Instructions

### Windows

1. **Download the Installer**

   Download the `.msi` or `.exe` file from [URL].

   File size: [Size]
   SHA256: [Hash for verification]

2. **Run the Installer**

   Double-click the downloaded file.

   If you see a security warning, click "Run anyway".

3. **Follow the Setup Wizard**

   - Click "Next" on the welcome screen
   - Accept the license agreement
   - Choose installation directory (default: C:\Program Files\[Product])
   - Select components to install
   - Click "Install"

4. **Complete Installation**

   - Wait for installation to complete (typically 2-3 minutes)
   - Click "Finish"
   - Restart your computer if prompted

### macOS

1. **Download the Package**

   Download the `.dmg` file from [URL].

2. **Mount and Install**

   ```bash
   # Open the DMG
   open [Product].dmg

   # Drag to Applications folder
   # Or double-click the installer package
   ```

3. **Grant Permissions**

   System Preferences > Security & Privacy > Allow [Product]

### Linux

**Ubuntu/Debian**:

```bash
# Add repository
curl -fsSL https://[url]/gpg | sudo gpg --dearmor -o /usr/share/keyrings/[product].gpg

echo "deb [signed-by=/usr/share/keyrings/[product].gpg] https://[url] stable main" | \
  sudo tee /etc/apt/sources.list.d/[product].list

# Update and install
sudo apt update
sudo apt install [product]

# Verify installation
[product] --version
```

**Red Hat/CentOS/Fedora**:

```bash
# Add repository
sudo dnf config-manager --add-repo https://[url]/[product].repo

# Install
sudo dnf install [product]

# Verify installation
[product] --version
```

**From Source**:

```bash
# Install dependencies
sudo apt install build-essential git

# Clone repository
git clone https://github.com/[org]/[product].git
cd [product]

# Build
./configure
make
sudo make install

# Verify
[product] --version
```

## Post-Installation

### Verify Installation

```bash
# Check version
[product] --version

# Run health check
[product] check

# View installation directory
which [product]
```

### Initial Configuration

1. **Create Configuration File**

   ```bash
   [product] init
   ```

   This creates a default configuration at `~/.config/[product]/config.yaml`

2. **Edit Configuration**

   Open the configuration file and set:

   ```yaml
   server:
     host: localhost
     port: 8080

   database:
     url: postgresql://localhost:5432/mydb

   logging:
     level: info
   ```

3. **Start the Service**

   ```bash
   # Start
   [product] start

   # Enable auto-start
   [product] enable

   # Check status
   [product] status
   ```

### Next Steps

- [ ] [Link to Quick Start Guide]
- [ ] [Link to Configuration Reference]
- [ ] [Link to User Guide]

## Troubleshooting Installation Issues

### Issue: "Permission denied"

**Cause**: Insufficient privileges

**Solution**:
```bash
sudo [command]
```

### Issue: "Port already in use"

**Cause**: Another service is using the default port

**Solution**:
1. Identify the process using the port:
   ```bash
   lsof -i :8080
   ```
2. Stop the conflicting service or change the port in configuration

### Issue: "Dependency not found"

**Cause**: Required dependencies not installed

**Solution**:
```bash
# Install dependencies
[package manager] install [dependency]
```

## Uninstallation

**Windows**:
- Control Panel > Programs > Uninstall a Program
- Select [Product] and click Uninstall

**macOS**:
```bash
sudo rm -rf /Applications/[Product].app
rm -rf ~/Library/Application\ Support/[Product]
```

**Linux**:
```bash
sudo apt remove [product]  # Debian/Ubuntu
sudo dnf remove [product]  # Red Hat/Fedora
```

## Getting Help

- Documentation: [URL]
- Community Forum: [URL]
- Support Email: [Email]
- GitHub Issues: [URL]
```

### Troubleshooting Guides

**Purpose**: Help users diagnose and resolve problems quickly.

**Structure**

1. **Problem-Solution Format**

   ```markdown
   ## [Problem Description]

   **Symptoms**:
   - Symptom 1
   - Symptom 2

   **Possible Causes**:
   - Cause 1
   - Cause 2
   - Cause 3

   **Solutions**:

   ### Solution 1: [Name]

   1. Step 1
   2. Step 2
   3. Step 3

   **Result**: What to expect if this solved the problem

   ### Solution 2: [Name]

   [Alternative solution]

   **When to Use**: This solution applies if [conditions]

   **Prevention**: How to avoid this problem in the future
   ```

2. **Error Message Format**

   ```markdown
   ## Error: "[Error Message Text]"

   **Full Error**:
   ```
   ERROR: Connection timeout
   Failed to connect to database at localhost:5432
   Error code: ECONNREFUSED
   ```

   **What This Means**: The application cannot connect to the database server.

   **Common Causes**:
   1. Database server is not running
   2. Incorrect connection settings
   3. Firewall blocking connection
   4. Network issues

   **How to Fix**:

   **Step 1: Verify Database is Running**

   ```bash
   # Check if database process is running
   ps aux | grep postgres

   # Check database status
   systemctl status postgresql
   ```

   If not running, start it:
   ```bash
   systemctl start postgresql
   ```

   **Step 2: Verify Connection Settings**

   Check your configuration file:
   ```yaml
   database:
     host: localhost
     port: 5432
     username: myuser
     database: mydb
   ```

   **Step 3: Test Connection**

   ```bash
   psql -h localhost -p 5432 -U myuser -d mydb
   ```

   **Step 4: Check Firewall**

   ```bash
   # Linux
   sudo ufw allow 5432/tcp

   # macOS
   sudo pfctl -d  # Disable firewall temporarily for testing
   ```

   **Still Having Issues?**

   Collect diagnostic information:
   ```bash
   [product] diagnose > diagnostic.log
   ```

   Share the log file when seeking help.
   ```

3. **Diagnostic Flowchart**

   ```markdown
   ## Troubleshooting Flowchart

   1. **Is the service running?**
      - No → Start the service: `[product] start`
      - Yes → Go to step 2

   2. **Can you access the web interface?**
      - No → Check if port is open: `netstat -an | grep 8080`
      - Yes → Go to step 3

   3. **Are there errors in the logs?**
      - Yes → See [Error Reference](#error-reference)
      - No → Go to step 4

   4. **Is the problem intermittent?**
      - Yes → Check resource usage: `top` or `htop`
      - No → Contact support with diagnostic log
   ```

4. **Common Issues Table**

   ```markdown
   ## Quick Reference: Common Issues

   | Symptom | Likely Cause | Quick Fix |
   |---------|-------------|-----------|
   | Slow performance | Insufficient memory | Increase RAM or reduce concurrent users |
   | Connection timeout | Network/firewall | Check network connectivity and firewall rules |
   | 404 errors | Incorrect URL/path | Verify URL and check path configuration |
   | Authentication failure | Invalid credentials | Reset password or check API key |
   | Database errors | Connection issue | Verify database is running and credentials are correct |
   ```

5. **Self-Diagnosis Section**

   ```markdown
   ## Self-Diagnosis Tools

   **Built-in Diagnostic Command**:
   ```bash
   [product] diagnose
   ```

   This checks:
   - Configuration validity
   - Network connectivity
   - Database connection
   - File permissions
   - Disk space
   - Memory usage

   **Health Check**:
   ```bash
   [product] health
   ```

   Returns:
   - Service status
   - Uptime
   - Version
   - Active connections

   **Verbose Logging**:

   Enable detailed logging for troubleshooting:
   ```yaml
   logging:
     level: debug
     output: /var/log/[product]/debug.log
   ```
   ```

### Release Notes

**Purpose**: Inform users about changes, new features, fixes, and breaking changes.

**Format**: Follow [Keep a Changelog](https://keepachangelog.com/) format

**Structure**

```markdown
# Release Notes

## [Version Number] - YYYY-MM-DD

Brief summary of this release: what's new, why it matters.

### Added
New features and capabilities.

- **Feature Name**: Description of what it does and why it's useful
  - Details or usage example
  - [#123](link-to-pr)

- **Another Feature**: Description
  - [#124](link-to-pr)

### Changed
Updates to existing functionality.

- **Updated [Component]**: What changed and why
  - Migration notes if needed
  - [#125](link-to-pr)

### Deprecated
Features that will be removed in future versions.

- **[Feature] is deprecated**: Will be removed in version X.Y
  - Use [Alternative] instead
  - Migration guide: [Link]
  - [#126](link-to-pr)

### Removed
Features that have been removed.

- **Removed [Feature]**: What was removed and why
  - Alternative: Use [Solution] instead
  - [#127](link-to-pr)

### Fixed
Bug fixes.

- **Fixed [Issue]**: Description of the bug and how it was fixed
  - Affected versions: X.Y.Z
  - [#128](link-to-pr)

### Security
Security improvements and vulnerability fixes.

- **[CVE-YYYY-XXXXX]**: Description of the vulnerability
  - Severity: Critical/High/Medium/Low
  - Affected versions: X.Y.Z
  - Credit: [Researcher name]
  - [#129](link-to-pr)

### Breaking Changes ⚠️
Changes that may break existing implementations.

- **[Change]**: What changed and why

  **Before**:
  ```javascript
  oldFunction(param1, param2);
  ```

  **After**:
  ```javascript
  newFunction({ param1, param2 });
  ```

  **Migration Guide**: [Link to detailed migration guide]

  - [#130](link-to-pr)

### Documentation
Documentation improvements.

- Updated [Guide] with [improvement]
- Added [tutorial/example]
- Fixed typos and broken links

### Dependencies
Updated dependencies.

- Updated [dependency] from X.Y.Z to A.B.C
- Added [new dependency] A.B.C
- Removed [dependency]

### Performance
Performance improvements.

- Improved [operation] performance by X%
- Reduced memory usage by Y%
- Optimized [component]

### Contributors
Thank you to all contributors!

- @username1
- @username2
- @username3

### Download
- [Download version X.Y.Z](link)
- [Installation instructions](link)
- [Docker image](link)

---

## [Previous Version] - YYYY-MM-DD

[Same format as above]
```

**Best Practices for Release Notes**

1. **Write for Users, Not Developers**
   - ❌ "Refactored the authentication module"
   - ✅ "Improved login speed by 50%"

2. **Be Specific and Clear**
   - ❌ "Fixed various bugs"
   - ✅ "Fixed issue where password reset emails weren't being sent"

3. **Include Visual Changes**
   - Before/after screenshots
   - Animated GIFs for UI changes
   - Demo videos for new features

4. **Highlight Breaking Changes**
   - Use clear warnings
   - Provide migration guides
   - Give advance notice in previous releases

5. **Link to Detailed Documentation**
   - Link to feature documentation
   - Link to API changes
   - Link to migration guides

6. **Use Semantic Versioning**
   - MAJOR.MINOR.PATCH
   - MAJOR: Breaking changes
   - MINOR: New features (backward compatible)
   - PATCH: Bug fixes (backward compatible)

**Release Notes Example**

```markdown
## [2.5.0] - 2024-01-15

We're excited to announce version 2.5.0 with improved performance, new analytics features, and important security updates.

### Added

- **Real-time Analytics Dashboard**: Monitor your system performance in real-time
  - Live metrics for requests/second, response times, and error rates
  - Customizable dashboard widgets
  - Export data to CSV or JSON
  - [Documentation](link) | [#456](link)

  ![Analytics Dashboard](screenshot.png)

- **Webhook Support**: Get notified when events occur
  - Configure webhooks for any event type
  - Automatic retry with exponential backoff
  - Webhook signature verification for security
  - [Webhook Guide](link) | [#457](link)

### Changed

- **Improved Search Performance**: Search is now 3x faster
  - Implemented indexed search
  - Added search result caching
  - [#458](link)

- **Updated UI Design**: Refreshed user interface with better accessibility
  - Increased color contrast for WCAG AA compliance
  - Improved keyboard navigation
  - [#459](link)

### Fixed

- **Fixed Memory Leak**: Resolved memory leak in long-running processes
  - Memory usage now stable over time
  - Affects versions 2.0.0 - 2.4.2
  - [#460](link)

- **Fixed Email Delivery**: Fixed issue where emails weren't sent to Gmail addresses
  - [#461](link)

### Security

- **[CVE-2024-12345]**: Fixed SQL injection vulnerability in search
  - Severity: High (CVSS 7.5)
  - Affected versions: 2.0.0 - 2.4.2
  - All users should update immediately
  - Thanks to @securityresearcher for responsible disclosure
  - [#462](link)

### Breaking Changes ⚠️

- **API Authentication Changes**: OAuth 2.0 is now required for API access

  API keys are deprecated and will be removed in version 3.0.0.

  **Migration Steps**:
  1. Register an OAuth application
  2. Update your code to use OAuth tokens
  3. [Complete Migration Guide](link)

  **Old (deprecated)**:
  ```bash
  curl -H "X-API-Key: abc123" https://api.example.com/data
  ```

  **New**:
  ```bash
  curl -H "Authorization: Bearer $TOKEN" https://api.example.com/data
  ```

  [#463](link)

### Performance

- Reduced Docker image size by 40% (250MB → 150MB)
- Improved startup time by 60% (10s → 4s)
- Database queries are now 2x faster with optimized indexes

### Dependencies

- Updated Node.js from 18.x to 20.x
- Updated PostgreSQL driver from 8.10.0 to 8.11.0
- Added zod 3.22.4 for schema validation

### Contributors

Thank you to our amazing contributors:
- @contributor1 - Added webhook support
- @contributor2 - Improved search performance
- @contributor3 - Fixed memory leak
- @securityresearcher - Security vulnerability disclosure

### Download

- [Download v2.5.0](https://example.com/download/2.5.0)
- [Docker Image](https://hub.docker.com/r/example/product)
- [Installation Guide](https://docs.example.com/install)
```

### README Files

**Purpose**: First point of contact for users and developers. Explain what the project is, how to use it, and how to contribute.

**Essential Sections**

```markdown
# Project Name

[Badges: build status, version, license, downloads, etc.]

One-sentence description of what this project does.

Expanded description explaining the problem it solves and key benefits.

![Demo Screenshot or GIF](path/to/demo.gif)

## Features

- **Feature 1**: Brief description
- **Feature 2**: Brief description
- **Feature 3**: Brief description
- **Feature 4**: Brief description

## Quick Start

### Prerequisites

- Node.js 18+ / Python 3.9+ / etc.
- Database (PostgreSQL 12+)
- Additional requirements

### Installation

```bash
# Clone the repository
git clone https://github.com/username/project.git

# Navigate to directory
cd project

# Install dependencies
npm install

# Configure
cp .env.example .env
# Edit .env with your settings

# Run
npm start
```

### Your First [Task]

```bash
# Example command
project create myapp

# Expected output
✓ Created myapp successfully
  Start with: cd myapp && project serve
```

## Documentation

- [User Guide](link) - Complete guide for users
- [API Reference](link) - API documentation
- [Examples](link) - Example implementations
- [FAQ](link) - Frequently asked questions

## Usage

### Basic Example

```javascript
const Project = require('project');

const app = new Project({
  option1: 'value',
  option2: true
});

app.start();
```

### Advanced Example

[More complex usage]

## Configuration

```yaml
# config.yaml
server:
  port: 8080
  host: localhost

database:
  url: postgresql://localhost/mydb
  pool_size: 10

logging:
  level: info
  output: stdout
```

## Development

### Setup

```bash
# Clone with development dependencies
git clone https://github.com/username/project.git
cd project
npm install --include=dev
```

### Running Tests

```bash
# Unit tests
npm test

# Integration tests
npm run test:integration

# Coverage
npm run test:coverage
```

### Code Style

This project uses [ESLint/Prettier/Black/etc.].

```bash
# Lint
npm run lint

# Format
npm run format
```

### Building

```bash
# Development build
npm run build:dev

# Production build
npm run build:prod
```

## Contributing

We welcome contributions! Please see [CONTRIBUTING.md](CONTRIBUTING.md) for details.

### Quick Contribution Guide

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## Roadmap

- [x] Feature 1 (Completed)
- [x] Feature 2 (Completed)
- [ ] Feature 3 (In Progress)
- [ ] Feature 4 (Planned)
- [ ] Feature 5 (Planned)

See [ROADMAP.md](ROADMAP.md) for detailed plans.

## License

This project is licensed under the [MIT License](LICENSE).

## Support

- Documentation: https://docs.example.com
- Issues: https://github.com/username/project/issues
- Discussions: https://github.com/username/project/discussions
- Email: support@example.com
- Discord: [Join our community](link)

## Acknowledgments

- [Inspiration or related project](link)
- [Libraries used](link)
- [Contributors](link)

## Related Projects

- [Related Project 1](link)
- [Related Project 2](link)

---

Made with ❤️ by [Your Name/Organization]
```

**README Best Practices**

1. **Lead with Value**
   - Explain what it does immediately
   - Show, don't just tell (screenshots, GIFs)
   - Highlight key differentiators

2. **Make It Scannable**
   - Use clear headings
   - Short paragraphs
   - Bullet points
   - Code examples

3. **Quick Start First**
   - Get users running quickly
   - Detailed docs can come later
   - Provide copy-paste commands

4. **Keep It Updated**
   - Update version numbers
   - Update screenshots
   - Archive deprecated sections
   - Add new features

5. **Use Badges**
   - Build status
   - Version
   - Downloads
   - License
   - Code coverage

## Structure & Organization

### Information Architecture

**Principle**: Organize content to match user mental models and tasks.

**Organization Patterns**

1. **Task-Based Organization** (Recommended for most documentation)

   Organize by what users want to accomplish:

   ```
   - Getting Started
   - Creating Your First Project
   - Managing Users
     - Adding Users
     - Editing User Permissions
     - Removing Users
   - Configuring Settings
   - Deploying to Production
   - Troubleshooting
   ```

2. **Topic-Based Organization**

   Organize by subject matter:

   ```
   - Concepts
     - Architecture Overview
     - Core Principles
     - Terminology
   - Components
     - Component A
     - Component B
     - Component C
   - Reference
     - API Reference
     - Configuration Reference
     - CLI Reference
   ```

3. **Role-Based Organization**

   Organize by user role:

   ```
   - For End Users
     - Basic Tasks
     - FAQ
   - For Administrators
     - Installation
     - Configuration
     - User Management
   - For Developers
     - API Documentation
     - SDK Guide
     - Integration Examples
   ```

4. **Sequential Organization**

   Organize in logical progression:

   ```
   1. Introduction
   2. Installation
   3. Configuration
   4. First Steps
   5. Basic Usage
   6. Advanced Features
   7. Best Practices
   8. Reference
   ```

**Choosing an Organization Pattern**

- **Use Task-Based** when users have clear goals and want step-by-step instructions
- **Use Topic-Based** when users need reference material and deep understanding
- **Use Role-Based** when different users have completely different needs
- **Use Sequential** when there's a clear learning path or workflow

**Hybrid Approach**

Combine patterns for comprehensive documentation:

```
Documentation Home

Quick Start (Sequential)
├── Installation
├── Configuration
└── Hello World Tutorial

User Guides (Task-Based)
├── Creating Content
├── Managing Files
├── Collaborating with Others
└── Publishing

Concepts (Topic-Based)
├── Architecture
├── Security Model
└── Data Model

Reference (Topic-Based)
├── API Reference
├── CLI Reference
└── Configuration Reference

Administrator Guide (Role-Based)
├── Deployment
├── Monitoring
└── Backup & Recovery

Developer Guide (Role-Based)
├── API Integration
├── Plugin Development
└── Contributing
```

### Task-Based Organization

**Structure for Task Documentation**

```markdown
## Task Name (Verb + Object)

**What you'll accomplish**: One-sentence goal

**Time required**: Estimate (e.g., "5 minutes")

**Prerequisites**:
- Prerequisite 1
- Prerequisite 2

**Steps**:

1. **Action 1**

   Detailed explanation if needed.

   ```bash
   command --option value
   ```

   Expected output:
   ```
   Output text
   ```

2. **Action 2**

   [Details]

3. **Action 3**

   [Details]

**Result**: What success looks like

**Verify**: How to check it worked

**What's next**: Related tasks or next steps

**Troubleshooting**:
- If [problem], [solution]
```

**Example**:

```markdown
## Creating a Database Backup

**What you'll accomplish**: Create a backup of your database that you can restore later

**Time required**: 5-10 minutes

**Prerequisites**:
- Database administrator access
- At least 1GB free disk space
- pg_dump installed (included with PostgreSQL)

**Steps**:

1. **Open a terminal**

   Navigate to a directory where you want to save the backup.

   ```bash
   cd ~/backups
   ```

2. **Run the backup command**

   Replace `mydb` with your database name:

   ```bash
   pg_dump -U postgres -F c -f mydb_backup.dump mydb
   ```

   Options explained:
   - `-U postgres`: Connect as postgres user
   - `-F c`: Custom format (compressed and allows selective restore)
   - `-f mydb_backup.dump`: Output filename
   - `mydb`: Database name

   You'll be prompted for the password.

3. **Verify the backup**

   Check that the file was created:

   ```bash
   ls -lh mydb_backup.dump
   ```

   You should see a file with a size similar to your database size.

**Result**: You now have a backup file named `mydb_backup.dump`

**Verify**:
```bash
# Check file integrity
pg_restore --list mydb_backup.dump | head -20
```

You should see a list of database objects (tables, indexes, etc.).

**What's next**:
- [Schedule automatic backups](link)
- [Learn how to restore from backup](link)
- [Set up off-site backup storage](link)

**Troubleshooting**:
- **If "pg_dump: command not found"**: Install PostgreSQL client tools
- **If "authentication failed"**: Verify your username and password
- **If "permission denied"**: Ensure you have database access rights
```

### Hierarchical Structure

**Heading Hierarchy Rules**

1. **Use Semantic HTML Heading Levels**
   - H1: Page title (only one per page)
   - H2: Major sections
   - H3: Subsections
   - H4: Sub-subsections
   - H5-H6: Rarely needed, consider restructuring if you need these

2. **Don't Skip Levels**
   - ❌ H1 → H3 (skip H2)
   - ✅ H1 → H2 → H3

3. **Parallel Structure at Same Level**
   - All H2s should have similar structure
   - All H3s under an H2 should be related

**Example Hierarchy**:

```markdown
# User Guide (H1)

## Getting Started (H2)

### Installation (H3)
#### Windows (H4)
#### macOS (H4)
#### Linux (H4)

### Configuration (H3)
#### Basic Configuration (H4)
#### Advanced Configuration (H4)

## Core Features (H2)

### Feature A (H3)
#### Using Feature A (H4)
#### Configuring Feature A (H4)

### Feature B (H3)

## Advanced Topics (H2)
```

**Visual Hierarchy**

Use formatting to create visual structure:

```markdown
# Main Title
Large, prominent text

## Section Heading
Slightly smaller but still prominent

Normal paragraph text provides the details. Keep paragraphs short (3-4 sentences max) for readability.

### Subsection

- **Bold for emphasis** on key terms
- *Italics for technical terms* or citations
- `Code formatting` for commands and code

> Blockquotes for important callouts

**Lists** for sequential or related items:
1. First item
2. Second item
3. Third item
```

### Navigation and Findability

**Table of Contents**

Always include a TOC for documents longer than 2-3 pages:

```markdown
# Documentation Title

## Table of Contents

1. [Introduction](#introduction)
2. [Getting Started](#getting-started)
   - [Installation](#installation)
   - [Configuration](#configuration)
3. [Core Features](#core-features)
   - [Feature A](#feature-a)
   - [Feature B](#feature-b)
4. [Advanced Topics](#advanced-topics)
5. [Troubleshooting](#troubleshooting)
6. [FAQ](#faq)
7. [Reference](#reference)
```

**In-Page Navigation**

```markdown
## Complex Section

**Jump to**:
- [Option A](#option-a)
- [Option B](#option-b)
- [Option C](#option-c)

### Option A
[Content]

### Option B
[Content]

### Option C
[Content]

[Back to top](#complex-section)
```

**Cross-References**

Link liberally to related content:

```markdown
## Authentication

[Authentication method] requires a valid API key.

For information about getting an API key, see [API Keys](link).
For information about authentication errors, see [Troubleshooting Authentication](link).
```

**Breadcrumbs**

For deep hierarchies, show the path:

```
Home > User Guide > Core Features > Feature A > Advanced Configuration
```

**Search Optimization**

Write for discoverability:

1. **Use Descriptive Headings**
   - ✅ "Installing on macOS"
   - ❌ "Installation" (too generic)

2. **Include Keywords**
   - Include terms users might search for
   - Use synonyms and alternative phrasings

3. **Define Terms**
   - Define technical terms explicitly
   - Use consistent terminology

4. **Comprehensive First Paragraph**
   - Include key terms in the first paragraph
   - Summarize the topic

**Meta Information**

Include metadata for better navigation:

```markdown
---
title: Installing on macOS
description: Step-by-step guide to install [Product] on macOS systems
keywords: install, installation, setup, mac, macos, osx
last_updated: 2024-01-15
---
```

### Chunking Content

**Principle**: Break content into digestible chunks for better comprehension and scanability.

**Chunking Strategies**

1. **Paragraph Length**
   - 3-5 sentences per paragraph
   - One main idea per paragraph
   - Break long paragraphs into multiple

2. **Section Length**
   - 300-500 words per section
   - Use headings every 2-3 paragraphs
   - Create subsections for complex topics

3. **List Length**
   - 5-7 items per list (maximum 9)
   - Break longer lists into multiple lists
   - Use nested lists for hierarchy

4. **Code Block Length**
   - Show complete examples
   - Break very long code into logical chunks
   - Use comments to explain sections

**Progressive Disclosure**

Reveal information gradually:

```markdown
## Feature Name

Brief introduction (1-2 sentences).

### Basic Usage

Simple example and explanation.

### Advanced Usage

More complex scenarios.

<details>
<summary>Click to expand: Technical Details</summary>

Detailed technical information for advanced users.

</details>
```

**Layered Content**

```markdown
## Installation

**Quick Install** (For most users):
```bash
npm install package
```

<details>
<summary>Custom Installation Options</summary>

**From Source**:
```bash
git clone repo
cd repo
npm run build
```

**With Specific Version**:
```bash
npm install package@1.2.3
```

**Behind Corporate Proxy**:
```bash
npm install package --proxy=http://proxy:8080
```

</details>
```

## Technical Details

### Code Samples and Syntax Highlighting

**Guidelines for Code Examples**

1. **Use Syntax Highlighting**

   Always specify the language:

   ````markdown
   ```javascript
   const greeting = "Hello, World!";
   console.log(greeting);
   ```
   ````

2. **Complete, Runnable Examples**

   ❌ **Incomplete**:
   ```javascript
   user.save()
   ```

   ✅ **Complete**:
   ```javascript
   const user = new User({
     name: "John Doe",
     email: "john@example.com"
   });

   await user.save();
   console.log("User saved successfully");
   ```

3. **Include Context**

   ```javascript
   // Import required modules
   const express = require('express');
   const app = express();

   // Configure middleware
   app.use(express.json());

   // Define route
   app.get('/api/users', async (req, res) => {
     const users = await User.find();
     res.json(users);
   });

   // Start server
   app.listen(3000, () => {
     console.log('Server running on port 3000');
   });
   ```

4. **Add Comments**

   ```python
   # Connect to database
   connection = psycopg2.connect(
       host="localhost",
       database="mydb",
       user="postgres",
       password="password"
   )

   # Create cursor for executing queries
   cursor = connection.cursor()

   # Execute query
   cursor.execute("SELECT * FROM users WHERE active = true")

   # Fetch results
   users = cursor.fetchall()

   # Clean up
   cursor.close()
   connection.close()
   ```

5. **Show Input and Output**

   ```bash
   $ npm install express

   added 50 packages, and audited 51 packages in 3s

   7 packages are looking for funding
     run `npm fund` for details

   found 0 vulnerabilities
   ```

6. **Highlight Important Lines**

   Use comments or callouts:

   ```javascript
   const app = express();

   // IMPORTANT: This must come before routes
   app.use(express.json());

   app.get('/api/data', handler);
   ```

7. **Use Realistic Examples**

   ❌ **Generic**:
   ```javascript
   function foo(bar) {
     return baz(bar);
   }
   ```

   ✅ **Realistic**:
   ```javascript
   function calculateTax(income) {
     const taxRate = 0.22;
     return income * taxRate;
   }
   ```

**Common Languages and Their Syntax**

````markdown
```javascript
// JavaScript / Node.js
```

```typescript
// TypeScript
```

```python
# Python
```

```bash
# Shell / Bash
```

```sql
-- SQL
```

```yaml
# YAML
```

```json
// JSON (note: JSON doesn't support comments, but syntax highlighter does)
```

```html
<!-- HTML -->
```

```css
/* CSS */
```

```go
// Go
```

```rust
// Rust
```

```java
// Java
```

```csharp
// C#
```

```php
// PHP
```

```ruby
# Ruby
```
````

**Code Example Template**

```markdown
## [Operation Name]

[Brief description]

**Example**:

```[language]
// [Description of what this code does]
[code]
```

**Explanation**:
1. Line 1: [What it does]
2. Line 3-5: [What this section does]
3. Line 8: [Important detail]

**Output**:
```
[Expected output]
```

**Common Variations**:

[Alternative approaches or parameters]
```

### Screenshots and Diagrams

**Screenshot Guidelines**

1. **When to Use Screenshots**
   - UI elements that are hard to describe
   - Complex visual layouts
   - Error messages and dialogs
   - Multi-step visual processes

2. **When NOT to Use Screenshots**
   - Simple button clicks (describe with text)
   - Frequently changing UI
   - Text that can be copied
   - Decorative purposes

3. **Screenshot Best Practices**

   - **Resolution**: High DPI (2x for retina displays)
   - **File Format**: PNG for UI, JPG for photos, GIF/MP4 for animations
   - **File Size**: Compress to < 200KB when possible
   - **Cropping**: Show only relevant area
   - **Annotations**: Add arrows, boxes, numbers, highlights
   - **Consistency**: Same OS theme, browser, zoom level
   - **Accessibility**: Always include alt text

4. **Annotating Screenshots**

   ```markdown
   ![Dashboard showing the Analytics tab highlighted in red with an arrow pointing to the Export button](path/to/annotated-screenshot.png)

   *Figure 1: Click the Export button (circled) to download your data*
   ```

5. **Screenshot Example**

   ```markdown
   ## Accessing Settings

   1. Click your profile icon in the top-right corner
   2. Select **Settings** from the dropdown menu

   ![Dropdown menu with Settings option highlighted](images/settings-menu.png)

   *The Settings option is the second item in the profile menu*
   ```

**Diagram Guidelines**

1. **Types of Diagrams**

   - **Architecture Diagrams**: System components and relationships
   - **Flow Diagrams**: Process flows and decision trees
   - **Sequence Diagrams**: Interactions over time
   - **Entity Relationship Diagrams**: Database structure
   - **Network Diagrams**: Infrastructure and connectivity
   - **Wireframes**: UI layout and structure

2. **Diagram Best Practices**

   - **Clarity**: Simple and uncluttered
   - **Labels**: Clear, concise labels
   - **Legend**: Explain symbols and colors
   - **Direction**: Top-to-bottom or left-to-right flow
   - **Consistency**: Same style across all diagrams
   - **Source Files**: Keep editable source (draw.io, Mermaid, etc.)

3. **Creating Diagrams**

   **ASCII Art** (Simple, text-based):
   ```
   ┌──────────┐      ┌──────────┐      ┌──────────┐
   │  Client  │─────>│  Server  │─────>│ Database │
   └──────────┘      └──────────┘      └──────────┘
   ```

   **Mermaid** (Code-based diagrams):
   ````markdown
   ```mermaid
   graph LR
       A[Client] --> B[API Server]
       B --> C[Database]
       B --> D[Cache]
   ```
   ````

   **PlantUML** (Complex diagrams):
   ````markdown
   ```plantuml
   @startuml
   User -> Web: HTTP Request
   Web -> API: API Call
   API -> Database: Query
   Database -> API: Results
   API -> Web: JSON Response
   Web -> User: HTML Page
   @enduml
   ```
   ````

4. **Architecture Diagram Example**

   ```markdown
   ## System Architecture

   The system consists of three main components:

   ```mermaid
   graph TB
       subgraph "Client Layer"
           A[Web Browser]
           B[Mobile App]
       end

       subgraph "Application Layer"
           C[Load Balancer]
           D[Web Server 1]
           E[Web Server 2]
           F[API Server]
       end

       subgraph "Data Layer"
           G[PostgreSQL]
           H[Redis Cache]
           I[S3 Storage]
       end

       A --> C
       B --> C
       C --> D
       C --> E
       D --> F
       E --> F
       F --> G
       F --> H
       F --> I
   ```

   **Components**:
   - **Load Balancer**: Distributes traffic across web servers
   - **Web Servers**: Serve static content and handle requests
   - **API Server**: Business logic and data processing
   - **PostgreSQL**: Primary data storage
   - **Redis**: Session and query caching
   - **S3**: File and media storage
   ```

### Tables and Lists

**When to Use Tables**

Tables are ideal for:
- Comparing multiple items across several attributes
- Reference information (parameters, options, values)
- Structured data with clear columns
- Matrix comparisons

**Table Best Practices**

1. **Simple Tables**

   ```markdown
   | Parameter | Type | Required | Default | Description |
   |-----------|------|----------|---------|-------------|
   | name | string | Yes | - | User's full name |
   | email | string | Yes | - | Email address |
   | age | integer | No | null | User's age |
   | active | boolean | No | true | Account status |
   ```

2. **Alignment**

   ```markdown
   | Item | Price | Quantity | Total |
   |:-----|------:|---------:|------:|
   | Widget | $10.00 | 5 | $50.00 |
   | Gadget | $25.00 | 2 | $50.00 |
   ```

   - Left align text (`:---`)
   - Right align numbers (` ---:`)
   - Center align labels (`:---:`)

3. **Keep It Simple**

   ❌ **Too Complex**:
   ```markdown
   | Feature | Basic Plan ($10/mo) | Pro Plan ($25/mo) including all Basic features plus advanced analytics and priority support | Enterprise (Custom pricing with dedicated account manager) |
   ```

   ✅ **Simplified**:
   ```markdown
   | Feature | Basic | Pro | Enterprise |
   |---------|:-----:|:---:|:----------:|
   | Price | $10/mo | $25/mo | Custom |
   | Users | 5 | 25 | Unlimited |
   | Storage | 10GB | 100GB | Unlimited |
   | Support | Email | Priority | Dedicated |
   ```

4. **Decision Tables**

   ```markdown
   ## Choosing a Deployment Method

   | If you... | Use this method | Why |
   |-----------|----------------|-----|
   | Are deploying to production | Docker | Best isolation and scalability |
   | Need quick local testing | npm start | Fastest startup |
   | Are developing locally | npm run dev | Hot reloading enabled |
   | Are on shared hosting | Binary release | No Node.js required |
   ```

**When to Use Lists**

**Unordered Lists** (bullet points) for:
- Related items without sequence
- Features and capabilities
- Requirements
- Options

```markdown
Features:
- Real-time synchronization
- End-to-end encryption
- Multi-device support
- Offline mode
```

**Ordered Lists** (numbered) for:
- Sequential steps
- Procedures
- Rankings
- Chronological items

```markdown
Installation Steps:
1. Download the installer
2. Run the installer
3. Follow the setup wizard
4. Restart your computer
```

**Nested Lists** for:
- Hierarchical information
- Sub-tasks
- Detailed breakdowns

```markdown
Project Structure:
1. Planning Phase
   - Define requirements
   - Create timeline
   - Assign resources
2. Development Phase
   - Backend development
     - API endpoints
     - Database schema
     - Authentication
   - Frontend development
     - UI components
     - State management
     - Routing
3. Testing Phase
   - Unit tests
   - Integration tests
   - User acceptance testing
```

**Definition Lists** for:
- Term definitions
- Key-value pairs
- Glossaries

```markdown
**API Key**: A unique identifier used to authenticate requests to the API.

**Webhook**: An HTTP callback that notifies your application when specific events occur.

**Rate Limit**: The maximum number of API requests you can make in a given time period.
```

### Callouts (Notes, Warnings, Tips)

**Types of Callouts**

1. **Note** - Additional information that's useful but not critical
2. **Tip** - Helpful suggestion or best practice
3. **Important** - Critical information that users must know
4. **Warning** - Potential problems or data loss
5. **Danger** - Serious risks (security, data loss, breaking changes)

**Callout Formats**

**Markdown with Emojis**:

```markdown
ℹ️ **Note**: This feature is available in version 2.0 and later.

💡 **Tip**: Use keyboard shortcuts to work more efficiently.

⚠️ **Important**: Back up your data before proceeding.

🚨 **Warning**: This action cannot be undone.

🔥 **Danger**: This will permanently delete all your data.
```

**Blockquote Style**:

```markdown
> **Note**: This feature is available in version 2.0 and later.

> ⚠️ **Warning**: This action cannot be undone.
```

**HTML Details/Summary**:

```markdown
<details>
<summary>⚠️ Important: Read before proceeding</summary>

Make sure you have:
- Backed up your data
- Tested in a staging environment
- Reviewed the migration guide
</details>
```

**When to Use Each Type**

**Note** - Supplementary information:
```markdown
ℹ️ **Note**: You can also access this feature from the Settings menu.
```

**Tip** - Optimization or best practice:
```markdown
💡 **Tip**: Enable caching to improve performance by up to 10x.
```

**Important** - Must-know information:
```markdown
⚠️ **Important**: You must restart the server after changing this configuration.
```

**Warning** - Potential problems:
```markdown
🚨 **Warning**: Running this command will delete all log files. This action cannot be undone.
```

**Danger** - Serious consequences:
```markdown
🔥 **Danger**: This will permanently delete your account and all associated data. This action is irreversible.
```

**Placement**

Place callouts:
- **Before** the relevant content (warnings, prerequisites)
- **After** the relevant content (tips, notes)
- **Inline** when closely related to specific text

Example:
```markdown
## Deleting Your Account

🚨 **Warning**: This action is permanent and cannot be undone. All your data will be deleted.

To delete your account:

1. Go to Settings > Account
2. Click "Delete Account"
3. Confirm by entering your password

💡 **Tip**: If you just want to take a break, consider deactivating your account instead.
```

### Cross-References

**Linking Best Practices**

1. **Descriptive Link Text**

   ❌ **Generic**:
   ```markdown
   Click [here](link) for more information.
   ```

   ✅ **Descriptive**:
   ```markdown
   See [Installing on Linux](link) for detailed instructions.
   ```

2. **Contextual Links**

   ```markdown
   Authentication requires a valid API key. For information about obtaining an API key, see [API Authentication](link).

   If authentication fails, see [Troubleshooting Authentication Errors](link).
   ```

3. **Related Links Section**

   ```markdown
   ## Creating a Project

   [Content about creating projects]

   **Related Topics**:
   - [Project Settings](link)
   - [Inviting Team Members](link)
   - [Project Templates](link)
   ```

4. **See Also Boxes**

   ```markdown
   ## Configuration

   [Configuration content]

   ---

   **See Also**:
   - [Environment Variables](link) - Configure using environment variables
   - [Configuration File Reference](link) - Complete configuration options
   - [Best Practices](link) - Recommended configurations
   ```

5. **Inline References**

   ```markdown
   The [authentication system](link) uses JWT tokens (see [Security](link)) to verify user identity. Tokens expire after 24 hours (configurable via [token_expiry setting](link)).
   ```

6. **Version-Specific Links**

   ```markdown
   ℹ️ **Note**: This feature was added in version 2.0. If you're using an earlier version, see [Migration Guide](link).
   ```

7. **External Links**

   ```markdown
   This project uses [PostgreSQL](https://postgresql.org) as its database. For installation instructions, see the [PostgreSQL documentation](https://postgresql.org/docs).
   ```

## Style Guides

### Microsoft Manual of Style Basics

**Key Principles**

1. **Voice and Tone**
   - Warm and friendly
   - Professional but conversational
   - Respectful and inclusive
   - Encouraging and supportive

2. **Person and Voice**
   - Second person (you) for instructions
   - First person plural (we) for company perspective
   - Active voice preferred
   - Present tense for general information

3. **Word Choice**

   **Preferred Terms**:
   - "app" not "application"
   - "sign in" not "log in" or "login"
   - "email" not "e-mail"
   - "internet" not "Internet"
   - "website" not "web site"
   - "username" not "user name"
   - "select" not "click" (more device-agnostic)
   - "choose" for menu items

   **Avoid**:
   - "simply" or "just" (dismissive)
   - "easy" or "easily" (subjective)
   - "obviously" or "clearly" (condescending)
   - Exclamation points (except sparingly)

4. **UI Elements**

   - **Bold** for UI elements: "Click the **Save** button"
   - Use exact text from UI: "Select **File** > **Open**"
   - Don't use quotes around UI element names

5. **Capitalization**

   - Sentence case for headings: "Creating a new project"
   - UI elements: Match the UI exactly
   - Feature names: Lowercase unless proper noun
   - Capitalize internet terms as common nouns: "web", "internet", "email"

6. **Punctuation**

   - One space after periods
   - Oxford comma in lists: "red, white, and blue"
   - No period after headings
   - Periods after complete sentences in lists

7. **Numbers**

   - Spell out one through nine
   - Use numerals for 10 and above
   - Use numerals for technical measurements: "8 GB RAM"
   - Use numerals with units: "5 minutes"

8. **Accessibility**

   - Write clear, simple sentences
   - Use plain language
   - Avoid idioms and colloquialisms
   - Define technical terms
   - Provide alt text for images
   - Use descriptive link text

### Google Developer Documentation Style Guide

**Key Principles**

1. **Be Consistent**
   - Use the same term for the same concept
   - Follow established patterns
   - Maintain consistency within and across documents

2. **Write for a Global Audience**
   - Use simple, clear English
   - Avoid colloquialisms and slang
   - Avoid culturally specific references
   - Use "for example" not "e.g."
   - Use "that is" not "i.e."

3. **Word Choice**

   **Preferred Terms**:
   - "can" for capability, "might" for possibility
   - "press" for keyboard keys
   - "select" or "click" for UI elements
   - "tap" for touch interfaces
   - "turn on/turn off" not "enable/disable"
   - "earlier/later" not "above/below" (page location)

   **Avoid**:
   - Latin abbreviations (e.g., i.e., etc.)
   - Future tense when possible
   - Anthropomorphism (don't say code "wants" or "thinks")

4. **Capitalization**

   - Sentence case for headings
   - Proper nouns: Google, Python, JavaScript
   - API names as shown: getElementById()
   - Lowercase for generic terms: "the API", "the database"

5. **Code in Text**

   - Use `code font` for:
     - Code elements
     - Command names
     - File names
     - Paths
     - HTTP status codes
     - HTML/XML elements

   - Don't use code font for:
     - General concepts
     - Company/product names
     - URLs (unless in code)

6. **Lists**

   - Introduce lists with a complete sentence
   - Use parallel structure
   - Capitalize first word
   - Use periods if items are sentences

7. **Procedures**

   - Use numbered lists for steps
   - One action per step
   - Start each step with a verb
   - Include expected results

### Consistency in Terminology

**Creating a Terminology Guide**

1. **Identify Key Terms**

   List all important terms in your domain:

   ```markdown
   ## Terminology Guide

   | Term | Usage | Don't Use | Example |
   |------|-------|-----------|---------|
   | API key | Authentication credential | API token, access token | "Enter your API key in the configuration file" |
   | endpoint | API resource URL | route, path, URL | "Call the /users endpoint" |
   | parameter | Function input | argument, variable | "The limit parameter accepts integers from 1-100" |
   | field | Form or data element | property (in UI context) | "Enter your email in the Email field" |
   | property | Object attribute | field (in code context) | "The user object has a name property" |
   ```

2. **Standardize Verbs**

   ```markdown
   ## Action Verbs

   | Action | Use This | Not This |
   |--------|----------|----------|
   | User interaction | Click, select, enter, choose | Hit, press, tap (unless touch) |
   | Code execution | Run, execute | Start |
   | System action | Returns, sends, creates | Gives back |
   | Navigation | Go to, navigate to | Access |
   | Authentication | Sign in | Log in, login |
   ```

3. **Product Names**

   ```markdown
   ## Product Name Usage

   - **Product Name**: [Product] (capitalized, no "the")
   - **Short form**: [Shortname] or "the application"
   - **Version references**: "[Product] 2.0" or "version 2.0"
   - **Feature names**: Lowercase unless proper noun
   ```

4. **Abbreviations and Acronyms**

   ```markdown
   ## Abbreviations

   Always spell out on first use:

   - ✅ "Application Programming Interface (API)"
   - ✅ "Representational State Transfer (REST)"
   - ✅ "JavaScript Object Notation (JSON)"

   Subsequent uses: use abbreviation

   **Common Abbreviations** (don't need spelling out):
   - API
   - URL
   - HTTP/HTTPS
   - HTML/CSS/JavaScript
   - JSON/XML
   - SQL
   ```

### Formatting Conventions

**Text Formatting**

1. **Bold**
   - UI elements: buttons, menu items, dialog boxes
   - Important warnings
   - Defined terms (first use)
   - User inputs (in procedures)

2. **Italic**
   - Emphasis (sparingly)
   - Citations and references
   - Variable names in text
   - New terminology (first use, then define)

3. **Code/Monospace**
   - Code elements
   - Commands
   - File names and paths
   - API endpoints
   - HTTP methods
   - Data types
   - Function names
   - Variable names

**Examples**:

```markdown
1. Open the **Settings** dialog.

2. In the **Port** field, enter `8080`.

3. Select **File** > **Save**.

4. Run the `npm install` command.

5. Navigate to `/etc/config/app.conf`.

6. The `getUserById()` function returns a `User` object.

7. Send a `POST` request to `/api/users`.

*Note*: You must restart the server after making changes.

**Warning**: This will delete all data.
```

**Consistency Checklist**

- [ ] Same term used throughout for each concept
- [ ] Same capitalization rules applied
- [ ] Same formatting for same element types
- [ ] Same voice and tone throughout
- [ ] Same heading structure
- [ ] Same code style conventions
- [ ] Same screenshot style
- [ ] Same callout formatting
- [ ] Same list punctuation

**Style Guide Template**

Create your own style guide:

```markdown
# [Project Name] Documentation Style Guide

## Voice and Tone
[Define your voice and tone]

## Terminology
[List standardized terms]

## Formatting
[Define formatting rules]

## Code Samples
[Define code style]

## Visual Elements
[Screenshot and diagram guidelines]

## Review Checklist
[Items to check during review]

## Examples
[Before/after examples]
```

---

*This skill provides comprehensive technical writing knowledge for creating clear, professional, user-focused documentation across all formats and audiences.*
