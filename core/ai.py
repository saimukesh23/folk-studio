import streamlit as st
import groq
from config.config import GROQ_API_KEY
import httpx

def check_internet_connection():
    try:
        httpx.get("https://www.google.com", timeout=5)
        return True
    except (httpx.ConnectError, httpx.TimeoutException):
        return False

def generate_lyrics(prompt):
    if not check_internet_connection():
        st.warning("No internet connection. AI features are unavailable.")
        return None

    if GROQ_API_KEY == "YOUR_GROQ_API_KEY":
        st.warning("Groq API key is not set. Please configure it in `config/config.py`.")
        return None

    try:
        client = groq.Groq(api_key=GROQ_API_KEY)
        chat_completion = client.chat.completions.create(
            messages=[
                {
                    "role": "user",
                    "content": prompt,
                }
            ],
            model="llama3-8b-8192",
        )
        return chat_completion.choices[0].message.content
    except Exception as e:
        st.error(f"An error occurred with the AI service: {e}")
        return None
