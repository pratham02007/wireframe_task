import streamlit as st
import pandas as pd


st.title("My First Streamlit APP")

st.write("Welcome to my app! This is my simple wireframe.")
st.subheader("Student Information")
text = st.text_input("Enter your name:")
st.write(f"Your name is {text}")
age = [1, 2, 3, 4, 5, 6,7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24,] 
select_age = st.selectbox("Select your age:", age )
st.write(f"Your age is : {select_age}")