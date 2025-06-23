import streamlit as st

st.title("Mein kleiner Chatbot")

# Texte laden
with open("data.txt", "r", encoding="utf-8") as f:
    texts = f.read().split("\n\n")  # Texte durch Leerzeilen trennen

user_input = st.text_input("Frag mich etwas:")

def simple_search(query, texts):
    results = [text for text in texts if query.lower() in text.lower()]
    return results

if user_input:
    results = simple_search(user_input, texts)
    if results:
        st.write("Ich habe Folgendes gefunden:")
        for res in results:
            st.write("- " + res)
    else:
        st.write("Sorry, dazu habe ich nichts gefunden.")

