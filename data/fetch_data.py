#!/usr/bin/env python3

#
#
#

from pandas_datareader import data as pdr
import csv
import datetime
import matplotlib.pyplot as plt
import yfinance as yf

start   = datetime.datetime(2021, 1, 1)
end     = datetime.datetime(2023,12,31)
symbols = ['VTI', 'VPU', 
           'CTA', 'KMLM', 
	   'LTPZ', 'TLT', 'VTIP' ]
csvfile = 'daily_asset_prices.csv'

yf.pdr_override()
data = pdr.get_data_yahoo(symbols, start, end)['Adj Close']
print(data.head())
data.to_csv(csvfile)

#plt.figure(figsize = (20,10))
#plt.title('Prices from {} to {}'.format(start,end))
#plt.plot(data['Open'])
#plt.show()
