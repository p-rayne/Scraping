import time
import random

# from selenium import webdriver
from seleniumwire import webdriver
from fake_useragent import UserAgent

from proxy_auth_data import login, password

# url = "https://www.python.org/"

user_agents_list = [
    "hello_world",
    "best_wishes",
    "python-3",
]

useragent = UserAgent()
# options
options = webdriver.ChromeOptions()
# options.add_argument("user-agent=HelloWorld:")
# options.add_argument(f"user-agent={random.choice(user_agents_list)}")
# options.add_argument(f"user-agent={useragent.opera}")
options.add_argument(f"user-agent={useragent.random}")

# set proxy
# options.add_argument("--proxy-server=138.128.91.65:8000")

proxy_options = {"proxy": {"https": f"http://{login}:{password}@138.128.91.65:8000"}}

# driver = webdriver.Chrome(
#     executable_path="/home/p-rayne/Python/Learning/Scraping/selenium_0/chromedriver/chromedriver",
#     options=options,
# )

driver = webdriver.Chrome(
    executable_path="/home/p-rayne/Python/Learning/Scraping/selenium_0/chromedriver/chromedriver",
    seleniumwire_options=proxy_options,
)

try:
    # driver.get(url="https://www.whatismybrowser.com/detect/what-is-my-user-agent")
    # time.sleep(5)
    # driver.get_screenshot_as_file("1.png")

    driver.get("https://2ip.ru")
    time.sleep(5)
except Exception as ex:
    print(ex)
finally:
    driver.close()
    driver.quit()
