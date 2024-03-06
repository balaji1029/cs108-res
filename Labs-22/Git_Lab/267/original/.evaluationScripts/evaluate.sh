#! /bin/bash

# For Testing
INSTRUCTOR_SCRIPTS="/home/.evaluationScripts"
LAB_DIRECTORY="/home/labDirectory"

ptcd=$(pwd)

cd $INSTRUCTOR_SCRIPTS
# echo $ptcd

list_of_files="$(ls $LAB_DIRECTORY)"

cp -r $LAB_DIRECTORY/merge_repo.tar.gz autograder/

cd ./autograder/

chmod -R 777 merge_repo.tar.gz

./grader.sh

rm -r merge_repo.tar.gz

cd "$ptcd"