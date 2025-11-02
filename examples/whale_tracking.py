"""
Example: Track a whale wallet and get alerts
"""

import asyncio
from cipherx import CipherXClient

async def main():
    # Initialize client
    client = CipherXClient(api_key="your_api_key_here")
    
    # Whale wallet to track
    whale_address = "7xKXtg2CW87d97TXJSDpbD5jBkheTqA83TZRuJosgAsU"
    
    # Get wallet information
    wallet = await client.wallets.get(whale_address)
    print(f"Tracking wallet: {wallet.address}")
    print(f"Balance: {wallet.balance} SOL")
    print(f"Risk Score: {wallet.risk_score}")
    print(f"Tags: {', '.join(wallet.tags)}")
    
    # Start tracking with alerts
    tracking = await client.wallets.track(
        address=whale_address,
        alerts={
            "min_transaction": 10000,  # Alert on transactions > 10k SOL
            "new_tokens": True,        # Alert on new token purchases
            "large_transfers": True    # Alert on large transfers
        }
    )
    
    print(f"\n✅ Now tracking wallet!")
    print(f"Tracking ID: {tracking.id}")
    print(f"Webhook URL: {tracking.webhook_url}")
    
    # Listen for webhook events
    async for event in client.webhooks.listen(tracking.webhook_url):
        print(f"\n🚨 Alert: {event.type}")
        print(f"Transaction: {event.signature}")
        print(f"Amount: {event.amount} SOL")
        print(f"Token: {event.token_symbol}")

if __name__ == "__main__":
    asyncio.run(main())
