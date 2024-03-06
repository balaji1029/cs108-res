import pandas as pd
import numpy as np
import json
import csv

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
    column_list = ['2014','2015','2016','2017','2018','Grand Total']
    d = dict()
    with open('Test.csv', mode ='r') as file:
        for lines in csv.reader(file):
            d[lines[0]] = lines[1:]
    try:
        df = pd.read_excel('Sales.xlsx', 'Pivot',engine='openpyxl').to_numpy()
        flag = True
        for row in df:
            if row[0] in d:
                for index, value in enumerate(d[row[0]]):
                    if int(value) != int(row[index+1]):
                        # print("On " + column_list[index] + " and item " + row[0] + " expected value is " + str(int(value)) + " , your output is " + str(int(row[index+1])))
                        result['message'] = "On " + column_list[index] + " and item " + row[0] + " expected value is " + str(int(value)) + " , your output is " + str(int(row[index+1])) 
                        flag = False
                        break
                if flag == False:
                    break
                del d[row[0]]
        else:
            if bool(d) :
                # print("Item " + list(d.keys())[0] + " is missing")
                result['message'] = "Item " + list(d.keys())[0] + " is missing"
                flag = False
        if flag:
            # print("Success")
            result['status'] = 'success' 
            result['score'] = 1 
            result['message'] = 'success and passed the test case' 
    except KeyError:
        # print("Unable to find sheet named Pivot. Name the Pivot table sheet as 'Pivot'")
        result['message'] = "Unable to find sheet named Pivot. Name the Pivot table sheet as 'Pivot'"
except Exception as e: 
    result['message'] = f'Script could not run due to error : {str(e)}'
    
data.append(result) 
overall['data'] = data
print(json.dumps(overall, indent=4)) 
with open('../evaluate.json', 'w') as f: 
    json.dump(overall,f,indent=4)
    

    