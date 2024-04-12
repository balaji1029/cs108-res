#!/bin/bash
#Author: Saksham Rathi
# Function to calculate derangements recursively
derangement() {
    # local restricts the scope of n to this function.
    local n=$1

    # Base cases
    if [ $n -eq 0 ]; then       # See the syntax of if statements carefully. -eq stands for equality comparison
        echo 1                  # D(0) = 1
    elif [ $n -eq 1 ]; then
        echo 0                  # D(1) = 0
    else
        # Recursive formula: D(n) = (n-1) * (D(n-1) + D(n-2))
        local prev1=$(derangement $((n-1)))         # Arithmetic operatiosn are calculated using $(())
        local prev2=$(derangement $((n-2)))         # Function is called recursively two times
        echo $(( (n-1) * (prev1 + prev2) ))         # Final rescursive equation
    fi                                              # End of if-else statements
}

# Input: the value of n; read is for inputs, -p option is for a prompt message before input is received.
read -p "Enter the value of n: " y

# Calculate and display the derangement for the given n
result=$(derangement $y)                # Function call
echo "D($y) = $result"                  # Result printed in the format.


## This calculation is although smart but exponential. For example D(6) = 5*(D(5)+D(4)). Now for D(5), we will again have to calculate D(4). D(4) is effectively calculated two times.

# Additional Exercise: As you calculate D(n), store them in an array. So, next time you encounter the same n again,
# see if its value is already calculated or not. If yes, then access it directly from the array.


# Thanks for reading! ~ Saksham Rathi