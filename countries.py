import requests
from bs4 import BeautifulSoup

url = "https://olympics.com/en/olympic-games/tokyo-2020/medals"

headers = {
    # 'Accept-Encoding': 'gzip, deflate, br, sdch',
    # 'Accept-Language': 'en-GB,en;q=0.8,en-US;q=0.6,ml;q=0.4',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)',
    # 'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    # 'Referer': 'https://www.google.com/',
    # 'Connection': 'keep-alive',
}


try:
    print('Scraping Countries from Olympics.com')
    response = requests.get(url, headers)
    # response = requests.get("https://google.com", headers)
except requests.exceptions.RequestException as e:
    print('Error Occured')
    print(e)
# print('Scraping Countries from Olympics.com')
# response = requests.get(url, headers)
# response = requests.get("https://google.com", headers)

print('Parsing the response')
soup = BeautifulSoup(response.text, 'lxml')

countries = soup.find_all('span', {'data-cy': 'country-name'})
for country in countries:
    print(country.text)
    print('------------------')

print('Done')