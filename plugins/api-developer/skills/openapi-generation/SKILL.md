# OpenAPI Generation Skill

**Best practices for creating comprehensive OpenAPI 3.0 specifications with schemas, examples, and complete documentation**

## Core Principles

1. **Completeness**: Document every endpoint, parameter, and response
2. **Reusability**: Use $ref to avoid duplication
3. **Accuracy**: Match actual implementation exactly
4. **Examples**: Provide realistic, helpful examples
5. **Maintainability**: Structure for easy updates

---

## OpenAPI 3.0 Structure

### Complete Specification Template

```yaml
openapi: 3.0.0

info:
  title: API Title
  description: |
    # Overview
    Brief description of what this API does.

    ## Authentication
    This API uses JWT Bearer token authentication.

    To authenticate:
    1. POST to `/auth/login` with credentials
    2. Receive JWT token in response
    3. Include token in Authorization header: `Bearer <token>`

    ## Rate Limiting
    - Authenticated: 1000 requests/hour
    - Unauthenticated: 100 requests/hour

    Rate limit info is returned in response headers:
    - `X-RateLimit-Limit`: Request limit per window
    - `X-RateLimit-Remaining`: Requests remaining
    - `X-RateLimit-Reset`: Unix timestamp when limit resets

    ## Pagination
    List endpoints support pagination with `page` and `limit` parameters.
    Default page size is 20, maximum is 100.

    ## Versioning
    Current version: v1
    Breaking changes will increment the major version number.

  version: 1.0.0
  termsOfService: https://example.com/terms
  contact:
    name: API Support
    email: api-support@example.com
    url: https://example.com/support
  license:
    name: MIT
    url: https://opensource.org/licenses/MIT

servers:
  - url: https://api.example.com/v1
    description: Production server
  - url: https://staging-api.example.com/v1
    description: Staging server
  - url: http://localhost:8000/v1
    description: Local development server

security:
  - bearerAuth: []  # Applied to all endpoints by default

tags:
  - name: Authentication
    description: User authentication and authorization
  - name: Users
    description: User management operations
  - name: Posts
    description: Blog post operations
  - name: Comments
    description: Comment operations

paths:
  # Endpoint definitions here

components:
  securitySchemes:
    # Authentication definitions

  schemas:
    # Reusable data models

  responses:
    # Reusable responses

  parameters:
    # Reusable parameters

  examples:
    # Reusable examples

  requestBodies:
    # Reusable request bodies
```

---

## Component Definitions

### Security Schemes

**JWT Bearer Token**:
```yaml
components:
  securitySchemes:
    bearerAuth:
      type: http
      scheme: bearer
      bearerFormat: JWT
      description: |
        JWT authentication. Include the token in the Authorization header:
        ```
        Authorization: Bearer <token>
        ```

        Tokens expire after 15 minutes. Use the refresh token endpoint
        to obtain a new access token without re-authenticating.
```

**API Key**:
```yaml
components:
  securitySchemes:
    apiKeyAuth:
      type: apiKey
      in: header
      name: X-API-Key
      description: |
        API key authentication. Obtain your API key from the dashboard:
        https://example.com/dashboard/api-keys

        Include in X-API-Key header:
        ```
        X-API-Key: your-api-key-here
        ```
```

**OAuth 2.0**:
```yaml
components:
  securitySchemes:
    oauth2:
      type: oauth2
      description: OAuth 2.0 authentication
      flows:
        authorizationCode:
          authorizationUrl: https://example.com/oauth/authorize
          tokenUrl: https://example.com/oauth/token
          refreshUrl: https://example.com/oauth/refresh
          scopes:
            read: Read access to resources
            write: Write access to resources
            delete: Delete access to resources
            admin: Administrative access
```

### Schema Definitions

**User Schema**:
```yaml
components:
  schemas:
    User:
      type: object
      required:
        - id
        - email
        - name
        - role
        - createdAt
      properties:
        id:
          type: string
          format: uuid
          description: Unique user identifier
          example: "123e4567-e89b-12d3-a456-426614174000"
          readOnly: true
        email:
          type: string
          format: email
          description: User email address (must be unique)
          example: "user@example.com"
        name:
          type: string
          minLength: 1
          maxLength: 100
          description: User full name
          example: "John Doe"
        role:
          type: string
          enum: [admin, user, guest]
          default: user
          description: User role for authorization
          example: "user"
        avatar:
          type: string
          format: uri
          description: URL to user avatar image
          example: "https://example.com/avatars/user123.jpg"
          nullable: true
        createdAt:
          type: string
          format: date-time
          description: User creation timestamp (ISO 8601)
          example: "2025-01-20T10:00:00Z"
          readOnly: true
        updatedAt:
          type: string
          format: date-time
          description: User last update timestamp (ISO 8601)
          example: "2025-01-20T15:30:00Z"
          readOnly: true
```

**Request Schemas**:
```yaml
components:
  schemas:
    CreateUserRequest:
      type: object
      required:
        - email
        - name
        - password
      properties:
        email:
          type: string
          format: email
          example: "newuser@example.com"
        name:
          type: string
          minLength: 1
          maxLength: 100
          example: "Jane Smith"
        password:
          type: string
          format: password
          minLength: 8
          maxLength: 128
          description: Must be at least 8 characters
          example: "securePassword123"
        role:
          type: string
          enum: [admin, user, guest]
          default: user
          example: "user"

    UpdateUserRequest:
      type: object
      properties:
        name:
          type: string
          minLength: 1
          maxLength: 100
          example: "Jane Doe"
        avatar:
          type: string
          format: uri
          example: "https://example.com/avatars/new.jpg"
          nullable: true
        role:
          type: string
          enum: [admin, user, guest]
          example: "admin"
```

**Pagination**:
```yaml
components:
  schemas:
    Pagination:
      type: object
      required:
        - page
        - limit
        - total
        - totalPages
      properties:
        page:
          type: integer
          minimum: 1
          description: Current page number (1-indexed)
          example: 1
        limit:
          type: integer
          minimum: 1
          maximum: 100
          description: Number of items per page
          example: 20
        total:
          type: integer
          minimum: 0
          description: Total number of items
          example: 150
        totalPages:
          type: integer
          minimum: 0
          description: Total number of pages
          example: 8
        hasNext:
          type: boolean
          description: Whether there is a next page
          example: true
        hasPrev:
          type: boolean
          description: Whether there is a previous page
          example: false

    PaginatedUsers:
      type: object
      required:
        - data
        - pagination
      properties:
        data:
          type: array
          items:
            $ref: '#/components/schemas/User'
        pagination:
          $ref: '#/components/schemas/Pagination'
```

**Error Responses**:
```yaml
components:
  schemas:
    Error:
      type: object
      required:
        - error
        - message
      properties:
        error:
          type: string
          description: Machine-readable error code
          example: "validation_error"
        message:
          type: string
          description: Human-readable error message
          example: "Request validation failed"
        requestId:
          type: string
          format: uuid
          description: Unique request identifier for tracing
          example: "abc-123-def-456"
        timestamp:
          type: string
          format: date-time
          description: Error timestamp
          example: "2025-01-20T10:00:00Z"
        details:
          type: array
          description: Detailed error information (e.g., validation errors)
          items:
            type: object
            properties:
              field:
                type: string
                description: Field that caused the error
                example: "email"
              message:
                type: string
                description: Error message for this field
                example: "Invalid email format"
              code:
                type: string
                description: Error code for this field
                example: "INVALID_FORMAT"
```

### Reusable Parameters

```yaml
components:
  parameters:
    PageParam:
      name: page
      in: query
      description: Page number for pagination (1-indexed)
      required: false
      schema:
        type: integer
        minimum: 1
        default: 1
      example: 1

    LimitParam:
      name: limit
      in: query
      description: Number of items per page (max 100)
      required: false
      schema:
        type: integer
        minimum: 1
        maximum: 100
        default: 20
      example: 20

    SortParam:
      name: sort
      in: query
      description: |
        Sort order. Prefix with `-` for descending.
        Examples: `createdAt`, `-createdAt`, `name,-createdAt`
      required: false
      schema:
        type: string
      example: "-createdAt"

    UserIdParam:
      name: userId
      in: path
      description: User unique identifier
      required: true
      schema:
        type: string
        format: uuid
      example: "123e4567-e89b-12d3-a456-426614174000"
```

### Reusable Responses

```yaml
components:
  responses:
    BadRequestError:
      description: Bad request - Invalid input
      content:
        application/json:
          schema:
            $ref: '#/components/schemas/Error'
          example:
            error: "bad_request"
            message: "Invalid request parameters"
            requestId: "abc-123"
            timestamp: "2025-01-20T10:00:00Z"

    UnauthorizedError:
      description: Unauthorized - Authentication required
      content:
        application/json:
          schema:
            $ref: '#/components/schemas/Error'
          example:
            error: "unauthorized"
            message: "Authentication required"
            requestId: "abc-123"
            timestamp: "2025-01-20T10:00:00Z"

    ForbiddenError:
      description: Forbidden - Insufficient permissions
      content:
        application/json:
          schema:
            $ref: '#/components/schemas/Error'
          example:
            error: "forbidden"
            message: "Insufficient permissions"
            requestId: "abc-123"
            timestamp: "2025-01-20T10:00:00Z"

    NotFoundError:
      description: Not found - Resource doesn't exist
      content:
        application/json:
          schema:
            $ref: '#/components/schemas/Error'
          example:
            error: "not_found"
            message: "Resource not found"
            requestId: "abc-123"
            timestamp: "2025-01-20T10:00:00Z"

    ConflictError:
      description: Conflict - Resource already exists
      content:
        application/json:
          schema:
            $ref: '#/components/schemas/Error'
          example:
            error: "conflict"
            message: "Email already exists"
            requestId: "abc-123"
            timestamp: "2025-01-20T10:00:00Z"

    ValidationError:
      description: Validation error - Invalid input data
      content:
        application/json:
          schema:
            $ref: '#/components/schemas/Error'
          example:
            error: "validation_error"
            message: "Request validation failed"
            requestId: "abc-123"
            timestamp: "2025-01-20T10:00:00Z"
            details:
              - field: "email"
                message: "Invalid email format"
                code: "INVALID_FORMAT"
              - field: "password"
                message: "Password must be at least 8 characters"
                code: "TOO_SHORT"

    RateLimitError:
      description: Too many requests - Rate limit exceeded
      headers:
        X-RateLimit-Limit:
          schema:
            type: integer
          description: Request limit per window
          example: 100
        X-RateLimit-Remaining:
          schema:
            type: integer
          description: Requests remaining in current window
          example: 0
        X-RateLimit-Reset:
          schema:
            type: integer
          description: Unix timestamp when limit resets
          example: 1642694400
        Retry-After:
          schema:
            type: integer
          description: Seconds until rate limit resets
          example: 3600
      content:
        application/json:
          schema:
            $ref: '#/components/schemas/Error'
          example:
            error: "rate_limit_exceeded"
            message: "Too many requests. Please try again in 3600 seconds."
            requestId: "abc-123"
            timestamp: "2025-01-20T10:00:00Z"

    InternalServerError:
      description: Internal server error
      content:
        application/json:
          schema:
            $ref: '#/components/schemas/Error'
          example:
            error: "internal_error"
            message: "An unexpected error occurred"
            requestId: "abc-123"
            timestamp: "2025-01-20T10:00:00Z"
```

---

## Path Definitions

### Complete Endpoint Example

```yaml
paths:
  /users:
    get:
      summary: List users
      description: |
        Retrieve a paginated list of users with optional filtering and sorting.

        ## Filtering
        Filter results using query parameters:
        - `role`: Filter by user role (admin, user, guest)
        - `status`: Filter by account status
        - `search`: Search in name and email fields

        ## Sorting
        Use `sort` parameter with field names. Prefix with `-` for descending:
        - `sort=createdAt`: Oldest first
        - `sort=-createdAt`: Newest first
        - `sort=name,-createdAt`: By name, then newest first

        ## Pagination
        Use `page` and `limit` parameters:
        - Default: page=1, limit=20
        - Maximum limit: 100

        ## Permissions
        Requires `read:users` permission (admin role).
      operationId: listUsers
      tags:
        - Users
      security:
        - bearerAuth: []
      parameters:
        - $ref: '#/components/parameters/PageParam'
        - $ref: '#/components/parameters/LimitParam'
        - $ref: '#/components/parameters/SortParam'
        - name: role
          in: query
          description: Filter by user role
          required: false
          schema:
            type: string
            enum: [admin, user, guest]
          example: "admin"
        - name: search
          in: query
          description: Search in name and email fields
          required: false
          schema:
            type: string
          example: "john"
      responses:
        '200':
          description: Successful response
          headers:
            X-RateLimit-Limit:
              schema:
                type: integer
              description: Request limit per hour
              example: 1000
            X-RateLimit-Remaining:
              schema:
                type: integer
              description: Requests remaining
              example: 950
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/PaginatedUsers'
              examples:
                success:
                  summary: Successful response with users
                  value:
                    data:
                      - id: "123e4567-e89b-12d3-a456-426614174000"
                        email: "admin@example.com"
                        name: "Admin User"
                        role: "admin"
                        avatar: "https://example.com/avatars/admin.jpg"
                        createdAt: "2025-01-20T10:00:00Z"
                        updatedAt: "2025-01-20T10:00:00Z"
                      - id: "223e4567-e89b-12d3-a456-426614174001"
                        email: "user@example.com"
                        name: "Regular User"
                        role: "user"
                        avatar: null
                        createdAt: "2025-01-21T10:00:00Z"
                        updatedAt: "2025-01-21T10:00:00Z"
                    pagination:
                      page: 1
                      limit: 20
                      total: 150
                      totalPages: 8
                      hasNext: true
                      hasPrev: false
        '401':
          $ref: '#/components/responses/UnauthorizedError'
        '403':
          $ref: '#/components/responses/ForbiddenError'
        '422':
          $ref: '#/components/responses/ValidationError'
        '429':
          $ref: '#/components/responses/RateLimitError'
        '500':
          $ref: '#/components/responses/InternalServerError'

    post:
      summary: Create user
      description: |
        Create a new user account.

        ## Validation Rules
        - Email must be unique
        - Password must be at least 8 characters
        - Name is required

        ## Permissions
        Requires `create:users` permission (admin role).

        ## Response
        Returns the created user object with a `Location` header
        pointing to the new resource.
      operationId: createUser
      tags:
        - Users
      security:
        - bearerAuth: []
      requestBody:
        required: true
        description: User data to create
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/CreateUserRequest'
            examples:
              adminUser:
                summary: Create admin user
                value:
                  email: "admin@example.com"
                  name: "Admin User"
                  password: "securePassword123"
                  role: "admin"
              regularUser:
                summary: Create regular user
                value:
                  email: "user@example.com"
                  name: "Regular User"
                  password: "securePassword123"
      responses:
        '201':
          description: User created successfully
          headers:
            Location:
              schema:
                type: string
              description: URL of the created user
              example: "/users/123e4567-e89b-12d3-a456-426614174000"
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/User'
              example:
                id: "123e4567-e89b-12d3-a456-426614174000"
                email: "newuser@example.com"
                name: "New User"
                role: "user"
                avatar: null
                createdAt: "2025-01-20T10:00:00Z"
                updatedAt: "2025-01-20T10:00:00Z"
        '400':
          $ref: '#/components/responses/BadRequestError'
        '401':
          $ref: '#/components/responses/UnauthorizedError'
        '403':
          $ref: '#/components/responses/ForbiddenError'
        '409':
          $ref: '#/components/responses/ConflictError'
        '422':
          $ref: '#/components/responses/ValidationError'
        '500':
          $ref: '#/components/responses/InternalServerError'
```

---

## Best Practices

### Documentation Quality

1. **Clear Descriptions**: Explain what each endpoint does and why
2. **Examples**: Provide realistic examples for all requests/responses
3. **Permissions**: Document required permissions
4. **Error Cases**: Document all possible error responses
5. **Validation Rules**: Explain validation constraints
6. **Rate Limits**: Document rate limiting policies

### Schema Design

1. **Use $ref**: Avoid duplication by referencing shared schemas
2. **Mark readOnly**: Fields like `id`, `createdAt` should be readOnly
3. **Provide Defaults**: Specify default values where applicable
4. **Constraints**: Add min/max lengths, patterns, enums
5. **Descriptions**: Explain what each field represents
6. **Examples**: Include realistic example values

### Maintainability

1. **Consistent Naming**: Use same conventions throughout
2. **Versioning**: Plan for API evolution
3. **Deprecation**: Mark deprecated endpoints with `deprecated: true`
4. **Tags**: Group related endpoints
5. **Operation IDs**: Provide unique operation IDs for code generation

---

## Validation

### OpenAPI Validator

```bash
# Install validator
npm install -g @apidevtools/swagger-cli

# Validate specification
swagger-cli validate openapi.yaml

# Bundle into single file (resolve $refs)
swagger-cli bundle openapi.yaml -o openapi-bundled.yaml
```

---

## Best Practices Checklist

- [ ] All endpoints documented
- [ ] All parameters described
- [ ] All request bodies defined
- [ ] All responses documented (success + errors)
- [ ] Schemas use $ref for reusability
- [ ] Examples provided for requests/responses
- [ ] Security requirements specified
- [ ] Rate limiting documented
- [ ] Pagination explained
- [ ] Validation rules documented
- [ ] Permissions documented
- [ ] Tags used for grouping
- [ ] Contact info provided
- [ ] Servers defined (prod/staging/dev)
- [ ] Specification validates successfully

---

**Version**: 1.0
**Last Updated**: January 2025
**Use Cases**: OpenAPI 3.0 specification generation, API documentation
