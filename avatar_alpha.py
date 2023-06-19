import requests
from bs4 import BeautifulSoup

query = 'cats'
url = f'https://www.kiddle.co/s.php?q={query}'

page = requests.get(url).text
soup = BeautifulSoup(page, 'html.parser')

for raw_img in soup.find_all('img'):
    link = raw_img.get('src')
    if link and link.startswith('https'):
        response = requests.get(link)
        with open("./today_avatar.jpg", 'wb') as f:
            f.write(response.content)
        break 