# DCF_S-p500
Collects DCF implied share price of each stock in the S&P 500 using the FMP Api to determine if a stock is overvalued or undervalued based on it's current price, the API however does not have all json DCF data for every stock. 

This will (hopefully) help automate screening of available public listed stocks for users interested to invest in stocks included in the S&P 500.

dependencies:
from flask import Flask, render_template_string
numpy
pandas
threading
time
requests
API key for FMP

url = https://financialmodelingprep.com/api/v3/discounted-cash-flow/{symbol}?apikey={api_key} #symbol is ticker

FMP DCF API description:
The FMP Discounted Cash Flow endpoint provides access to the DCF valuation for a company. DCF is a valuation method that estimates the value of an investment based on its expected future cash flows. The DCF valuation is calculated by discounting the expected future cash flows to their present value.Investors can use DCF valuation to compare the value of different investment opportunities, to assess the riskiness of an investment, and to make investment decisions. The FMP Discounted Cash Flow endpoint provides a simple and easy-to-use way to calculate the DCF valuation for a company. The endpoint requires the user to provide the company's expected future cash flows and the discount rate. The endpoint will then calculate the DCF valuation and return it to the user.

Example Json Format:
[
	{
		"symbol": "AAPL",
		"date": "2023-03-03",
		"dcf": 151.0983806294802,
		"Stock Price": 149.65
	}
]


The DCF script will iterate through the S&P500 tickers to request each stocks implied share price and current stock price, which will then be calculated to see the percentage differences to determine if it's overvalued or undervalued according to the dcf model provided by FinancialModelingPrep's Api. It will then convert the pandas dataframe to an excel file which will be used for the flask web framework. 

The changes of stock price and implied share price are updated as according to FMP Api which is every 1 minute

to run flask, in terminal, cd (folder path of project), python/python3 ui.py, go to http://127.0.0.1:5000 once live


<img width="1440" alt="Screenshot 2024-04-14 at 5 17 57 AM" src="https://github.com/Ged0x/DCF_S-p500/assets/143278786/3c58332e-76cf-43cd-b71f-e2460fab6b42">
