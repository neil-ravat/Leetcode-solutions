import pandas as pd

def find_patients(patients: pd.DataFrame) -> pd.DataFrame:
    condition = ((patients['conditions']).str.contains(r'^DIAB1')) | ((patients['conditions']).str.contains(r' DIAB1'))
    return patients.loc[condition,['patient_id','patient_name','conditions']]