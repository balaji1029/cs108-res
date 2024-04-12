#!/usr/bin/bash

declare -A words
while read -r line; do
    for word in $line; do
        if [[ ${words[$word]} -eq "" ]]; then
            words[$word]=1
        else
            (( words[$word]+=1 ))
        fi
    done
done < input.txt


for word in ${!words[@]}; do
    echo "$word: ${words[$word]}"
done