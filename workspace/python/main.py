"""Script to gather and plot average rgb values from amazon book covers."""
import sys
import json
from lxml import html
import requests

def load_json_file(json_object):
    """Loads the scraped json file of amazon book information"""
   
    list = []
    for year in range(0,13):                #This is inelegant. Fix it.
        #print json_object['key'][year]['id_number']
        list.append(json_object['key'][year]['book_cover_url'])
    return list
    pass

def get_avg_rgb(url_list, json_object):
    """Gets average rgb values from book covers by querying a color API using requests"""
    url = 'http://mkweb.bcgsc.ca/color_summarizer/?xml=1&url='
    
    color_list = []
    for year in range(0,13):
         
         for i in range(0,len(json_object['key'][year]['book_cover_url'])):
             url = 'http://mkweb.bcgsc.ca/color_summarizer/?xml=1&url='
             website = json_object['key'][year]['book_cover_url'][i]
             url = url + website
             url += '&precision=medium'

             page = requests.get(url)
             tree = html.fromstring(page.text)
             color_list.append(tree.xpath('variable[@name="rgb"]/statistic[@name="avg"]//text()')[1])
             print tree.xpath('variable[@name="rgb"]/statistic[@name="avg"]//text()')[1]         
    return(color_list)
    pass

def main():
    """Main entry point for the script."""
    f = open('../data/json_good.json')  #Make sure this file is in the right path!
    json_object = json.load(f)
    url_list =  load_json_file(json_object)
      
    get_avg_rgb(url_list, json_object)
    pass


if __name__ == '__main__':
    sys.exit(main())
