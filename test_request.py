import requests

url = "https://kidkodschool.github.io/welcome.html"

response = requests.get(url)

with open("./python_is_cool.html", 'wb') as f:
    f.write(response.content)