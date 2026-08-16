import sys

import pandas as pn
import yfinance as yf

print("enter ticker for any stock")
ticker = input("")

print("please enter a time period you would like data for eg 1d, 1m, 1y")
ticker_period = input("")

stock_info_final = yf.download(ticker, period=ticker_period, interval="1d")

print(f"\nStock Information for: {ticker}")
print(f"\nStock Details of {ticker} : {stock_info_final}")
print(f"Company Name: {stock_info_final.iloc[0]}")
pn.DataFrame.to_csv(stock_info_final, index=False, path_or_buf="stock_info.csv")


print("would you like more information regarding'{ticker}'?")
print("to proceed type the number 1 or greater, to end type the number 0 or less")
des_str = input("")
perm = int(des_str)
if perm <= 0:
  sys.exit(0)
else:
  print({ticker})









