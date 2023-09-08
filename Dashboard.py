import pandas as pd 
import numpy as np 
import streamlit as st
import plotly.express as px

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


st.set_page_config(
    page_title="Dashboard",
    page_icon="🐟",
    layout="wide"

)

st.markdown("<h1 style='text-align: center; color: grey;'>Sales Analysis Dashboard</h1>", unsafe_allow_html=True)


col1, col2 = st.columns([1,1])

# Answering Business Questions

# Q1 :  What was the best month for sales? How much was earned that month?

Sells_month = df.groupby('month')['Total Price'].sum().sort_values(ascending=False)

Sells_df = pd.DataFrame({'Total Price': Sells_month})
Sells_df.reset_index(inplace=True)

# Q2 : What city had the highest number of sales?

sum_city = df.groupby('City')['Total Price'].sum().sort_values(ascending=False)

sum_city = pd.DataFrame({'Total Price': sum_city})
sum_city.reset_index(inplace=True)

# Q3: What product sold the most?

Sold_most = df.groupby('Product')['Quantity Ordered'].sum().sort_values(ascending=False).head(10)
Sold_most_df = pd.DataFrame({'Quantity Sold': Sold_most})
Sold_most_df.reset_index(inplace=True)

# Q4: What products are most often sold together?

duplicates = df[df['Order ID'].duplicated(keep=False)]
duplicates['Sold Together'] = duplicates.groupby('Order ID')['Product'].transform(lambda x: ','.join(x))
duplicates = duplicates[['Order ID', 'Sold Together']].drop_duplicates()
duplicates_head = duplicates['Sold Together'].value_counts().head(10)




# Graphs

## Q1

most_sales_month = Sells_df['Total Price'].idxmax()
Months = px.bar(Sells_df
             ,x="month",
             y="Total Price",
             title="Total Sales Per Month",
             width=750,
             height=500
             )
Months.update_traces(marker_color=['royalblue' if x == most_sales_month else 'grey' for x in Sells_df.index])
Months.update_xaxes(nticks=24)




## Q2 


Prices = px.bar(sum_city,
             x="City",
             y="Total Price",
             title="Total Sales Per City",
             width=750,
             height=500
             )
Prices.update_xaxes(nticks=24)

## Q3

QProducs = px.bar(Sold_most_df,
                  x= 'Quantity Sold',
                  y= 'Product',
                  title="Quantity of Sold Products",
                  orientation='h',
                  )
QProducs.update_xaxes(nticks=20)
QProducs.update_layout(yaxis=dict(autorange="reversed"))


# Columns values.

with col1:
    st.plotly_chart(Months, theme="streamlit")
    st.caption('This is a string that explains something above.')
    st.plotly_chart(QProducs, theme="streamlit")
    
    
with col2:
    st.plotly_chart(Prices, theme="streamlit")
    st.caption('This is a string that explains something above.')
    st.dataframe(duplicates_head)
    
