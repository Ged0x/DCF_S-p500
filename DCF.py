import pandas as pd
import numpy as np
import requests
from SECRETS import api_key
import threading
import time

stocks = pd.read_csv('/Users/omarazlan/Financial_analysis_crypto/DCF_Model/sp_500_stocks.csv')
my_columns = ['Date', 'Ticker', 'Share_Price', 'Implied_Share_Price', 'Difference']
dataframe = pd.DataFrame(columns=my_columns)

def process_symbol(symbol):
    global dataframe

    try:
        url = f'https://financialmodelingprep.com/api/v3/discounted-cash-flow/{symbol}?apikey={api_key}'
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            dcf_value = data[0]["dcf"] if data else None
            share_price_value = data[0]["Stock Price"] if data else None
            new_data = pd.DataFrame([[pd.Timestamp.now(), symbol, share_price_value, dcf_value, None]], columns=my_columns)
            dataframe = pd.concat([dataframe, new_data], ignore_index=True)
            # print("Ticker:", symbol)
            # print("DCF:", dcf_value)
            # print("Share Price:", share_price_value)
            if share_price_value is None or dcf_value is None:
                print(f'No data available for {symbol}')
            else:
                difference = ((dcf_value - share_price_value) / share_price_value)
                dataframe.loc[dataframe['Ticker'] == symbol, 'Difference'] = difference
                if difference > 0:
                    print(f'Undervalued by {difference:.2%}')
                else:
                    print(f'Overvalued by {difference:.2%}')
        elif response.status_code == 429:
            print("Rate limit exceeded. Waiting before retrying...")
            time.sleep(5)  # Wait for 10 seconds before retrying
            process_symbol(symbol)  # Retry the request
        else:
            print("Error fetching data for ticker", symbol, ":", response.status_code)
    except Exception as e:
        print("An error occurred:", e)


threads = []
iteration = 0
for symbol in stocks['Ticker']:
    if iteration >= 200:
        print("Maximum iterations reached. Stopping further processing.")
        break

    thread = threading.Thread(target=process_symbol, args=(symbol,))
    thread.start()
    threads.append(thread)
    iteration += 1
    time.sleep(0.4)  # Add a 0.1-second delay between starting each thread

# Wait for all threads to complete
for thread in threads:
    thread.join()

# Export DataFrame to Excel
dataframe.to_excel('stock_data.xlsx', index=False)
print("DataFrame exported to 'stock_data.xlsx'.")
