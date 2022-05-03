from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import re
import requests
from bs4 import BeautifulSoup

from datetime import datetime

link = 'https://www.instagram.com/accounts/login/'
login_url = 'https://www.instagram.com/accounts/login/ajax/'

time = int(datetime.now().timestamp())

payload = {
    'username': 'test.cmon.nomc',
    'enc_password': f'#PWD_INSTAGRAM_BROWSER:0:{time}:jCE9Ja3K8SY4n9Q',
    'queryParams': {},
    'optIntoOneTap': 'false'
}

with requests.Session() as s:
    r = s.get(link)
    csrf = re.findall(r"csrf_token\":\"(.*?)\"", r.text)[0]
    r = s.post(login_url, data=payload, headers={
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36",
        "X-Requested-With": "XMLHttpRequest",
        "Referer": "https://www.instagram.com/accounts/login/",
        "x-csrftoken": csrf
    })
    print(r.status_code)








# from instascrape import *
# # Instantiate the scraper objects
# google = Profile('https://www.instagram.com/google/')
# google_post = Post('https://www.instagram.com/p/CG0UU3ylXnv/')
# google_hashtag = Hashtag('https://www.instagram.com/explore/tags/google/')
#
# # Scrape their respective data
# google.scrape()
# google_post.scrape()
# google_hashtag.scrape()
#
# print(google.followers)
# print(google_post['hashtags'])
# print(google_hashtag.amount_of_posts)