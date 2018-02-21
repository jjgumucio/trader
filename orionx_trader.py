#!/user/bin/python
import orionx_lib as orionx
import utils
from time import sleep
from os import system

def run():
    print('--- OrionX Experiment ---\n')

    LOGIN_TOKEN = input('Enter login-token --> ')
    USER_ID = input('Enter user id --> ')
    orionx.HEADERS['login-token'] = LOGIN_TOKEN

    SPREAD_TO_OPERATE = int(input('Enter spread to operate --> '))
    CHA_TO_TRADE = int(input('Enter num of CHA to trade --> ')) * pow(10, 8)

    while True:
        print('\n--- Getting orders book ---')
        try:
            orders = orionx.get_market_order_book("CHACLP", 1)
        except Exception as e:
            print('Error getting Orders Book:', e)

        SPREAD = orders['spread']
        MID = orders['mid']
        BUY = utils.get_highest_buy_price(orders['mid'], orders['spread'])
        SELL = utils.get_lowest_sell_price(orders['mid'], orders['spread'])
        BUYING = utils.is_market_buying(
            orders['buy'][0]['accumulated'],
            orders['sell'][0]['accumulated'])
        SELLING = utils.is_market_selling(
            orders['buy'][0]['accumulated'],
            orders['sell'][0]['accumulated'])
        SPREAD_PERCENTAGE = utils.spread_as_price_percentage(MID, SPREAD)

        print('Market Spread:', SPREAD)
        print('Spread as %:', SPREAD_PERCENTAGE)
        print('MID Price:', MID)
        print('Highest Buy Price:', BUY)
        print('Lowest Sell Price:', SELL)
        print('Is the market buying:', BUYING)
        print('Is the market selling:', SELLING)

        try:
            open_orders = orionx.get_orders("CHACLP", USER_ID, 'true', 'false', 10)['items']
            print('Open Orders:', open_orders)
        except Exception as e:
            print('Error getting users orders:', e)

        try:
            wallet = orionx.get_wallet(USER_ID, "CHACLP")
            print('WALLET:', wallet)
        except Exception as e:
            print('Error getting wallet:', e)

        # buy_price = 0
        # if len(open_orders) == 0:
        #     if SPREAD >= SPREAD_TO_OPERATE:
        #         buy_price = BUY + 2
        #         print('PRICE:', buy_price)
        #         try:
        #             buy_order = orionx.place_limit_order('CHACLP', CHA_TO_TRADE, buy_price, 'false')
        #             print('BUY ORDERS PLACED:', buy_order)
        #         except Exception as e:
        #             print('Error placing buy limit order:', e)
        # else if 
        #     if SPREAD >= SPREAD_TO_OPERATE:
        #         sell_price = buy_price + SPREAD - 2
        #         try:
        #             sell_order = orionx.place_limit_order('CHACLP', CHA_TO_TRADE, sell_price, 'true')
        #             print('SELL ORDER:', sell_order)
        #         except Exception as e:
        #             print('Error placing sell limit order:', e)

        sleep(5)

if __name__ == '__main__':
    run()
