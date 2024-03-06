Purpose of this part is update some filenames based on a mapping.

Say the mapping file has an entry "22B1053 Kavya", then you have to search for a pdf (in same directory as submission.sh) named "22B1053.pdf" and IF it exists, then RENAME it as "22B1053_Kavya.pdf"

Note : The name of that mapping file will not be necessarily "mapping.txt", it is passed as a command line argument (the very first command line argument)

Side Note : Given mapping entry file may not exist in the directory. Also there may be files (non pdf files or those pdf files whose entry is not present in the mapping file), so DON'T disturb those files.

To see your correctness of program, goto 250/evaluationScripts/ directory (using cd command) and run "./evaluate.sh", all the comments and evaluation will come on the 
terminal or in "evaluate.json".

If there is a permission denied problem, do "chmod +x evaluate.sh" first.

In case of any problem with autograder, please contact me.