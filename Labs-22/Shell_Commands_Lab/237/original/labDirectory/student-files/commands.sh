#!/bin/bash

mkdir -p demo
cd demo
mkdir -p code
mkdir -p doc
cd code
PROG=hello.c
cp ../../$PROG ./
gcc -o hello $PROG
./hello
