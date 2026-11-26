import streamlit as st
from google import genai

st.title("Generative AI Text Summarizer")

api_key = st.text_input("Enter your Gemini API key", type="password")
text = st.text_area("Enter your text here")

if st.button("Summarize"):
    if api_key and text:
        client = genai.Client(api_key=api_key)
        response = client.models.generate_content(
            model="gemini-3.8-flash",
            contents="Summarize this text in simple English:\n" + text,
        )
        st.subheader("Summary")
        st.write(response.text)
    else:
        st.warning("Please enter API key and text.")
