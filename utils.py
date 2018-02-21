#!/user/bin/python
def get_highest_buy_price(mid, spread):
    "Returns the price for the first buying order"
    return mid - int(spread / 2)

def get_lowest_sell_price(mid, spread):
    "Returns the price for the first selling order"
    return mid + int(spread / 2)

def is_market_buying(sell_amount, buy_amount):
    "Return True if the buying volume is higher than the selling volume"
    return buy_amount >= sell_amount

def is_market_selling(sell_amount, buy_amount):
    "Returns True if the selling volume is higher than the buying volume"
    return not is_market_buying(sell_amount, buy_amount)

def spread_as_price_percentage(mid, spread):
    "Returns the spread as a percentage of the mid price"
    return (spread * 100) / mid
