import json
import pandas as pd
import getSystem

def getStationByID():
    id = input('Enter the ID of the Station: ')

    with open ('stations.json', 'r') as f:
        data =json.load(f)

    filtered = list(filter(lambda x:x["id"]==int(id),data))

    df = pd.DataFrame(filtered, columns=['id','name','system_id','max_landing_pad_size','distance_to_star','type'])

    systemID = df.iloc[0]['system_id']

    print(systemID)

    print (df)

    getSystem.getSystemByID(systemID)
