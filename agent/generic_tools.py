from agent.schemas import (
    AppendDataInput,
    SearchDataInput,
    UpdateDataInput,
    DeleteDataInput,
)
from langchain_core.tools import tool

from sheets.generic_append import append_row
from sheets.generic_search import search_rows
from sheets.generic_update import update_row
from sheets.generic_delete import delete_row
from sheets.utils import validate_sheet

@tool(args_schema=AppendDataInput)
def append_data(
    sheet_name: str,
    row_data: dict,
):
    """
    Add a row to any worksheet.

    Parameters
    ----------
    sheet_name : Existing worksheet name

    row_data : Dictionary containing
               column names and values.
    """

    valid, sheet_names = validate_sheet(sheet_name)

    if not valid:

        return (
            f"Worksheet '{sheet_name}' does not exist.\n"
            f"Available worksheets:\n"
            f"{', '.join(sheet_names)}"
        )

    return append_row(
        sheet_name,
        row_data,
    )
@tool(args_schema=SearchDataInput)
def search_data(
    sheet_name: str,
    filters: dict,
):
    """
    Search rows in any worksheet.

    filters should contain
    column names and values.
    """

    valid, sheet_names = validate_sheet(sheet_name)

    if not valid:

        return (
            f"Worksheet '{sheet_name}' does not exist.\n"
            f"Available worksheets:\n"
            f"{', '.join(sheet_names)}"
        )

    return search_rows(
        sheet_name,
        filters,
    )
@tool(args_schema=UpdateDataInput)
def update_data(
    sheet_name: str,
    filters: dict,
    updates: dict,
):
    """
    Update rows in any worksheet.
    """

    valid, sheet_names = validate_sheet(sheet_name)

    if not valid:

        return (
            f"Worksheet '{sheet_name}' does not exist.\n"
            f"Available worksheets:\n"
            f"{', '.join(sheet_names)}"
        )

    return update_row(
        sheet_name,
        filters,
        updates,
    )
@tool(args_schema=DeleteDataInput)
def delete_data(
    sheet_name: str,
    filters: dict,
):
    """
    Delete rows in any worksheet.
    """

    valid, sheet_names = validate_sheet(sheet_name)

    if not valid:

        return (
            f"Worksheet '{sheet_name}' does not exist.\n"
            f"Available worksheets:\n"
            f"{', '.join(sheet_names)}"
        )

    return delete_row(
        sheet_name,
        filters,
    )