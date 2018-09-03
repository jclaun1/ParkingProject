@echo off

python driver.py %*
cat pixels.py

gcc -o Analyze Analyze.c
./Analyze

cat spots.txt
