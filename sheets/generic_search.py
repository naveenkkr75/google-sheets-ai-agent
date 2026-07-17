from sheets.service import get_sheet_service
from config import SPREADSHEET_ID


def search_rows(sheet_name, filters):
    """
    Search rows in any worksheet.

    Parameters
    ----------
    sheet_name : str

    filters : dict

    Example

    {
        "Product Name": "Laptop"
    }

    Returns

    List of matching rows.
    """

    service = get_sheet_service()

    result = (
        service.spreadsheets()
        .values()
        .get(
            spreadsheetId=SPREADSHEET_ID,
            range=sheet_name,
        )
        .execute()
    )

    values = result.get("values", [])

    if len(values) <= 1:
        return []

    headers = values[0]

    data = values[1:]

    matches = []

    for row_number, row in enumerate(data, start=2):

        row_dict = {}

        for i, header in enumerate(headers):

            if i < len(row):
                row_dict[header] = row[i]
            else:
                row_dict[header] = ""

        matched = True

        for column, value in filters.items():

            if str(row_dict.get(column, "")).lower() != str(value).lower():
                matched = False
                break

        if matched:

            matches.append(
                {
                    "row_number": row_number,
                    "data": row_dict,
                }
            )

    return matches