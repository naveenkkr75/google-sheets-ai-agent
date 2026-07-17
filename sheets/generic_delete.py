from sheets.service import get_sheet_service
from sheets.generic_search import search_rows
from config import SPREADSHEET_ID


def delete_row(sheet_name, filters):
    """
    Delete the first row matching the filters.
    """

    matches = search_rows(sheet_name, filters)

    if not matches:
        return "No matching row found."

    row_number = matches[0]["row_number"]

    service = get_sheet_service()

    spreadsheet = service.spreadsheets().get(
        spreadsheetId=SPREADSHEET_ID
    ).execute()

    sheet_id = None

    for sheet in spreadsheet["sheets"]:
        if sheet["properties"]["title"] == sheet_name:
            sheet_id = sheet["properties"]["sheetId"]
            break

    if sheet_id is None:
        return "Worksheet not found."

    body = {
        "requests": [
            {
                "deleteDimension": {
                    "range": {
                        "sheetId": sheet_id,
                        "dimension": "ROWS",
                        "startIndex": row_number - 1,
                        "endIndex": row_number,
                    }
                }
            }
        ]
    }

    service.spreadsheets().batchUpdate(
        spreadsheetId=SPREADSHEET_ID,
        body=body,
    ).execute()

    return "Row deleted successfully."