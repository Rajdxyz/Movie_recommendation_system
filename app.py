import streamlit as st
import pandas as pd
import pickle
similarity=pickle.load(open("sim.pkl","rb"))
def recommend(movie):
    m_index = x[x["title"] == movie].index[0]
    distance = similarity[m_index]
    mov_list = sorted(list(enumerate(distance)), reverse=True, key=lambda x: x[1])[1:6]
    y=[]
    for a in mov_list:
        y.append((x["title"].iloc[a[0]]))
    return y
options=pickle.load(open("movies_dict.pkl","rb"))
x=pd.DataFrame(options)
movies_list=x["title"].values
st.title("Movie Recommendation System")
Answer=st.selectbox("Enter the movie",movies_list)
if st.button('Recommend'):
    recommendations=recommend(Answer)
    for a in recommendations:
        st.write(a)

