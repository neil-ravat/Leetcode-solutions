import pandas as pd

def calculate_special_bonus(employees: pd.DataFrame) -> pd.DataFrame:
    condition = (~(employees['name']).str.startswith("M")) & (employees['employee_id']%2!=0)
    employees['bonus'] = 0
    employees.loc[condition,'bonus'] = employees['salary']

    return employees.sort_values(by = "employee_id",ascending = True)[['employee_id','bonus']]