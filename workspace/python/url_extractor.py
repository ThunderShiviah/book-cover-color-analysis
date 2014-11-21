import sys
import json
from lxml import html
import requests

f = open('json_good.json')
json_object = json.load(f)

color_list = []
for year in range(0,13):                #This is inelegant. Fix it.
    for i in range(0,1):
        url = 'http://mkweb.bcgsc.ca/color_summarizer/?xml=1&url='
        website = json_object['key'][year]['book_cover_url'][i]
        url = url + website
        url += '&precision=medium'
        page = requests.get(url)
        tree = html.fromstring(page.text)
        color_list.append(tree.xpath('variable[@name="rgb"]/statistic[@name="avg"]//text()')[1])
        print tree.xpath('variable[@name="rgb"]/statistic[@name="avg"]//text()')[1]
#return(color_list)

colors_file = open('colors.txt', 'w') 

for item in color_list:
    print>>colors_file, item  #outputs avg rgb values to a colors.txt file.
