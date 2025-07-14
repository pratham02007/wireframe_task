import streamlit as st
import pandas as pd


st.title("This Is My Streamlit APP")
st.write("Welcome to my app! This is my simple wireframe.")
st.subheader("Student Information")

text = st.text_input("Enter your name:")
st.write(f"Your name is {text}")

age = [1, 2, 3, 4, 5, 6,7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24,] 
select_age = st.selectbox("Select your age:", age )
st.write(f"Your age is : {select_age}")

st.checkbox("I Agree Terms and condtions")

st.subheader("Select Your Branch")
branch = ["CO", "CE", "EE", "EJ", "IT", "CSE", "ECE", "ME"]
select_branch = st.selectbox("select branch : ", branch)
st.write(f"Your Branch: {select_branch}")

rate = st.slider("Rate my wireframe : ", 0, 10)
st.write(f"Your rating : {rate}/10")
st.text_area("Write your message ")

col1, col2 = st.columns(2)
with col1:
    st.write("This is column 1")
    if st.button("button 1"):
        st.write("Button 1 clicked!!")

with col2:
    st.write("This is column 2")
    if st.button("button 2"):
        st.write("Button 2 clicked!!")

st.success("Thanks for your information..!!!")