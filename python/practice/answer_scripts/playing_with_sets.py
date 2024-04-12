f=open("q2-input.txt", "r")

#Defining an empty set at first, will take unions and update with the entries
#Use "update()" and not "union()" as union() doesn't change value of this variable set
#Careful using the split() command, it takes the '\n' next line character when it reads from file
union_of_sets=set()
for line in f.readlines():
    if line[len(line)-1]=='\n':
        union_of_sets.update(set(line[:len(line)-1].split(",")))
    else:
        union_of_sets.update(set(line.split(",")))
print(len(union_of_sets))

f.close()