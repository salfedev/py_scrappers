import requests
from bs4 import BeautifulSoup

url = "https://www.google.com/doodles"

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)',
}


try:
    print('Scraping Doodles from Google.com')
    response = requests.get(url, headers)
except requests.exceptions.RequestException as e:
    print('Error Occured')
    print(e)

print('Parsing the response')
soup = BeautifulSoup(response.text, 'lxml')

doodles = soup.find_all('li', {'class': 'latest-doodle'})
for doodle in doodles:
    inputs = doodle.find_all('input')
    for input in inputs:
      print(input.get('class')[0] + " : " + input.get('value'))
    print('------------------')

print('Done')