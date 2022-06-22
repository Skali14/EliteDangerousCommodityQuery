import json
import pandas as pd

def getSystemByID(id):
    
    with open ('systems.json', 'r') as f:
        data =json.load(f)

    filtered = list(filter(lambda x:x["id"]==int(id),data))

    df = pd.DataFrame(filtered, columns=['id','name','needs_permit'])

    print (df)