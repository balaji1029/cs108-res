#!/bin/bash

# For Testing

cd ..
temp=$(pwd)
# echo $temp
cd ./evaluationScripts

INSTRUCTOR_SCRIPTS=$temp"/evaluationScripts"
LAB_DIRECTORY=$temp"/labDirectory"

ptcd=$(pwd)

cd $INSTRUCTOR_SCRIPTS
# echo $ptcd

list_of_files="$(ls $LAB_DIRECTORY)"


cp -r $LAB_DIRECTORY/* $INSTRUCTOR_SCRIPTS"/"autograder/

cd $INSTRUCTOR_SCRIPTS"/"autograder/

chmod -R 777 $list_of_files

./grader.sh

rm -r $list_of_files

cd "$ptcd"
