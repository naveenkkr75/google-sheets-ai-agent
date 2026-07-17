import os
import streamlit as st
from dotenv import load_dotenv

load_dotenv()

if "GEMINI_API_KEY" in st.secrets:
    GEMINI_API_KEY = st.secrets["GEMINI_API_KEY"]
    SPREADSHEET_ID = st.secrets["SPREADSHEET_ID"]
else:
    GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
    SPREADSHEET_ID = os.getenv("SPREADSHEET_ID")

GOOGLE_SERVICE_ACCOUNT = os.getenv("GOOGLE_SERVICE_ACCOUNT")