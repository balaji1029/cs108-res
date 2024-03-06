#! /bin/bash

# For Testing
INSTRUCTOR_SCRIPTS="home/.evaluationScripts"
LAB_DIRECTORY="../labDirectory"


ptcd=$(pwd)

cd $INSTRUCTOR_SCRIPTS
# echo $ptcd

list_of_files="$(ls $LAB_DIRECTORY)"

# echo $ptcd
cp -r $LAB_DIRECTORY/* autograder/
# echo $ptcd

cd ./autograder/

chmod -R 777 $list_of_files

./grader.sh $1 $2

rm -r $list_of_files

cd "$ptcd"
