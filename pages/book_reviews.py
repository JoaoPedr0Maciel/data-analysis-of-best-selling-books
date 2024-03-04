import streamlit as st
import pandas as pd

st.set_page_config(layout="wide")

df_reviews = pd.read_csv("data/customer reviews.csv")
df_top100_books = pd.read_csv("data/Top-100 Trending Books.csv")

books = df_top100_books["book title"].unique()
book = st.sidebar.selectbox("Books", books)

books_filtered = df_top100_books[df_top100_books["book title"] == book]
book_review_filtered = df_reviews[df_reviews["book name"] == book] 


book_title = books_filtered["book title"].iloc[0]
book_genre = books_filtered["genre"].iloc[0]
book_price = f"${books_filtered['book price'].iloc[0]}"
book_rating = books_filtered["rating"].iloc[0]
book_year = books_filtered["year of publication"].iloc[0]


st.title(book_title)
st.subheader(book_genre)
col1, col2, col3 = st.columns(3)
col1.metric("Price", book_price)
col2.metric("Rating", book_rating)
col3.metric("Year of publication", book_year)

st.divider()

filtered_reviews = df_reviews.values[df_reviews["book name"] == book]


for row in filtered_reviews:
  message = st.chat_message(f"{row[4]}")
  message.subheader(row[2])
  message.write(row[5])