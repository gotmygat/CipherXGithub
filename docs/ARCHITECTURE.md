# CipherX Architecture

## 🏗️ System Overview

CipherX is built on a modern, scalable microservices architecture designed for high-throughput cryptocurrency market analysis and real-time data processing.

```
┌─────────────────────────────────────────────────────────────────┐
│                         Client Layer                             │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐          │
│  │  Web App     │  │ Chrome Ext   │  │ Telegram Bot │          │
│  │  (React)     │  │  (TypeScript)│  │   (Python)   │          │
│  └──────────────┘  └──────────────┘  └──────────────┘          │
└─────────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────────┐
│                      API Gateway Layer                           │
│  ┌──────────────────────────────────────────────────────────┐   │
│  │  AWS API Gateway + CloudFront CDN                        │   │
│  │  • Rate Limiting  • Authentication  • Request Routing    │   │
│  └──────────────────────────────────────────────────────────┘   │
└─────────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────────┐
│                    Application Layer                             │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐          │
│  │  REST API    │  │  GraphQL     │  │  WebSocket   │          │
│  │  (Node.js)   │  │  (Apollo)    │  │  (Socket.io) │          │
│  └──────────────┘  └──────────────┘  └──────────────┘          │
└─────────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────────┐
│                    Business Logic Layer                          │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐          │
│  │  Wallet      │  │  Trading     │  │  Analytics   │          │
│  │  Service     │  │  Service     │  │  Service     │          │
│  └──────────────┘  └──────────────┘  └──────────────┘          │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐          │
│  │  AI/ML       │  │  Alert       │  │  Risk        │          │
│  │  Service     │  │  Service     │  │  Service     │          │
│  └──────────────┘  └──────────────┘  └──────────────┘          │
└─────────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────────┐
│                      Data Layer                                  │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐          │
│  │  PostgreSQL  │  │  MongoDB     │  │  Redis       │          │
│  │  (Relational)│  │  (Documents) │  │  (Cache)     │          │
│  └──────────────┘  └──────────────┘  └──────────────┘          │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐          │
│  │  InfluxDB    │  │  Elasticsearch│  │  S3          │          │
│  │  (Time-Series│  │  (Search)    │  │  (Storage)   │          │
│  └──────────────┘  └──────────────┘  └──────────────┘          │
└─────────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────────┐
│                   External Services Layer                        │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐          │
│  │  Solana RPC  │  │  Helius API  │  │  Chainlink   │          │
│  │  (Blockchain)│  │  (On-chain)  │  │  (Oracles)   │          │
│  └──────────────┘  └──────────────┘  └──────────────┘          │
└─────────────────────────────────────────────────────────────────┘
```

---

## 🧩 Core Components

### 1. API Gateway
**Technology**: AWS API Gateway + CloudFront

**Responsibilities**:
- Request routing and load balancing
- API authentication and authorization
- Rate limiting and throttling
- Request/response transformation
- SSL termination

### 2. REST API Service
**Technology**: Node.js + Express + TypeScript

**Features**:
- RESTful endpoints for wallet tracking, signals, analytics
- JWT-based authentication
- Input validation with Joi
- Async/await error handling
- OpenAPI/Swagger documentation

### 3. GraphQL API Service
**Technology**: Apollo Server + TypeScript

**Benefits**:
- Flexible data fetching (clients request exactly what they need)
- Real-time subscriptions for live data
- Type-safe schema with code generation
- Batching and caching optimizations

### 4. WebSocket Service
**Technology**: Socket.io + Redis adapter

**Use Cases**:
- Real-time price updates
- Whale transaction alerts
- AI signal notifications
- Market event streaming

---

## 🤖 AI/ML Pipeline

```
┌─────────────────────────────────────────────────────────────────┐
│                     Data Ingestion                               │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐          │
│  │  Helius      │  │  Solana RPC  │  │  Chainlink   │          │
│  │  Webhooks    │  │  Polling     │  │  Price Feeds │          │
│  └──────┬───────┘  └──────┬───────┘  └──────┬───────┘          │
└─────────┼──────────────────┼──────────────────┼─────────────────┘
          │                  │                  │
          ▼                  ▼                  ▼
┌─────────────────────────────────────────────────────────────────┐
│                   Message Queue (Kafka)                          │
└─────────────────────────────────────────────────────────────────┘
          │
          ▼
┌─────────────────────────────────────────────────────────────────┐
│                    Data Processing                               │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐          │
│  │  Cleansing   │  │  Enrichment  │  │  Feature     │          │
│  │  (Python)    │  │  (Python)    │  │  Engineering │          │
│  └──────────────┘  └──────────────┘  └──────────────┘          │
└─────────────────────────────────────────────────────────────────┘
          │
          ▼
┌─────────────────────────────────────────────────────────────────┐
│                      ML Models                                   │
│  ┌──────────────────────────────────────────────────────────┐   │
│  │  Price Prediction Model (LSTM + Transformer)             │   │
│  │  • Historical price data                                 │   │
│  │  • Volume patterns                                       │   │
│  │  • Market sentiment                                      │   │
│  └──────────────────────────────────────────────────────────┘   │
│  ┌──────────────────────────────────────────────────────────┐   │
│  │  Whale Behavior Analysis (Random Forest)                │   │
│  │  • Transaction patterns                                  │   │
│  │  • Wallet clustering                                     │   │
│  │  • Time-series analysis                                  │   │
│  └──────────────────────────────────────────────────────────┘   │
│  ┌──────────────────────────────────────────────────────────┐   │
│  │  Risk Scoring Model (XGBoost)                           │   │
│  │  • Liquidity analysis                                    │   │
│  │  • Holder distribution                                   │   │
│  │  • Contract verification                                 │   │
│  └──────────────────────────────────────────────────────────┘   │
└─────────────────────────────────────────────────────────────────┘
          │
          ▼
┌─────────────────────────────────────────────────────────────────┐
│                   Signal Generation                              │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐          │
│  │  Confidence  │  │  Risk/Reward │  │  Alert       │          │
│  │  Scoring     │  │  Calculation │  │  Generation  │          │
│  └──────────────┘  └──────────────┘  └──────────────┘          │
└─────────────────────────────────────────────────────────────────┘
```

### Model Training Pipeline

1. **Data Collection**: Continuous ingestion from Solana blockchain
2. **Feature Engineering**: Create indicators (RSI, MACD, volume profiles, etc.)
3. **Model Training**: Weekly retraining on new data (SageMaker)
4. **Validation**: Backtesting on historical data with walk-forward analysis
5. **Deployment**: Blue-green deployment with A/B testing
6. **Monitoring**: Track prediction accuracy and drift detection

---

## 📊 Data Flow

### Wallet Tracking Flow

```
User Request
    │
    ▼
API Gateway
    │
    ▼
Wallet Service ──────► PostgreSQL (Store subscription)
    │                      │
    │                      ▼
    │                  Redis (Cache wallet data)
    │
    ▼
Helius API ──────────► Create Webhook
    │
    ▼
Transaction Event
    │
    ▼
Webhook Handler
    │
    ├──► Alert Service ──► Send Telegram notification
    │
    ├──► Analytics Service ──► Update metrics
    │
    └──► WebSocket Service ──► Push to connected clients
```

### AI Signal Generation Flow

```
Market Data Ingestion
    │
    ▼
Kafka Topic
    │
    ▼
Stream Processor
    │
    ├──► Feature Store (InfluxDB)
    │
    ▼
ML Model Inference (SageMaker)
    │
    ▼
Signal Validation
    │
    ├──► Confidence > 0.7? ──► Yes ──► Store in PostgreSQL
    │                               │
    │                               ▼
    │                           Publish to Redis Pub/Sub
    │                               │
    │                               ▼
    │                           Alert Service
    │                               │
    │                               ├──► Telegram Bot
    │                               ├──► WebSocket
    │                               └──► Email (Premium users)
    │
    └──► No ──► Log and discard
```

---

## 🔐 Security Architecture

### Authentication Flow

```
Client Request
    │
    ▼
API Gateway
    │
    ├──► Extract JWT from Authorization header
    │
    ▼
JWT Verification
    │
    ├──► Expired? ──► Yes ──► Return 401 Unauthorized
    │
    ├──► Invalid signature? ──► Yes ──► Return 401 Unauthorized
    │
    ▼
Extract User ID & Permissions
    │
    ▼
Check Rate Limit (Redis)
    │
    ├──► Exceeded? ──► Yes ──► Return 429 Too Many Requests
    │
    ▼
Route to Service
    │
    ▼
Service Handler
```

### Encryption

- **At Rest**: AES-256 encryption for sensitive data (PostgreSQL TDE)
- **In Transit**: TLS 1.3 for all external connections
- **API Keys**: bcrypt hashing with per-user salt
- **Secrets**: AWS Secrets Manager for environment variables

---

## ☁️ Infrastructure

### AWS Services Used

- **Compute**: ECS Fargate (containerized services)
- **Database**: RDS PostgreSQL (Multi-AZ), DocumentDB
- **Cache**: ElastiCache Redis (cluster mode)
- **Storage**: S3 (static assets, backups)
- **CDN**: CloudFront (global distribution)
- **Messaging**: SQS, SNS, Kinesis
- **ML**: SageMaker (model training & inference)
- **Monitoring**: CloudWatch, X-Ray
- **Security**: WAF, Shield, Secrets Manager

### High Availability

- **Multi-AZ Deployment**: Services run across 3 availability zones
- **Auto-Scaling**: Horizontal scaling based on CPU/memory metrics
- **Load Balancing**: Application Load Balancer with health checks
- **Failover**: Automatic failover for RDS and ElastiCache
- **Backups**: Automated daily backups with 30-day retention

---

## 📈 Scalability

### Current Capacity
- **API Requests**: 10,000 req/sec
- **WebSocket Connections**: 50,000 concurrent
- **Data Ingestion**: 1M events/sec via Kafka
- **Database**: 10TB PostgreSQL, auto-sharding

### Scaling Strategy
- **Horizontal**: Add more ECS tasks for increased load
- **Vertical**: Upgrade RDS instance class when needed
- **Database**: Read replicas for query distribution
- **Cache**: Redis cluster with sharding for large datasets

---

## 🔄 Deployment Pipeline

```
Code Commit (GitHub)
    │
    ▼
GitHub Actions Workflow
    │
    ├──► Lint & Format (ESLint, Prettier)
    ├──► Unit Tests (Jest, PyTest)
    ├──► Integration Tests
    ├──► Security Scan (Snyk, OWASP)
    │
    ▼
Build Docker Images
    │
    ▼
Push to ECR (AWS Container Registry)
    │
    ▼
Deploy to Staging
    │
    ├──► Smoke Tests
    ├──► Load Tests (k6)
    │
    ▼
Manual Approval
    │
    ▼
Blue-Green Deployment to Production
    │
    ├──► Route 10% traffic to new version
    ├──► Monitor metrics
    ├──► Route 50% traffic
    ├──► Monitor metrics
    │
    ▼
Full Cutover
    │
    ▼
Terminate Old Version
```

---

## 📊 Monitoring & Observability

### Metrics Tracked
- **System**: CPU, memory, disk I/O, network
- **Application**: Request latency, error rates, throughput
- **Business**: Active users, API calls, signals generated
- **ML Models**: Prediction accuracy, inference latency

### Alerting Rules
- Error rate > 1% for 5 minutes
- API latency p99 > 500ms
- Database connections > 80% of max
- ML model accuracy drop > 10%

### Dashboards
- **Operations**: Real-time system health
- **Business**: User metrics and revenue
- **ML**: Model performance and drift detection

---

## 🧪 Testing Strategy

- **Unit Tests**: 80%+ code coverage (Jest, PyTest)
- **Integration Tests**: API endpoint validation
- **E2E Tests**: User flow simulation (Playwright)
- **Load Tests**: 10,000 concurrent users (k6)
- **Chaos Engineering**: Random service failures (Chaos Monkey)

---

For implementation details, see the source code in this repository.
