import os
import json
import subprocess

overall = {"data": []
}

data = [];

expected_obj=['add.o','sub.o','mul.o','divi.o']

os.system('clear')

# ----------------------test cxase 1---------------------------

msg = ""
total = 0
result = {
    "testid": "1",
    "status": "success",
    "score": 0,
    "maximum marks" : 25,
    "message": ""
    }

os.system('make clean 2>/dev/null')

for file in os.scandir(path='./'):
    if(not file.is_file()):
        continue
    if(file.name.endswith('.o')):
        msg='Object Files present after running make clean'
        result["score"] = total
        result["message"] = msg
        data.append(result)
        overall['data'] = data
        
        os.system('rm *.o 2>/dev/null')
        os.system('rm main[0-9] 2>/dev/null')
        print(json.dumps(overall, indent=4))
        with open('../evaluate.json', 'w') as f:
            json.dump(overall,f,indent=4)
        exit(0)
        
for file in os.scandir(path='./src/'):
    if(not file.is_file()):
        continue
    if(file.name.endswith('.o')):
        msg='Object Files present in src/ after running make clean'
        result['score']=total
        result["score"] = total
        result["message"] = msg
        data.append(result)
        overall['data'] = data
        
        os.system('rm *.o 2>/dev/null')
        os.system('rm main[0-9] 2>/dev/null')
        print(json.dumps(overall, indent=4))
        with open('../evaluate.json', 'w') as f:
            json.dump(overall,f,indent=4)
        exit(0)

os.system('make 2>/dev/null')

obj=[]

for file in os.scandir(path='./'):
    if(not file.is_file()):
        continue
    
    if(file.name.endswith('.cpp')):
        continue
    elif(file.name.endswith('.o')):
        obj.append(file.name)
        continue
    elif(not file.name.endswith('.txt')):
        continue
    name=file.name
    # print(name)
    command=f"./{name[:-4]} > output.txt 2>/dev/null"
    os.system(command)
    command=f"diff -Bw output.txt {name}"
    
    val=os.system(command)
    if(val==0):
        total+=1
    else:
        msg+=f'{file.name} output is not as expected. '

os.system('rm output.txt')
os.system('make clean 2>/dev/null')

check_list = [x for x in expected_obj if x in obj]

if(expected_obj == check_list):
    total+=2
else:
    msg+='List of created object files does not match with expected list of object files'
    result["score"] = total
    result["message"] = msg
    data.append(result)
    overall['data'] = data
    
    os.system('rm *.o 2>/dev/null')
    os.system('rm main[0-9] 2>/dev/null')
    print(json.dumps(overall, indent=4))
    with open('../evaluate.json', 'w') as f:
        json.dump(overall,f,indent=4)
    exit(0)

for file in os.scandir(path='./'):
    if(not file.is_file()):
        continue
    if(file.name.endswith('.o')):
        msg='Object Files present after running make clean'
        result["score"] = total
        result["message"] = msg
        data.append(result)
        overall['data'] = data
        
        os.system('rm *.o 2>/dev/null')
        os.system('rm main[0-9] 2>/dev/null')
        print(json.dumps(overall, indent=4))
        with open('../evaluate.json', 'w') as f:
            json.dump(overall,f,indent=4)
        exit(0)
    elif(len(file.name)==5 and file.name[-1]>='1' and file.name[-1]<='9' and file.name[:4]=="main"):
        msg='Executable Files present after running make clean'
        result["score"] = total
        result["message"] = msg
        data.append(result)
        overall['data'] = data
        
        os.system('rm *.o 2>/dev/null')
        os.system('rm main[0-9] 2>/dev/null')
        print(json.dumps(overall, indent=4))
        with open('../evaluate.json', 'w') as f:
            json.dump(overall,f,indent=4)
        exit(0)
        
for file in os.scandir(path='./src/'):
    if(not file.is_file()):
        continue
    if(file.name.endswith('.o')):
        msg='Object Files present in src/ after running make clean'
        result['score']=total
        result["score"] = total
        result["message"] = msg
        data.append(result)
        overall['data'] = data
        
        os.system('rm *.o 2>/dev/null')
        os.system('rm main[0-9] 2>/dev/null')
        print(json.dumps(overall, indent=4))
        with open('../evaluate.json', 'w') as f:
            json.dump(overall,f,indent=4)
        exit(0)

total+=4

if(total==15):
    
    os.system('make')
    os.system('touch src/add.cpp src/sub.cpp src/mul.cpp src/divi.cpp')
    earlier=[]
    for i in range(1,10):
        command=f'stat -c "%Y" main{i}'
        earlier.append(subprocess.check_output(command, shell=True))    
        pass
    
    os.system('sleep 2')
    os.system('make')
    latest=[]
    for i in range(1,10):
        command=f'stat -c "%Y" main{i}'
        latest.append(subprocess.check_output(command, shell =True))    
        pass
    
    val=0
    
    for i in range(len(latest)):
        if(earlier[i]==latest[i]):
            val=1
            break
    
    if(val):    
        msg+="Dependencies on the src/ files have not been specified properly"
        result['score']=total
        result["score"] = total
        result["message"] = msg
        data.append(result)
        overall['data'] = data
        
        os.system('rm *.o 2>/dev/null')
        os.system('rm main[0-9] 2>/dev/null')
        print(json.dumps(overall, indent=4))
        with open('../evaluate.json', 'w') as f:
            json.dump(overall,f,indent=4)
        exit(0)
    else:
        total+=4
    
    for i in range(1,10):
        command=f'touch main{i}.cpp'
        os.system(command)
        
    earlier=[]
    for i in range(1,10):
        command=f'stat -c \"%Y\" main{i}'
        earlier.append(subprocess.check_output(command, shell =True))    
        pass
    
    os.system('sleep 2')
    os.system('make')
    latest=[]
    for i in range(1,10):
        command=f'stat -c \"%Y\" main{i}'
        latest.append(subprocess.check_output(command,shell=True))    
        pass
    
    val=0
    
    for i in range(len(latest)):
        if(earlier[i]==latest[i]):
            val=1
            break
    
    if(val):    
        msg+="Dependencies on the main{digit}.cpp files have not been specified properly"
        result['score']=total
        result["score"] = total
        result["message"] = msg
        data.append(result)
        overall['data'] = data
        os.system('rm *.o 2>/dev/null')
        os.system('rm main[0-9] 2>/dev/null')
        print(json.dumps(overall, indent=4))
        with open('../evaluate.json', 'w') as f:
            json.dump(overall,f,indent=4)
        exit(0)
    else:
        total+=6
    pass
    os.system('make clean')

result['score']=total
result["score"] = total
result["message"] = msg
data.append(result)
overall['data'] = data
print(json.dumps(overall, indent=4))
with open('../evaluate.json', 'w') as f:
    json.dump(overall,f,indent=4)
os.system('rm *.o 2>/dev/null')
os.system('rm main[0-9] 2>/dev/null')
exit(0)
        

