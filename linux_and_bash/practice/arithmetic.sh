#!/bin/bash
#Author: Saksham Rathi
# Takes a file path as command line argument, and then reads 3 numbers and calculates their mean and variance.

# Check if a file path is provided as a command line argument. $# is the number of command line arguments
if [ "$#" -ne 1 ]; then         # See the syntax of if statement carefully. Conditions inside [] and -ne stands for not equal to.
    echo "Usage: $0 <file_path>"        
    exit 1                      # Stops the execution of the code
fi                              # If statement exits

# Check if the file exists or not
file_path=$1                    # First command line argument as $1
if [ ! -e "$file_path" ]; then          # ! = not, -e for file existence, the spaces around [ ] are necessary
    echo "Error: File $file_path not found."
    exit 1
fi

# Read the numbers from the file
numbers=()
while read -r number; do
    numbers+=("$number")
done < "$file_path"

# Calculate the sum
sum=0
for number in "${numbers[@]}"; do
    sum=$((sum + number))
done

# Calculate the average
average=$(bc -l <<< "scale=2; $sum / ${#numbers[@]}")

# Calculate the variance
variance=0
for number in "${numbers[@]}"; do
    variance=$(bc -l <<< "scale=2; $variance + ($number - $average)^2")
done
variance=$(bc -l <<< "scale=2; $variance / ${#numbers[@]}")

# Display the result
echo "The average of ${numbers[*]} is: $average"
echo "The variance of ${numbers[*]} is: $variance"

# Additional Exercise: The current code takes only three numbers, take n numbers, where n is another command line argument.


# Also, modify the code to support floating point calculations.

# Thanks for reading! ~ Saksham Rathi