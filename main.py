#import numpy as np
import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt
from io import BytesIO
import plotly.graph_objects as go
from plotly.subplots import make_subplots
from my_plots import *
import streamlit as st

@st.cache_data

# Load the data
def load_books_data():
    url = 'https://raw.githubusercontent.com/brinleyostler/AZ-top-books/main/AZ_top_books.csv'
    df = pd.read_csv(url)

    # Ebook and Audiobook data
    df_e = df[df['Format'] == 'EBOOK']
    df_a = df[df['Format'] == 'AUDIOBOOK']

    return df, df_e, df_a
books, ebooks, audiobooks = load_books_data()

# Set up the page
st.title('Arizona\'s Top Books')
st.sidebar.title('Arizona\'s Top Books')
st.sidebar.write('Input the order we should sort the data:')
with st.sidebar:
    input_order = st.toggle('Ascending', True)


# Set up tabs
tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs(['Alphabet', 'Rank', 'Wait Times/Copies', 'Format', 'Rank/Rating', 'About'])

with tab1:
    input_letter = st.text_input('Enter a letter:', 'A')

    e_letter = alphabet_ebooks(books, input_letter, input_order)
    st.write(f'Top 5 Ebooks that start with the letter {input_letter}')
    st.dataframe(e_letter)

    a_letter = alphabet_audiobooks(books, input_letter, input_order)
    st.write(f'Top 5 Audiobooks that start with the letter {input_letter}')
    st.dataframe(a_letter)

with tab2:
    input_rank = st.slider('Enter a rank:', 1, 240, 1, 1)

    ebook_rank = rank_comparison(ebooks, input_rank)
    audiobook_rank = rank_comparison(audiobooks, input_rank)
    st.write(f'Book info at rank {input_rank}')
    st.write('Ebook:')
    st.table(ebook_rank)
    st.write('Audiobook:')
    st.table(audiobook_rank)

with tab3:
    input_wait = st.slider('Enter a wait time:', 0, 27, 0, 1)
    books_wait = books[books['Wait Weeks'] == input_wait]

    fig3 = px.histogram(books_wait, x='Copies', nbins=80, title='Number of Copies Available When Wait Time is ' + str(input_wait) + ' weeks')
    st.plotly_chart(fig3)

with tab4:
    format_choice = st.radio('Choose a format:', ['EBOOK', 'AUDIOBOOK'])
    format_books = format_comparison(books, format_choice)

    fig4 = px.histogram(format_books, x='Rating', title='Ratings of ' + format_choice + 's')
    st.plotly_chart(fig4)

with tab5:
    input_rating = st.slider('Enter a rating:', 2.4, 4.7, 4.0, 0.1)
    
    books_rating = rank_rating_comparison(books, input_rating, input_order)

    fig5 = px.histogram(books_rating, x='Rank', nbins=12, title='Ranks of Books with a ' + str(input_rating) + ' Rating')
    st.plotly_chart(fig5)
    st.write('Books with a rating of ' + str(input_rating))
    st.table(books_rating)
    
with tab6:
    input_sort = st.selectbox('Sort by:', ['Rank', 'Title', 'Author', 'Rating', 'Format', 'Copies', 'Availability', 'Wait Weeks'])
    books_sorted = about(books, input_sort, input_order)
    st.dataframe(books_sorted)