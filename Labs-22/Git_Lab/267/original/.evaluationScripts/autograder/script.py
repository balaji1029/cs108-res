# pip install GitPython

import git
import json
import tarfile
import os

overall = {"data":[
	{
		"testid": "1",
		"status": "success",
		"score": -1,
		"message": ""
	}
]
}

my_tar = tarfile.open('/home/labDirectory/merge_repo.tar.gz')
my_tar.extractall("/home/labDirectory/") # specify which folder to extract to
my_tar.close()
os.system('clear')

try:
	repo = git.Repo("/home/labDirectory/merge_repo/")
except:

	overall['data'][0]["score"] = 0
	overall['data'][0]["message"] = "Could Not Find project folder"
	overall['data'][0]["status"] = "failure"
	print(json.dumps(overall, indent=4))

	with open('../evaluate.json', 'w') as f:
		json.dump(overall,f,indent=4)
	os.system("rm -rf /home/labDirectory/merge_repo/")      
	exit()

result = 0

# Task that must be present in the assignment 

os.system("git config --global --add safe.directory '*'")

try:	

	msg=""	
 
	branches = [head.name for head in repo.heads]
 
	if(len(branches)!=2 or "master" not in branches or "development" not in branches):
		msg+="Branches of the repository seem to have been modified. Only two branches, master and development must exist. Use git branch to see all branches."
	
	# print("Hello!")
	commit=list(repo.iter_commits("master"))[0]
	# print("Guys!")
	
	blobs={}
	
	for blob in commit.tree.blobs:
		blobs[blob.name]=blob

	# print(blobs)
 	# File 1

	if("file_1.cpp" not in blobs.keys()):
		msg+="file_1.cpp does not exist in HEAD of master. "
	else:
		curr_blob=blobs["file_1.cpp"]
		os.system("touch file_1.cpp")
		curr_blob.stream_data(open("file_1.cpp","wb"))
		code = os.system("g++ file_1.cpp")

		if(code!=0):
			msg+="file_1.cpp has compilation errors. "
		else:
			result+=1
			temp=0
			with open('input.txt','w') as f:
				f.write("2 3 5\n")
			os.system("./a.out < input.txt > output.txt")
			with open('true_output.txt','w') as g:
				g.write("26\nHello File1\n")
			temp+=1-os.system("diff -Bw true_output.txt output.txt")
   
			with open('input.txt','w') as f:
				f.write("45 340 20\n")
			os.system("./a.out < input.txt > output.txt")
			with open('true_output.txt','w') as g:
				g.write("3317\nHello File1\n")
			temp+=1-os.system("diff -Bw true_output.txt output.txt")
   
			with open('input.txt','w') as f:
				f.write("133 174 195\n")
			os.system("./a.out < input.txt > output.txt")
			with open('true_output.txt','w') as g:
				g.write("43938\nHello File1\n")
			temp+=1-os.system("diff -Bw true_output.txt output.txt")

			if(temp==3):
				result+=temp
				msg+="file_1.cpp has been merged perfectly! "
			else:
				msg+="Results of execution of file_1.cpp on test cases is not as expected. "
    
    # File 2
    
	if("file_2.cpp" not in blobs.keys()):
		msg+="file_2.cpp does not exist in HEAD of master. "
	else:
		curr_blob=blobs["file_2.cpp"]
		os.system("touch file_2.cpp")

		curr_blob.stream_data(open("file_2.cpp","wb"))

		code = os.system("g++ file_2.cpp")

		if(code!=0):
			msg+="file_2.cpp has compilation errors. "
		else:
			result+=1
			temp=0
			with open('input.txt','w') as f:
				f.write("2 3 5\n")
			os.system("./a.out < input.txt > output.txt")
			with open('true_output.txt','w') as g:
				g.write("-25\nHello File2\n")
			temp+=1-os.system("diff -Bw true_output.txt output.txt")
   
			with open('input.txt','w') as f:
				f.write("45 340 20\n")
			os.system("./a.out < input.txt > output.txt")
			with open('true_output.txt','w') as g:
				g.write("-319\nHello File2\n")
			temp+=1-os.system("diff -Bw true_output.txt output.txt")
   
			with open('input.txt','w') as f:
				f.write("133 174 195\n")
			os.system("./a.out < input.txt > output.txt")
			with open('true_output.txt','w') as g:
				g.write("-65\nHello File2\n")
			temp+=1-os.system("diff -Bw true_output.txt output.txt")

			if(temp==3):
				result+=temp
				msg+="file_2.cpp has been merged perfectly! "
			else:
				msg+="Results of execution of file_2.cpp on test cases is not as expected. "
    
    # File 3
    
	if("file_3.cpp" not in blobs.keys()):
		msg+="file_3.cpp does not exist in HEAD of master. "
	else:
		curr_blob=blobs["file_3.cpp"]
		os.system("touch file_3.cpp")

		curr_blob.stream_data(open("file_3.cpp","wb"))

		code = os.system("g++ file_3.cpp")

		if(code!=0):
			msg+="file_3.cpp has compilation errors. "
		else:
			result+=1
			temp=0
			with open('input.txt','w') as f:
				f.write("1\n3 8 10 9\n3 8 10 9\n")
			os.system("./a.out < input.txt > output.txt")
			with open('true_output.txt','w') as g:
				g.write("[ 10, 9, 8 ]\n{ 8 | 9 | 10 }\n")
			temp+=1-os.system("diff -Bw true_output.txt output.txt")
   
			with open('input.txt','w') as f:
				f.write("1\n5 67 83 10 48 38\n5 67 83 10 48 38\n")
			os.system("./a.out < input.txt > output.txt")
			with open('true_output.txt','w') as g:
				g.write("[ 83, 67, 48, 38, 10 ]\n{ 10 | 38 | 48 | 67 | 83 }\n")
			temp+=1-os.system("diff -Bw true_output.txt output.txt")
   
			with open('input.txt','w') as f:
				f.write("2\n5 8 29 46 123 38\n4 376 129 10 47\n4 376 129 10 47\n5 8 29 46 123 38\n")
			os.system("./a.out < input.txt > output.txt")
			with open('true_output.txt','w') as g:
				g.write("[ 123, 46, 38, 29, 8 ]\n{ 10 | 47 | 129 | 376 }\n[ 376, 129, 47, 10 ]\n{ 8 | 29 | 38 | 46 | 123 }\n")
			temp+=1-os.system("diff -Bw true_output.txt output.txt")

			if(temp==3):
				result+=temp
				msg+="file_3.cpp has been merged perfectly! "
			else:
				msg+="Results of execution of file_3.cpp on test cases is not as expected. "
    
    # File 4 Master
    
	if("file_4_master.cpp" not in blobs.keys()):
		msg+="file_4_master.cpp does not exist in HEAD of master. "
	else:
		curr_blob=blobs["file_4_master.cpp"]
		os.system("touch file_4_master.cpp")

		curr_blob.stream_data(open("file_4_master.cpp","wb"))

		code = os.system("g++ file_4_master.cpp")

		if(code!=0):
			msg+="file_4_master.cpp has compilation errors. "
		else:
			result+=1
			temp=0
			os.system("echo 5 | ./a.out > output.txt")
		
			temp+=1-os.system("diff -Bw true_output_master_1.txt output.txt")
   
			os.system("echo 8 | ./a.out > output.txt")
			temp+=1-os.system("diff -Bw true_output_master_2.txt output.txt")
   
			os.system("echo 12 | ./a.out  > output.txt")
			temp+=1-os.system("diff -Bw true_output_master_3.txt output.txt")

			if(temp==3):
				result+=temp
				msg+="file_4_master.cpp has been merged perfectly! "
			else:
				msg+="Results of execution of file_4_master.cpp on test cases is not as expected. "
    
    # File 4 Development
    
    
	if("file_4_development.cpp" not in blobs.keys()):
		msg+="file_4_development.cpp does not exist in HEAD of master. "
	else:
		curr_blob=blobs["file_4_development.cpp"]
		os.system("touch file_4_development.cpp")

		curr_blob.stream_data(open("file_4_development.cpp","wb"))

		code = os.system("g++ file_4_development.cpp")

		if(code!=0):
			msg+="file_4_development.cpp has compilation errors. "
		else:
			result+=1
			temp=0
			os.system("echo 5 | ./a.out  > output.txt")
		
			temp+=1-os.system("diff -Bw true_output_development_1.txt output.txt")
   
			os.system("echo 8 | ./a.out  > output.txt")
			temp+=1-os.system("diff -Bw true_output_development_2.txt output.txt")
   
			os.system("echo 12 | ./a.out  > output.txt")
			temp+=1-os.system("diff -Bw true_output_development_3.txt output.txt")

			result+=temp
			if(temp==3):
				msg+="file_4_development.cpp has been merged perfectly! "
			else:
				msg+="Results of execution of file_4_development.cpp on test cases is not as expected. "
    
	overall['data'][0]["score"] = result
	overall['data'][0]["message"] = msg
	print(json.dumps(overall, indent=4))
	with open('../evaluate.json', 'w') as f:
     
		json.dump(overall,f,indent=4)
except Exception as e:
	print(str(e))
	pass

os.system("rm -rf /home/labDirectory/merge_repo/ 2>/dev/null")
os.system("rm a.out file_1.cpp file_2.cpp file_3.cpp file_4_development.cpp file_4_master.cpp input.txt output.txt true_output.txt 2>/dev/null")
    
# 	commits = list(repo.iter_commits("master"))
# 	branchResult = branchResult + 1

# 	for file in repo.tree(commits[0].hexsha) :
# 		if file.path == "hdr.h" :
# 			masterFiles = masterFiles + 0.5
# 		if file.path == "main.cpp" :
# 			masterFiles = masterFiles + 0.5
# 		if file.path == "math.cpp" :
# 			masterFiles = masterFiles + 0.5
	
# 	if(commits[0].message.strip("\n").strip(" ") == "Multiplication") :
# 		masterCommitResult = masterCommitResult + 1
# 	if(commits[1].message.strip("\n").strip(" ") == "Git commit without going to staging area") :
# 		masterCommitResult = masterCommitResult + 1
# 	if(commits[2].message.strip("\n").strip(" ") == "Git commit with message") :
# 		masterCommitResult = masterCommitResult + 1
# 	if(commits[3].message.strip("\n").strip(" ") == "Commit") :
# 		masterCommitResult = masterCommitResult + 1
	
# except :
# 	pass

# try :

# 	commits = list(repo.iter_commits("merge_example"))
# 	branchResult = branchResult + 1

# 	for file in repo.tree(commits[0].hexsha) :
# 		if file.path == "hdr.h" :
# 			mergeExampleFiles = mergeExampleFiles + 0.5
# 		if file.path == "main.cpp" :
# 			mergeExampleFiles = mergeExampleFiles + 0.5
# 		if file.path == "math.cpp" :
# 			mergeExampleFiles = mergeExampleFiles + 0.5
	
# 	if(commits[0].message.strip("\n").strip(" ") == "Subtraction") :
# 		mergeExampleCommitResult = mergeExampleCommitResult + 1
# 	if(commits[1].message.strip("\n").strip(" ") == "Git commit without going to staging area") :
# 		mergeExampleCommitResult = mergeExampleCommitResult + 1
# 	if(commits[2].message.strip("\n").strip(" ") == "Git commit with message") :
# 		mergeExampleCommitResult = mergeExampleCommitResult + 1
# 	if(commits[3].message.strip("\n").strip(" ") == "Commit") :
# 		mergeExampleCommitResult = mergeExampleCommitResult + 1
	
# except :
# 	pass

# print("--------------------Master Brach------------------")
# print("Master commit result ", masterCommitResult)
# print("Master file result ", masterFiles)

# print("--------------------Merge example Brach------------------")
# print("Master commit result ", mergeExampleCommitResult)
# print("Master file result ", mergeExampleFiles)

# print("-------------------Branch------------------------")
# print("Brach result ", branchResult)

# indexChecks["masterCommitResult"]= masterCommitResult
# indexChecks["masterFiles"]= masterFiles
# indexChecks["mergeExampleCommitResult"]= mergeExampleCommitResult
# indexChecks["mergeExampleFiles"]= mergeExampleFiles
# indexChecks["branchResult"]= branchResult
# total = masterCommitResult + masterFiles  + mergeExampleCommitResult + mergeExampleFiles + branchResult
# overall['data'][0]["score"] = total
# overall['data'][0]["message"] = indexChecks
# print(json.dumps(overall, indent=4))
# with open('../evaluate.json', 'w') as f:
# 	json.dump(overall,f,indent=4)

