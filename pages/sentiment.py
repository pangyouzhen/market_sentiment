import pandas as pd

import streamlit as st
import pandas as pd
from .utils.date_utils import trade_date

def app():
    df  = pd.read_csv(f"/data/project/stock/raw_data/{trade_date}.csv")
    st.dataframe(df)