from time import sleep
from selenium import webdriver
from selenium.common import ElementClickInterceptedException
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

INSTA_EMAIL = "EMAIL"
INSTA_PASSWORD = "PASSWORD"


class InstaFollower:
    def __init__(self):
        options = webdriver.ChromeOptions()
        options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(options=options)

    def login(self):
        self.driver.get("https://www.instagram.com/?flo=true")
        sleep(3)
        email_field = self.driver.find_element(By.XPATH, '//*[@id="loginForm"]/div[1]/div[1]/div/label/input')
        email_field.send_keys(INSTA_EMAIL)
        password_field = self.driver.find_element(By.NAME, "password")
        password_field.send_keys(INSTA_PASSWORD)
        password_field.send_keys(Keys.ENTER)

    def find_followers(self):
        sleep(2)
        self.driver.get("https://www.instagram.com/fcbarcelona/")
        sleep(5)

        following_button = self.driver.find_element(
            By.CLASS_NAME, "x5n08af x1s688f"
        )
        following_button.click()

        # Wait for modal
        modal = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "x6nl9eh x1a5l9x9 x7vuprf x1mg3h75 x1lliihq x1iyjqo2 "
                                                           "xs83m0k xz65tgg x1rife3k x1n2onr6"))
        )

        # Scroll the modal to load more users
        for _ in range(10):  # Adjust number of scrolls
            self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", modal)
            sleep(1.5)

    def follow(self):
        follow_buttons = self.driver.find_elements(By.XPATH, "/html/body/div[5]/div[2]/div/div/div[1]/div/div["
                                                             "2]/div/div/div/div/div[2]/div/div/div[3]/div["
                                                             "1]/div/div[1]/div/div/div/div[3]/div/button/div/div")

        print(f"Found {len(follow_buttons)} buttons.")
        for button in follow_buttons:
            try:
                button.click()
                sleep(1.2)
            except ElementClickInterceptedException:
                pass




bot = InstaFollower()
bot.login()
bot.find_followers()
bot.follow()
