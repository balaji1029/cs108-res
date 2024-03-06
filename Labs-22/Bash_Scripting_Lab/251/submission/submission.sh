#!/bin/bash
while read -r line|| [[ -n "$line" ]]
do
arr=($line)
if [ -e "${arr[0]}.pdf" ]
then
mv "${arr[0]}.pdf" "${arr[0]}_${arr[1]}.pdf"
fi
done < $1
