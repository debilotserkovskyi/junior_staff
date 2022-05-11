from bs4 import BeautifulSoup
import requests

with open('path to .html file') as fp:
    soup = BeautifulSoup(fp, 'html.parser')
links = []
for link in soup.find_all('a'):
    links.append(link.get('href'))

all_links = []
discord_links = []

for link in links:
    print(f'{len(discord_links)} / {len(links)}')
    response = requests.get(link).text
    requests.get(link).raise_for_status()
    soup_discord = BeautifulSoup(response, 'html.parser')
    permanent = ''
    for link2 in soup_discord.find_all('a'):
        all_links.append(link2.get('href'))
        for line in all_links:
            if 'https://discord.' in str(line):
                permanent = line
    discord_links.append(permanent)


print(links)
print(discord_links)
# also you can write it in .txt file
