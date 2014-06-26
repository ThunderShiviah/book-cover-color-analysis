import json
from pprint import pprint
json_data=open('test.json')

data = json.load(json_data)
pprint(data)


json_data.close()

