# Imports

import pandas as pd 
import numpy as np 
import streamlit as st
import plotly.express as px

# Loading Data

df = pd.read_csv("https://raw.githubusercontent.com/Arancium98/Dashboard1/121d48b19105b854c6fff18dcd2b3669305fa924/all_data.csv")


# Data Preparation

def DataCleaning(df):
    
    # Removing null values
    df.dropna(inplace=True)
    
    # Removing 'Order Date' from the dataframe
    df.drop(df[df['Order Date'] == 'Order Date'].index, inplace=True)
    
    return df

def DataFormatting(df):
    
    # converting 'Order Date' to datetime
    df['Order Date'] = pd.to_datetime(df['Order Date'], format='%m/%d/%y %H:%M')
    
    # adding new columns to dataframe , like day, month, year
    df['day'] = df['Order Date'].dt.day
    df['month'] = df['Order Date'].dt.month
    df['year'] = df['Order Date'].dt.year
    
    # Converting 'Quantity Ordered' and 'Price Each' to numeric
    df['Quantity Ordered'] = df['Quantity Ordered'].astype(int)
    df['Price Each'] = df['Price Each'].astype(float)
    

    
    return df

def CreateColumns(df):
    def get_city(address):
        return address.split(",")[1].strip(" ")

    def get_state(address):
        return address.split(",")[2].split(" ")[1]

    df['Total Price'] = df['Quantity Ordered'] * df['Price Each']
    df['City'] = df['Purchase Address'].apply(lambda x: f"{get_city(x)}  ({get_state(x)})")
    
    return df 


# Applying functions

df = DataCleaning(df)
df = DataFormatting(df)
df = CreateColumns(df)



print(df.head)      


st.set_page_config(
    page_title="Dashboard",
    page_icon="🐟",

)


# Answering Business Questions


Sells = df.groupby('month')['Total Price'].sum().sort_values(ascending=False)

# Convert 'Sells' Series to a DataFrame
Sells_df = pd.DataFrame({'Total Price': Sells})

# Reset the index if needed
Sells_df.reset_index(inplace=True)

Months = px.bar(Sells_df
             ,x="month",
             y="Total Price",
             title="Total Sales Per Month",
             )
Months.update_xaxes(nticks=24)
st.plotly_chart(Months, theme="streamlit")