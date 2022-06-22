import pandas as pd

def getCommodity(id):

    direction = input('Do you want to buy or sell the commodity? ')
    quantity = input('How much should be available? ')
    price = input('What price do you want to buy/sell at? ')

    data = pd.read_csv('listings.csv')
    data = data[data['commodity_id'] == id]
    if direction == 'Buy':
        data = data[data['supply'] > int(quantity)]
        data = data[data['buy_price'] < int(price)]
    elif direction == 'Sell':
        data = data[data['demand'] > int(quantity)]
        data = data[data['sell_price'] > int(price)]

    if direction == 'Buy':
        df = pd.DataFrame(data, columns=['station_id','commodity_id','supply','buy_price'])
        df.sort_values(by=['buy_price'], inplace=True)
    elif direction == 'Sell':
        df = pd.DataFrame(data, columns=['station_id','commodity_id','sell_price','demand'])
        df.sort_values(by=['sell_price'], inplace=True, ascending=False)

    print(df)

