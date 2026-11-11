import pandas as pd

def second_highest_salary(employee: pd.DataFrame) -> pd.DataFrame:
    employee = employee.drop_duplicates(subset = "salary",keep = "first")
    employee = employee.sort_values(by = "salary",ascending = False)
    
    if (len(employee) >= 2):
        value = employee['salary'].iloc[1]
    else:
        value = None

    return pd.DataFrame({'SecondHighestSalary' : [value]})