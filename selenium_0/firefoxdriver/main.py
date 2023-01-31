from selenium import webdriver
import time
from fake_useragent import UserAgent

# url = "https://www.python.org/"

useragent = UserAgent()
# options
options = webdriver.FirefoxOptions()


# change user-agent
# options.set_preference("general.useragent.override", "hello World")
options.set_preference("general.useragent.override", useragent.random)

driver = webdriver.Firefox(
    executable_path="/home/p-rayne/Python/Learning/Scraping/selenium_0/firefoxdriver/geckodriver",
    options=options,
)

try:
    driver.get(url="https://www.whatismybrowser.com/detect/what-is-my-user-agent")
    time.sleep(5)
except Exception as ex:
    print(ex)
finally:
    driver.close()
    driver.quit()
