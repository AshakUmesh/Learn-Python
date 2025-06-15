import requests
from dotenv import load_dotenv
from twilio.rest import Client
import os
load_dotenv(dotenv_path="API_keys.env")

account_sid = os.getenv("TWILIO_ACCOUNT_SID")
auth_token = os.getenv("TWILIO_AUTH_TOKEN")
client = Client(account_sid, auth_token)
STOCK_API_KEY = os.getenv("STOCK_API_KEY")
NEWS_API_KEY = os.getenv("NEWS_API_KEY")

stock_para = {"function": "TIME_SERIES_DAILY",
              "symbol": "IBM",
              "interval": "5min",
              "apikey": STOCK_API_KEY}

news_para = {"qInTitle": "IBM",
             "country": "us",
             "apiKey": NEWS_API_KEY}

res_stock = requests.get("https://www.alphavantage.co/query",params=stock_para)
stock_data = res_stock.json()["Time Series (Daily)"]
data_list =[value for (key, value) in stock_data.items()]
yesterday_data = data_list[0]
yesterday_closing_price = yesterday_data["4. close"]
print(yesterday_closing_price)

day_before_yesterday_data = data_list[1]
day_before_yesterday_closing_price = day_before_yesterday_data["4. close"]
print(day_before_yesterday_closing_price)

difference = abs(float(yesterday_closing_price) - float(day_before_yesterday_closing_price))
print(difference)

difference_perc = (difference/float(yesterday_closing_price))*100
print(difference_perc)

if difference_perc > 5:
    print("get news")
    stock_news = requests.get("https://newsapi.org/v2/top-headlines",params=news_para)
    news_data = stock_news.json()["articles"]
    three_articles = news_data[:3]
    print(news_data)

formatted_article = [f"Headline: {article['title']}. \nBrief: {article['description']}" for article in three_articles]
for article in formatted_article:
    try:
        message = client.messages.create(
            from_="whatsapp:+14155238886",
            body=article,
            to=os.getenv("NUMBER")
        )
        print(f"Message sent: {message.sid}")
    except Exception as e:
        print(f"Failed to send message: {e}")