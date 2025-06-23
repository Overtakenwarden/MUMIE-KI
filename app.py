import streamlit as st
import openai

# OpenAI API-Key laden
openai.api_key = st.secrets["OPENAI_API_KEY"]

st.title("Chatbot mit OpenAI")

user_input = st.text_input("Frag mich etwas:")

if user_input:
    response = openai.ChatCompletion.create(
        model="gpt-4o",
        messages=[{"role": "user", "content": user_input}]
    )
    st.write(response.choices[0].message["content"])


