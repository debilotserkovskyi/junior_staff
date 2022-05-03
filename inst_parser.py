from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import re
import requests
from bs4 import BeautifulSoup
from instascrape import *
import datetime


link = 'https://www.instagram.com/accounts/login/'
login_url = 'https://www.instagram.com/accounts/login/ajax/'
url = 'https://www.instagram.com/'


# fire_path = '/Users/maksimbelocerkovskij/dev_elo_pme_nt/geckodriver'
# driver = webdriver.Firefox(executable_path=fire_path)
# driver.get(url)


time_ = int(datetime.datetime.now().timestamp())

payload = {
    'username': 'test.cmon.nomc',
    'enc_password': f'#PWD_INSTAGRAM_BROWSER:0:{time_}:jCE9Ja3K8SY4n9Q',
    'pass': 'jCE9Ja3K8SY4n9Q',
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


hashtags = ["cooking", "ny"]

response = requests.get(url).text
bs = BeautifulSoup(response, 'html.parser')
profile_name = []
bio = []
num_posts = []

hashtag = Hashtag(f"https://www.instagram.com/explore/tags/cooking/")
hashtag.scrape(headers={
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36",
    "X-Requested-With": "XMLHttpRequest",
    "Referer": "https://www.instagram.com/accounts/login/",
    "x-csrftoken": csrf
})
post = hashtag.get_recent_posts()

for i in post:
    i.to_csv(fp='new.csv')

print(post[0].scrape(mapping={
    ""
}))


#
# for i in range(len(post)):
#     post[i].to_json(fp=f'scrapped_posts{i}.txt')
#     with open("scrapped_posts.txt", "a") as scr:
#         scr.write(post[i].scrape())


driver.\
    find_element(by=By.XPATH,
                 value='/html/body/div[1]/section/main/article/div[2]/div[1]/div[2]/form/div/div[1]/div/label/input')\
    .send_keys(payload['username'], Keys.TAB, payload['pass'], Keys.ENTER)
time.sleep(2)
#
#
# for i in hashtags:
#     driver.refresh()
#     driver.find_element(by=By.XPATH,
#                         value="/html/body/div[1]/section/nav/div[2]/div/div/div[2]/input").send_keys(i, Keys.ENTER)
#
# time.sleep(10)
# driver.quit()



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