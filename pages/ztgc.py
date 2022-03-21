import pandas as pd

import streamlit as st
import pandas as pd
from .utils.date_utils import DateUtils

#  涨停股池
def app():
    trade_date,today_is_trade_date = DateUtils().trade_date()
    df  = pd.read_csv(f"./data/stock_zt_pool_em/{trade_date}.csv",index_col=0)
    st.dataframe(df)