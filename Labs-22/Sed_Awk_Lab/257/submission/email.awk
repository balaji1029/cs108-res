#!/bin/awk

BEGIN {FS=","} 

NR==1 {print("Student ID,First Name,Middle Name,Last Name,Email-ID")}
NR!=1 {print $0 "," $2 $4 "@surveycorps.com"}


