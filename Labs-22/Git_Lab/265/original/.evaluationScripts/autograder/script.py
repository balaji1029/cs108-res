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

my_tar = tarfile.open('working_directory.tar.gz')
my_tar.extractall("/home/labDirectory/") # specify which folder to extract to
my_tar.close()
os.system('clear')
try:
	repo = git.Repo("/home/labDirectory/working_directory/")
except:
	try:
		repo = git.Repo("./temp/submission/project/")
	except:
		overall['data'][0]["score"] = 0
		overall['data'][0]["message"] = "Could Not Find project folder"
		overall['data'][0]["status"] = "failure"
		print(json.dumps(overall, indent=4))

		with open('../evaluate.json', 'w') as f:
			json.dump(overall,f,indent=4)
		os.system("rm -rf ./working_directory/")      
		exit()

branchResult = 0
commitResult = 0

# Task that must be present in the assignment 

os.system("git config --global --add safe.directory '*'")

try:    
	# Checking for branches
	heads = repo.heads 
	for head in heads:
		if(head.name=='master'):
			branchResult+=1

	if(branchResult==0):
		overall['data'][0]["score"] = branchResult+commitResult
		overall['data'][0]["message"] = "The \"master\" branch does not seem to exist here. Try git branch to see results."
		overall['data'][0]["status"] = "failure"
		print(json.dumps(overall, indent=4))

		with open('../evaluate.json', 'w') as f:
			json.dump(overall,f,indent=4)
		os.system("rm -rf ./working_directory/")    
		exit()

	if(len(heads)==1):
		branchResult+=1
	else:
		overall['data'][0]["score"] = branchResult+commitResult
		overall['data'][0]["message"] = "There seems to be more than one branch existing here. Try git branch to see results."
		overall['data'][0]["status"] = "failure"
		print(json.dumps(overall, indent=4))

		with open('../evaluate.json', 'w') as f:
			json.dump(overall,f,indent=4)
		os.system("rm -rf ./working_directory/")    
		exit()

	# print("Reached")
	# Checking for commits
	commits = list(repo.iter_commits("master"))

	if(len(commits)!=3):
		print(len(commits))
		overall['data'][0]["score"] = branchResult+commitResult
		overall['data'][0]["message"] = "There should be exactly 3 commits in the repository. Try git log to see the commits."
		overall['data'][0]["status"] = "failure"
		print(json.dumps(overall, indent=4))  
		with open('../evaluate.json', 'w') as f:
			json.dump(overall,f,indent=4)
		os.system("rm -rf ./working_directory/")    
		exit()

	if(commits[2].message.strip("\n").strip(" ").lower() == "added readme.txt") :
		commitResult = commitResult + 1
	if(commits[1].message.strip("\n").strip(" ").lower() == "added add.h") :
		commitResult = commitResult + 1
	if(commits[0].message.strip("\n").strip(" ").lower() == "added main.cpp") :
		commitResult = commitResult + 1
	
	# print(commits[2].message.strip("\n").strip(" ").lower())
	# print(commits[1].message.strip("\n").strip(" ").lower())
	# print(commits[0].message.strip("\n").strip(" ").lower())
	msg = ""

	for i in range(3):
		tree=commits[i].tree
		# print("try")
		if len(tree.trees)>0:
			# print("this")
			msg += "There seems to be some subdirectory in commit "+str(3-i)+". Use checkout command to see the commit."
		else: 
			# print(i)
			if(i==2):
				if(len(tree.blobs)!=1 or tree.blobs[0].name!='README.txt'):
					msg += "The files don't seem to be correct in commit "+str(3-i)+". Use checkout command to see the commit."
				else:
					msg += "Commit "+str(3-i)+" is as expected."
					commitResult+=2
			elif(i==1):
				
				file_list = [entry.name for entry in tree]
				if(len(tree.blobs)!=2 or ('README.txt' not in file_list) or ('add.h' not in file_list)):
					msg += "The files don't seem to be correct in commit "+str(3-i)+". Use checkout command to see the commit."
				else:
					msg += "Commit "+str(3-i)+" is as expected."
					commitResult+=2

			else:
				file_list = [entry.name for entry in tree]
				# print(file_list)
				if(len(tree.blobs)!=3 or ('README.txt' not in file_list) or ('add.h' not in file_list) or ('main.cpp' not in file_list)):
					msg += "The files don't seem to be correct in commit "+str(3-i)+". Use checkout command to see the commit."
				else:
					msg += "Commit "+str(3-i)+" is as expected."
					commitResult+=2

	overall['data'][0]["score"] = branchResult+commitResult
	overall['data'][0]["message"] = msg
	print(json.dumps(overall, indent=4))
	with open('../evaluate.json', 'w') as f:
		json.dump(overall,f,indent=4)
except :
	pass

os.system("rm -rf /home/labDirectory/working_directory/")

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

