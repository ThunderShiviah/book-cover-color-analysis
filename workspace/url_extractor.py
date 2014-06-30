import sys
import json
from lxml import html
import requests

f = open('json_good.json')
json_object = json.load(f)

list = []
for year in range(0,13):                #This is inelegant. Fix it.
    list.append(json_object['key'][year]['book_cover_url']) 
    # print type(list)
    url_string = ', '.join(map(str, list))
    # print type(url_string)
    
    
i = iter(json_object['key'][year]['book_cover_url'])
item = i.next()
item = i.next()
# print item
print json_object['key'][year]

