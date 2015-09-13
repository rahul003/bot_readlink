import praw, obot, pyimgur
import time, os
import requests, json
from screenshot import Screenshot
import pickle
# from bs4 import BeautifulSoup

def uploadImage(path):
	# obot.imgur_access_token, 
	im = pyimgur.Imgur(obot.imgur_client_id, obot.imgur_client_secret, refresh_token=obot.imgur_refresh_token)
	ui = im.upload_image(path)
	os.remove(path)
	return ui.link

def get_string(x):
	if x is None:
		return ''
	else:
		return str(x)



head_text = 'Here is a screenshot of the linked page in case you cant access the page or it gets removed or you just dont want to open the page!\n'
foot_text = '\n\n-----------------------------------------------------------\nThis action was performed by a bot. Contact /u/YesIAmTheMorpheus or reply back to this message for feedback or suggestions.'

s = Screenshot()

# r = obot.login_lcb()
r = obot.login()


try:
	already_done = pickle.load('already_done.pkl')
except:
	already_done = []

while True:
	subr = r.get_subreddit('all')
	for sub in subr.get_new():
		if sub.id not in already_done:
			if not any(x in sub.url for x in ["imgur.com","reddit.com"]):
				# print sub.url
				
				# api_url_prefix = 'http://boilerpipe-web.appspot.com/extract?output=json&url='
				# req_url = api_url_prefix+sub.url
				# rval_get_request = requests.get(req_url)
				# value = json.loads(rval_get_request.text)
				
				# print value
				# if value['status'] == 'success':
					# print value
					# respons = value['response']
					# # print resp
					# titl = respons['title']
					# # print titl
					
					# suburl_title = get_string(titl)
					# # print '1: ', req_url
					# # print '\n'
					# # print '2: ',value
					# # print '\n'

					# suburl_content = respons['content'].encode("ascii", errors="ignore")
					# # print '3: ',suburl_content
					# # print '\n4: '
					# # print value['response']['content'].encode('ascii',errors="ignore")
					# # print '\n'

					s.capture(sub.url, 'temp.png')
					link = uploadImage('temp.png')
					# print link
					st = head_text + link +'\n'
					# print st
					# st += suburl_title
					# st += '\n' 
					# # print st
					# st += suburl_content 
					# # print st
					st += foot_text
					# print 'got st'	
					sub.add_comment(st)
		already_done.append(sub.id)
	time.sleep(1800)
	pickle.dump(already_done, 'already_done.pkl')
	r.refresh_access_information(obot.refresh_token)


	
