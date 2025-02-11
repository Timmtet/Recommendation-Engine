import pandas as pd
import numpy as np
import pickle
import streamlit as st
import requests
from scipy.sparse import csr_matrix
from sklearn.neighbors import NearestNeighbors


st.header("Movie Recommendation Engine")

# Load the movie list pickle file
df = pickle.load(open('movie_list.pkl', 'rb'))

# load the vectorized_sparse file
vectorized_sparse = pickle.load(open('vectorized_sparse.pkl', 'rb'))

# Extract the movie titles
movie_list = sorted(df['movie_title'].values)

# convert the id column to whole numbers
df['id'] = df['id'].astype(int)

# Use sparse matrix in NearestNeighbors
nn = NearestNeighbors(metric="cosine", algorithm="brute")
nn.fit(vectorized_sparse)

# create a function to get movie poster
def get_poster(movie_id):
    url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key=########################"
    response = requests.get(url)
    data = response.json()
    poster_path1 = data.get('poster_path')
    full_path = f'https://image.tmdb.org/t/p/w500{poster_path1}'
    return full_path



# function to recommend similar movies
def get_recommendations(query_index, df, vectorized_sparse, n_neighbors=11):
    distances, indices = nn.kneighbors(vectorized_sparse[query_index], n_neighbors=n_neighbors)
    
    # Exclude the movie itself
    recommended_indices = indices[0][1:11]  
   
    # Get the movie that the user queried
    query_movie = df.iloc[query_index]
    
    # create empty lists to store recommended movie titles and movie
    index = []
    tmdb_id = []
    recommended_movies = []
    movie_poster = []

    for i in recommended_indices:
        index.append(i)
        recommended_movies.append(df.iloc[i]['movie_title'])
        movie_poster.append(get_poster(df.iloc[i]['id']))
        tmdb_id.append(df.iloc[i]['id'])

    # Print the movie that the user queried    
    print(f"Recommendations for: **{query_movie['movie_title']}**\n") 



    return recommended_movies, movie_poster


#define the search box
search_term = st.selectbox("Type or select a movie to find similar movies", movie_list) 

if st.button("Show similar movies"):
    # Get the movie index
    movie_index = df[df['movie_title'] == search_term].index[0]
    recommended_movies, movie_poster = get_recommendations(movie_index, df, vectorized_sparse, n_neighbors=11)
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.write(recommended_movies[0])
        st.image(movie_poster[0])

        st.write(recommended_movies[1]) 
        st.image(movie_poster[1])

    with col2:
        st.write(recommended_movies[2])
        st.image(movie_poster[2])

        st.write(recommended_movies[3])
        st.image(movie_poster[3])

    with col3:
        st.write(recommended_movies[4])
        st.image(movie_poster[4])

        st.write(recommended_movies[5])
        st.image(movie_poster[5])

    with col4:
        st.write(recommended_movies[6])
        st.image(movie_poster[6])

        st.write(recommended_movies[7])
        st.image(movie_poster[7])
    
    with col5:
        st.write(recommended_movies[8])
        st.image(movie_poster[8])

        st.write(recommended_movies[9])
        st.image(movie_poster[9])

