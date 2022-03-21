import pandas as pd

import streamlit as st
import pandas as pd
from .utils.date_utils import DateUtils

def app():
    trade_date,today_is_trade_date = DateUtils().trade_date()
    df  = pd.read_csv(f"/data/project/stock/raw_data/{trade_date}.csv")
    st.dataframe(df)