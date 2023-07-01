import scrapy
import nltk
from items import WebItem

class WebSpider(scrapy.Spider):
    name = 'web'

    def __init__(self, url: str):
        self.start_urls = [ url ]

    def parse(self, response) -> WebItem:
        # get all text on the page
        item = WebItem()
        item['url'] = self.url[0]

        item['text'] = ''.join(response.css('body').extract()).strip()

        return item