import streamlit as st
import pickle
import pandas as pd

def recommend(movie):
    movie_index=movies[movies['title']==movie].index[0]
    distances=similarity[movie_index]
    movies_list=sorted(list(enumerate(distances)),reverse=True,key=lambda x:x[1])[1:6]
    
    recommended_movies=[]
    for i in movies_list:
        recommended_movies.append(movies.iloc[i[0]].title)
    return recommended_movies


st.title('Movie Recommender System')

movies_dict=pickle.load(open('movie_list.pkl','rb'))
similarity_dict=pickle.load(open('similarity.pkl','rb'))
movies=pd.DataFrame(movies_dict)
similarity=pd.DataFrame(similarity_dict)

selected_movie_name=st.selectbox('Enter the movie name',movies['title'].values)

if st.button('Recommend'):
    recommendations=recommend(selected_movie_name)
    for i in recommendations:
        st.write(i)