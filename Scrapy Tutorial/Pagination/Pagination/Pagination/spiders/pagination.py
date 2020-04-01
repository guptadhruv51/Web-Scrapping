import scrapy
from ..items import PaginationItem

class PageItem(scrapy.Spider):
    name='quotes'
    page_number=2
    start_urls=[
        'http://quotes.toscrape.com/page/1/'
    ]

    def parse(self,response):
        items=PaginationItem()
        all_div_quotes=response.css('div.quote')
        for quotes in all_div_quotes:
            title=quotes.css('span.text::text').extract()
            author=quotes.css('.author.text::text').extract()
            tags=quotes.css('.tag::text').extract()

            items['title']=title
            items['author']=author
            items['tags']=tags
            yield items

        next_page='http://quotes.toscrape.com/page/'+str(PageItem.page_number)+'/'
        if PageItem.page_number <11 :
            PageItem.page_number +=1
            yield response.follow(next_page , callback=self.parse)
