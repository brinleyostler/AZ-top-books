import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import matplotlib.pyplot as plt
import pandas as pd

def alphabet_rating_df(books, letter='A'):
    ebooks = books[books['Format'] == 'EBOOK'].copy()
    audiobooks = books[books['Format'] == 'AUDIOBOOK'].copy()

    # Return the highest rated books that start with the letter
    books_letter = books[books['Title'].str.startswith(letter)]
    ebooks_letter = books_letter[books_letter['Format'] == 'EBOOK']
    ebooks_letter = ebooks_letter.sort_values(by=['Format', 'Rating'], ascending=False)

    audiobooks_letter = books_letter[books_letter['Format'] == 'AUDIOBOOK']
    audiobooks_letter = audiobooks_letter.sort_values(by=['Format', 'Rating'], ascending=False)

    df_e = ebooks_letter.head(5)
    df_a = audiobooks_letter.head(5)

    return df_e, df_a