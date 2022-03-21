import pandas as pd

import streamlit as st
from PIL import Image
import pandas as pd

from .utils.date_utils import DateUtils

def app():
    trade_date,today_is_trade_date = DateUtils().trade_date()
    img = Image.open(f"./data/cls_img/{trade_date}.png")
    st.image(img)