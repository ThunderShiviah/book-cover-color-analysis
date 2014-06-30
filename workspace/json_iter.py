import json

f = open('json_good.json')
json_object = json.load(f)
print type(json_object)
print  json_object['key'][0].keys()
print json_object['key'][0]['id_number']

rank = json_object['key'][13]['rank']

"""
list = []
i = 0
while i != 14:
    list.append(json_object['key'][i]['id_number'])
    i += 1
print list
print len(list)
"""

"""
Generates a list of urls
"""
list = []
i = 0
while i != 14:
    list.append(json_object['key'][i]['book_cover_url'])
    i += 1
print list
print len(list)
