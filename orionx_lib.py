#!/usr/bin/python
import requests

API_URL = 'https://api.orionx.io/graphql'
HEADERS = {
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36',
    'fingerprint': '219e82a5f2507ca3e9e8beb016dfc103',
    'origin': 'https://orionx.io',
    'referer': 'https://orionx.io/exchange/CHACLP',
    'authority': 'api.orionx.io',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'es,en;q=0.9',
    'content-type': 'application/json',
    'accept': '*/*'
}

def log_in_with_password(email, plainPassword):
    "Log in to OrionX"
    mutation = f'''
        mutation {{
            loginWithPassword(email: "{email}" plainPassword: "{plainPassword}") {{
                id
                token
            }}
        }}'''

    return requests.post(API_URL, json={'query': mutation})

def get_market_order_book(market_code, limit=10):
    "Get a markets orders book"
    query = f'''
        {{marketOrderBook(marketCode: "{market_code}", limit: {limit})
            {{
                spread
                mid
                buy {{
                    amount
                    accumulated
                    accumulatedPrice
                }}
                sell {{
                    amount
                    accumulated
                    accumulatedPrice
                }}
            }}
        }}'''

    response = requests.post(API_URL, json={'query': query}).json()
    return response['data']['marketOrderBook']
    

def place_limit_order(market_code, amount, limit_price, is_sell):
    "Place a limit market order"
    mutation = f'''
        mutation {{
            placeLimitOrder(marketCode: "{market_code}", amount: {amount}, limitPrice: {limit_price}, sell: {is_sell}) {{
                _id
                type
                amount
                limitPrice
                sell
                status
            }}
        }}'''

    response = requests.post(API_URL, json={'query': mutation}, headers=HEADERS).json()
    return response['data']['placeLimitOrder']

def cancel_order(order_id):
    mutation = f'''
        mutation {{
            cancelOrder(orderId: "{order_id}") {{
                _id
                type
                amount
                limitPrice
                sell
                status
            }}
        }}'''

    response = requests.post(API_URL, json={'query': mutation}, headers=HEADERS).json()
    return response['data']['cancelOrder']

def get_orders(market_code, user_id, only_open, only_closed, limit=10):
    "Gets the orders book from a user specified by id"
    query = f'''
        query {{
            orders(marketCode: "{market_code}", userId: "{user_id}", onlyOpen: {only_open}, onlyClosed: {only_closed}, limit: {limit}) {{
                items {{
                    sell
                    type
                    amount
                    amountToHold
                    limitPrice
                    status
                    isStop
                }}
            }}
        }}'''

    response = requests.post(API_URL, json={'query': query}, headers=HEADERS).json()
    return response['data']['orders']

def get_market_current_stats(market_code, aggregation):
    query = f'''
        query {{
            marketCurrentStats(marketCode: "{market_code}", aggregation: {aggregation}) {{
                open
                close
                high
                low
                variation
                average
                volume
                fromDate
                toDate
            }}
        }}'''

    return requests.post(API_URL, json={'query': query}, headers=HEADERS)

def get_wallet(user_id, code):
    query = f'''
        query {{
            wallet(code: "{code}", userId: "{user_id}") {{
                currency {{
                    code
                }}
                balance
                availableBalance
            }}
    }}'''
    return requests.post(API_URL, json={'query': query}, headers=HEADERS).json()
    return response['data']['wallet']
