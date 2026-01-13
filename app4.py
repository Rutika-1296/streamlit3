import streamlit as st
import google.generativeai as genai

st.title("welcome to my Streamlit app")

user_input = st.text_input("ask me anything")
genai.configure(api_key= "AIzaSyB0VfE3QTVcbYshaaSvhpIOLDiKM_9zlYg")

model = genai.GenerativeModel("models/gemini-2.5-flash")

if user_input:
    response = model.generate_content(user_input)
    st.write("Response" ,response.text)
