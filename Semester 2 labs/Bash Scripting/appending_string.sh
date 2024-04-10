: '
Write a Bash program to append a string (given as a command line argument) to all files in the same directory as the Bash Script having the extension .out.



Usage :- bash submission.sh <string>



Example :- Command :- “bash submission.sh Hello World 123 @”



On executing this command, the string “Hello World 123 @” will be appended to every file in the directory having the extension .out. All other files should remain untouched.



Example :- If there is a file in the directory “a.out” containing data “Hello CS104 Students!” then after executing the script the data contained in “a.out” would become “Hello CS104 Students!Hello World 123 @”



Though only one file (a.out) has been supplied to the GUI, feel free to create more files for testing using the “touch” command from the terminal and populate them with data by piping the output of the “echo” command. The contents can be viewed using the “cat” command.
'

for file in $(find . -regex ./[^/]+.out -type f)
do
    echo -ne "$*\n" >> $file;
done
