#!/bin/bash

# rm log.txt
co=0

for file in $1/*.py
do
    
    rm $file
    a=$(basename $file)
    echo "Deleted" $a >> log.txt
    co=$((co+1))
done

echo $co