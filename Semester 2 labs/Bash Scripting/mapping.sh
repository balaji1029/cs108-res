: '
Write a Bash Program to rename all pdf files in the current directory in the form of {rollno}.pdf to {rollno}_{name}.pdf. The mapping between roll numbers and names is provided in a file, the address of which is provided as a command line argument. Assume all names are a single word.



Mapping File Format:- 



<rollno> <name>



Example :- 



200050049 Harsh

200050100 Parth

200050129 Sarthak

... (continued)



Usage :- “bash submission.sh <path_to_mapping_file>”



Example :- If we use the above mapping file, the file 200050100.pdf should be renamed to 200050100_Parth.pdf.



If for some file, the mapping does not exist, that file should remain untouched.



The directory has an editable mapping file, along with the submission.sh file. Feel free to create more files for testing using “touch”, and see the change in their names on running the script by using the “ls” command.



For reading from a file, you can use the following piece of code :- 



while read -r line

do

arr=($line)

done < a.txt



This piece of code reads from the file “a.txt” line by line. The line is broken up into tokens using spaces as a separator and stored as an array in “arr”. Now, the words can be indexed as in a normal array.
'
#!/bin/bash

if [[ $# == 1 ]]; then
    declare -A roll_map;
    while read -r line
    do
        arr=($line);
        if [[ ${#arr[@]} -ge 2 ]]; then
            roll_map["${arr[0]}"]="${arr[1]}";
        fi
    done < "$1"
    for key in "${!roll_map[@]}"
    do

    echo "Key: $key Value: ${roll_map[$key]}"

    done


    for file in $(ls *.pdf)
    do
        mv "$file" "${file:0: -4}_${roll_map[${file:0: -4}]}.pdf";
    done
fi
