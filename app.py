import streamlit as st
from openai import OpenAI

# OpenAI API-Key (aus Streamlit Secrets)
openai_api_key = st.secrets["OPENAI_API_KEY"]

client = OpenAI(api_key=openai_api_key)

st.title("Chatbot mit OpenAI")

user_input = st.text_input("Frag mich etwas:")

if user_input:
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[{"role": "user", "content": user_input}]
    )
    st.write(response.choices[0].message.content)

