# bitcoin-streamer

1. Receive streaming bitcoin transaction data from here: https://www.blockchain.com/api/api_websocket
2. Stream the transaction log to Kafka
3. Analyze the transactions in realtime and count the rate of transactions on a given minute, save this in Redis
4. Consume the transactions from a Kafka consumer and persist only the transactions made in the last 3 hours
5. Rest API in any python framework to read from Redis to show the latest transactions
