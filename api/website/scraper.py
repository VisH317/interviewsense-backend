import requests
from bs4 import BeautifulSoup

def getHTML(url: str):
    fp = requests.get(url).text
    soup = BeautifulSoup(fp, features="html.parser")
    text = soup.get_text()

    return "\n".join(line.strip() for line in text.splitlines() if line)