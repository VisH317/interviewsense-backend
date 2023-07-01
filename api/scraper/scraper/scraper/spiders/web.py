import scrapy
import nltk

class WebSpider(scrapy.Spider):
    name = 'web'

    def __init__(self, url: str):
        self.start_urls = [ url ]

    def parse(self, response):
        # get all text on the page
        return ''.join(response.css('body').extract()).strip()