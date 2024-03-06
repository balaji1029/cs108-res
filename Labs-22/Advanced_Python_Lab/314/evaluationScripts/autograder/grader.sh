#! /bin/bash

echo 'Please wait, this may take around a minute..'
cd ..
wget -q https://sarthakmittal92.github.io/taships/plots.tar.gz
tar -xf plots.tar.gz
cd autograder
mkdir -p plots
mkdir -p files
../algo 1>/dev/null
python3 main.py
python3 autograder.py
rm -rf ../plots
rm -rf ../plots.tar.gz
