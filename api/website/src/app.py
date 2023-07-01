from fastapi import FastAPI
from dotenv import load_dotenv
import openai

from scrapy.crawler import CrawlerProcess, Crawler
from scrapy.utils.project import get_project_settings
from scrapy import signals

from pydantic import BaseModel
from scraper.scraper.spiders.web import WebSpider, WebItem



env = load_dotenv("../.env")
openai.api_key = env['OPENAI_API_KEY']

app = FastAPI()


# response model
class Res(BaseModel):
    url: str
    info: str


@app.get("/scrape", status_code=200)
async def scrape(url: str, job_desc: str) -> Res:

    settings = get_project_settings()
    item: WebItem | None = None

    # helper function
    def updateItem(i, response, spider):
        global item
        item = i

    crawler = Crawler(WebSpider(url))
    crawler.signals.connect(updateItem, signal=signals.item_scraped)
    process = CrawlerProcess(settings)
    process.crawl(crawler)
    process.start()

    # set up openai smart extraction

    completion = openai.ChatCompletion.create(
        model='gpt-3.5-turbo',
        messages = [
            { "role": "system", "content": "You are a reader who extracts information from a webpage based on its relevance to a specific job. You will be provided with a job description and a blob of text extracted from a website. Use the text and extract information considered important and relevant according to the job description. Return your processed information in bullet point format, organized with headers for different topics." },
            { "role": "user", "content": f"Job Description: {job_desc} \n\nExtracted Text from Webpage: {item['text']}" }
        ],
        temperature=0.3
    )

    out = completion.choices[0].message.content

    return { "url": url, "info": out }