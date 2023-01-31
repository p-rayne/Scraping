import time
import random
from selenium import webdriver
from fake_useragent import UserAgent

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

driver = webdriver.Chrome(
    executable_path="/home/p-rayne/Python/Learning/Scraping/selenium_0/chromedriver/chromedriver",
    options=options,
)

try:
    driver.get(url="https://www.whatismybrowser.com/detect/what-is-my-user-agent")
    time.sleep(5)
    # driver.get_screenshot_as_file("1.png")
except Exception as ex:
    print(ex)
finally:
    driver.close()
    driver.quit()
