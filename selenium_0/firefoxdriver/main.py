# from selenium import webdriver
from seleniumwire import webdriver
import time
from fake_useragent import UserAgent
from proxy_auth_data import login, password

# url = "https://www.python.org/"

useragent = UserAgent()
# options
options = webdriver.FirefoxOptions()


# change user-agent
# options.set_preference("general.useragent.override", "hello World")
options.set_preference("general.useragent.override", useragent.random)

# set proxy
# proxy = "138.128.91.65:8000"
# firefox_capabilities = webdriver.DesiredCapabilities.FIREFOX
# firefox_capabilities["marionette"] = True

# firefox_capabilities["proxy"] = {
#     "proxyType": "MANUAL",
#     "httpProxy": proxy,
#     "ftpProxy": proxy,
#     "sslProxy": proxy,
# }

proxy_options = {"proxy": {"https": f"http://{login}:{password}@138.128.91.65:8000"}}

# driver = webdriver.Firefox(
#     executable_path="/home/p-rayne/Python/Learning/Scraping/selenium_0/firefoxdriver/geckodriver",
#     options=options,
#     proxy=proxy,
# )

driver = webdriver.Firefox(
    executable_path="/home/p-rayne/Python/Learning/Scraping/selenium_0/firefoxdriver/geckodriver",
    seleniumwire_options=proxy_options,
)

try:
    # driver.get(url="https://www.whatismybrowser.com/detect/what-is-my-user-agent")
    # time.sleep(5)

    driver.get("https://2ip.ru")
    time.sleep(5)
except Exception as ex:
    print(ex)
finally:
    driver.close()
    driver.quit()
