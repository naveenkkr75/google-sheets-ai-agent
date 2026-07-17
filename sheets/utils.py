from sheets.service import get_sheet_service
from config import SPREADSHEET_ID


def get_sheet_names():
    """
    Return a list of all worksheet names in the spreadsheet.
    """

    service = get_sheet_service()

    spreadsheet = service.spreadsheets().get(
        spreadsheetId=SPREADSHEET_ID
    ).execute()

    sheet_names = []

    for sheet in spreadsheet["sheets"]:
        sheet_names.append(
            sheet["properties"]["title"]
        )

    return sheet_names


def validate_sheet(sheet_name):
    """
    Check whether a worksheet exists.

    Returns:
        (True, sheet_names) if found
        (False, sheet_names) otherwise
    """

    sheet_names = get_sheet_names()

    if sheet_name in sheet_names:
        return True, sheet_names

    return False, sheet_names