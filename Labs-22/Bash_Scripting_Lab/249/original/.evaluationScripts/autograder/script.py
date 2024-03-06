import os
import json

overall = {"data": []
}

data = [];

test_case_num = 3
test_file_name = 'append_string'
submission_file_name = 'submission.sh'
output_dir_name = 'output'
true_output_dir_name = 'true_output'
string_list=['Hello World','Is this done?','How difficult can it be34590uawef oiasdoncoiw ?? ojosdsf','This coeOIHERTOIgknk RANDOM STRING!!!--==++','3459u eeargfy09q3b  0988yq344tjaefefn   wefiuhaefe9y8  wefuhuha sff9898y  ewef88yy  908qywr  0q04t45ef.f.gf..asd...-=-.=-.4-.4-= ']

command='clear'
os.system(command)
command=f"mkdir ./{output_dir_name}"
os.system(command)
# command=f"mkdir ./{true_output_dir_name}"
# os.system(command)
#------------------------------test cxase 1---------------------------

for i in range(1,test_case_num+1):
    
    msg = ""
    total = 0
    result = {
        "testid": "1",
        "status": "success",
        "score": 0,
        "maximum marks" : 3,
        "message": ""
        }
    
    # command=f"mkdir ./{output_dir_name}/{i}"
    # os.system(command)

    # command=f"mkdir ./{true_output_dir_name}/{i}"
    # os.system(command)
        
    # print(file_data)
    
    command=f"cp -R ./testcases/{i}/ ./{output_dir_name}/"
    # print(command)
    os.system(command)
    
    
    # command=f"cp -R ./testcases/{i}/ ./{true_output_dir_name}/"
    # # print(command)
    # os.system(command)
    
    # exit(0)
    
    # command=f"cp ./{test_file_name} ./{true_output_dir_name}/{i}/{test_file_name}"
    # # print(command)
    # os.system(command)
    
    
    command=f"cp ./{submission_file_name} ./{output_dir_name}/{i}/{submission_file_name}"
    # print(command)
    os.system(command)
    
    # exit(0)
    # command=f"cd ./{true_output_dir_name}/{i}/ && ./{test_file_name} {string_list[i-1]} && rm {test_file_name} && cd ../../"
    # # print(command)
    # os.system(command)
    
    # command=f"bash {test_file_name}"
    # # print(command)
    # rval = os.system(command)
    
    # command=f"rm {test_file_name}"
    # # print(command)
    # os.system(command)
    
    # command=f"cd ../../"
    # # print(command)
    # os.system(command)
    
    # exit(0)
    
    command=f"cd ./{output_dir_name}/{i}/ && bash {submission_file_name} {string_list[i-1]} && rm {submission_file_name} && cd ../../"
    # print(command)
    rval = os.system(command)
    
    # exit(0)
    
    # command=f"bash {submission_file_name}"
    # # print(command)
    # rval = os.system(command)
    
    # command=f"rm {submission_file_name}"
    # # print(command)
    # os.system(command)
    
    # command=f"cd ../../"
    # # print(command)
    # os.system(command)
  
  
    if rval == 0 :
        msg = msg + str("Script Executed Successfully. ")
    else :
        msg = msg + str("Error in Executing Script. ")
        result["status"]="failed"
        
    command=f"diff -bw ./{true_output_dir_name}/{i}/ ./{output_dir_name}/{i}/ > /dev/null 2>/dev/null"
    rval2 = os.system(command)
    
    directory=f"./{output_dir_name}/{i}/"
    
    if rval2 == 0 and rval==0:
        total=total+3
        msg = msg + str("Test Case Passed.")
    elif rval==0:
        msg = msg + str("Something went wrong.")
        msg = msg + str("Refer to testcases/") # For the failing test case, refer to /home/.evaluationScripts/autograder/testcases/")
        msg = msg + str(i) +"/ ."
        msg = msg + str("Expected Output is in true_output/") # For the failing test case, refer to /home/.evaluationScripts/autograder/testcases/")
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

command=f"rm -rf ./{output_dir_name}/"
# print(command)
os.system(command)
# command=f"rm -rf ./{true_output_dir_name}/"
# # print(command)
# os.system(command)

overall['data'] = data
print(json.dumps(overall, indent=4))
with open('../evaluate.json', 'w') as f:
	json.dump(overall,f,indent=4)
