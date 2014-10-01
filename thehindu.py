import requests
from bs4 import BeautifulSoup
import time

from twilio.rest import TwilioRestClient 

base_url = 'http://www.thehindu.com/news/'


def latest_news():
	r = requests.get(base_url)
	text = r.text
	soup = BeautifulSoup(text)
	latest_news_links = soup.find("div", {"class":"breakingNews_list"})
	news = latest_news_links.find_all('a')
	news = str(news).split("</a>")
	j = 0
	#print news[10].split(">")[1]
	latest_news = []
	for i in range(len(news)-1):
		#print j
		#print i[j].split(">")[1]
		latest_news.append(news[j].split(">")[1])
		j = j + 1
	send_mobile(latest_news)
	#print latest_news

def send_mobile(latest_news):
	try:
		ACCOUNT_SID = "ENTER YOUR ACCOUNT SID"
		AUTH_TOKEN = "ENTER YOUR AUTH TOKEN"
		client = TwilioRestClient(ACCOUNT_SID, AUTH_TOKEN)
		message = '1.' + latest_news[0] + '\n' + ' 2.' + latest_news[1] + '\n' + ' 3.' + latest_news[2]
		client.messages.create(
		to="ENTER YOUR MOBILE NUMBER", 
		from_=" ", 
		body=message,  
    	)
	except Exception as e:
		print e

if __name__ == '__main__':
	while True:
		latest_news()
		time.sleep(900)