import streamlit as st
from openai import OpenAI

# OpenAI-Client mit API-Key aus Streamlit Secrets
client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

st.set_page_config(page_title="Mini-Chatbot", page_icon="💬")
st.title("💬 Mini-Chatbot mit GPT-4o")

user_input = st.text_input("Was möchtest du wissen?")

if user_input:
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": "Du bist ein freundlicher und hilfreicher Assistent."},
            {"role": "user", "content": user_input}
        ]
    )
    st.markdown("**Antwort:**")
    st.write(response.choices[0].message.content)
