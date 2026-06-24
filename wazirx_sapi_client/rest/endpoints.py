ENDPOINTS = {
    # Public API Endpoints
    "ping": 'v1/ping',
    "time": 'v1/time',
    "system_status": 'v1/systemStatus',
    "exchange_info": 'v1/exchangeInfo',
    "tickers": 'v1/tickers/24hr',
    "ticker": 'v1/ticker/24hr',
    "depth": 'v1/depth',
    "trades": 'v1/trades',
    "historical_trades": 'v1/historicalTrades',

    "klines": 'v1/klines',

    # Account API Endpoints
    "my_trades": 'v1/myTrades',
    "order": 'v1/order',
    "test_order": 'v1/order/test',
    "open_orders": 'v1/openOrders',
    "all_orders": 'v1/allOrders',
    "account": 'v1/account',
    "funds": 'v1/funds',

    # WebSocket-Client
    "create_auth_token": "v1/create_auth_token",

    # Crypto SAPIs
    "coins": "v1/coins",
    "crypto_withdraws": "v1/crypto/withdraws",
    "crypto_deposit_address": "v1/crypto/deposits/address",

    # Sub-Account
    "sub_account_transfer_history": "v1/sub_account/fund_transfer/history",
    "sub_accounts": "v1/sub_account/accounts",
    "sub_account_fund_transfer": "v1/sub_account/fund_transfer",

}
