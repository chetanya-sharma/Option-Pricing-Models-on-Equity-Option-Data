import yfinance as yf
import numpy as np
from datetime import datetime,timedelta

class stock_volatility:
    def __init__(self,ticker):
        self.ticker=ticker
        self.data=None
    
    def fetch_data(self):
        end_date=datetime.today()
        start_date=end_date-timedelta(days=365)
        self.data=yf.download(self.ticker,start=start_date,end=end_date)

    def get_data(self):
        if self.data is None:
            self.fetch_data()

        return self.data
    
    def calc_volatility(self):
        if self.data is None:
            self.fetch_data()

        self.data["Log Returns"]=np.log(self.data['Adj Close']/self.data['Adj Close'].shift(1))

        volatility=self.data["Log Returns"].std()*np.sqrt(252)

        return volatility