# System Architecture Diagrams

Collection of Mermaid diagrams for documenting system architecture.

## High-Level System Architecture

```mermaid
graph TB
    subgraph "Client Layer"
        Web[Web App]
        Mobile[Mobile App]
        API_Client[API Consumers]
    end

    subgraph "Edge Layer"
        CDN[CDN]
        LB[Load Balancer]
    end

    subgraph "Application Layer"
        GW[API Gateway]
        Auth[Auth Service]
        API1[API Server 1]
        API2[API Server 2]
        API3[API Server 3]
    end

    subgraph "Data Layer"
        Cache[(Redis Cache)]
        DB_Primary[(PostgreSQL Primary)]
        DB_Replica[(PostgreSQL Replica)]
        Queue[Message Queue]
    end

    subgraph "Storage Layer"
        S3[Object Storage]
    end

    subgraph "External Services"
        Email[Email Service]
        Payment[Payment Gateway]
        Analytics[Analytics]
    end

    Web --> CDN
    Mobile --> LB
    API_Client --> LB
    CDN --> LB
    LB --> GW
    GW --> Auth
    GW --> API1
    GW --> API2
    GW --> API3
    API1 --> Cache
    API2 --> Cache
    API3 --> Cache
    API1 --> DB_Primary
    API2 --> DB_Primary
    API3 --> DB_Primary
    DB_Primary -.Replication.-> DB_Replica
    API1 --> Queue
    API2 --> Queue
    API3 --> Queue
    API1 --> S3
    Queue --> Email
    API1 --> Payment
    API1 --> Analytics

    style Web fill:#e1f5ff
    style Mobile fill:#e1f5ff
    style API_Client fill:#e1f5ff
    style GW fill:#fff4e1
    style Auth fill:#fff4e1
    style Cache fill:#ffe1f5
    style DB_Primary fill:#ffe1f5
    style DB_Replica fill:#ffe1f5
```

## Data Flow Sequence

```mermaid
sequenceDiagram
    participant Client
    participant CDN
    participant LoadBalancer
    participant APIGateway
    participant AuthService
    participant APIServer
    participant Cache
    participant Database
    participant Queue

    Client->>CDN: Request static asset
    CDN-->>Client: Return cached asset

    Client->>LoadBalancer: API Request
    LoadBalancer->>APIGateway: Forward request
    APIGateway->>AuthService: Validate JWT
    AuthService-->>APIGateway: Token valid

    APIGateway->>APIServer: Authenticated request
    APIServer->>Cache: Check cache
    alt Cache hit
        Cache-->>APIServer: Return cached data
    else Cache miss
        APIServer->>Database: Query data
        Database-->>APIServer: Return data
        APIServer->>Cache: Store in cache
    end

    APIServer->>Queue: Publish event (async)
    APIServer-->>APIGateway: Response
    APIGateway-->>LoadBalancer: Response
    LoadBalancer-->>Client: Response

    Queue->>EmailService: Process async task
```

## Deployment Architecture

```mermaid
graph LR
    subgraph "Production Environment - Region: US-East"
        subgraph "Availability Zone 1"
            App1[API Server 1]
            DB1[(Primary DB)]
            Cache1[(Redis Primary)]
        end
        subgraph "Availability Zone 2"
            App2[API Server 2]
            DB2[(Replica DB)]
            Cache2[(Redis Replica)]
        end
        subgraph "Availability Zone 3"
            App3[API Server 3]
        end

        LB[Load Balancer]
        CDN[CloudFront CDN]
    end

    subgraph "Monitoring & Logging"
        Monitor[CloudWatch]
        Logs[Log Aggregation]
    end

    Users[Users] --> CDN
    CDN --> LB
    LB --> App1
    LB --> App2
    LB --> App3

    App1 --> DB1
    App2 --> DB1
    App3 --> DB1

    DB1 -.Replication.-> DB2

    App1 --> Cache1
    App2 --> Cache1
    App3 --> Cache1

    Cache1 -.Replication.-> Cache2

    App1 -.Metrics.-> Monitor
    App2 -.Metrics.-> Monitor
    App3 -.Metrics.-> Monitor

    App1 -.Logs.-> Logs
    App2 -.Logs.-> Logs
    App3 -.Logs.-> Logs

    style Users fill:#e1f5ff
    style CDN fill:#fff4e1
    style LB fill:#fff4e1
    style DB1 fill:#ffe1e1
    style DB2 fill:#ffe1e1
    style Monitor fill:#e1ffe1
    style Logs fill:#e1ffe1
```

## Microservices Architecture

```mermaid
graph TB
    subgraph "Client"
        Web[Web App]
        Mobile[Mobile App]
    end

    subgraph "API Gateway"
        Gateway[Kong/NGINX]
    end

    subgraph "Services"
        UserService[User Service]
        OrderService[Order Service]
        PaymentService[Payment Service]
        NotificationService[Notification Service]
    end

    subgraph "Data Stores"
        UserDB[(User DB)]
        OrderDB[(Order DB)]
        PaymentDB[(Payment DB)]
    end

    subgraph "Message Bus"
        EventBus[Event Bus - Kafka]
    end

    Web --> Gateway
    Mobile --> Gateway

    Gateway --> UserService
    Gateway --> OrderService
    Gateway --> PaymentService

    UserService --> UserDB
    OrderService --> OrderDB
    PaymentService --> PaymentDB

    OrderService --> EventBus
    PaymentService --> EventBus
    EventBus --> NotificationService

    style UserService fill:#e1f5ff
    style OrderService fill:#ffe1f5
    style PaymentService fill:#fff4e1
    style NotificationService fill:#e1ffe1
```

## Database ER Diagram

```mermaid
erDiagram
    USER ||--o{ POST : creates
    USER ||--o{ COMMENT : writes
    POST ||--o{ COMMENT : has
    POST }o--o{ TAG : "tagged with"

    USER {
        uuid id PK
        string email UK
        string name
        string password_hash
        enum role
        boolean email_verified
        timestamp created_at
        timestamp updated_at
    }

    POST {
        uuid id PK
        uuid user_id FK
        string title
        string slug UK
        text content
        enum status
        timestamp published_at
        int view_count
        jsonb metadata
        timestamp created_at
        timestamp updated_at
    }

    COMMENT {
        uuid id PK
        uuid post_id FK
        uuid user_id FK
        uuid parent_id FK
        text content
        boolean is_approved
        timestamp created_at
        timestamp updated_at
    }

    TAG {
        uuid id PK
        string name UK
        string slug UK
        timestamp created_at
    }

    POST_TAG {
        uuid post_id FK
        uuid tag_id FK
        timestamp created_at
    }
```

## Event-Driven Architecture Flow

```mermaid
graph LR
    subgraph "Event Producers"
        UserService[User Service]
        OrderService[Order Service]
        PaymentService[Payment Service]
    end

    subgraph "Event Bus"
        Kafka[Apache Kafka]
    end

    subgraph "Event Consumers"
        EmailService[Email Service]
        AnalyticsService[Analytics Service]
        AuditService[Audit Service]
    end

    UserService -->|UserCreated| Kafka
    OrderService -->|OrderPlaced| Kafka
    PaymentService -->|PaymentProcessed| Kafka

    Kafka -->|UserCreated| EmailService
    Kafka -->|OrderPlaced| AnalyticsService
    Kafka -->|All Events| AuditService

    EmailService -.Sends.-> SMTP[SMTP Server]
    AnalyticsService -.Writes.-> Warehouse[(Data Warehouse)]
    AuditService -.Writes.-> AuditDB[(Audit DB)]

    style Kafka fill:#fff4e1
    style EmailService fill:#e1f5ff
    style AnalyticsService fill:#ffe1f5
    style AuditService fill:#e1ffe1
```

## CI/CD Pipeline

```mermaid
graph LR
    Dev[Developer] -->|git push| GitHub[GitHub]
    GitHub -->|webhook| CI[CI/CD - GitHub Actions]

    CI -->|1. Test| Tests[Run Tests]
    Tests -->|2. Build| Build[Build Docker Image]
    Build -->|3. Push| Registry[Container Registry]

    Registry -->|4. Deploy| Staging[Staging Environment]
    Staging -->|5. Integration Tests| StagingTests[E2E Tests]

    StagingTests -->|6. Manual Approval| Approval{Approval}
    Approval -->|Approved| Prod[Production Deploy]
    Approval -->|Rejected| Notify[Notify Team]

    Prod -->|Blue-Green Deploy| ProdServers[Production Servers]
    ProdServers -->|Health Check| Monitor[Monitoring]

    style GitHub fill:#e1f5ff
    style CI fill:#fff4e1
    style Staging fill:#ffe1f5
    style Prod fill:#e1ffe1
    style Approval fill:#ffcccc
```

## Notes

- Customize these diagrams based on your specific architecture
- Update regularly as system evolves
- Include in architecture documentation
- Use for onboarding new team members
- Reference in ADRs and design docs
