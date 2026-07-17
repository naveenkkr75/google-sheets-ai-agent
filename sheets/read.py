from sheets.service import get_sheet_service
from config import SPREADSHEET_ID


def read_sheet(sheet_name):
    """
    Return all rows from a worksheet.
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

    if not values:
        return []

    headers = values[0]

    data = []

    for row in values[1:]:

        row_dict = {}

        for i, header in enumerate(headers):

            if i < len(row):
                row_dict[header] = row[i]
            else:
                row_dict[header] = ""

        data.append(row_dict)

    return data