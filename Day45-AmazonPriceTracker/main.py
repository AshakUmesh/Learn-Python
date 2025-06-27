import smtplib
from bs4 import BeautifulSoup
import requests
import os
from dotenv import load_dotenv
load_dotenv(dotenv_path="key.env")
api_key = os.getenv("API_KEY")
payload = { 'api_key': api_key, 'url': 'https://www.amazon.in/SLOVIC-Cotton-Stylish'
                                                                  '-Adjutsable-Straps/dp/B0F5B9GX59/?_encoding=UTF8&ref_=pd_hp_d_atf_ci_mcx_mr_ca_hp_atf_d' }
response = requests.get('https://api.scraperapi.com/', params=payload)
data = response.text
soup = BeautifulSoup(data, "html.parser")
title = "SLOVIC Cap for Men Stylish | Unisex Cap with Adjutsable Straps | Summer Caps for Men & All Sports - Cricket, " \
        "Football | Comfortable fit Baseball Caps for Mens & Boys | Free Size"
price = soup.find(class_="a-price-whole").getText()
amount = float(price)
my_amount = 200

if my_amount > amount:
    message = f"{title} is on sale for {amount}!"
    email = os.getenv("EMAIL")
    password = os.getenv("PASSWORD")
    connection = smtplib.SMTP("smtp.gmail.com")
    connection.starttls()
    connection.login(user=email, password=password)
    send_message = "Subject: Discount !! \n\n" + message
    connection.sendmail(from_addr=email, to_addrs=email, msg=send_message.encode("utf-8"))
    print("mail sent successfully")