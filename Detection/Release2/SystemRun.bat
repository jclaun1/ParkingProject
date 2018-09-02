echo off
set pixels = python ssh_Driver.py %*

gcc -o Analyze Analyze.c
./Analyze

cat spots.txt
