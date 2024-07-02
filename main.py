import requests
from datetime import datetime,timedelta
# from twilio.rest import Client
# STOCK = "TSLA"
# company name here
NEWS_ENDPOINT="https://newsapi.org/v2/everything"
STOCL_API_KEY='LYW0DE58H3MOSSGB'
NEWS_API_KEY= '4176baca72bd48429ac7e01a4eea7976'
# account SID here
AUTH_TOKEN='a5a3f680aec5503b7a7169c3841e869b'

def send_text(message_body):
# STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and description to your phone number.
    client = Client(ACCOUNT_SID, AUTH_TOKEN)
    message = client.messages \
        .create(
        body=message_body,
        from_='+14344741856',
        to='+44123456789'
    )
    print(message.status)

def get_news():
    ## STEP 2: Use https://newsapi.org
    # Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME.
    news_params = {
        "apiKey": NEWS_API_KEY,
        "qInTitle": COMPANY_NAME,
    }
    news_response = requests.get(NEWS_ENDPOINT, params=news_params)
    articles = news_response.json()["articles"]

    print(articles)
    for article in articles[:3]:
        message_body = ' '
        headline = article["title"]
        url = article["url"]
        message_body += (f"\n TSLA:\n Headline {up_or_down}{round(percentage_difference)}%{headline}{url}")
        send_text(message_body)



## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").


time_now = datetime.now()
today = time_now.date()
yesterday = today - timedelta(days=1)
day_before_yesterday=today - timedelta(days=2)
stock_at_close_yesterday=' '
stock_at_close_day_before_yesterday=' '
response = requests.get(url=f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY_ADJUSTED&symbol=TSLA&apikey=4176baca72bd48429ac7e01a4eea7976")
response.raise_for_status()
data = response.json()

for x in data["Time Series (Daily)"]:
    if x == str(yesterday):
        stock_at_close_yesterday=(data["Time Series (Daily)"][x]["4. close"])
        print(stock_at_close_yesterday)
    if x == str(day_before_yesterday):
        stock_at_close_day_before_yesterday = (data["Time Series (Daily)"][x]["4. close"])
        print(stock_at_close_day_before_yesterday)

if stock_at_close_yesterday <= stock_at_close_day_before_yesterday:
    up_or_down= "🔺"
else:
   up_or_down = "🔻"

difference = abs(float(stock_at_close_day_before_yesterday) - float(stock_at_close_yesterday))
percentage_difference = difference /float(stock_at_close_day_before_yesterday) * 100

print(percentage_difference)
if percentage_difference >=5:
    get_news()




#return

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

