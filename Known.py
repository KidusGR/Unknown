from requests_html import HTMLSession
import json

session = HTMLSession()

baseurl = "https://api.dictionaryapi.dev/api/v2/entries/en/hello"
Headers = {}
Json = {}


with session as ses:
    res = ses.get(baseurl)
    data = json.loads(res.text)
    print(data[0])