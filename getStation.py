import json

def getStationByID():
    id = input('Enter the ID of the Station: ')

    with open ("stations.json", "r") as f:
        data =json.load(f)

    filtered = list(filter(lambda x:x['id']==id,data))

    print (filtered)

    #stationName = dict(filtered[0])['name']

    #print(stationName)

