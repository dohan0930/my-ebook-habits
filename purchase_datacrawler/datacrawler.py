#datacrawler.py
#crawl my purchase data from RIDIBOOKS(https://ridibooks.com/library/)

import requests
from bs4 import BeautifulSoup as bs

URL = 'https://ridibooks.com/account/login?return_url=http%3A%2F%2Fridibooks.com%2Flibrary%2F'

LOGIN_INFO = {
		'user_id' : 'dohan0930',
		'password' : '######################',
#		'auto_login' : '1'
}

with requests.Session() as login_try :
	login_request = login_try.post(URL, data=LOGIN_INFO, allow_redirects=False)
	print(login_request.status_code)
	print(login_request.cookies)
	print(login_request.text)
