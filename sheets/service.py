import json
import os

import streamlit as st
from google.oauth2.service_account import Credentials
from googleapiclient.discovery import build

from config import GOOGLE_SERVICE_ACCOUNT

SCOPES = [
    "https://www.googleapis.com/auth/spreadsheets"
]


def get_sheet_service():
    # Running on Streamlit Cloud
    if "GOOGLE_SERVICE_ACCOUNT" in st.secrets:
        credentials = Credentials.from_service_account_info(
            dict(st.secrets["GOOGLE_SERVICE_ACCOUNT"]),
            scopes=SCOPES,
        )

    # Running locally
    else:
        credentials = Credentials.from_service_account_file(
            GOOGLE_SERVICE_ACCOUNT,
            scopes=SCOPES,
        )

    service = build(
        "sheets",
        "v4",
        credentials=credentials,
    )

    return service