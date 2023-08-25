from selenium import webdriver
from bs4 import BeautifulSoup

driver = webdriver.Firefox()

def getHTML(url: str):
    fp = driver.get(url)
    html = fp.page_source
    soup = BeautifulSoup(html, features="html.parser")
    text = soup.get_text()

    return "\n".join(line.strip() for line in text.splitlines() if line)