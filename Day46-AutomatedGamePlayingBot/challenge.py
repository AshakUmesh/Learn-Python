from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

chrome_option = webdriver.ChromeOptions()
chrome_option.add_experimental_option("detach",True)
driver = webdriver.Chrome(options=chrome_option)
driver.get("https://secure-retreat-92358.herokuapp.com/")
value = driver.find_element(By.NAME, value="fName")
value.send_keys("ashak")
value2 = driver.find_element(By.NAME, value="lName")
value2.send_keys("umesh")
value3 = driver.find_element(By.NAME, value="email")
value3.send_keys("ashak@gmail.com")
value3.send_keys(Keys.ENTER)

