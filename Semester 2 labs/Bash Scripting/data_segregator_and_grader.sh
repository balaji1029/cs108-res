#!/usr/bin/bash

echo "" > ug23.csv
: '
# Data Segregator and Grader

---------------------------------------------------------------------------

Task:

- You have been given a csv file called "grades.csv" which consists of "," separated columns "rollno,quiz1,quiz2,midsem,endsem,total-marks". The column names should be self-explanatory for this csv file.

- The first line of the csv file contains header in the sequence described above, and from line 2 onwards the csv file contains actual data within their respective column.

- The csv file contains all the students from btech batch 2023 (roll no starting from 23B001 to 23B999) and 2024 (roll no starting from 24B001 to 24B999) in an unordered manner.

- Your task is to create a bash script in "submission.sh" file where below conditions are fulfilled:

   1. Segregate the data based on if a row contains student of batch 2023 or 2024. All the data of batch 2023 should be written in a separate file called "ug23.csv", and the same way all the data of batch 2024 should be written in a separate file called "ug24.csv"

   2. You also have to add a new "grades" column in these data with following matrix:

       | marks | grades |

       | >85 | AA |

       | >65 and <=85 | AB |

       | >45 and <= 65 | BB |

       | >35 and <= 45 | CC |

       | <=35 | F |

   3. The final csv file must be sorted by grades column(from AA to F) and if 2 students have same grades than then are sorted in non-descending order of the roll no.

- The filename must be taken via command-line argument. Ideally the execution of bash script must be done via:

   - "bash submission.sh grades.csv"

- **NOTE**: You can assume that the total-marks add up using quiz1,quiz2,midsem,and endsem marks. You can also assume that total-marks in range [0,100].

- **EXTRA**: You are also given you some extra testcases in /home/labDirectory/testcases folder for you to refer.



---------------------------------------------------------------------------

Example:



grades.csv



rollno,quiz1,quiz2,midsem,endsem,total-marks

23B001,10,8,25,45,88

23B010,9,8,25,40,82

23B009,5,0,25,45,75

23B002,10,5,25,5,45

24B001,10,8,25,45,88

24B010,3,2,10,5,20

24B009,5,10,25,45,85

24B002,10,5,25,25,65



-----------------------------------------------



ug23.csv



rollno,name,quiz1,quiz2,midsem,endsem,total-marks,grades

23B001,10,8,25,45,88,AA

23B009,5,0,25,45,75,AB

23B010,9,8,25,40,82,AB

23B002,10,5,25,5,45,CC





ug24.csv



rollno,quiz1,quiz2,midsem,endsem,total-marks,grades

24B001,10,8,25,45,88,AA

24B009,5,10,25,45,85,AB

24B002,10,5,25,25,65,BB

24B010,3,2,10,5,20,F




'
echo "" > ug24.csv

pattern='^23B';
index=0;
IFS=',';
while read -r line; do
    if [[ $index == 0 ]]; then
        index=1;
    else
    arr=($line);
    grade="";
    if [[ ${#arr[@]} -gt 0 ]]; then
    var6=$(echo ${arr[5]} | tr -d '\r');
    if [[ $var6 -gt 85 ]]; then
        arr+=("AA");
    elif [[ $var6 -gt 65 ]]; then
        arr+=("AB");
    elif [[ $var6 -gt 45 ]]; then
        arr+=("BB");
    elif [[ $var6 -gt 35 ]]; then
        arr+=("CC");
    else
        arr+=("F");
    fi
    if [[ ${arr[0]} =~ $pattern ]]; then
        file="ug23.csv";
    else
        file="ug24.csv"
    fi
    starting_here=1
    for val in ${arr[@]};
    	do
        if [[ starting_here -eq 1 ]]; then
        	starting_here=0
        else
        	echo -n "," >> $file;
    	fi
        echo -n $(echo $val | tr -d '\r') >> $file
    	done
    echo -ne "\n" >> $file;
    fi
    fi
done < "$1"

echo -e "$(head -1 $1 | tr -d '\r'),grades$(sort -t "," -k7,7 -k1,1 ug23.csv)" > ug23.csv
echo -e "$(head -1 $1 | tr -d '\r'),grades$(sort -t "," -k7,7 -k1,1 ug24.csv)" > ug24.csv
