import pandas as pd

from sheets.read import read_sheet


def get_inventory_dataframe(sheet_name="Inventory"):
    data = read_sheet(sheet_name)

    if not data:
        return pd.DataFrame()

    df = pd.DataFrame(data)

    if "Price" in df.columns:
        df["Price"] = (
            pd.to_numeric(
                df["Price"],
                errors="coerce"
            )
            .fillna(0)
            .astype(float)
        )

    if "Product ID" in df.columns:
        df["Product ID"] = (
            pd.to_numeric(
                df["Product ID"],
                errors="coerce"
            )
            .fillna(0)
            .astype(int)
        )

    return df


def get_inventory_stats(df):

    if df.empty:
        return {
            "products": 0,
            "total_value": 0,
            "average_price": 0,
            "max_price": 0,
        }

    return {
        "products": int(len(df)),
        "total_value": int(df["Price"].sum()),
        "average_price": float(round(df["Price"].mean(), 2)),
        "max_price": int(df["Price"].max()),
    }