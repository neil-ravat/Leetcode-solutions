import pandas as pd

def department_highest_salary(employee: pd.DataFrame, department: pd.DataFrame) -> pd.DataFrame:
    employee['Max'] = employee.groupby('departmentId')['salary'].transform('max')
    condition = (employee['Max'] == employee['salary'])
    employee = employee.loc[condition]
    employee = employee.rename(columns = {'name': 'Employee'})
    merged = pd.merge(employee,department,left_on = "departmentId",right_on = "id",how = "left")
    merged = merged.rename(columns = {'name':'Department'})
    merged = merged.rename(columns = {'salary': 'Salary'})
    return merged[['Department','Employee','Salary']]