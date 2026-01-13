import streamlit as st

st.title("some basic commands like slider button etc")

age = st.slider("Enter your age",1 , 100)
city = st.selectbox("choose your city" , ["pune","Mehkar" , "Buldhana"])
if st.button("show details"):
    st.write("age",age)
    st.write("city",city)