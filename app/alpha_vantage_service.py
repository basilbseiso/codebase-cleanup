# maybe something like the following rough organizational structure would be reasonable.
# then we can import these functions into other files that need them (i.e. crypto.py, stocks.py, unemployment.py).
# one benefit of doing so is we get to refactor all the request-related code out of those files.
# for example, as a result, we'll only have the api key definition in one place (which is good)!

import os
import json
from dotenv import load_dotenv
import requests
from pandas import read_csv
from app.utils import to_usd

load_dotenv()

ALPHAVANTAGE_API_KEY = os.getenv("ALPHAVANTAGE_API_KEY", default="demo")


def fetch_crypto_data(symbol):
    url = f"https://www.alphavantage.co/query?function=DIGITAL_CURRENCY_DAILY&market=USD&symbol={symbol}&apikey={ALPHAVANTAGE_API_KEY}"
    response = requests.get(url)
    parsed_response = json.loads(response.text)
    #print(parsed_response)
    tsd = parsed_response["Time Series (Digital Currency Daily)"]

    dates = list(tsd.keys())
    latest_date = dates[0]
    latest = tsd[latest_date]
    #print(latest)
    # not sure about the difference between '4a. close (USD)' and '4b. close (USD)'
    print(symbol)
    print(latest_date)
    print(latest['4a. close (USD)'])
    print(to_usd(float(latest['4a. close (USD)'])))


def fetch_stocks_data(symbol):
    url = f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY_ADJUSTED&symbol={symbol}&apikey={ALPHAVANTAGE_API_KEY}&datatype=csv"

    df = read_csv(url)
    #print(df.columns)
    #breakpoint()

    latest = df.iloc[0]

    print(symbol)
    print(latest["timestamp"])
    print(latest["close"])
    print('${:,.2f}'.format(latest["close"]))


def fetch_unemployment_data():
    url = f"https://www.alphavantage.co/query?function=UNEMPLOYMENT&apikey={ALPHAVANTAGE_API_KEY}"
    response = requests.get(url)
    parsed_response = json.loads(response.text)
    #print(parsed_response)

    data = parsed_response["data"]
    latest = data[0]
    print(latest) #> {'date': '2022-02-01', 'value': '3.8'}