import pandas as pd

def find_customers(customers: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    merged = pd.merge(customers,orders,left_on = "id",right_on = "customerId",how = "left")
    merged = merged.rename(columns = {'name':'Customers'})
    condition = merged['customerId'].isna()
    return merged.loc[condition,['Customers']]