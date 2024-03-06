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
		"message": "",
		"maximum_marks":"14"
	}
]
}

my_tar = tarfile.open('repo.tar.gz')
my_tar.extractall("./") # specify which folder to extract to
my_tar.close()
try:
	repo = git.Repo("./repo/")
except:

	overall['data'][0]["score"] = 0
	overall['data'][0]["message"] = "Could Not Find project folder"
	overall['data'][0]["status"] = "failure"
	print(json.dumps(overall, indent=4))

	with open('../evaluate.json', 'w') as f:
		json.dump(overall,f,indent=4)
	os.system("rm -rf ./big_repo/")      
	exit()

branchResult = 0

# Task that must be present in the assignment 

os.system("git config --global --add safe.directory '*'")

try:	

	# Checking for branches
	total=0
	msg=""
 
	branch_objects=[head.name for head in repo.heads]
	
	if(len(branch_objects)!=2 or 'master' not in branch_objects or 'development' not in branch_objects):
		overall['data'][0]["score"] = 0
		overall['data'][0]["status"] = 'failure'
		overall['data'][0]["message"] = "There should be exactly 2 branches in the repository, master and development. "
		print(json.dumps(overall, indent=4))
		with open('../evaluate.json', 'w') as f:
			json.dump(overall,f,indent=4)
		os.system("rm -rf ./repo/")
		exit()
	
	total+=1
	master_commit_list = list(repo.iter_commits("master"))
	development_commit_list = list(repo.iter_commits("development"))

	if(len(master_commit_list)!=3 or len(development_commit_list)!=3):
		overall['data'][0]["score"] = total
		overall['data'][0]["status"] = 'failure'
		overall['data'][0]["message"] = "Both the master and development branch should have exactly 3 commits. "
		print(json.dumps(overall, indent=4))
		with open('../evaluate.json', 'w') as f:
			json.dump(overall,f,indent=4)
		os.system("rm -rf ./repo/")
		exit()

	total+=2

	if(master_commit_list[2].hexsha!='1f02915dd7f2be1f4784b6ddd8ff0bbd4802fa66'):
		overall['data'][0]["score"] = total
		overall['data'][0]["status"] = 'failure'
		overall['data'][0]["message"] = "The original commit in the repo seems to have been modified in some way. "
		print(json.dumps(overall, indent=4))
		with open('../evaluate.json', 'w') as f:
			json.dump(overall,f,indent=4)
		os.system("rm -rf ./repo/")
		exit()

	total+=1

	if(development_commit_list[2].hexsha!='1f02915dd7f2be1f4784b6ddd8ff0bbd4802fa66' or development_commit_list[1].hexsha!=master_commit_list[1].hexsha):
		overall['data'][0]["score"] = total
		overall['data'][0]["status"] = 'failure'
		overall['data'][0]["message"] = "Possibly the development branch has not been branched off at the right commit. "
		print(json.dumps(overall, indent=4))
		with open('../evaluate.json', 'w') as f:
			json.dump(overall,f,indent=4)
		os.system("rm -rf ./repo/")
		exit()
	
	total+=1
	
	if(master_commit_list[1].message.strip().lower()!='recreated files' or development_commit_list[0].message.strip().lower()!='removed file_master.cpp' or master_commit_list[0].message.strip().lower()!='removed file_development.cpp'):
		overall['data'][0]["score"] = total
		overall['data'][0]["status"] = 'failure'
		overall['data'][0]["message"] = "The commit messages are not as specified. "
		print(json.dumps(overall, indent=4))
		with open('../evaluate.json', 'w') as f:
			json.dump(overall,f,indent=4)
		os.system("rm -rf ./repo/")
		exit()

	total+=3
 
	file_names = [blob.name for blob in master_commit_list[1].tree.blobs]

	if(len(file_names)!=2 or 'file_master.cpp' not in file_names or 'file_development.cpp' not in file_names):
		overall['data'][0]["score"] = total
		overall['data'][0]["status"] = 'failure'
		overall['data'][0]["message"] = "The \'Recreated files\' commit should have exactly 2 files, file_master.cpp and file_development.cpp. "
		print(json.dumps(overall, indent=4))
		with open('../evaluate.json', 'w') as f:
			json.dump(overall,f,indent=4)
		os.system("rm -rf ./repo/")
		exit()
	
	total+=2
	if(len(master_commit_list[0].tree.blobs)!=1 or 'file_master.cpp' != master_commit_list[0].tree.blobs[0].name):
		overall['data'][0]["score"] = total
		overall['data'][0]["status"] = 'failure'
		overall['data'][0]["message"] = "The latest master commit should have exactly 1 file, file_master.cpp. "
		print(json.dumps(overall, indent=4))
		with open('../evaluate.json', 'w') as f:
			json.dump(overall,f,indent=4)
		os.system("rm -rf ./repo/")
		exit()

	total+=2
 
	if(len(development_commit_list[0].tree.blobs)!=1 or 'file_development.cpp' != development_commit_list[0].tree.blobs[0].name):
		overall['data'][0]["score"] = total
		overall['data'][0]["status"] = 'failure'
		overall['data'][0]["message"] = "The latest development commit should have exactly 1 file, file_development.cpp. "
		print(json.dumps(overall, indent=4))
		with open('../evaluate.json', 'w') as f:
			json.dump(overall,f,indent=4)
		os.system("rm -rf ./repo/")
		exit()
	
	total+=2
 
	# for blob in master_commit_list[1].tree.blobs:
	# 	blob.stream_data(open(blob.name,"wb"))

	# rval=os.system('g++ file_master.cpp 2>/dev/null')
	# # score=0
	# if(rval==0):
	# 	score=1
	# 	for i in range(1,4):
	# 		os.system(f'./a.out < input{i}.txt > out.txt')
	# 		rval=os.system(f'diff output{i}_master.txt out.txt')
	# 		if(rval==0):
	# 			score+=2
	# 	os.system('rm out.txt a.out')
	# 	total+=score
	# 	if(score!=7):
	# 		msg = msg + str('The output for file_master.cpp in Recreated Files commit is not matching. ')
	# else:
	# 	msg = msg + str('There seems to be some compilation error in file_master.cpp in Recreated Files commit. ')
	
	# rval=os.system('g++ file_development.cpp 2>/dev/null')
	
	# if(rval==0):
	# 	score=1
	# 	for i in range(1,4):
	# 		os.system(f'./a.out < input{i}.txt > out.txt')
	# 		rval=os.system(f'diff output{i}_development.txt out.txt')
	# 		if(rval==0):
	# 			score+=2
	# 	os.system('rm out.txt a.out')
	# 	total+=score
	# 	if(score!=7):
	# 		msg = msg + str('The output for file_development.cpp in Recreated Files commit is not matching. ')
	# else:
	# 	msg = msg + str('There seems to be some compilation error in file_development.cpp in Recreated Files commit. ')
	
	# os.system('rm file_master.cpp file_development.cpp')
	
	# development_commit_list[0].tree.blobs[0].stream_data(open(development_commit_list[0].tree.blobs[0].name,"wb"))
	# master_commit_list[0].tree.blobs[0].stream_data(open(master_commit_list[0].tree.blobs[0].name,"wb"))

	# rval=os.system('g++ file_master.cpp 2>/dev/null')
	# # score=0
	# if(rval==0):
	# 	score=0	
	# 	for i in range(1,4):
	# 		os.system(f'./a.out < input{i}.txt > out.txt')
	# 		rval=os.system(f'diff output{i}_master.txt out.txt')
	# 		if(rval==0):
	# 			score+=2
	# 	os.system('rm out.txt a.out')
	# 	total+=score
	# 	if(score!=6):
	# 		msg = msg + str('The output for file_master.cpp in Removed file_development.cpp commit is not matching. ')
	# else:
	# 	msg = msg + str('There seems to be some compilation error in file_master.cpp in Removed file_development.cpp commit. ')
	
	# rval=os.system('g++ file_development.cpp 2>/dev/null')
	
	# if(rval==0):
	# 	score=0
	# 	for i in range(1,4):
	# 		os.system(f'./a.out < input{i}.txt > out.txt')
	# 		rval=os.system(f'diff output{i}_development.txt out.txt')
	# 		if(rval==0):
	# 			score+=2
	# 	os.system('rm out.txt a.out')
	# 	total+=score
	# 	if(score!=6):
	# 		msg = msg + str('The output for file_development.cpp in Removed file_master.cpp commit is not matching. ')
	# else:
	# 	msg = msg + str('There seems to be some compilation error in file_development.cpp in Removed file_master.cpp commit. ')
	
	# os.system('rm file_master.cpp file_development.cpp')
	
	overall['data'][0]["score"] = total
	overall['data'][0]["status"] = 'success'
	overall['data'][0]["message"] = msg + str("Test case processed. ")
	print(json.dumps(overall, indent=4))
	with open('../evaluate.json', 'w') as f:
		json.dump(overall,f,indent=4)
	os.system("rm -rf ./repo/")
	exit()

 	# # print(branch_objects)
	
 
	# hashes = ['a47c2e6ff4e89f8384ca4263bda017a28403d1b5','f3b067b5329888ed53b5b78ba94d0572c160ab91','47d3221c8b17d00745b2f8c02240eb33ff8bf19b','33267a4e142c8c46e27389b4d32034bcd942be90'\
    #  		  '401c7987dd3e5c7eca39b59872d3fc201ff06e88','64afe69c25367353f46799a7f15e99667e4a0742','03adf90521b4365fed0c2e2b344abc751e7918e6']
 
	# if( len(master_commit_list)!=7 or \
    # 	master_commit_list[0].hexsha!='a47c2e6ff4e89f8384ca4263bda017a28403d1b5' or \
    # 	master_commit_list[1].hexsha!='f3b067b5329888ed53b5b78ba94d0572c160ab91' or \
    # 	master_commit_list[2].hexsha!='47d3221c8b17d00745b2f8c02240eb33ff8bf19b' or \
    # 	master_commit_list[3].hexsha!='33267a4e142c8c46e27389b4d32034bcd942be90' or \
	# 	master_commit_list[4].hexsha!='401c7987dd3e5c7eca39b59872d3fc201ff06e88' or \
	# 	master_commit_list[5].hexsha!='64afe69c25367353f46799a7f15e99667e4a0742' or \
	# 	master_commit_list[6].hexsha!='03adf90521b4365fed0c2e2b344abc751e7918e6' 
  	# ):
	# 	overall['data'][0]["score"] = 0
	# 	overall['data'][0]["status"] = 'failure'
	# 	overall['data'][0]["message"] = "The master branch seems to have been modified in some way. Run the reset.sh script and try again."
	# 	print(json.dumps(overall, indent=4))
	# 	with open('../evaluate.json', 'w') as f:
	# 		json.dump(overall,f,indent=4)
	# 	os.system("rm -rf ./big_repo/")
	# 	exit()

	# temp=0
	# # correct_dfs
	# if('correct_dfs' not in branch_objects):
	# 	msg+='"correct_dfs" branch does not exist. '
	# else:
	# 	commit_list = list(repo.iter_commits('correct_dfs'))
	# 	temp+=1
	# 	if(len(commit_list)<2 or ( (commit_list[1].hexsha!='33267a4e142c8c46e27389b4d32034bcd942be90' or commit_list[0].hexsha in hashes) and commit_list[0].hexsha!='33267a4e142c8c46e27389b4d32034bcd942be90')):
	# 		msg+='"correct_dfs" branch not branched out at the right commit from master. Try git branch and git log for further information. '
	# 	else:
	# 		temp+=2
	# 	if(len(commit_list[0].tree.blobs)!=1 or len(commit_list[0].tree.trees)!=0 or commit_list[0].tree.blobs[0].name != 'dfs.cpp' or commit_list[0].message.strip("\n").strip(" ").lower()!='saved dfs.cpp'):
	# 		msg+=' "correct_dfs" branch HEAD does not have the correct directory structure or commit message. Try git checkout to see the directory. '
	# 	else:
	# 		temp+=2

	# 	if(temp==5):
	# 		msg+=' "correct_dfs" branch done perfectly!'
	# branchResult+=temp
	# temp=0
	# # correct_bfs
 
	# if('correct_bfs' not in branch_objects):
	# 	msg+='"correct_bfs" branch does not exist. '
	# else:
	# 	commit_list = list(repo.iter_commits('correct_bfs'))
	# 	temp+=1
	# 	if(len(commit_list)<2 or ( (commit_list[1].hexsha!='47d3221c8b17d00745b2f8c02240eb33ff8bf19b' or commit_list[0].hexsha in hashes) and commit_list[0].hexsha!='47d3221c8b17d00745b2f8c02240eb33ff8bf19b')):
	# 		msg+=' "correct_bfs" branch not branched out at the right commit from master commit. Try git branch and git log for further information. '
	# 	else:
	# 		temp+=2
	# 	if(len(commit_list[0].tree.blobs)!=1 or len(commit_list[0].tree.trees)!=0 or commit_list[0].tree.blobs[0].name != 'bfs.cpp' or commit_list[0].message.strip("\n").strip(" ").lower()!='saved bfs.cpp'):
	# 		msg+=' "correct_bfs" branch HEAD does not have the correct directory structure or commit message. Try git checkout to see the directory. '
	# 	else:
	# 		temp+=2
   
	# 	if(temp==5):
	# 		msg+=' "correct_bfs" branch done perfectly!'
	# branchResult+=temp
	# temp=0
	
	# # correct_binary_search
 
	# if('correct_binary_search' not in branch_objects):
	# 	msg+='"correct_binary_search" branch does not exist. '
	# else:
	# 	commit_list = list(repo.iter_commits('correct_binary_search'))
	# 	temp+=1
	# 	if(len(commit_list)<2 or ( (commit_list[1].hexsha!='f3b067b5329888ed53b5b78ba94d0572c160ab91' or commit_list[0].hexsha in hashes) and commit_list[0].hexsha!='f3b067b5329888ed53b5b78ba94d0572c160ab91')):
	# 		msg+=' "correct_binary_search" branch not branched out at the right commit from master. Try git branch and git log for further information. '
	# 	else:
	# 		temp+=2
	# 	if(len(commit_list[0].tree.blobs)!=1 or len(commit_list[0].tree.trees)!=0 or commit_list[0].tree.blobs[0].name != 'binary_search.cpp' or commit_list[0].message.strip("\n").strip(" ").lower()!='saved binary_search.cpp'):
	# 		msg+=' "correct_binary_search" branch HEAD does not have the correct directory structure or commit message. Try git checkout to see the directory. '
	# 	else:
	# 		temp+=2
   
	# 	if(temp==5):
	# 		msg+=' "correct_binary_search" branch done perfectly!'
	# branchResult+=temp
	# temp=0

	# # correct_matrixmul
 
	# if('correct_matrixmul' not in branch_objects):
	# 	msg+='"correct_matrixmul" branch does not exist. '
	# else:
	# 	commit_list = list(repo.iter_commits('correct_matrixmul'))
	# 	temp+=1
	# 	if(len(commit_list)<2 or ( (commit_list[1].hexsha!='f3b067b5329888ed53b5b78ba94d0572c160ab91' or commit_list[0].hexsha in hashes) and commit_list[0].hexsha!='f3b067b5329888ed53b5b78ba94d0572c160ab91')):
	# 		msg+=' "correct_matrixmul" branch not branched out at the right commit from master. Try git branch and git log for further information. '
	# 	else:
	# 		temp+=2
	# 	if(len(commit_list[0].tree.blobs)!=1 or len(commit_list[0].tree.trees)!=0 or commit_list[0].tree.blobs[0].name != 'matrixmul.cpp' or commit_list[0].message.strip("\n").strip(" ").lower()!='saved matrixmul.cpp'):
	# 		msg+=' "correct_matrixmul" branch HEAD does not have the correct directory structure or commit message. Try git checkout to see the directory. '
	# 	else:
	# 		temp+=2
   
	# 	if(temp==5):
	# 		msg+=' "correct_matrixmul" branch done perfectly!'
	# branchResult+=temp
	# temp=0

	# # correct_sieve
 
	# if('correct_sieve' not in branch_objects):
	# 	msg+=' "correct_sieve " branch does not exist. '
	# else:
	# 	commit_list = list(repo.iter_commits('correct_sieve'))
	# 	temp+=1
	# 	if(len(commit_list)<2 or ( (commit_list[1].hexsha!='a47c2e6ff4e89f8384ca4263bda017a28403d1b5' or commit_list[0].hexsha in hashes) and commit_list[0].hexsha!='a47c2e6ff4e89f8384ca4263bda017a28403d1b5')):
	# 		msg+=' "correct_sieve" branch not branched out at the right commit from master. Try git branch and git log for further information. '
	# 	else:
	# 		temp+=2
	# 	if(len(commit_list[0].tree.blobs)!=1 or len(commit_list[0].tree.trees)!=0 or commit_list[0].tree.blobs[0].name != 'sieve.cpp' or commit_list[0].message.strip("\n").strip(" ").lower()!='saved sieve.cpp'):
	# 		msg+=' "correct_sieve" branch HEAD does not have the correct directory structure or commit message. Try git checkout to see the directory. '
	# 	else:
	# 		temp+=2
   
	# 	if(temp==5):
	# 		msg+=' "correct_sieve" branch done perfectly!'
	# branchResult+=temp
	# temp=0


	# print("Hello!")

	# if(len(commits)!=3):
	# 	print(len(commits))
	# 	overall['data'][0]["score"] = branchResult+commitResult
	# 	overall['data'][0]["message"] = "There should be exactly 3 commits in the repository. Try git log to see the commits."
	# 	overall['data'][0]["status"] = "failure"
	# 	print(json.dumps(overall, indent=4))  
	# 	with open('../evaluate.json', 'w') as f:
	# 		json.dump(overall,f,indent=4)
	# 	os.system("rm -rf ./big_repo/")    
	# # 	exit()
	# overall['data'][0]["score"] = branchResult
	# overall['data'][0]["message"] = msg
	# print(json.dumps(overall, indent=4))
	# with open('../evaluate.json', 'w') as f:
	# 	json.dump(overall,f,indent=4)

except Exception as e:
	print(str(e))
	pass

os.system("rm -rf ./repo/")

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

