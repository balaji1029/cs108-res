#!/usr/bin/bash

declare -a array
j=0
for i in "$@"; do
    array[$j]=$i
    ((j++))
done
last_ind=$(($#-1))
count=0
while [[ $last_ind -gt 0 ]]
do
    for ((i=0; i<last_ind; i++)); do
        j=$(($i+1))
        if [[ ${array[$i]} -gt ${array[$j]} ]]; then
            temp=${array[$i]}
            array[$i]=${array[$j]}
            array[$j]=$temp
            last_index=$i
            ((count+=1))
        fi
    done
    if [[ $last_ind -eq $last_index ]]; then
        break
    fi
    last_ind=$last_index
done
echo ${array[@]}
echo "$count"