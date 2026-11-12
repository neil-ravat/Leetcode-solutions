import pandas as pd

def top_three_salaries(employee: pd.DataFrame, department: pd.DataFrame) -> pd.DataFrame:
    employee['rank'] = employee.groupby('departmentId')['salary'].rank(method = "dense",ascending = False)
    department = department.rename(columns = {'name':'Department'})
    employee = employee.rename(columns = {"name" : "Employee"})
    employee = employee.rename(columns = {"salary" : "Salary"})
    condition = (employee['rank'] <= 3)
    employee = employee.loc[condition]
    merged =  pd.merge(employee,department,left_on = 'departmentId',right_on = "id",how = "left")
    return merged[['Department','Employee','Salary']]