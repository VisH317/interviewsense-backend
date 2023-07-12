import urllib.request

def getHTML(url: str):
    fp = urllib.request.urlopen(url)
    bytes = fp.read()

    html = bytes.decode('utf8')

    fp.close()

    return html