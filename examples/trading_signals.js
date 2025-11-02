/**
 * Example: Get AI trading signals and execute trades
 */

import CipherX from '@cipherx/sdk';

const client = new CipherX({
  apiKey: process.env.CIPHERX_API_KEY
});

async function main() {
  try {
    // Get latest AI signals with high confidence
    const signals = await client.signals.list({
      minConfidence: 0.8,
      limit: 5
    });
    
    console.log(`📊 Found ${signals.length} high-confidence signals\n`);
    
    for (const signal of signals) {
      console.log(`🎯 Signal #${signal.id}`);
      console.log(`   Token: ${signal.token.symbol}`);
      console.log(`   Action: ${signal.action}`);
      console.log(`   Confidence: ${(signal.confidence * 100).toFixed(1)}%`);
      console.log(`   Target Price: $${signal.targetPrice}`);
      console.log(`   Stop Loss: $${signal.stopLoss}`);
      console.log(`   Reasoning: ${signal.reasoning}`);
      console.log('');
      
      // Get detailed token information
      const token = await client.tokens.get(signal.token.address);
      console.log(`   Current Price: $${token.price}`);
      console.log(`   24h Change: ${token.priceChange24h.toFixed(2)}%`);
      console.log(`   Volume: $${token.volume24h.toLocaleString()}`);
      console.log(`   Market Cap: $${token.marketCap.toLocaleString()}`);
      console.log(`   Risk Score: ${token.riskScore}`);
      console.log('\n---\n');
      
      // Example: Execute trade based on signal
      if (signal.action === 'BUY' && signal.confidence > 0.85) {
        console.log(`⚡ High-confidence BUY signal detected!`);
        console.log(`   Consider purchasing ${signal.token.symbol}`);
        console.log(`   Target: ${signal.targetPrice}`);
        console.log(`   Stop Loss: ${signal.stopLoss}`);
        
        // In production, this would execute actual trade
        // await executeTrade(signal);
      }
    }
    
    // Subscribe to real-time signal updates
    console.log('\n🔄 Subscribing to real-time signals...\n');
    
    const ws = client.stream.connect();
    
    ws.on('signal', (signal) => {
      console.log(`\n🚨 NEW SIGNAL: ${signal.action} ${signal.token.symbol}`);
      console.log(`   Confidence: ${(signal.confidence * 100).toFixed(1)}%`);
      console.log(`   ${signal.reasoning}`);
    });
    
    ws.on('error', (error) => {
      console.error('WebSocket error:', error);
    });
    
  } catch (error) {
    console.error('Error:', error.message);
  }
}

main();
