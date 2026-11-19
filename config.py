
import os
import streamlit as st
from dotenv import load_dotenv

load_dotenv()

try:
    GROQ_API_KEY = st.secrets["GROQ_API_KEY"]
except Exception:
    GROQ_API_KEY = os.getenv("GROQ_API_KEY")

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

APP_NAME = "SchemeSathi AI"
APP_TAGLINE = "Government Schemes Made Simple, For Everyone."

SUPPORTED_LANGUAGES = {
    "English": "en",
    "मराठी": "mr",
    "हिंदी": "hi"
}
