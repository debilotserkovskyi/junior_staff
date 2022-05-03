import time
from bs4 import BeautifulSoup
import requests
import re
import pandas as pd
import openpyxl
import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

from selenium.webdriver.common.by import By

# data = pd.read_excel('DAO Discords.xlsx')
# data = pd.read_csv('DAO Discords.xlsx')

# print(data.head(5))

# fire_path = '/Users/maksimbelocerkovskij/dev_elo_pme_nt/geckodriver'
# driver = webdriver.Firefox(executable_path=fire_path)
# driver.get("file:///Users/maksimbelocerkovskij/Downloads/DAO%20Discords/Priority.html")

# driver.find_element(by=By.CLASS_NAME, value='s1')
# elems = driver.find_element(by=By.CSS_SELECTOR, value=".waffle > tbody:nth-child(2) > tr:nth-child(2) > td:nth-child(2)")
# links = [elem.get_attribute('href') for elem in elems]

url = 'file:///Users/maksimbelocerkovskij/Downloads/DAO%20Discords/Priority.html'

with open('/Users/maksimbelocerkovskij/Downloads/DAO Discords/Priority.html') as fp:
    soup = BeautifulSoup(fp, 'html.parser')
links = []
for link in soup.find_all('a'):
    links.append(link.get('href'))
    
    
print(links)
response = requests.get(links[0]).text
requests.get(links[0]).raise_for_status()
soup_discord = BeautifulSoup(response, 'html.parser')


all_links = []
discord_links = []
for link in links:
    for link in soup_discord.find_all('a'):
        all_links.append(link.get('href'))
        for line in all_links:
            if 'https://discord.com' in str(line):
                discord_links.append(line)

print(set(discord_links))

# for link in links:
#     responce = requests.get(link).text