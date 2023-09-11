import pandas as pd 
import numpy as np 
import streamlit as st



st.set_page_config(
    page_title="Dashboard",
    page_icon="🐄"
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
         3) What product sold the most?
         4) What products are most often sold together?
         
         """)





st.image("https://img.freepik.com/free-vector/gradient-stock-market-concept_23-2149166910.jpg?w=1380&t=st=1694103651~exp=1694104251~hmac=ddb0765d021630b98143f04c7af3e23305e2b2c583e4e69e3df440860922e251")

st.markdown("""
            The data and the idea are from Keith Gallin video : "Solving real world data science tasks with Python Pandas!"
            source: https://www.youtube.com/watch?v=eMOA1pPVUc4&t
            """)