#!/usr/bin/env bash

mkdir Day${1}
touch Day${1}/day${1}-1.py
touch Day${1}/day${1}-2.py
touch Day${1}/input.txt

printf "import re\n" >> Day${1}/day${1}-1.py
printf "import sys\nsys.path.append(\"..\")\nfrom input_reader import InputReader\n" >> Day${1}/day${1}-1.py

cat Day${1}/day${1}-1.py >> Day${1}/day${1}-2.py
