import streamlit as st

st.title("Mein kleiner Chatbot")

user_input = st.text_input("Frag mich etwas:")

if user_input:
    st.write("Du hast gefragt:", user_input)
    st.write("Antwort (noch nicht schlau 😅): Dies ist ein Platzhalter.")
