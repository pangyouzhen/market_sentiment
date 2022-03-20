import pandas as pd

import streamlit as st
import pandas as pd

def app():
    df  = pd.read_csv("/data/project/stock/raw_data/2022-03-18.csv")
    # img = Image.open("/data/project/stock/img/2022-03-18.png")
    st.dataframe(df)