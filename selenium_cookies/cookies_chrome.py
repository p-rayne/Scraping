from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

from auth_data import LOGIN, PASSWORD
import pickle


# options
options = webdriver.ChromeOptions()

options.add_argument(
    "user-agent=Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36"
)

driver = webdriver.Chrome(
    executable_path="/home/p-rayne/Python/Learning/Scraping/chromedriver",
    options=options,
)


try:
    # # driver.delete_all_cookies()
    # driver.get("https://vk.com")
    # time.sleep(5)

    # email_input = driver.find_element("id", "index_email")
    # email_input.clear()
    # email_input.send_keys(LOGIN)
    # time.sleep(5)
    # email_input.send_keys(Keys.ENTER)

    # # login_button = driver.find_element(
    # #     "xpath", '//*[@id="index_login"]/div[1]/form/button[1]'
    # # ).click()
    # time.sleep(10)

    # switch_to_password = driver.find_element(
    #     "css selector",
    #     "button.vkc__PureButton__button.vkc__Link__link.vkc__Link__primary.vkc__Bottom__switchToPassword",
    # ).click()
    # time.sleep(5)

    # password_input = driver.find_element("name", "password")
    # password_input.clear()
    # password_input.send_keys(PASSWORD)
    # time.sleep(5)

    # continue_button = driver.find_element(
    #     "xpath", '//*[@id="root"]/div/div/div/div/div[2]/div/div/div/form/div[2]/button'
    # ).click()
    # time.sleep(15)

    # # cookies
    # with open("cookies", "wb") as file:
    #     pickle.dump(driver.get_cookies(), file)

    ############################## read cookie ###############################################

    driver.get("https://vk.com")
    time.sleep(5)

    with open("cookies", "rb") as file:
        for cookie in pickle.load(file):
            driver.add_cookie(cookie)

    time.sleep(5)
    driver.refresh()
    time.sleep(10)

except Exception as ex:
    print(ex)
finally:
    driver.close()
    driver.quit()
