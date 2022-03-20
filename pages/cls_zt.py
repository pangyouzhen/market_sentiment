import pandas as pd

import streamlit as st
from PIL import Image
import pandas as pd

from .utils.date_utils import trade_date

def app():
    img = Image.open(f"./data/cls_img/{trade_date}.png")
    st.image(img)