from datetime import datetime, timedelta
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException


chrome_option = webdriver.ChromeOptions()
chrome_option.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_option)
driver.get("http://ozh.github.io/cookieclicker/")

wait = WebDriverWait(driver, 10)


lang_button = wait.until(EC.element_to_be_clickable((By.ID, "langSelect-EN")))
lang_button.click()
print("Language selected.")


cookie = driver.find_element(By.ID, "bigCookie")


wait_time = 5  # seconds between upgrade checks
timeout = datetime.now() + timedelta(seconds=wait_time)
end_time = datetime.now() + timedelta(minutes=5)

while datetime.now() < end_time:
    cookie.click()


    if datetime.now() >= timeout:
        try:
            cookies_el = wait.until(EC.visibility_of_element_located((By.ID, "cookies")))
            cookie_count = int(cookies_el.text.split()[0].replace(",", ""))
            products = driver.find_elements(By.CSS_SELECTOR, "div[id^='product']")
            for prod in reversed(products):
                if "enabled" in prod.get_attribute("class"):
                    prod.click()
                    print(f"Bought {prod.get_attribute('id')}")
                    break
        except (NoSuchElementException, ValueError) as e:
            print("Upgrade failed:", e)
        timeout = datetime.now() + timedelta(seconds=wait_time)

try:
    final = driver.find_element(By.ID, "cookies").text
    print(f"Final cookies after 5 minutes: {final}")
except NoSuchElementException:
    print("Couldn't retrieve final cookie count.")

