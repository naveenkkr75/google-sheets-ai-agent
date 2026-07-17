from sheets.service import get_sheet_service
from config import SPREADSHEET_ID


def get_headers(sheet_name):
    """
    Return the headers of a worksheet.

    Example:

    Inventory

    Product Name | Product ID | Price

    returns

    [
        "Product Name",
        "Product ID",
        "Price"
    ]
    """

    service = get_sheet_service()

    result = (
        service.spreadsheets()
        .values()
        .get(
            spreadsheetId=SPREADSHEET_ID,
            range=f"{sheet_name}!1:1",
        )
        .execute()
    )

    values = result.get("values", [])

    if not values:
        return []

    return values[0]