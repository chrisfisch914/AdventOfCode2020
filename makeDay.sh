#!/usr/bin/env bash

mkdir Day${1}
touch Day${1}/day${1}-1.py
touch Day${1}/day${1}-2.py
touch Day${1}/input.txt

printf "import re\n" >> Day${1}/day${1}-1.py
printf "import re\n" >> Day${1}/day${1}-2.py
