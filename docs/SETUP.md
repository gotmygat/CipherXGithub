# CipherX Setup Guide

## 📋 Prerequisites

Before setting up CipherX, ensure you have the following installed:

### Required Software
- **Node.js**: >= 18.x ([Download](https://nodejs.org/))
- **Python**: >= 3.10 ([Download](https://python.org/))
- **PostgreSQL**: >= 14 ([Download](https://postgresql.org/))
- **Redis**: >= 7.x ([Download](https://redis.io/))
- **Git**: Latest version

### Recommended Tools
- **Docker**: For containerized development
- **VS Code**: With recommended extensions
- **Postman**: For API testing

---

## 🚀 Quick Start (Development)

### 1. Clone the Repository

```bash
git clone https://github.com/gotmygat/CipherXGithub.git
cd CipherXGithub
```

### 2. Environment Setup

Create environment files:

```bash
# Root environment
cp .env.example .env

# Bot environment
cp bot/.env.example bot/.env

# Extension environment
cp extension/.env.example extension/.env
```

Edit `.env` files with your configuration:

```bash
# .env
DATABASE_URL=postgresql://user:password@localhost:5432/cipherx
REDIS_URL=redis://localhost:6379
JWT_SECRET=your_super_secret_jwt_key
HELIUS_API_KEY=your_helius_api_key
CHAINLINK_RPC=https://your-chainlink-node.io
SOLANA_RPC=https://api.mainnet-beta.solana.com
```

### 3. Install Dependencies

#### Telegram Bot
```bash
cd bot
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

#### Chrome Extension
```bash
cd extension
npm install
```

#### API Server (if included)
```bash
cd api
npm install
```

### 4. Database Setup

```bash
# Create PostgreSQL database
createdb cipherx

# Run migrations
npm run migrate

# Seed test data (optional)
npm run seed
```

### 5. Start Services

#### Terminal 1: Redis
```bash
redis-server
```

#### Terminal 2: Telegram Bot
```bash
cd bot
source venv/bin/activate
python main.py
```

#### Terminal 3: Chrome Extension (Dev Mode)
```bash
cd extension
npm run dev
```

#### Terminal 4: API Server (if applicable)
```bash
cd api
npm run dev
```

---

## 🐳 Docker Setup (Recommended)

### Quick Start with Docker Compose

```bash
# Build and start all services
docker-compose up -d

# View logs
docker-compose logs -f

# Stop services
docker-compose down
```

### Docker Compose Configuration

The `docker-compose.yml` includes:
- PostgreSQL database
- Redis cache
- Telegram bot service
- API server
- Extension build container

---

## 🤖 Telegram Bot Setup

### 1. Create Bot with BotFather

1. Open Telegram and search for `@BotFather`
2. Send `/newbot` command
3. Follow prompts to set bot name and username
4. Copy the API token provided

### 2. Configure Bot

Add token to `bot/.env`:

```bash
TELEGRAM_BOT_TOKEN=1234567890:ABCdefGHIjklMNOpqrsTUVwxyz
TELEGRAM_WEBHOOK_URL=https://your-domain.com/webhook
```

### 3. Set Bot Commands

```bash
cd bot
python setup_commands.py
```

This configures the bot's command menu in Telegram.

### 4. Run Bot

```bash
python main.py
```

---

## 🧩 Chrome Extension Setup

### Development Mode

1. Build the extension:
```bash
cd extension
npm run build:dev
```

2. Load in Chrome:
   - Open `chrome://extensions`
   - Enable "Developer mode"
   - Click "Load unpacked"
   - Select the `extension/dist` folder

3. Pin extension to toolbar for easy access

### Production Build

```bash
npm run build:prod
```

Creates optimized production bundle in `dist/` folder.

---

## 🔑 API Keys Setup

### Required Services

#### 1. Helius API
- Sign up at [helius.dev](https://helius.dev)
- Create new project
- Copy API key to `.env`

```bash
HELIUS_API_KEY=your_api_key_here
```

#### 2. Solana RPC
- Use public endpoint (rate limited):
```bash
SOLANA_RPC=https://api.mainnet-beta.solana.com
```

- Or use private RPC (recommended):
  - [QuickNode](https://quicknode.com)
  - [GenesysGo](https://genesysgo.com)
  - [Triton](https://triton.one)

#### 3. Chainlink Oracle (Optional)
- For advanced price feeds
- Contact Chainlink for API access

---

## 🗄️ Database Configuration

### PostgreSQL Setup

```sql
-- Create database
CREATE DATABASE cipherx;

-- Create user
CREATE USER cipherx_user WITH PASSWORD 'secure_password';

-- Grant privileges
GRANT ALL PRIVILEGES ON DATABASE cipherx TO cipherx_user;
```

### Run Migrations

```bash
# Using npm scripts
npm run migrate:latest

# Using knex directly
npx knex migrate:latest

# Rollback (if needed)
npx knex migrate:rollback
```

### Database Schema

Tables created:
- `users`: User accounts and preferences
- `wallets`: Tracked wallet addresses
- `signals`: AI-generated trading signals
- `transactions`: Cached blockchain transactions
- `alerts`: User alert configurations
- `api_keys`: API key management

---

## 🧪 Testing

### Run Tests

```bash
# All tests
npm test

# Unit tests only
npm run test:unit

# Integration tests
npm run test:integration

# E2E tests
npm run test:e2e

# Coverage report
npm run test:coverage
```

### Test Environment

Tests use separate test database:

```bash
# .env.test
DATABASE_URL=postgresql://user:password@localhost:5432/cipherx_test
REDIS_URL=redis://localhost:6379/1
```

---

## 🔧 Configuration

### Bot Configuration

Edit `bot/config.py`:

```python
# Alert thresholds
WHALE_THRESHOLD = 100000  # SOL
LARGE_TX_THRESHOLD = 50000  # SOL

# Update intervals
PRICE_UPDATE_INTERVAL = 60  # seconds
WALLET_SCAN_INTERVAL = 300  # seconds

# AI model settings
MODEL_CONFIDENCE_THRESHOLD = 0.7
MAX_SIGNALS_PER_HOUR = 10
```

### Extension Configuration

Edit `extension/src/config.ts`:

```typescript
export const config = {
  apiBaseUrl: 'https://api.cipherx.io/v1',
  wsUrl: 'wss://api.cipherx.io/v1/stream',
  updateInterval: 5000, // ms
  maxCachedTokens: 100,
  enableNotifications: true,
};
```

---

## 🚀 Production Deployment

### Environment Variables

Set production environment variables:

```bash
NODE_ENV=production
DATABASE_URL=your_production_db_url
REDIS_URL=your_production_redis_url
JWT_SECRET=strong_random_secret
API_RATE_LIMIT=1000
LOG_LEVEL=info
```

### Build for Production

```bash
# API
cd api && npm run build

# Extension
cd extension && npm run build:prod

# Bot
cd bot && pip install -r requirements.txt
```

### Deployment Checklist

- [ ] Set all environment variables
- [ ] Run database migrations
- [ ] Enable SSL/TLS certificates
- [ ] Configure firewall rules
- [ ] Set up monitoring and alerting
- [ ] Configure backup strategy
- [ ] Enable rate limiting
- [ ] Set up CDN (if applicable)
- [ ] Test all endpoints
- [ ] Enable logging

---

## 📊 Monitoring Setup

### Application Monitoring

Install monitoring tools:

```bash
npm install @sentry/node @sentry/profiling-node
```

Configure Sentry:

```javascript
import * as Sentry from '@sentry/node';

Sentry.init({
  dsn: process.env.SENTRY_DSN,
  tracesSampleRate: 1.0,
});
```

### Health Checks

API health endpoint: `GET /health`

```json
{
  "status": "ok",
  "timestamp": "2025-11-01T15:30:00Z",
  "services": {
    "database": "ok",
    "redis": "ok",
    "solana": "ok"
  }
}
```

---

## 🐛 Troubleshooting

### Common Issues

#### Port Already in Use
```bash
# Find process using port
lsof -i :3000

# Kill process
kill -9 PID
```

#### Database Connection Failed
```bash
# Check PostgreSQL is running
pg_isready

# Restart PostgreSQL
sudo service postgresql restart
```

#### Redis Connection Failed
```bash
# Check Redis is running
redis-cli ping

# Start Redis
redis-server
```

#### Bot Not Responding
- Verify bot token is correct
- Check internet connection
- Ensure webhook URL is accessible
- Review bot logs: `tail -f logs/bot.log`

---

## 📚 Additional Resources

- [API Documentation](./API.md)
- [Architecture Overview](./ARCHITECTURE.md)
- [Contributing Guidelines](../CONTRIBUTING.md)
- [Security Policy](../SECURITY.md)

---

## 💬 Support

Need help? Reach out:

- **Discord**: [Join our server](https://discord.gg/cipherx)
- **Telegram**: [@CipherXSupport](https://t.me/CipherXSupport)
- **Email**: support@cipherx.com
- **GitHub Issues**: [Report a bug](https://github.com/gotmygat/CipherXGithub/issues)

---

**Last Updated**: November 1, 2025
