#!/usr/bin/bash

catalan() {
    if [[ $1 -eq 0 ]]; then
        echo 1
        exit 0
    fi
    if [[ $1 -eq 1 ]]; then
        echo 1
        exit 0
    fi
    local sum=0
    local num=$1
    # echo $1
    for ((i=0; i<$num; i++)); do
        local j=$((num - i - 1))
        # echo $i $j
        (( sum += $(catalan $i)*$(catalan $j) ))
    done
    echo $sum
}

echo $(catalan $1)