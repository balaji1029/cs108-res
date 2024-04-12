f=open("buggy_marksheet.txt", "r")
marks_dictionary={}

def section(roll_no):
    return int(roll_no.split("_")[2])

for line in f.readlines():
    roll_no=line.split(" ")[0]
    marks=line.split(" ")[1]
    if marks[len(marks)-1]=='\n':
        marks=marks[:len(marks)-1]
    marks_dictionary[roll_no]=marks
f.close()

#Now sorting the dictionary using the sorted() function. You may need to see its syntax on net.
#This is complex step so see carefully.
sorted_marksheet=list(sorted(marks_dictionary.items(), key=lambda x: (section(x[0]), -int(x[1]))))
#print(sorted_marksheet)

f=open("fixed_marksheet.txt", "w")
for entry in sorted_marksheet:
    line=entry[0]+" "+entry[1]+"\n"
    f.write(line)
f.close()