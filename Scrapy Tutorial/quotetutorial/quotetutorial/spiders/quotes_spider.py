import scrapy
from ..items import QuotetutorialItem

class QouteSpider(scrapy.Spider):
    name='quotes' #name of spider
    start_urls=[
        'http://quotes.toscrape.com/'
    ]
    def parse(self,response):
        item=QuotetutorialItem()
        all_div_quotes=response.css("div.quote") #extract is not used because we want the data inside the class
        for quote in all_div_quotes:
            title=quote.css("span.text::text").extract()
            author=quote.css(".author::text").extract()
            tags=quote.css(".tag::text").extract()

            item['title']=title
            item['author']=author
            item['tags']=tags

            yield item