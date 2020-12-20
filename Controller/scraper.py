import re

import bs4
import requests
from bs4 import BeautifulSoup


wallstreetbets = requests.get("https://www.reddit.com/r/wallstreetbets/")
soup = bs4.BeautifulSoup(wallstreetbets.content, "lxml")

linksToComments = []
data = []


def remove_duplicates(l): # remove duplicates and unURL string
    for item in l:
        match = re.search("(?P<url>https?://[^\s]+)", item)
        if match is not None:
            linksToComments.append((match.group("url")))

for linksToComments in soup.find_all('a', href=True):
    data.append(str(linksToComments.get('href')))

flag = True
remove_duplicates(data)
while flag:
    try:
        for link in linksToComments:
            for j in soup.find_all('a', href=True):
                temp = []
                source_code = requests.get(link)
                soup = BeautifulSoup(source_code.content, 'lxml')
                temp.append(str(j.get('href')))
                remove_duplicates(temp)

                if len(linksToComments) > 162: # set limitation to number of URLs
                    break
            if len(linksToComments) > 162:
                break
        if len(linksToComments) > 162:
            break
    except Exception as e:
        print(e)
        if len(linksToComments) > 162:
            break

for url in linksToComments:
    print(url)