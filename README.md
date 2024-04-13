# DCF_S-p500
Collects DCF implied share price of each stock in the S&amp;P 500 using the FMP Api to determine if a stock is overvalued or undervalued based on it's current price, the API however does not have all json DCF data for every stock. 

The DCF script will iterate through the S&P500 tickers to request each stocks implied share price and current stock price, which will then be calculated to see the percentage differences to determine if it's overvalued or undervalued according to the dcf model provided by FinancialModelingPrep's Api. It will then convert the pandas dataframe to an excel file which will be used for the flask web framework. 

The changes of stock price and implied share price are updated as according to FMP Api which is every 1 minute

to run flask, in terminal, cd (folder path of project), python/python3 ui.py, go to http://127.0.0.1:5000 once live

![Uploading Screenshot 2024-04-14 at 5.17.57 AM.png…]()
