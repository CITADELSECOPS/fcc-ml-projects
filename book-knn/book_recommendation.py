"""FCC Book Recommendation Engine using KNN.

Returns list of 5 most similar books based on user ratings collaborative filtering.
"""
import numpy as np
import pandas as pd
from scipy.sparse import csr_matrix
from sklearn.neighbors import NearestNeighbors

books_filename = "BX-Books.csv"
ratings_filename = "BX-Book-Ratings.csv"

df_books = pd.read_csv(
    books_filename, encoding="ISO-8859-1", sep=";", header=0,
    names=["isbn", "title", "author"], usecols=["isbn", "title", "author"],
    dtype={"isbn": "str", "title": "str", "author": "str"},
)
df_ratings = pd.read_csv(
    ratings_filename, encoding="ISO-8859-1", sep=";", header=0,
    names=["user", "isbn", "rating"], usecols=["user", "isbn", "rating"],
    dtype={"user": "int32", "isbn": "str", "rating": "float32"},
)

# Filter: users with >=200 ratings, books with >=100 ratings
user_counts = df_ratings["user"].value_counts()
df_ratings = df_ratings[df_ratings["user"].isin(user_counts[user_counts >= 200].index)]
isbn_counts = df_ratings["isbn"].value_counts()
df_ratings = df_ratings[df_ratings["isbn"].isin(isbn_counts[isbn_counts >= 100].index)]

# Merge titles
df = pd.merge(df_ratings, df_books, on="isbn").drop_duplicates(["title", "user"])

# Pivot: rows=titles, cols=users
matrix = df.pivot(index="title", columns="user", values="rating").fillna(0)
sparse = csr_matrix(matrix.values)
model = NearestNeighbors(metric="cosine", algorithm="brute")
model.fit(sparse)


def get_recommends(book=""):
    try:
        idx = matrix.index.get_loc(book)
    except KeyError:
        return [book, []]
    distances, indices = model.kneighbors(matrix.iloc[idx, :].values.reshape(1, -1), n_neighbors=6)
    similar = [
        [matrix.index[indices.flatten()[i]], float(distances.flatten()[i])]
        for i in range(1, 6)
    ][::-1]
    return [book, similar]
