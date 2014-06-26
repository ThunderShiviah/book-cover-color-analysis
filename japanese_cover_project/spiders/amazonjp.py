from scrapy.selector import Selector
#from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.spider import BaseSpider
from japanese_cover_project.items import JapaneseCoverProjectItem
import re

# to run use the following command in the top directory
# scrapy crawl amazonjp -o itemsBookData.json

class AmazonjpSpider(BaseSpider):
    scrape_number = 2014
    name = 'amazonjp'
    allowed_domains = ['http://www.amazon.co.jp']
    start_urls = ['http://www.amazon.co.jp/gp/bestsellers/%d/books/' %n for n in range(2000,scrape_number)]

  
  #  rules = (
 #       Rule(SgmlLinkExtractor(allow=r'Items/'), callback='parse_item', follow=True),
  #  )

    def parse(self, response):
        sel = Selector(response)
        items = []
        i = JapaneseCoverProjectItem()
        i['id_number'] = response.url
        i['title'] = sel.xpath('//div[@class="zg_title"]/a/text()').extract()
        i['rank'] = sel.xpath('//span[@class="zg_rankNumber"]/text()').extract()
        i['book_cover_url'] = sel.xpath('//div[@class="zg_itemImage_normal"]//@src').extract()
        items.append(i)
        print i
        return i
