import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import matplotlib.pyplot as plt
import pandas as pd

def alphabet_ebooks(books, letter='A'):
    # Return the highest rated ebooks that start with the letter
    ebooks_letter = books[books['Title'].str.startswith(letter)]
    ebooks_letter = ebooks_letter[ebooks_letter['Format'] == 'EBOOK']
    ebooks_letter = ebooks_letter.sort_values(by=['Format', 'Rating'], ascending=False)
    df_e = ebooks_letter.head(5)

    return df_e

def alphabet_audiobooks(books, letter='A'):
    # Return the highest rated audiobooks that start with the letter
    audiobooks_letter = books[books['Title'].str.startswith(letter)]
    audiobooks_letter = audiobooks_letter[audiobooks_letter['Format'] == 'AUDIOBOOK']
    audiobooks_letter = audiobooks_letter.sort_values(by=['Format', 'Rating'], ascending=False)
    df_a = audiobooks_letter.head(5)

    return df_a

def rank_comparison(books, rank=1):
    # Return the ratings of the book at the rank
    book_rank = books[books['Rank'] == rank]

    return book_rank