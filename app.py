import streamlit as st

st.title("Gen AI Text Summarizer")

text = st.text_area("Enter your text")

if st.button("Summarize"):
    st.write("Your text:")
    st.write(text)
