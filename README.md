book-cover-color-analysis
=========================

This project analyses the colors used in the book covers of the top twenty books by year on amazon.co.jp from 2000 to 2014.


The folder japanese_cover_project contains a webspider written using the scrapy framework.
To run the spider, run the following command in the top level of japanese_cover_project:

scrapy crawl amazonjp -o itemsBookData.json -t json
