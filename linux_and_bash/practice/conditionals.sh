#!/bin/bash

# Author: Guramrit Singh
# Date: 2024/02/19
# Description: This script demonstrates the use of conditional statements in bash

<< COMMENT
if [ condition ]
then
    command1
    command2
    ...
fi
COMMENT

<< COMMENT
if [ condition ]
then
    command1
    command2
    ...
else
    command3
    command4
    ...
fi
COMMENT

<< COMMENT
if [ condition ]
then
    command1
    command2
    ...
elif [ condition ]
then
    command3
    command4
    ...
else
    command5
    command6
    ...
fi
COMMENT

# x="1"
x=1

# Example 1 - If condition is true
if [ 1 -eq 1 ]
then
    echo "Test $x: 1 is equal to 1"
fi

let x++

# Example 2 - If condition is false
if [ 1 -eq 2 ]
then
    echo "Test $x: 1 is equal to 2"
else
    echo "Test $x: 1 is not equal to 2"
fi

let "x++"

# Example 3 - If-elif-else
if [ 1 -lt 2 ]
then
    echo "Test $x: 1 is less than 2"
elif [ 1 -gt 2 ]
then
    echo "Test $x: 1 is greater than 2"
else
    echo "Test $x: 1 is equal to 2"
fi

let x+=1

# Example 4 - File exists
if [ -e /etc/shells ]
then
    echo "Test $x: /etc/shells exists"
else
    echo "Test $x: /etc/shells does not exist"
fi

let "x+=1"

# Example 5 - File type
if [ -d /etc/shells ]
then
    echo "Test $x: /etc/shells is a directory"
elif [ -f /etc/shells ]
then
    echo "Test $x: /etc/shells is a file"
else
    echo "Test $x: /etc/shells is not a directory or file"
fi

x=$(($x+1))

# Example 6 - String is empty
if [ -z "" ]
then
    echo "Test $x: String is empty"
else
    echo "Test $x: String is not empty"
fi

((x=x+1))

# Example 7 - String is not empty
if [ -n "Hello" ]
then
    echo "Test $x: String is not empty"
else
    echo "Test $x: String is empty"
fi

((x+=1))

# Example 8 - String comparison
if [ "Hello" == "Hello" ]
then
    echo "Test $x: Strings are equal"
else
    echo "Test $x: Strings are not equal"
fi

x=$(($x+1))

# Example 9 - String comparison
if [ "Hello" != "World" ]
then
    echo "Test $x: Strings are not equal"
else
    echo "Test $x: Strings are equal"
fi

x=$(($x+1))

# Example 10 - Logical AND 
if [ 2 -le 2 ] && [ 3 -ge 1 ]
then
    echo "Test $x: Both conditions are true"
else
    echo "Test $x: At least one condition is false"
fi

x=$(($x+1))

# Example 11 - Logical AND, OR - single expression
if [[ 2 -lt 2 && 3 -le 1 || 4 -ne 2 ]]
then
    echo "Test $x: Condition is true"
else
    echo "Test $x: Condition is false"
fi

x=$(($x+1))

# Example 12  - Logical AND, OR - multiple expressions
if [ 2 -lt 2 ] && [ 3 -le 1 ] || [ 4 -ne 2 ]
then
    echo "Test $x: Condition is true"
else
    echo "Test $x: Condition is false"
fi

x=$(($x+1))

# Example 13 - Parentheses are used to group conditions
if [ 2 -lt 2 ] && ([ 3 -le 1 ] || [ 4 -ne 2 ])
then
    echo "Test $x: Condition is true"
else
    echo "Test $x: Condition is false"
fi

x=$(($x+1))

# Example 14 - Nested if-else
if [ ! 1 -ne 1 ]
then
    if [ 2 -eq 2 ]
    then
        echo "Test $x: Both conditions are true"
    else
        echo "Test $x: Second condition is false"
    fi
else
    echo "Test $x: First condition is false, no need to check the second condition"
fi
