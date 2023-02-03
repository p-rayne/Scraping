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

options.add_argument("--disable-blink-features=AutomationControlled")

# uncomment on the VPS
# options.add_argument("--no-sandbox")

# headless mode (2 variants)
# options.add_argument("--headless")
# options.headless = True

driver = webdriver.Chrome(
    executable_path="/home/p-rayne/Python/Learning/Scraping/chromedriver",
    options=options,
)


try:
    driver.get("https://vk.com")
    time.sleep(5)

    print("Passing auth...")
    email_input = driver.find_element("id", "index_email")
    email_input.clear()
    email_input.send_keys(LOGIN)
    time.sleep(5)
    email_input.send_keys(Keys.ENTER)

    # login_button = driver.find_element(
    #     "xpath", '//*[@id="index_login"]/div[1]/form/button[1]'
    # ).click()
    time.sleep(15)

    print("Switch to password page")
    switch_to_password = driver.find_element(
        "css selector",
        "button.vkc__PureButton__button.vkc__Link__link.vkc__Link__primary.vkc__Bottom__switchToPassword",
    ).click()
    time.sleep(5)

    print("Password input...")
    password_input = driver.find_element("name", "password")
    password_input.clear()
    password_input.send_keys(PASSWORD)
    time.sleep(5)

    continue_button = driver.find_element(
        "xpath", '//*[@id="root"]/div/div/div/div/div[2]/div/div/div/form/div[2]/button'
    ).click()
    time.sleep(5)

    print("Going to the profile page...")
    profile_page = driver.find_element("id", "l_pr").click()
    time.sleep(5)

    print("Scrolling window...")
    scroll = driver.execute_script("window.scrollTo(0,700)")
    time.sleep(3)

    print("Click comment button...")
    comment_icon = (
        driver.find_element("class name", "like_btns")
        .find_element("class name", "comment")
        .click()
    )
    time.sleep(5)

    print("Writing a comment...")
    driver.find_element("class name", "reply_field").send_keys(
        "Hey! I was here" + Keys.ENTER
    )
    time.sleep(5)

    print("Job is done!")


except Exception as ex:
    print(ex)
finally:
    driver.close()
    driver.quit()
