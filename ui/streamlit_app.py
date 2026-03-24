import streamlit as st
import requests

API_URL = "http://localhost:8000/chat"

st.title("MediRAG AI Chatbot")

query = st.text_input("Ask a medical question:")

if st.button("Submit"):
    response = requests.post(API_URL, json={"question": query})

    if response.status_code == 200:
        data = response.json()
        st.write("### Answer")
        st.write(data["answer"])

        st.write("### Sources")
        st.write(data["sources"])