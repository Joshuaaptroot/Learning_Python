import pandas as pd

def combine_two_tables(person: pd.DataFrame, address: pd.DataFrame) -> pd.DataFrame:
    result = address.merge(person, on="personId", how="right").drop("addressId", axis=1)
    result.drop("personId", axis=1)
    New_order_df =  result[["firstName", "lastName", "city", "state"]]
    return New_order_df.sort_values(by="lastName", ascending=False)

