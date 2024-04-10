: '
In this activity write getEmails.sh bash file, which satisfies the following conditions:



It should accept a single argument representing a txt file. Otherwise it should show "Usage: ./getEmails.sh <file>". Meaning if "./getEmails.sh <arg1> <arg2>" is used then it should show the error message.


Check if the argument file exists or not. If not, show error message "Input File doesnt exists".


When executed, It should create 3 files = "emails.txt", "sortedEmails.txt", "cseEmails.txt". 


The bash script should extract all the emails of format "<alpha_num>@<alpha>.iitb.ac.in" and store in "emails.txt". Here <alpha_num> consists of alphabets and digits and <alpha> means only alphabets. Assume input txt file have one email address per line, and only email addresses will be present in those lines.


Next it should sort all the emails based on descending order with case-insensitivity and store the results in "sortedEmails.txt". The sorting is based on lexicographical order.


Next it should extract all the cse dept emails from sorted emails and store the results in "cseEmails.txt". The cse dept emails are of format "<alpha_num>@cse.iitb.ac.in".

'
#!/bin/bash

if [[ $# > 1 || $# == 0 ]]; then
    echo "Usage: ./getEmails.sh <file>";
elif ! [[ -f $1 ]]; then
    echo "Input File doesn't exists";
else
    touch emails.txt sortedEmails.txt cseEmails.txt;
    grep -E "^[[:alnum:]]+@[[:alpha:]]+\.iitb\.ac\.in[[:space:]]*$" $1 > emails.txt;
    sort -fr emails.txt > sortedEmails.txt;
    grep -E "^[[:alnum:]]+@cse\.iitb\.ac\.in[[:space:]]*$" sortedEmails.txt > cseEmails.txt;
fi
