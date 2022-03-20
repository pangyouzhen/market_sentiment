import pandas as pd

import streamlit as st
import pandas as pd
from .utils.date_utils import trade_date

def app():
    df  = pd.read_csv(f"./data/stock_em_zt_pool/{trade_date}.csv",index_col=0)
    st.dataframe(df)