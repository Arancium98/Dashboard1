import pandas as pd 
import numpy as np 
import streamlit as st
import plotly.express as px


st.set_page_config(
    page_title="Dashboard",
    page_icon="🐄",
    layout="wide")


st.markdown("<h1 style='text-align: center; color: grey;'>Sales Analysis Dashboard by city</h1>", unsafe_allow_html=True)

df = pd.read_csv("https://raw.githubusercontent.com/Arancium98/Dashboard1/121d48b19105b854c6fff18dcd2b3669305fa924/all_data.csv")


def DataCleaning(df):
    
    df.dropna(inplace=True)
    df.drop(df[df['Order Date'] == 'Order Date'].index, inplace=True)
    
    return df

def DataFormatting(df):
    
    df['Order Date'] = pd.to_datetime(df['Order Date'], format='%m/%d/%y %H:%M')   
    
    df['day'] = df['Order Date'].dt.day
    df['month'] = df['Order Date'].dt.month
    df['year'] = df['Order Date'].dt.year    
    df['hour'] = df['Order Date'].dt.hour

    
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

df = DataCleaning(df)
df = DataFormatting(df)
df = CreateColumns(df)

city = st.selectbox("City", df['City'].unique())  
df_city = df[df['City'] == city]
    


    # Sold most
Sold_most = df_city.groupby('Product')['Quantity Ordered'].sum().sort_values(ascending=False).head(10)
Sold_most_df = pd.DataFrame({'Quantity Sold': Sold_most})
Sold_most_df.reset_index(inplace=True)

# Sells by Hour
hourly_counts = df_city['hour'].value_counts().sort_index()
Sell_hourly = pd.DataFrame({'Total Sells': hourly_counts})
Sell_hourly.reset_index(inplace=True)

# Graphs

## Sold most
col1, col2 = st.columns([1,1])

QProducs = px.bar(Sold_most_df,
                x= 'Quantity Sold',
                y= 'Product',
                title="Quantity of Sold Products",
                orientation='h',
                )

QProducs.update_xaxes(nticks=20)
QProducs.update_layout(yaxis=dict(autorange="reversed"))




SellHour = px.line(Sell_hourly,
        x='hour',
        y='Total Sells',
            markers=True,
        title="Sells by hour")
SellHour.update_xaxes(nticks=24)



with col1:
        st.plotly_chart(QProducs, theme="streamlit")

with col2:
        st.plotly_chart(SellHour, theme="streamlit")











