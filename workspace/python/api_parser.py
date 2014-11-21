import requests
from lxml import html

"""
Constructs request to a color API and returns the average rgb value.
"""
#r = requests.get('http://mkweb.bcgsc.ca/color_summarizer/?xml=1&url=http://ecx.images-amazon.com/images/I/61hx3cWprOL._SL160_PIsitb-sticker-arrow-dp,TopRight,12,-18_SH30_OU09_SL160_.jpg&precision=medium')


url = 'http://mkweb.bcgsc.ca/color_summarizer/?xml=1&url='
website = 'http://ecx.images-amazon.com/images/I/61hx3cWprOL._SL160_PIsitb-sticker-arrow-dp,TopRight,12,-18_SH30_OU09_SL160_.jpg'
url = url + website
url += '&precision=medium'

page = requests.get(url, stream=True)

tree = html.fromstring(page.text)

rgb_avg = tree.xpath('variable[@name="rgb"]/statistic[@name="avg"]//text()')[1]
print rgb_avg



