import random, webbrowser, requests, re
from bs4 import BeautifulSoup as bs
from randomsearch import search

num = random.randint(1000, 10000)

val = random.randint(0,3)

if val == 3:
	url = (f"https://www.youtube.com/results?search_query={search()}")
elif val == 2:
	url = (f"https://www.youtube.com/results?search_query=IMG+0{num}")
elif val == 1:
	url = (f"https://www.youtube.com/results?search_query=MOV+0{num}")
else:
	url = (f"https://www.youtube.com/results?search_query=MP4+0{num}")

# To open search results
#webbrowser.open(url)

page = requests.get(url)
website = str(bs(page.text, 'lxml'))
links = re.findall(r"/watch\?v=\S\S\S\S\S\S\S\S\S\S\S",website)
webbrowser.open(f"https://www.youtube.com/{links[random.randint(0,len(links))]}")