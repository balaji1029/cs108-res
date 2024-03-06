import pandas as pd
import numpy as np
import json

overall = {"data": [] 
} 
data = [] 
result = { 
    "testid": "1", 
    "status": "failed", 
    "score": 0, 
    "maximum marks" : 1, 
    "message": "not evaluated"
} 
try: 
    column_list = ['EMPLOYEE_ID','FIRST_NAME','LAST_NAME','SALARY','MANAGER_ID','Manager Name']
    df = pd.read_excel('Employee.xlsx',engine='openpyxl')[column_list].head(106).fillna(0).to_numpy()
    csv = pd.read_csv('Test.csv').fillna(0).to_numpy()
    a,b = np.where(df != csv)
    if a.size == 0:
        # print("Success")
        result['status'] = 'success' 
        result['score'] = 1 
        result['message'] = 'success and passed the test case' 
    else:
        # print("Mismatch at row " + str(a[0]+2) + " and column '" + column_list[b[0]]+"'. Expected value is: " + str(csv[a[0]][b[0]]) + ", your output is:  " + str(df[a[0]][b[0]]))
        result['message'] = "Mismatch at row " + str(a[0]+2) + " and column '" + column_list[b[0]]+"'. Expected value is: " + str(csv[a[0]][b[0]]) + ", your output is: " + str(df[a[0]][b[0]]) 
except Exception as e: 
    result['message'] = f'Script could not run due to error : {str(e)}'
    
data.append(result) 
overall['data'] = data
print(json.dumps(overall, indent=4)) 
with open('../evaluate.json', 'w') as f: 
    json.dump(overall,f,indent=4)