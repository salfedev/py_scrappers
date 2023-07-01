import requests
from bs4 import BeautifulSoup

url = 'https://www.brainyquote.com/quote_of_the_day'
headers = {
    'Accept-Encoding': 'gzip, deflate, br, sdch',
    'Accept-Language': 'en-GB,en;q=0.8,en-US;q=0.6,ml;q=0.4',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Referer': 'https://www.brainyquote.com/',
    'Connection': 'keep-alive',
}

print('Scraping Quotes from BrainyQuote.com')
response = requests.get(url, headers)

print('Parsing the response')
print(response)
# soup = BeautifulSoup(response.text, 'lxml')

# quotes = soup.find_all('a', {'title': 'view quote'})

# for i in range(0, len(quotes)):
#     print(quotes[i].text)
#     print(authors[i].text)
#     print('')

# # Path: quotes_scrapper.py
