#import numpy as np
import pandas as pd
import zipfile
import plotly.express as px
import matplotlib.pyplot as plt
import requests
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
#with st.sidebar:
#    input_letter = st.text_input('Enter a letter:', 'A')

# Set up tabs
tab1, tab2 = st.tabs(['Alphabet', 'Format'])

with tab1:
    input_letter = st.text_input('Enter a letter:', 'A')

    e_letter = alphabet_ebooks(books, input_letter)
    st.write(f'Top 5 Ebooks that start with the letter {input_letter}')
    st.dataframe(e_letter)

    a_letter = alphabet_audiobooks(books, input_letter)
    st.write(f'Top 5 Audiobooks that start with the letter {input_letter}')
    st.dataframe(a_letter)

