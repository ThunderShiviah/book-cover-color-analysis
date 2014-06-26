# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

from scrapy.item import Item, Field

class JapaneseCoverProjectItem(Item):
    # define the fields for your item here like:
    # name = Field()
    #pass
    id_number = Field()
    title = Field()
    rank = Field()
    book_cover_url = Field()

    
