import streamlit as st
import numpy as np
import pandas as pd
import pickle


movies = pickle.load(open('movies_list.pkl', 'rb'))
movies_list = movies['title'].values
vector = pickle.load(open('similarity.pkl', 'rb'))

st.header("Movie Recommender System")
select_value = st.selectbox("Select movies from dropdown", movies_list)


#def print_similar_movies(movie):
#    index = movies[movies['title'] == movie].index[0]
#    print('Recommendations for {0}: \n'.format(movies[movies.movie_id == index+1].title.values[0]))
#    recommend_movie = []
#    for id in vector[index+1]:
#        movies_id = movies.iloc[id].movie_id
#        recommend_movie.append(movies[movies.movie_id ==id].title.values[0])

#    return recommend_movie

def print_similar_movies(movie):
    movieid = movies[movies['title'] == movie].values[0][0]
    movieind = movies[movies['title'] == movie].index[0]
    print('Recommendations for {0}: \n'.format(movies[movies.movie_id == movieid].title.values[0]))
    recommend_id = vector[movieind]
    print(recommend_id)
    recommend_movie = []
    for i in recommend_id:
        recommend_movie.append(movies[movies.movie_id == i+1].title.values[0])
    return recommend_movie

if st.button("Show recommend"):
    movie_name = print_similar_movies(select_value)
    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        st.text(movie_name[0])
    with col2:
        st.text(movie_name[1])
    with col3:
        st.text(movie_name[2])
    with col4:
        st.text(movie_name[3])
    with col5:
        st.text(movie_name[4])