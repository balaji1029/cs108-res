#!/bin/bash

# Author: Guramrit Singh
# Date: 2024/02/19
# Description: This script demonstrates the use of loops in bash

<< COMMENT
for variable in list
do
    command1
    command2
    ...
done
COMMENT

<< COMMENT
while [ condition ]
do
    command1
    command2
    ...
done
COMMENT

<< COMMENT
until [ condition ]
do
    command1
    command2
    ...
done
COMMENT

x=1

# Example 1 - For loop
for i in 1 2 3 4 5
do
    echo "Test $x: $i in 1 2 3 4 5"
done

let x++
let i=1

# Example 2 - While loop
while [ $i -le 5 ]
do
    echo "Test $x: $i is less than or equal to 5"
    let i++
done

let x++

# Example 3 - Until loop
until [ $i -eq 0 ]
do
    echo "Test $x: $i is not equal to 0"
    let i--
done

let x++

# Example 4 - Nested loops
for i in 1 2 3
do
    for j in 1 2 3
    do
        echo "Test $x: $i $j"
    done
done

let x++

# Example 5 - Break and continue
for i in 1 2 3 4 5 6 7 8 9 10
do
    if [ $i -eq 3 ]
    then
        continue
    fi
    if [ $i -eq 5 ]
    then
        break
    fi
    echo "Test $x: $i"
done

let x++

# Example 6 - For loop with ranges
for i in {1..5}
do
    echo "Test $x: $i in {1..5}"
done

let x++

# Example 7 - For loop with ranges and steps -- not supported in all versions of bash
for i in {1..10..2}
do
    echo "Test $x: $i in {1..10..2}"
done

x=$(($x+1))

# Example 8 - For loop with command substitution
for i in $(ls)
do
    echo "Test $x: $i"
done

x=$(($x+1))

# Example 9 - For loop in C style
for ((i=1; i<=5; i++))
do
    echo "Test $x: $i in C style"
done

x=$(($x+1))
a=(1 2 3 4 5)

# Example 10 - For loop with arrays
for i in ${a[*]}
do
    echo "Test $x: $i in array"
done

x=$(($x+1))

# Example 11 - Array access with index
for ((i=0; i<${#a[@]}; i++))
do
    echo "Test $x: $i in array indices"
done

x=$(($x+1))
str="Hey, how are you?"

# Example 12 - For loop with string without quotes
for i in $str
do
    echo "Test $x: $i in string"
done

x=$(($x+1))
str="Hey, how
are you?"

# Example 13 - For loop with string with quotes
for i in $str
do
    echo "Test $x: $i in string"
done

x=$(($x+1))

# Example 14 - For loop with string with quotes
for i in "$str"
do
    echo "Test $x: $i in string"
done
