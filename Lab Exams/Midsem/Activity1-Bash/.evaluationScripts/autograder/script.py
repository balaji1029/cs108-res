import os
import json

overall = {"data": []
}

data = [];

test_case_num = 2
submission_file_name = 'submission.sh'
output_dir_name = 'output'
true_output_dir_name = 'true_output'

files = [['a.py','b.py','c.py','d.py'],
         ['a.py','b.py','c.py','d.py'],
         ]

command=f"mkdir ./{output_dir_name}"
os.system(command)

#------------------------------test cxase 1---------------------------

for i in range(1,test_case_num+1):
    
    msg = ""
    total = 0
    result = {
        "testid": "1",
        "status": "success",
        "score": 0,
        "maximum marks" : 7,
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
    
    
    # command=f"cp ./{submission_file_name} ./{output_dir_name}/{i}/{submission_file_name}"
    # # print(command)
    # os.system(command)
    
    # exit(0)
    # command=f"cd ./{true_output_dir_name}/{i}/ && bash {test_file_name} && rm {test_file_name} && cd ../../"
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
    
    command=f"bash {submission_file_name} ./{output_dir_name}/{i}/ > temp.txt"
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
        msg['status']='failed'
        
    command=f"diff -Bw ./{true_output_dir_name}/{i}/ ./{output_dir_name}/{i}/ 2>/dev/null"
    rval2 = os.system(command)
    
    directory=f"./{output_dir_name}/{i}/"
    
    if rval2 == 0 and rval==0:
        total=total+3
    elif rval==0:
        msg = msg + str("Directory structure is not as Expected. ")
        co=0
        for file in os.listdir(directory):
            if file.endswith('.py'):
                co=co+1
                msg = msg + str("All .py files not deleted. ")
                break;
        # print(co)
        if(co==0):
            total=total+1
            msg = msg + str("All .py files deleted, but extra files deleted too. ")
        
    lines=[]
    try:
        f=open('log.txt','r')
        lines=f.readlines()
    except:
        msg = msg + str("log.txt file does not exist. ")
    
    check_file=[]
    for line in lines:
        if(len(line)<=8):
            msg = msg + str("log.txt format not correct. ")
            break
        # print(line[8:-1])
        check_file.append(line[8:-1])

    # print(len(check_file))
    # print(check_file)
    if(len(check_file)==len(files[i-1])):
        total+=1
    else:
        msg = msg+ str("Total number of log entries incorrect. ")
    
    co=0
    
    check_file.sort()
    # print(check_file)
    
    if(check_file==files[i-1]):
        total+=2
    else:
        msg = msg + str("List of deleted files not correct. ")
        
    f=open('temp.txt')
    try:
        line=(int)(f.readlines()[0].strip())
        if(line==len(files[i-1])):
            total+=1
        else:
            msg = msg+str('Number printed to console not correct. ')
    except:
        msg=msg + str("No valid integer value printed to terminal. ")
    
    if(total==7):
        msg = msg + str("Test Case Passed. ")

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
    os.system('rm log.txt 2>/dev/null')

command=f"rm -rf ./{output_dir_name}/"
# print(command)
os.system(command)
os.system('rm temp.txt')
# command=f"rm -rf ./{true_output_dir_name}/"
# # print(command)
# os.system(command)

overall['data'] = data
print(json.dumps(overall, indent=4))
with open('../evaluate.json', 'w') as f:
	json.dump(overall,f,indent=4)
