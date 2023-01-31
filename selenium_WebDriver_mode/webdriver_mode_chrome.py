from selenium import webdriver
import time


# options
options = webdriver.ChromeOptions()

# user-agent
options.add_argument(
    "user-agent=Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36"
)

# disable webdriver mode

## for older ChromeDriver under version 79.0.3945.16
# options.add_experimental_option("excludeSwitches", ["enable-automation"])
# options.add_experimental_option("useAutomationExtension", False)

## for ChromeDriver version 79.0.3945.16 or above
options.add_argument("--disable-blink-features=AutomationControlled")

driver = webdriver.Chrome(
    executable_path="/home/p-rayne/Python/Learning/Scraping/selenium_0/chromedriver/chromedriver",
    options=options,
)


try:
    driver.get(
        "https://intoli.com/blog/not-possible-to-block-chrome-headless/chrome-headless-test.html"
    )
    time.sleep(10)
except Exception as ex:
    print(ex)
finally:
    driver.close()
    driver.quit()
