#! /bin/bash

# For Testing
INSTRUCTOR_SCRIPTS="/home/labDirectory/.evaluationScripts"
LAB_DIRECTORY="/home/labDirectory"


ptcd=$(pwd)

cd $INSTRUCTOR_SCRIPTS
# echo $ptcd

list_of_files="$(ls $LAB_DIRECTORY)"

cp -r $LAB_DIRECTORY/repo.tar.gz autograder/

cd ./autograder/

chmod -R 777 repo.tar.gz

./grader.sh

rm -r repo.tar.gz

cd "$ptcd"