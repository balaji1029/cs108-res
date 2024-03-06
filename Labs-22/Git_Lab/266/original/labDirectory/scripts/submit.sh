#!/bin/bash

cd ../working_directory

tar -zcvf big_repo1.tar.gz big_repo/

mv big_repo1.tar.gz ../big_repo.tar.gz

cd ../scripts

rm -rf ../working_directory/big_repo