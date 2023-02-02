from selenium import webdriver
import time


# options
options = webdriver.ChromeOptions()

options.add_argument(
    "user-agent=Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36"
)

options.add_argument("--disable-blink-features=AutomationControlled")

# headless mode (2 variants)
# options.add_argument("--headless")
# options.headless = True

driver = webdriver.Chrome(
    executable_path="/home/p-rayne/Python/Learning/Scraping/chromedriver",
    options=options,
)


try:
    driver.implicitly_wait(5)
    driver.get(
        "https://www.avito.ru/moskva/tovary_dlya_kompyutera/komplektuyuschie/videokarty-ASgBAgICAkTGB~pm7gmmZw?cd=1"
    )
    # print(driver.window_handles)
    print(f"Currently URL is: {driver.current_url}")
    # time.sleep(5)

    items = driver.find_elements("xpath", "//div[@data-marker='item-photo']")
    items[0].click()
    # print(driver.window_handles)

    # time.sleep(5)

    driver.switch_to.window(driver.window_handles[1])
    # time.sleep(5)
    print(f"Currently URL is: {driver.current_url}")

    username = driver.find_element("xpath", "//div[@data-marker='seller-info/name']")
    print(f"Username is: {username.text}")
    # time.sleep(5)

    driver.close()
    driver.switch_to.window(driver.window_handles[0])
    # time.sleep(5)
    print(f"Currently URL is: {driver.current_url}")

    items[1].click()
    # time.sleep(5)

    driver.switch_to.window(driver.window_handles[1])
    # time.sleep(5)
    print(f"Currently URL is: {driver.current_url}")
    price = driver.find_element(
        "css selector",
        "span.js-item-price.style-item-price-text-_w822.text-text-LurtD.text-size-xxl-UPhmI",
    )
    print(f"price: {price.text}")
    date = driver.find_element("xpath", "//span[@data-marker='item-view/item-date']")
    print(f"date added: {date.text}")
    views = driver.find_element("xpath", "//span[@data-marker='item-view/total-views']")
    print(f"views: {views.text}")


except Exception as ex:
    print(ex)
finally:
    driver.close()
    driver.quit()
