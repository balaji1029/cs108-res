#!/bin/bash

for i in {444,644,666,755,777}
do
    touch $i.txt
    chmod $i $i.txt
done