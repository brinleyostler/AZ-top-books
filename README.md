# best-selling-books
## AZ's Top Books and Audiobooks Dataset

This project uses Python and Selenium to scrape the top 480 ebooks and audiobooks from my local library's digital collection, gathering information like titles, authors, availability, etc.
This repository contains all code used to collect, clean, and visualize the dataset, which was then used for analysis and featured in my blog.


## Project Overview

The purpose of this project was to collect data on popular ebooks and audiobooks available at the library to explore trends in titles, authors, and formats. This data will help answer questions like:

- Which authors are most represented among the top books?
- What is the average wait time for each book type?
- How does availability correlate with popularity?


## Dataset Description
The final dataset contains 480 entries (240 ebooks and 240 audiobooks), with the following columns:

- **Rank:** Ranking based on library popularity
- **Title:** Title of the book or audiobook
- **Author:** Author of the title
- **Rating:** Average user rating
- **Format:** Format of the title (ebook or audiobook)
- **Copies:** Number of copies available at the library
- **Availability:** Status of availability (e.g., available or on waitlist)


## Key Steps in the Data Collection Process

- **Setting up Selenium:** Utilized Selenium WebDriver with Chrome to navigate and scrape data from each page of the library’s collection.
- **Extracting Data:** Retrieved information for each title (title, author, format, etc.) using XPath selectors, and paginated through the first 10 pages for both ebooks and audiobooks.
- **Detailed Data Collection:** Accessed each book's detailed page to gather additional data on availability, number of copies, and ratings.
- **Data Cleaning and Storage:** Compiled the scraped data into a pandas DataFrame for analysis and further visualization.


## Visualizations and Analysis

Visualizations created using Seaborn include:

- **Availability Status:** Comparison of books on waitlist versus available.
- **Rank vs. Rating:** Scatter plot with regression line to explore trends in popularity and ratings.
- **Top Authors:** Bar plot of the most frequently appearing authors in the dataset.