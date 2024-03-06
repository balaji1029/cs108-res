import os
import json

overall = {"data": []
}

file_num=4

test_cases = [4,6,4,4]

data = [];
os.system('clear')

#------------------------------test cxase 1---------------------------

for i in range(1,file_num+1):
    
    msg = ""
    total = 0
    result = {
        "testid": "1",
        "status": "success",
        "score": 0,
        "maximum marks" : test_cases[i-1],
        "message": ""
        }
    
    command=f"g++ buggy{i}.cpp 2>/dev/null"
    os.system(command)
    
    for j in range(1,test_cases[i-1]+1):
        
        command=f'timeout 1s ./a.out < testcases/buggy{i}/input{j}.txt > output.txt 2>/dev/null'
        os.system(command)
    
        command=f"diff -Bw output.txt testcases/buggy{i}/output{j}.txt 2>/dev/null"
        val= os.system(command)
        
        if(val==0):
            total+=1
        else:
            msg+=f'Output not as expected on case {j}. '
    result['score']=total
    result["score"] = total
    result["message"] = msg
    data.append(result)
        
overall['data'] = data
print(json.dumps(overall, indent=4))
with open('../evaluate.json', 'w') as f:
	json.dump(overall,f,indent=4)
