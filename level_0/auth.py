from requests import Session
from bs4 import BeautifulSoup
from time import sleep

headers = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36"
}

payload = {
    "csrf_token": "",
    "username": "noname",
    "password": "password",
}

work = Session()


work.get("https://quotes.toscrape.com/", headers=headers)
response = work.get("https://quotes.toscrape.com/login", headers=headers)

soup = BeautifulSoup(response.text, "lxml")

token = soup.find("form").find("input").get("value").strip()

payload["csrf_token"] = token

result = work.post(
    "http://quotes.toscrape.com/login",
    headers=headers,
    data=payload,
    allow_redirects=True,
)

# parsing an unknown number of pages
#
# result = soup.find_all('span', class_='text')
# author = soup.find_all('small', class_='author')
# for .... :
#     if len(result) != 0:
#         pass
#     else:
#         break
