import time
from multiprocessing import Pool
from random import randrange
from selenium import webdriver
from selenium.webdriver.common.by import By


# options
options = webdriver.ChromeOptions()

options.add_argument(
    "user-agent=Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36"
)

options.add_argument("--disable-blink-features=AutomationControlled")

# headless mode (2 variants)
# options.add_argument("--headless")
# options.headless = True

urls_list = ["https://stackoverflow.com", "https://www.python.org", "https://vk.com"]


# def get_data(url):
#     try:
#         driver = webdriver.Chrome(
#             executable_path="/home/p-rayne/Python/Learning/Scraping/chromedriver",
#             options=options,
#         )
#         driver.get(url)
#         time.sleep(5)
#         driver.get_screenshot_as_file(
#             f"selenium_multiprocessing/media/{url.split('//')[1]}.png"
#         )
#     except Exception as ex:
#         print(ex)
#     finally:
#         driver.close()
#         driver.quit()


def get_data(url):
    try:
        driver = webdriver.Chrome(
            executable_path="/home/p-rayne/Python/Learning/Scraping/chromedriver",
            options=options,
        )
        driver.get(url)
        time.sleep(5)
        video = (
            driver.find_element(By.CLASS_NAME, "tiktok-1nncbiz-DivItemContainer")
            .find_element(By.CLASS_NAME, "tiktok-3g8031-DivVideoPlayerContainer")
            .click()
        )
        time.sleep(randrange(5, 10))
    except Exception as ex:
        print(ex)
    finally:
        driver.close()
        driver.quit()


if __name__ == "__main__":
    process_count = int(input("Enter nuimber of processes: "))
    url = input("Enter the URL: ")
    urls_list = [url] * process_count
    p = Pool(processes=process_count)
    p.map(get_data, urls_list)
