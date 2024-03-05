# Lab-2 Activities

## Activity 1

You have two folders, “input” and “output”. “input” has files and subfolders, while “output” is an empty directory.

Goal: Writing a Unix command line, which on executing will:-

Copy ONLY the files from “input” to “output”.
Any subfolder (empty or non-empty) in “input” should not be copied.
Files that might be present in any subfolder (or sub-subfolder or sub-sub-subfolder and so on) of “input” should ALSO be copied to “output”.


Example:- If the “input” folder directory structure is =>



input

├── .hidden

├── report.pdf

├── subfolder1

│- - - -├── file1.txt

│- - - -├── file2.txt

│- - - -├── file3.pdf

│- - - -└── sub-subfolder

│- - - - - - - └── test.sql

├── subfolder2

│- - - -├── file4.txt

│- - - -├── file5.txt

│- - - -└── file6.docx

├── test.cpp

└── test.zip



After executing your command line, the “output/” folder directory structure should look like =>



output

├── file1.txt

├── file2.txt

├── file3.pdf

├── file4.txt

├── file5.txt

├── file6.docx

├── .hidden

├── report.pdf

├── test.cpp

├── test.sql

└── test.zip



The command line that you will write in submission.sh will be of the form "cp $(_____) output/". Fill in the red space with an appropriate command.



Note:-

All filenames will be DISTINCT. There may be hidden files (their names begin with “.”); copy those, too.
Before running your command line ANYTIME, execute the “reset.sh” file by writing this command in the terminal at /home/labDirectory:- “./reset.sh”. This reset.sh will delete the old contents of output/ directory and provide you with a fresh empty "output/" directory to work on.
DO NOT touch/modify the “reset.sh” file.
Write your command line in “submission.sh”.
If you mess up the directory, you can restore it by clicking on More > Force Delete Activity. Remember to save the progress before doing this.


To execute your script, run the following in the Docker terminal:-

“./submission.sh”

Hint: Use the find command for the fill-in-the-blank.

## Solution
```bash
find ./input -type f -exec cp {} ./output \;
```
[OR]
```bash
cp $(find ./input/ -type f) output/
```

## Activity 2

A list of students is given with their first names, roll numbers, and a comment saying “PASSED” or “FAILED” for each student.

Goal →

Write a Unix command line to print the names and roll numbers of those students who have passed ONLY, from the result.csv present in the same directory as submission.sh.

The list of students will be given in “result.csv”. There will only be three columns:- the first being the student’s first name, the second as their roll number, and the last telling “PASSED” or “FAILED”, all separated by commas “,”.

Example:- If the “result.csv” looks like =>

Kavya,22B1053,PASSED

Saksham,22B1003,PASSED

Ayush,22B0001,FAILED

Guramrit,22B0002,PASSED

After executing your command line, your output should be =>

Kavya,22B1053

Saksham,22B1003

Guramrit,22B0002

Apart from the result.csv in /home/labDirectory/, there are 3 more such result.csv present in testcases/ folder. When you click the “Evaluate” button, the autograder will check the correctness of your command line (in submission.sh) against the 3 result.csv in testcases/ folder.

Note:-

You can print the entries in any order. But no entry should be missing, and extra entries should not be there.
All the roll numbers given in “result.csv” will be distinct.
All the test cases will have only 3 columns:- first name, roll number, and PASSED or FAILED, separated by commas.
In case you tamper with the testcases/ folder, still the autograder will check the correctness from the original version of the testcases/ provided to you.
Write your command line in “submission.sh”.
If you mess up the directory, you can restore it by clicking on More > Force Delete Activity. Remember to save the progress before doing this.


To execute your script, run the following in the Docker terminal:-

./submission.sh



Hint: Use the grep (as the name of title suggests :-) and cut commands.

## Solution

```bash
grep -E "PASSED$" result.csv | cut -d ',' -f 1,2
```

## Activity 3

You have a file named “collect.txt” with the following contents:



sakshamrathi21 1 22b1003@iitb.ac.in submission.sh

malaikaarora01 3 22b0069@iitb.ac.in submsubission.sh

guramritsingh07 2 22b0001@iitb.ac.in submission.sh

rahulgandhi04 5 22b0010@iitb.ac.in subpappu.sh

nithinkamath10 2 zerodha@iitb.ac.in trade.sh

narendramodi24 4 22b0024@iitb.ac.in submission.sh 

kavyagupta11 1 22b1053@iitb.ac.in submission.sh



(i) Every line has the following format: “username<space>number<space>email-id<space>file submitted.

(ii) You need to select the valid lines and print them back into output.txt. The following points will be used to judge whether a line is valid or not.

(iii) Every username contains some characters (of arbitrary length > 0, lowercase letters) in the start and then a two digit number at the end (00 to 99).

(iv) The next number should be between 1 and 4.

(v) The email address should be of the form <22b><four digit number><@iitb.ac.in>.

(vi) The name of the file submitted should be submission.sh. And the line should end after submission.sh.

(vii) You need to write your unix command (maybe, sequence of commands) in submission.sh.

(viii) Print the valid lines onto the terminal.

(viii) If you mess up the directory, you can restore it by clicking on More > Force Delete Activity. Remember to save the progress before doing this.



So, after executing your unix command, output will be:



sakshamrathi21 1 22b1003@iitb.ac.in submission.sh

guramritsingh07 2 22b0001@iitb.ac.in submission.sh

narendramodi24 4 22b0024@iitb.ac.in submission.sh 

kavyagupta11 1 22b1053@iitb.ac.in submission.sh



(2nd line - submitted file name not valid; 3rd line - integer not valid; 4th line - email id not valid)

Hint: Use regex to capture the proper fields and then use grep based on this.

## Solution

```bash
grep -E "^[a-z]+[0-9][0-9][[:space:]]*[1-4][[:space:]]*22b[0-9][0-9][0-9][0-9]\@iitb\.ac\.in[[:space:]]*submission.sh$" collect.txt
```

## Activity 4

Suppose you have a file “data.txt” with following contents: (X:Y:Z form lines, where X is username, Y is some integer, Z is their place)



sakrat:74:jodhpur

kavgup:95:lucknow

gursin:100:chandigarh

maykum:69:haryana

ridsar:88:jodhpur



You need to use UNIX commands to:

(i) Sort the lines based on the second column (numeric sorting) and in reverse order. Redirect the output to sort.txt. (Redirection can be done through “>”)

(ii) Extract the lines where the third column is “jodhpur”. (Perform this on sort.txt and redirect the result to extract.txt)

(iii) Take only the first two columns and print them to display.txt. These columns should be separated by tab instead of colon. (This command has to be performed on extract.txt.)

(iv) Combine these three files and tar them. The final file name will be “submission.tar.gz”.



Lots of stuff to do?? Let’s understand through the above example. In the above case, sort.txt will be:



gursin:100:chandigarh

kavgup:95:lucknow

ridsar:88:jodhpur

sakrat:74:jodhpur

maykum:69:haryana



extract.txt will be:



ridsar:88:jodhpur

sakrat:74:jodhpur



display.txt will be:



ridsar 88

sakrat 74

(display.txt contains the first two columns separated by tab.)

If you mess up the directory, you can restore it by clicking on More > Force Delete Activity. Remember to save the progress before doing this.

## Solution

```bash
sort -t ':' -k 2nr data.txt > sort.txt;
grep -Ei '^[^:]:[^:]:jodhpur' sort.txt > extract.txt;
cut -d ':' -f 1,2 --output-delimiter $'\t' extract.txt > display.txt;
tar -cvzf submission.tar.gz sort.txt extract.txt display.txt;
```

## Activity 5

You are given a zip file named “input.zip”. You must write Unix command lines in your Docker terminal to achieve the following goals.



Goals:-

1) Unzip input.zip to get input/ folder using the “unzip” command.

2) All the files given in the unzipped input/ folder have “read, write and execute” permission to ALL users. You must change the permissions to “read, write and execute” permission to the user who created the files ("user (u)") and "read and execute" only to any other user ("group (g)" and "others (o)"). This will be done for ALL the contents (files or subfolders) in the input/ directory using the “chmod” command.

3) Zip the modified unzipped directory and name it “output.zip”, using the “zip” command.



Note:-

Unlike other questions, you don’t have to write your commands in any file named “submission.sh”. You will run your commands in your terminal and prepare “output.zip”. The autograder will check this zip file for the correctness of your commands.
This directory will contain a LOT of files, so manually changing the permission to every file separately will not help. Use appropriate “flags” to complete the job for every file together.
If you mess up the directory, you can restore it by clicking on More > Force Delete Activity. Remember to save the progress before doing this.

## Solution

zip -r output.zip input

## Bonus

Please try this activity after you have completed all others.

There is a directory named inputs, which itself contains some sub-directories. Those directories contain some files. In this problem, your goal is to list the total number of lines in all the text files (*.txt). Provide a unix command (or a sequence of commands) to accomplish this task. Write this command in the submission.sh file. Remember, you need to exclude all the empty lines within the .txt file. Also, consider only .txt files. All other files have to be ignored.



Example: Suppose the input directory structure is as follows:

input

|-- project1/

| |-- file1.txt

| |-- file2.txt

    |-- file3.pdf

|-- project2/

| |-- file4.txt

| |-- file5.txt

    |-- file6.docx

|-- project3/

    |-- file7.txt

    |-- file8.txt 

 

Also, the number of non-empty lines in these files are:

file1.txt - 5, file2.txt - 7, file3.pdf - 4, file4.txt - 3, file5.txt - 6, file6.docx - 7, file7.txt - 2 and file8.txt - 0

So, you need to print the result in output.txt. In this case the output.txt file will contain a single integer = 5 + 7 + 3 + 6 + 2 = 23 (Exclude files having extensions other than .txt) If you mess up the directory, you can restore it by running ./reset.sh on terminal. (Do not modify the reset.sh file.)



Useful Links:

See exec command from : https://eng.libretexts.org/Bookshelves/Computer_Science/Operating_Systems/Linux_-_The_Penguin_Marches_On_(McClanahan)/13%3A_Working_with_Bash_Scripts/3.09%3A_Positional_Parameters_exec_Command_source_Command



Other commands to be used can be found here:

http://hirophysics.com/Electronics/linux/linux04.html#:~:text=This%20counts%20the%20number%20of,a%20file%20or%20multiple%20files.&text=The%20option%20ignores%20the%20case%20for%20the%20specified%20string.&text=The%20option%20searches%20a%20specific,and%20all%20of%20the%20subdirectories.



Also have a look at the links provided in slides



﻿If you mess up the directory, you can restore it by clicking on More > Force Delete Activity. Remember to save the progress before doing this.

## Solution

```bash
cat $(find ./input/ -name "*.txt") | grep -cE "^.+$"
```