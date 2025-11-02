# CipherX API Documentation

## 🌐 Base URL

```
Production: https://api.cipherx.io/v1
Staging: https://api-staging.cipherx.io/v1
```

## 🔑 Authentication

CipherX API uses Bearer token authentication.

```bash
curl -H "Authorization: Bearer YOUR_API_KEY" \
     https://api.cipherx.io/v1/wallets
```

### Obtaining an API Key

1. Sign up at [cipherx.io](https://cipherx.io)
2. Navigate to Settings → API Keys
3. Click "Generate New Key"
4. Store securely (displayed only once)

---

## 📊 Endpoints

### Wallet Tracking

#### `GET /wallets/:address`

Get detailed information about a Solana wallet.

**Parameters:**
- `address` (required): Solana wallet address

**Response:**
```json
{
  "address": "7xKXtg2CW87d97TXJSDpbD5jBkheTqA83TZRuJosgAsU",
  "balance": 1234.56,
  "isWhale": true,
  "riskScore": 0.23,
  "transactionCount": 4821,
  "firstSeen": "2024-01-15T10:30:00Z",
  "lastActivity": "2025-11-01T14:22:30Z",
  "tags": ["whale", "early-adopter", "high-activity"]
}
```

#### `POST /wallets/track`

Start tracking a wallet for real-time alerts.

**Request Body:**
```json
{
  "address": "7xKXtg2CW87d97TXJSDpbD5jBkheTqA83TZRuJosgAsU",
  "alerts": {
    "minTransaction": 10000,
    "newTokens": true,
    "largeTransfers": true
  }
}
```

**Response:**
```json
{
  "success": true,
  "trackingId": "track_abc123def456",
  "webhook": "https://api.cipherx.io/webhooks/track_abc123def456"
}
```

#### `DELETE /wallets/track/:trackingId`

Stop tracking a wallet.

---

### AI Signals

#### `GET /signals`

Get latest AI-generated trading signals.

**Query Parameters:**
- `token` (optional): Filter by token symbol (e.g., "BONK")
- `minConfidence` (optional): Minimum confidence score (0-1)
- `limit` (optional): Number of results (default: 20, max: 100)

**Response:**
```json
{
  "signals": [
    {
      "id": "sig_xyz789",
      "token": {
        "symbol": "BONK",
        "address": "DezXAZ8z7PnrnRJjz3wXBoRgixCa6xjnB7YaB1pPB263",
        "name": "Bonk"
      },
      "action": "BUY",
      "confidence": 0.87,
      "targetPrice": 0.000012,
      "stopLoss": 0.0000095,
      "timeframe": "4h",
      "reasoning": "AI detected accumulation pattern with whale wallet activity",
      "createdAt": "2025-11-01T15:30:00Z"
    }
  ],
  "pagination": {
    "total": 156,
    "page": 1,
    "perPage": 20
  }
}
```

#### `GET /signals/:id`

Get detailed information about a specific signal.

---

### Market Data

#### `GET /tokens/:address`

Get comprehensive token data.

**Response:**
```json
{
  "address": "DezXAZ8z7PnrnRJjz3wXBoRgixCa6xjnB7YaB1pPB263",
  "symbol": "BONK",
  "name": "Bonk",
  "price": 0.000011,
  "priceChange24h": 12.5,
  "volume24h": 8420000,
  "marketCap": 720000000,
  "holders": 142531,
  "liquidity": 3500000,
  "whaleHoldings": 0.28,
  "riskScore": 0.42,
  "ath": 0.000034,
  "atl": 0.0000008
}
```

#### `GET /tokens/trending`

Get currently trending tokens.

**Query Parameters:**
- `timeframe` (optional): "1h", "24h", "7d" (default: "24h")
- `limit` (optional): Number of results (default: 10, max: 50)

---

### Analytics

#### `GET /analytics/whale-activity`

Get recent whale wallet activity.

**Response:**
```json
{
  "recentTransactions": [
    {
      "signature": "5j7s8...",
      "wallet": "7xKXtg2CW87d97TXJSDpbD5jBkheTqA83TZRuJosgAsU",
      "type": "SWAP",
      "tokenIn": "SOL",
      "tokenOut": "BONK",
      "amountIn": 50000,
      "amountOut": 4545454545,
      "timestamp": "2025-11-01T15:45:23Z",
      "impact": "HIGH"
    }
  ]
}
```

---

## 🔌 WebSocket API

Real-time data streaming via WebSocket.

```javascript
const ws = new WebSocket('wss://api.cipherx.io/v1/stream');

ws.onopen = () => {
  // Authenticate
  ws.send(JSON.stringify({
    type: 'auth',
    token: 'YOUR_API_KEY'
  }));
  
  // Subscribe to whale alerts
  ws.send(JSON.stringify({
    type: 'subscribe',
    channels: ['whale-alerts', 'price-updates']
  }));
};

ws.onmessage = (event) => {
  const data = JSON.parse(event.data);
  console.log('Received:', data);
};
```

### Available Channels
- `whale-alerts`: Large wallet transactions
- `price-updates`: Real-time price changes
- `new-tokens`: Newly launched tokens
- `ai-signals`: New AI trading signals
- `market-events`: Significant market movements

---

## 📈 Rate Limits

| Tier | Requests/Minute | WebSocket Connections |
|------|----------------|----------------------|
| Free | 60 | 1 |
| Pro | 600 | 5 |
| Enterprise | Unlimited | 50 |

**Rate Limit Headers:**
```
X-RateLimit-Limit: 600
X-RateLimit-Remaining: 587
X-RateLimit-Reset: 1635789600
```

---

## ❌ Error Codes

```json
{
  "error": {
    "code": "INVALID_ADDRESS",
    "message": "The provided wallet address is invalid",
    "details": "Address must be a valid base58 Solana address"
  }
}
```

| Code | Description |
|------|-------------|
| `UNAUTHORIZED` | Invalid or missing API key |
| `RATE_LIMIT_EXCEEDED` | Too many requests |
| `INVALID_ADDRESS` | Invalid wallet/token address |
| `RESOURCE_NOT_FOUND` | Requested resource doesn't exist |
| `INTERNAL_ERROR` | Server error (we're notified) |

---

## 🧪 Example: Full Trading Flow

```python
import requests

API_KEY = "your_api_key_here"
BASE_URL = "https://api.cipherx.io/v1"
headers = {"Authorization": f"Bearer {API_KEY}"}

# 1. Get AI signals
signals = requests.get(
    f"{BASE_URL}/signals",
    headers=headers,
    params={"minConfidence": 0.8}
).json()

best_signal = signals["signals"][0]
print(f"AI recommends: {best_signal['action']} {best_signal['token']['symbol']}")

# 2. Get token details
token = requests.get(
    f"{BASE_URL}/tokens/{best_signal['token']['address']}",
    headers=headers
).json()

# 3. Check whale activity
whales = requests.get(
    f"{BASE_URL}/analytics/whale-activity",
    headers=headers,
    params={"token": token["address"]}
).json()

# 4. Track wallet
tracking = requests.post(
    f"{BASE_URL}/wallets/track",
    headers=headers,
    json={
        "address": whales["recentTransactions"][0]["wallet"],
        "alerts": {"minTransaction": 10000}
    }
).json()

print(f"Now tracking: {tracking['trackingId']}")
```

---

## 📚 SDKs

Official SDKs available:
- **Python**: `pip install cipherx-sdk`
- **JavaScript**: `npm install @cipherx/sdk`
- **Go**: `go get github.com/cipherx/cipherx-go`

```javascript
// JavaScript Example
import CipherX from '@cipherx/sdk';

const client = new CipherX({ apiKey: 'YOUR_API_KEY' });

const signals = await client.signals.list({ minConfidence: 0.8 });
console.log(signals);
```

---

For more examples, see our [GitHub repository](https://github.com/gotmygat/CipherXGithub).
