#! /bin/bash

# For Testing
INSTRUCTOR_SCRIPTS="/home/.evaluationScripts"
# INSTRUCTOR_SCRIPTS="."
LAB_DIRECTORY="../labDirectory"


ptcd=$(pwd)

cd $INSTRUCTOR_SCRIPTS
# echo $ptcd

list_of_files="$(ls $LAB_DIRECTORY)"


cp -r $LAB_DIRECTORY/* autograder/

cd ./autograder/

chmod -R 777 $list_of_files

./grader.sh

rm -r $list_of_files

cd "$ptcd"
