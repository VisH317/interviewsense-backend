import requests

if __name__=="__main__":
    res = requests.post("http://localhost:8000/scrape", json={ "url": "https://www.analyticsvidhya.com/machine-learning/", "job_desc": "test" }, headers={"content-type": "application/json"})
    print(res)