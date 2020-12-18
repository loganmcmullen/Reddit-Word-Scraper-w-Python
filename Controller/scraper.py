import requests
import bs4




wallstreetbets = requests.get("https://www.reddit.com/r/wallstreetbets/")

type(wallstreetbets)