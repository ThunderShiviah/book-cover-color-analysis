import requests
from xml.etree import ElementTree as ET


#r = requests.get('http://mkweb.bcgsc.ca/color_summarizer/?xml=1&url=http://ecx.images-amazon.com/images/I/61hx3cWprOL._SL160_PIsitb-sticker-arrow-dp,TopRight,12,-18_SH30_OU09_SL160_.jpg&precision=medium')


url = 'http://mkweb.bcgsc.ca/color_summarizer/?xml=1&url='
website = 'http://ecx.images-amazon.com/images/I/61hx3cWprOL._SL160_PIsitb-sticker-arrow-dp,TopRight,12,-18_SH30_OU09_SL160_.jpg'
url = url + website
url += '&precision=medium'

r = requests.get(url, stream=True)

tree = ET.parse(r.raw)
#print tree
root = tree.getroot()
#print root
items = root.findall('variable')
#print items

#for node in root:
#    for node in node:
#        for node in node:
#            print node

#print node[1:5]

#print r.status_code

#print r.headers

parent_map = dict((c, p) for p in tree.getiterator() for c in p) # creates a parent/child dictionary of the xml



