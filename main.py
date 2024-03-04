import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(layout="wide")

df_reviews = pd.read_csv("data/customer reviews.csv")
df_top100_books = pd.read_csv("data/Top-100 Trending Books.csv")

price_max = df_top100_books["book price"].max()
price_min = df_top100_books["book price"].min()

max_price = st.sidebar.slider("Price Range", price_min, price_max, price_max)

df_filtered_books = df_top100_books[df_top100_books["book price"] <= max_price]
df_filtered_books

fig = px.bar(df_filtered_books["year of publication"].value_counts())
fig_price = px.histogram(df_filtered_books["book price"])
fig_rating = px.bar(df_filtered_books["rating"].value_counts())

col1, col2 = st.columns(2)
col1.plotly_chart(fig)
col2.plotly_chart(fig_price)
col1.plotly_chart(fig_rating)