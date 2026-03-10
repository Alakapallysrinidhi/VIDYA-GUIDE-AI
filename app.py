import streamlit as st
import requests

st.title("VidyaGuide AI Career Mentor")

uploaded_file = st.file_uploader("Upload Resume", type=["txt"])

if uploaded_file:

    files = {"file": uploaded_file}

    response = requests.post(
        "http://127.0.0.1:8000/analyze",
        files=files
    )

    if response.status_code == 200:
        result = response.json()

        st.subheader("AI Resume Analysis")
        st.write(result["analysis"])