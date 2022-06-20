import csv
import pandas as pd

def getCommodity(id):

    data = pd.read_csv('listings.csv')
    data = data[data['commodity_id'] == id]
    data = data[data['demand'] > 50000]
    data = data[data['sell_price'] > 15000]

    print(data)

#    with open('listings.csv', mode='r') as csv_file:
#        csv_reader = csv.DictReader(csv_file, delimiter=",")
#        line_count = 0
#
#        for row in csv_reader:
#            if row['id'] == 1:
#                print(row['buy_price'])