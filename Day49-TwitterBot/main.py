from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

PROMISED_DOWN = 150
PROMISED_UP = 10
TWITTER_EMAIL = "EMAIL"
TWITTER_PASSWORD = "PASSWORD"


class InternetSpeedTwitterBot:
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.up = 0
        self.down = 0

    def get_internet_speed(self):
        self.driver.get("https://www.speedtest.net/")
        sleep(3)
        go_button = self.driver.find_element(By.CLASS_NAME, "start-text")
        go_button.click()
        sleep(60)
        self.up = self.driver.find_element(By.XPATH,
                                           '//*[@id="container"]/div[1]/div[3]/div/div/div/div[2]/div[2]/div/div[4]/div/div[3]/div/div/div[2]/div[1]/div[1]/div/div[2]/span').text
        self.down = self.driver.find_element(By.XPATH,
                                             '//*[@id="container"]/div[1]/div[3]/div/div/div/div[2]/div[2]/div/div[4]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span').text
        print(self.up)
        print(self.down)

    def tweet_at_provider(self):
        if self.up<PROMISED_UP and self.down<PROMISED_DOWN:
            self.driver.get("https://twitter.com/login")
            wait = WebDriverWait(self.driver, 20)
            email = wait.until(EC.presence_of_element_located((By.NAME, "text")))
            email.send_keys(TWITTER_EMAIL)
            email.send_keys("\n")  # proceed to next
            password = wait.until(EC.presence_of_element_located((By.NAME, "password")))
            password.send_keys(TWITTER_PASSWORD)
            password.send_keys("\n")
            tweet_box = wait.until(
                EC.element_to_be_clickable(
                    (By.CSS_SELECTOR, 'div[role="textbox"][data-testid="tweetTextarea_0"]')
                )
            )
            tweet_box.click()
            message = (
                f"Hi, I am a bot reporting speeds: down {self.down} Mbps, up {self.up} Mbps. "
                "#BSNL there’s room for improvement."
            )
            tweet_box.send_keys(message)
            send_button = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[2]/div[2]/div/div/div/button/div/span/span')))
            send_button.click()
            print("✅ Tweet sent successfully!")
        else:
            print("Delivered what was promised")


bot = InternetSpeedTwitterBot()
bot.get_internet_speed()
bot.tweet_at_provider()
