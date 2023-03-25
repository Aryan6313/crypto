import streamlit as st
from PIL import Image
import pandas as pd
import base64
import matplotlib.pyplot as plt
from bs4 import BeautifulSoup
import requests
import json
import time

#page layout
#page expands to full width
st.beta_set_page_config(layout="wide")

# Page layout (continued)
## Divide page to 3 columns (col1 = sidebar, col2 and col3 = page contents)
col1 = st.sidebar
col2, col3 = st.columns((2,1))

#---------------------------------#
# Sidebar + Main panel
col1.header('Input Options')

## Sidebar - Currency price unit
currency_price_unit = col1.selectbox('Select currency for price', ('USD', 'BTC', 'ETH'))










