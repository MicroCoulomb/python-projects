import requests
from twilio.rest import Client
import datetime as dt
from dotenv import load_dotenv
import os

load_dotenv(overide=True)

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
STOCK_API = "https://www.alphavantage.co/query"
NEWS_API = "https://newsapi.org/v2/everything"
TWILIO_SID = os.getenv("TWILIO_SID")
TWILIO_TKN = os.getenv("TWILIO_AUTH_TOKEN")

stock_params = {
    "function": "TIME_SERIES_DAILY",
    "symbol": "TSLA",
    "outputsize": 2,
    "apikey": os.getenv("STOCK_API"),
}

last_month = str(dt.date.today() - dt.timedelta(days=30))
# print(last_month)

news_params = {
    "q": "tesla inc.",
    "from": last_month,
    "apiKey": os.getenv("NEWS_API"),
    "sortBy": "popularity",
    "pageSize": 3,
}

r_stock = requests.get(STOCK_API, params=stock_params)
stock_data = r_stock.json()["Time Series (Daily)"]
# print(stock_data)
data_list = [value for (key, value) in stock_data.items()]

def stock_change():
    now_close_value = float(data_list[0]["4. close"])
    yesterday_close_value = float(data_list[1]["4. close"])
    return ((now_close_value - yesterday_close_value)/yesterday_close_value)*100

change_value = stock_change()
if change_value >= 0:
    plusminus = "🔺"
else:
    plusminus = "🔻"

r_news = requests.get(NEWS_API, params=news_params)
news_data = r_news.json()

client = Client(TWILIO_SID, TWILIO_TKN)

for news in news_data["articles"]:
    # print(news)
    message = client.messages.create(
        body=f"TESLA: {plusminus}{change_value:.2f}%\n"
             f"Headline: {news['title']}\n"
             f"Brief: {news['description']}",
        from_="+12202091923",
        to="+18777804236",
    )
    print(message.body)

## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 

## STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and description to your phone number. 




#Optional: Format the SMS message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

