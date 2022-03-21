from bisect import bisect
from typing import List

import arrow
import pandas as pd


class DateUtils:
    def __init__(self):
        trade_date_df = pd.read_csv('./data/utils/tool_trade_date_hist_sina_df.csv')
        self.trade_list = trade_date_df["trade_date"].tolist()

    def trade_date(self):
        self.input_date = arrow.now().format("YYYY-MM-DD")
        if self.input_date in self.trade_list:
            return self.input_date,True
        else:   
            #  get last trade date
            ind = bisect(self.trade_list,self.input_date)
            return self.trade_list[ind-1],False

