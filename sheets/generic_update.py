from sheets.service import get_sheet_service
from sheets.generic_search import search_rows
from sheets.schema import get_headers
from config import SPREADSHEET_ID


def get_column_letter(column_index):
    """
    Convert 0-based column index to Excel column letters.

    Example:
    0 -> A
    1 -> B
    25 -> Z
    26 -> AA
    """

    result = ""

    while column_index >= 0:
        result = chr(column_index % 26 + 65) + result
        column_index = column_index // 26 - 1

    return result


def update_row(sheet_name, filters, updates):
    """
    Update the first row matching the filters.
    """

    matches = search_rows(sheet_name, filters)

    if not matches:
        return "No matching row found."

    row_number = matches[0]["row_number"]

    headers = get_headers(sheet_name)

    service = get_sheet_service()

    for column_name, new_value in updates.items():

        if column_name not in headers:
            continue

        column_index = headers.index(column_name)

        column_letter = get_column_letter(column_index)

        cell = f"{column_letter}{row_number}"

        body = {
            "values": [[new_value]]
        }

        (
            service.spreadsheets()
            .values()
            .update(
                spreadsheetId=SPREADSHEET_ID,
                range=f"{sheet_name}!{cell}",
                valueInputOption="USER_ENTERED",
                body=body,
            )
            .execute()
        )

    return "Row updated successfully."