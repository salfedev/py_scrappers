import requests
from bs4 import BeautifulSoup

# free practice api
# url = 'https://jsonplaceholder.typicode.com/posts'
url='https://my-json-server.typicode.com/salfedev/JSON-placeholder-Server/posts'
# headers = {
#     'Accept-Encoding': 'gzip, deflate, br, sdch',
#     'Accept-Language': 'en-GB,en;q=0.8,en-US;q=0.6,ml;q=0.4',
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)',
#     'Accept': 'application/json',
#     'Referer': 'https://jsonplaceholder.typicode.com/',
#     'Connection': 'keep-alive',
# }

print('Scraping Quotes from BrainyQuote.com')
# response = requests.get(url, headers)
response = requests.get(url)

print('Parsing the response')
print(response.json())