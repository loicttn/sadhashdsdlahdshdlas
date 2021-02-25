#!/usr/bin/env bash

./main.py ./data/A.txt > ./results/A.txt
./main.py ./data/B.txt > ./results/B.txt
./main.py ./data/C.txt > ./results/C.txt
./main.py ./data/D.txt > ./results/D.txt
./main.py ./data/E.txt > ./results/E.txt
./main.py ./data/F.txt > ./results/F.txt

zip -r out.zip .
