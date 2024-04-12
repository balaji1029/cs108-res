# Variable definition
s="hello"

# Valid variable names
my_variable="value"
_variable="value"
Variable123="value"

# Invalid variable names
# 123variable="value" # Starts with a digit
# variable name="value" # Contains space

# Use the value in variable s
echo "The value of s is: $s"

echo "-----------------------------------------------"

# Escaping the spl characters
echo 'This is a single quote: '\''This is inside single quotes'\'
echo "This is a double quote: \"This is inside double quotes\""

echo "-----------------------------------------------"

# Single quotes vs double quotes
# Single quotes (') preserve the literal value of each character, 
# meaning that nothing inside single quotes will be interpreted as special characters.
# Double quotes (") preserve the literal value of most characters but allow 
# for variable expansion and command substitution.
greeting="Hello"
echo 'This is a single-quoted string: $greeting' 
echo "This is a double-quoted string: $greeting" 

echo "-----------------------------------------------"

# Commands enclosed in backticks (``) or $() will be substituted with their output
filename="python.sh"
echo "The contents of $filename are: $(cat $filename)"

echo "-----------------------------------------------"
# USER="hello"
# Environment variables
# SHELL
echo "The value of the SHELL environment variable is: $SHELL"
# PATH
echo "The value of the PATH environment variable is: $PATH"
# PWD
echo "The value of the PWD environment variable is: $PWD"
# USER
echo "The value of the USER environment variable is: $USER"