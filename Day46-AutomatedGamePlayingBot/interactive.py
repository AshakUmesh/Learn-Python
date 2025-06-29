from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_option = webdriver.ChromeOptions()
chrome_option.add_experimental_option("detach",True)
driver = webdriver.Chrome(options=chrome_option)
driver.get("https://en.wikipedia.org/wiki/Main_Page")
value = driver.find_element(By.CSS_SELECTOR, value="#articlecount a")
print(value.text)
