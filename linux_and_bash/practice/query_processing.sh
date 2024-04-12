#!/usr/bin/bash

num=$1

shift

array=$@

for array_num in $array; do
    # echo $array_num
    if [[ $array_num -eq $num ]]; then
        echo "YES"
        exit 0
    fi
done

echo "NO"