import random, webbrowser, requests, re
from bs4 import BeautifulSoup as bs
from randomsearch import search

def trysearch():
	try:
		f = random.randint(1000, 10000)

		val = random.randint(0,2)

		if val == 2:
			url = (f"https://www.youtube.com/results?search_query={search()}")
		elif val == 1:
			url = (f"https://www.youtube.com/results?search_query=MOV+0{f}")
		else:
			url = (f"https://www.youtube.com/results?search_query=MP4+0{f}")

		#To open search results
		#webbrowser.open(url)

		page = requests.get(url)
		website = str(bs(page.text, 'lxml'))
		links = re.findall(r"/watch\?v=\S\S\S\S\S\S\S\S\S\S\S",website)
		webbrowser.open(f"https://www.youtube.com/{links[random.randint(0,len(links))]}")
	except:
		return False

while (trysearch() == False):
	trysearch()