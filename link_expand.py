import praw, obot
import time
import requests, json
# from bs4 import BeautifulSoup

r = obot.login()

already_done = []

while True:
	subr = r.get_subreddit('test')
	for sub in subr.get_new():
		if sub.id not in already_done:
			
			if not any(x in sub.url for x in ["imgur.com","reddit.com"]):
				api_url_prefix = 'http://boilerpipe-web.appspot.com/extract?url='
				req_url = api_url_prefix+sub.url
				# data = json.dumps({'url':sub.url})
				r = requests.get(req_url)
				print r.json
				print sub.url

			already_done.append(sub.id)
	# time.sleep(1800)