from google.oauth2.service_account import Credentials
from googleapiclient.discovery import build

from config import GOOGLE_SERVICE_ACCOUNT


SCOPES = [
    "https://www.googleapis.com/auth/spreadsheets"
]


def get_sheet_service():
    """
    Create and return an authenticated Google Sheets service.
    """

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