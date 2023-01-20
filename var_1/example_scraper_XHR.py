# XHR(json) parsing example

import requests


url = "https://scrapingclub.com/exercise/ajaxdetail/"

response = requests.get(url).json()

title = response["title"]
price = response["price"]
description = response["description"]

print(response)
