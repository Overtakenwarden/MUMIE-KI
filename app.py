import streamlit as st
from openai import OpenAI

# OpenAI-Client mit API-Key aus secrets
client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

st.title("Chatbot mit GPT-4o")

user_input = st.text_input("Frag mich etwas:")

if user_input:
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": "Du bist ein hilfreicher Chatbot."},
            {"role": "user", "content": user_input}
        ]
    )
    st.write(response.choices[0].message.content)
