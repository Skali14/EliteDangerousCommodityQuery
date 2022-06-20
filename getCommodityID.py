import json
import getCommodity

def getCommodityID():

    name = 'Agronomic Treatment' # input('Enter the name of the commodity: ')

    with open ("commodities.json", "r") as f:
        data =json.load(f)

    filtered = list(filter(lambda x:x["name"]==name,data))

    commodityID = dict(filtered[0])['id']

    print(commodityID)

    getCommodity.getCommodity(commodityID)
