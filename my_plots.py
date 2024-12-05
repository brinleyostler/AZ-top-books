import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import matplotlib.pyplot as plt
import pandas as pd

def alphabet_ebooks(books, letter='A', order=False):
    # Return the highest rated ebooks that start with the letter
    ebooks_letter = books[books['Title'].str.startswith(letter)]
    ebooks_letter = ebooks_letter[ebooks_letter['Format'] == 'EBOOK']
    df_e = ebooks_letter.head(5)
    df_e = df_e.sort_values(by='Rating', ascending=order)

    return df_e

def alphabet_audiobooks(books, letter='A', order=False):
    # Return the highest rated audiobooks that start with the letter
    audiobooks_letter = books[books['Title'].str.startswith(letter)]
    audiobooks_letter = audiobooks_letter[audiobooks_letter['Format'] == 'AUDIOBOOK']
    df_a = audiobooks_letter.head(5)
    df_a = df_a.sort_values(by='Rating', ascending=order)

    return df_a

def rank_comparison(books, rank=1):
    # Return the ratings of the book at the rank
    book_rank = books[books['Rank'] == rank]

    return book_rank

def format_comparison(books, format='EBOOK'):
    # Return the ratings of the book of a specific format
    book_format = books[books['Format'] == format]
    book_format = book_format.sort_values(by=['Rating'], ascending=False)

    # Return the copies of the book of a specific format
    book_copies = books[books['Format'] == format]
    book_copies = book_copies.sort_values(by=['Copies'], ascending=False)

    return book_format, book_copies

def rank_rating_comparison(books, rating=4.0, order=False):
    # Return the ratings of the book at the rank
    book_rank_rating = books[books['Rating'] == rating]
    book_rank_rating = book_rank_rating.sort_values(by=['Rank'], ascending=order)

    return book_rank_rating

def top_authors(books, num_authors=5, order=False):
    # Return the top authors
    top_authors = books.groupby('Author').size().reset_index(name='Books').sort_values(by='Books', ascending=False).head(num_authors)
    top_authors = top_authors.sort_values(by='Books', ascending=order)

    return top_authors


def about(books, sortby='Rank', order=True):
    # Return the books sorted by a specific column
    books = books.sort_values(by=[sortby], ascending=order)

    return books
