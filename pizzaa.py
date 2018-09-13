import json
import pandas as pd

file=open('C://Users//Richa Sharma//Desktop//Pizza//train.json')

data=json.loads(file.read())

data=json.dumps(data,indent=2)

data=pd.read_json(data)

print(data.head())
print(data.columns)

