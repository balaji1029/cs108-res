'''
************Custom Character Counter*************

Write a python program that counts characters in a given file and print the stats in a log file.



************Problem Statement*************



Write a python program that takes filename as command line argument. If the filename is not given as command line argument the program should print exactly,



"""

Filename not provided.

Usage: python3 customCounter.py <file>

"""(without quotations)



The program should count occurrences of all the alphanumeric characters (i.e. A-Z, a-z, and 0-9) that are present in the file including common special characters belonging to [ `~!@#$%^&*()_+-=[]{}\|;'".>,</?]. Also the "A" and "a" are different characters, meaning the counting should be case sensitive. Once counting is done the program should output the stats (i.e. character and its count) in ":" separated form on standard output.



Testrun Command: python3 customCounter.py file1.txt >> output.log



************Example*************

Assume file1.txt has following text:

"""

I am Saksham Rathi. e-mail:sakshamrathi21@gmail.com

"""(without quotations)



Then the output should contain:



"""

I:1

 :4

a:9

m:6

S:1

k:2

s:3

h:4

R:1

t:2

i:4

.:2

e:1

-:1

l:2

r:1

2:1

1:1

@:1

g:1

c:1

o:1

"""(without quotations)



Please note that "A" and "a" have 2 different entries, also " "(space) as a character is also part of the output. Please also note that any other characters other than given in the problem statement will not be part of the testcases too (even newline characters will not be in testcases).





For command line argument handling, you will be required to use sys library. (It is already imported for you)

You can check these links to learn more about this library:

https://docs.python.org/3/library/sys.html
https://www.geeksforgeeks.org/python-sys-module/

'''
import sys
import string


n = len(sys.argv)
if n != 2:
    print("Filename not provided.")
    print("Usage: python3 customCounter.py <file>")
else:
    characters = {char: 0 for char in list(string.ascii_lowercase) + list(string.ascii_uppercase) + list(string.digits) + list(" `~!@#$%^&*()_+-=[]		{}\|;'\".>,</?")}
    # characters = string.lowercase + string.uppercase + string.digits
    # print(characters.keys())
    try:
        with open(sys.argv[1], 'r') as f:
                for line in f:
                    for char in line:
                        if char in characters:
                            characters[char] += 1

        for char, count in characters.items():
            if count != 0:
                print(f"{char}: {count}")
    except FileNotFoundError as error:
        print("Filename not provided.")
        print("Usage: python3 customCounter.py <file>")
