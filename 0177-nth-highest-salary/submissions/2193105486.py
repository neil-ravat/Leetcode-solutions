import pandas as pd

def nth_highest_salary(employee: pd.DataFrame, N: int) -> pd.DataFrame:
    employee = employee.drop_duplicates(subset="salary", keep="first")
    employee = employee.sort_values(by="salary", ascending=False)

    if 1 <= N <= len(employee):
        value = employee["salary"].iloc[N - 1]
    else:
        value = None

    return pd.DataFrame({
        f"getNthHighestSalary({N})": [value]
    })