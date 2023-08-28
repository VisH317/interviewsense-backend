from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')
chrome_options.add_argument('--disable-extensions')
chrome_options.add_argument('--disable-gpu')

capa = DesiredCapabilities.CHROME
capa["pageLoadStrategy"] = "eager"


service = Service(ChromeDriverManager(driver_version='114.0.5735.90').install())

def getHTML(url: str):
    driver = webdriver.Chrome(service=service, options=chrome_options, desired_capabilities=capa)
    fp = driver.get(url)
    print("fp: ", )
    html = driver.page_source
    soup = BeautifulSoup(html, features="html.parser")
    text = soup.get_text()

    driver.close()

    return "\n".join(line.strip() for line in text.splitlines() if line)