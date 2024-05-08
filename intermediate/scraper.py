# Requirements: requests, beautifulsoup4
# Difficulty: V

import requests
from bs4 import BeautifulSoup

response = requests.get('http://quotes.toscrape.com')
soup = BeautifulSoup(response.text, 'html.parser')
quotes = soup.find_all('div', class_='quote')

print("=====================================\nTop 5 quotes from http://quotes.toscrape.com\n=====================================")

for quote in quotes[:5]:
    text = quote.find('span', class_='text').text
    author = quote.find('small', class_='author').text
    print(f"{text} - {author}")
    print("=====================================")