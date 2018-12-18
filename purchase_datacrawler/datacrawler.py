#datacrawler.py
#crawl my purchase data from RIDIBOOKS(https://ridibooks.com/library/)

import requests
#from requests.auth import HTTPBasicAuth

URL = 'https://ridibooks.com/account/login'
# print(requests.get(URL, auth=HTTPBasicAuth('dohan0930', '####')))

LOGIN_INFO = {
		'cmd' : 'login',
		'return_url' : '/?genre=general',
		'return_query_string' : '',
		'user_id' : 'dohan0930',
		'password' : '',
#		'device_id' : '',
#		'msg' : ''
}

with requests.Session() as login_try :
	login_request = login_try.post(URL, data=LOGIN_INFO)
	print(login_request.status_code)
	print(login_request.cookies)
	print(login_request.text)
