import os
import json

overall = {"data": []
}

data = [];

test_case_num = 12
input_file_name = 'input.txt'
output_file_name = 'output.txt'
test_file_name = 'maxminsumavg'
submission_file_name = 'submission.sh'
output_dir_name = 'output'

command = 'clear'
os.system(command)
command=f"mkdir ./{output_dir_name}"
os.system(command)
#------------------------------test case 1---------------------------

for i in range(1,test_case_num+1):
    
    msg = ""
    total = 0
    result = {
        "testid": "1",
        "status": "success",
        "score": 0,
        "maximum marks" : 1,
        "message": ""
        }
    
    file_data=""
    
    with open(f"./testcases/{i}/{input_file_name}",'r') as file:
        file_data=file.readline()
        
    # print(file_data)
    
    # command=f"bash {test_file_name} {file_data} > ./testcases/{i}/{output_file_name}"
    # # print(command)
    # os.system(command)
    
    command=f"mkdir ./{output_dir_name}/{i}"
    os.system(command)
    
    command=f"bash {submission_file_name} {file_data} > ./{output_dir_name}/{i}/{output_file_name}"
    # print(command)
    rval = os.system(command)
  
  
    if rval == 0 :
        msg = msg + str("Script Executed Successfully. ")
    else :
        msg = msg + str("Error in Executing Script. ")
        result["status"]="failed"
        
    command=f"diff -bw ./testcases/{i}/{output_file_name} ./{output_dir_name}/{i}/{output_file_name} > /dev/null 2>/dev/null"
    rval = os.system(command)
    
    if rval == 0:
        total=total+1
        msg = msg + str("Test Case Passed.")
    else:
        msg = msg + str("Output is not as Expected.")
        msg = msg + str("Refer to testcases/") # For the failing test case, refer to /home/.evaluationScripts/autograder/testcases/")
        msg = msg + str(i) +"/ ."
        
    # # list to store files
    # files = []
    # tres = [('1992-13-22-sdads.jpg').strip(), ('1993-03-12-sadsadsda.jpg').strip(), ('2000-09-89-dsad.jpg').strip()]
    # # Iterate directory
    # cnt = 0
    # extra = 0

    # for file in os.listdir("./output/") :
    #     if file in tres:
    #         cnt = cnt + 1
    #     else:
    #         extra = extra + 1

    # if cnt == len(tres):
    #     if extra == 0 :
    #         total = total + 2
    #         msg = msg + str("Correct output. ")
    #     else :
    #         total = total + 1
    #         msg = msg + str("Correct output with extra files. ")
    # else : 
    #     total = total + 0
    #     msg = msg + str("Wrong output. ")

    result["testid"] = i
    result["score"] = total
    result["message"] = msg
    data.append(result)
    
os.system("rm -rf ./output")

overall['data'] = data
print(json.dumps(overall, indent=4))
with open('../evaluate.json', 'w') as f:
	json.dump(overall,f,indent=4)
