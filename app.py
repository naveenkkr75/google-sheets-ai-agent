from dashboard.stats import (
    get_inventory_dataframe,
    get_inventory_stats,
)

df = get_inventory_dataframe()

print(df)

print()

print(get_inventory_stats(df))