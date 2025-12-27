import pickle
import streamlit as st
import requests
import pandas as pd
from  dotenv import load_dotenv
import os
load_dotenv()
API_KEY=os.getenv("API_KEY")

def fetch_poster(movie_id):

    response = requests.get(f'https://api.themoviedb.org/3/movie/{movie_id}?api_key={API_KEY}&language=en-US')

    data = response.json()
    # st.text(data)
    # st.text()
    return "https://image.tmdb.org/t/p/w500/" + data['poster_path']


def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list= sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    recommended_movies = []
    recommended_movie_posters = []
    for i in movies_list:
        movie_id = movies.iloc[i[0]]['id'] # or whatever the actual column name is

        # for i in movies_list:
        recommended_movies.append(movies.iloc[i[0]].title)
        recommended_movie_posters.append(fetch_poster(movie_id))
    return recommended_movies,recommended_movie_posters

    #
    #     # fetch the movie poster
    #     movie_id = movies.iloc[i[0]]['movie_id']
    #
    #     recommended_movie_posters.append(fetch_poster(movie_id))
    #
    #
    # return recommended_movies


movies_dict=pickle.load(open('movie_dict.pkl','rb'))
movies=pd.DataFrame(movies_dict)

# movies = pickle.load(open('movie_list.pkl','rb'))
similarity = pickle.load(open('similarity.pkl','rb'))

# movies_list=pickle.load(open('movies.pkl','rb'))
# movie_list = movies_list['title'].values
st.title('Movie Recommender System')
# option=st.selectbox
selected_movie_name = st.selectbox(
   'How would you like to be contacted?',
    movies['title'].values)

if st.button(' Recommend'):
    names,posters = recommend(selected_movie_name)
    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        st.text(names[0])
        st.image(posters[0])
    with col2:
        st.text(names[1])
        st.image(posters[1])

    with col3:
        st.text(names[2])
        st.image(posters[2])
    with col4:
        st.text(names[3])
        st.image(posters[3])
    with col5:
        st.text(names[4])
        st.image(posters[4])