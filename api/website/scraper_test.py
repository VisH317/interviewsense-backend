from scraper import getHTML

html: str = getHTML("https://platform.openai.com/docs/guides/speech-to-text")

print(html)