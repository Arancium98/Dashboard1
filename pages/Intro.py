import pandas as pd 
import numpy as np 
import streamlit as st


df = pd.read_csv("https://raw.githubusercontent.com/Arancium98/Dashboard1/121d48b19105b854c6fff18dcd2b3669305fa924/all_data.csv")

import streamlit as st

st.set_page_config(
    page_title="Dashboard",
    page_icon="🐟",
)

st.write("# Analysis Dashboard")
st.sidebar.success("Select a page above.")

st.write("## Introduction")

st.markdown(
    """
    On this dashboard we are going to  analyze and answer business questions about 12 months worth of sales data.
    The data contains hundreds of thousands of electronics store purchases broken down by month, product type, cost, purchase address, etc.

    """
)

st.write("## Business Questions")

st.write("""
         
         1) What was the best month for sales? How much was earned that month?
         2) What city had the highest number of sales?
         3) What products are most often sold together?
         4) What product sold the most?
         
         """)




st.image("https://img.freepik.com/free-vector/gradient-stock-market-concept_23-2149166910.jpg?w=1380&t=st=1694103651~exp=1694104251~hmac=ddb0765d021630b98143f04c7af3e23305e2b2c583e4e69e3df440860922e251")