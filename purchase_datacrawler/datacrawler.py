#datacrawler.py
#crawl my purchase data from RIDIBOOKS(https://ridibooks.com/library/)

import requests
URL = 'https://ridibooks.com/library'
response = requests.get(URL)
print(response.status_code)
print(response.text)
