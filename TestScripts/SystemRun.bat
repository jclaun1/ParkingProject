@echo off

python ssh_Driver.py %*
cat pixels.py

gcc -o Analyze Analyze.c
./Analyze

cat spots.txt
