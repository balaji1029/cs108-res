input_string=input()
permutation=input().split(" ")
permutation=[int(x) for x in permutation]
flag=True #flag to check if permutation is valid or not
if len(permutation)!=len(input_string):
    flag=False
if len(set(permutation))!=len(permutation): #Duplicate elements
    flag=False
for i in permutation:
    if not(0<=i and i<len(permutation)):
        flag=False
        break
if flag==False:
    print("INVALID INPUT")
else:
    string_list=[input_string[i] for i in permutation]
    print("".join(string_list))