#! /bin/bash

# For Testing
INSTRUCTOR_SCRIPTS="/home/.evaluationScripts"
LAB_DIRECTORY="/home/labDirectory"


ptcd=$(pwd)

cd $INSTRUCTOR_SCRIPTS
# echo $ptcd

list_of_files="$(ls $LAB_DIRECTORY)"

cp -r $LAB_DIRECTORY/working_directory.tar.gz autograder/

cd ./autograder/

chmod -R 777 working_directory.tar.gz

./grader.sh

rm -r working_directory.tar.gz

cd "$ptcd"