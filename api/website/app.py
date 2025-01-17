import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv
import openai
from pydantic import BaseModel
from langchain.text_splitter import RecursiveCharacterTextSplitter

from chain import get_chain_output
from scraper import getHTML



load_dotenv("./.env")
openai.api_key = os.environ['OPENAI_API_KEY']

app = FastAPI()

# cors stuff

origins = [
    "http://localhost:3000"   
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["POST"],
    allow_headers=["*"]
)

class Req(BaseModel):
    url: str
    job_desc: str


# response model
class Res(BaseModel):
    url: str
    info: str


@app.post("/scrape")
async def scrape(info: Req):

    html: str = getHTML(info.url)

    # print("type: ", type(html))

    # splitter = RecursiveCharacterTextSplitter.from_language("html", chunk_size=500, chunk_overlap=30)

    # docs = splitter.create_documents([html])

    output = get_chain_output(html)

    print("output: ", output)

    return { "url": info.url, "output": output }