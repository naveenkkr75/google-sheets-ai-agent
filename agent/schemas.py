from pydantic import BaseModel, Field


class AppendDataInput(BaseModel):
    """Input schema for appending a row."""

    sheet_name: str = Field(
        description="Existing worksheet name."
    )

    row_data: dict = Field(
        description="Dictionary mapping column names to values."
    )


class SearchDataInput(BaseModel):
    """Input schema for searching rows."""

    sheet_name: str = Field(
        description="Existing worksheet name."
    )

    filters: dict = Field(
        description="Dictionary of column names and values to search."
    )


class UpdateDataInput(BaseModel):
    """Input schema for updating rows."""

    sheet_name: str = Field(
        description="Existing worksheet name."
    )

    filters: dict = Field(
        description="Dictionary used to find the row."
    )

    updates: dict = Field(
        description="Dictionary of columns and their new values."
    )


class DeleteDataInput(BaseModel):
    """Input schema for deleting rows."""

    sheet_name: str = Field(
        description="Existing worksheet name."
    )

    filters: dict = Field(
        description="Dictionary used to find the row."
    )