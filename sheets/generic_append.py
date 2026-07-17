from sheets.service import get_sheet_service
from sheets.schema import get_headers
from config import SPREADSHEET_ID


def append_row(sheet_name, row_data):
    """
    Append a row to any worksheet.

    Prevent duplicate Product IDs.
    """

    service = get_sheet_service()

    headers = get_headers(sheet_name)

    # --------------------------------
    # Required field validation
    # --------------------------------

    required_fields = [
        "Product Name",
        "Product ID",
        "Price",
    ]

    for field in required_fields:

        if field in headers:

            if field not in row_data:
                return f"{field} is required."

            if str(row_data[field]).strip() == "":
                return f"{field} cannot be empty."
            # --------------------------------
            # Product ID validation
            # --------------------------------

            if "Product ID" in row_data:

                try:
                    int(row_data["Product ID"])

                except (ValueError, TypeError):
                    return "Product ID must be a number."
            # --------------------------------
            # Price validation
            # --------------------------------

            if "Price" in row_data:

                try:
                    price = float(row_data["Price"])

                    if price < 0:
                        return "Price cannot be negative."

                except (ValueError, TypeError):
                    return "Price must be numeric."

    if not headers:
        return "Worksheet has no headers."

    # -----------------------------
    # Check duplicate Product ID
    # -----------------------------

    if "Product ID" in headers and "Product ID" in row_data:

        result = (
            service.spreadsheets()
            .values()
            .get(
                spreadsheetId=SPREADSHEET_ID,
                range=sheet_name,
            )
            .execute()
        )

        rows = result.get("values", [])

        product_id_index = headers.index("Product ID")

        for row in rows[1:]:   # Skip header row

            if len(row) > product_id_index:

                if str(row[product_id_index]) == str(row_data["Product ID"]):

                    return (
                        f"Product ID {row_data['Product ID']} already exists."
                    )

    # -----------------------------
    # Build row
    # -----------------------------

    values = []

    for header in headers:
        values.append(
            row_data.get(header, "")
        )

    body = {
        "values": [values]
    }

    (
        service.spreadsheets()
        .values()
        .append(
            spreadsheetId=SPREADSHEET_ID,
            range=sheet_name,
            valueInputOption="USER_ENTERED",
            body=body,
        )
        .execute()
    )

    return "Row added successfully."