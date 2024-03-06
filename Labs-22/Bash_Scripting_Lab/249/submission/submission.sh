#!/bin/bash

string=$*
for file in *.out
do
	echo $string >> $file
done