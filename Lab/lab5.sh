#!/bin/bash

echo "==============================="
echo "Q1.1: diff MultiN.fastq vs corrupted.fq"
echo "==============================="
diff MultiN.fastq corrupted.fq
echo

echo "==============================="
echo "Q1.2: Output explanation"
echo "==============================="
echo "Lines with < come from MultiN.fastq"
echo "Lines with > come from corrupted.fq"
echo

echo "==============================="
echo "Q2: TSV to CSV (eukaryotes.tsv)"
echo "==============================="
# Command to run this script for Q2:
# bash lab5.sh
sed 's/\t/,/g' eukaryotes.tsv > eukaryotes.csv
cat eukaryotes.csv
echo

echo "==============================="
echo "Q3: Largest string"
echo "==============================="
s1="This is a string"
s2="Hello"
s3="Strings are very cool"

len1=${#s1}
len2=${#s2}
len3=${#s3}

if [[ $len1 -ge $len2 && $len1 -ge $len3 ]]; then
    echo "String 1 is the biggest: $s1"
elif [[ $len2 -ge $len1 && $len2 -ge $len3 ]]; then
    echo "String 2 is the biggest: $s2"
else
    echo "String 3 is the biggest: $s3"
fi
echo

echo "==============================="
echo "Q4: FASTA headers"
echo "==============================="
for file in *.fasta; do
    echo "File: $file"
    grep "^>" "$file"
done
echo

echo "==============================="
echo "Q5: Print range of lines (2–5 from eukaryotes.tsv)"
echo "==============================="
# Command to run this script for Q5:
# bash lab5.sh
sed -n '2,5p' eukaryotes.tsv
echo


echo "==============================="
echo "Bonus I: Codon counting & conversion (example2.fasta)"
echo "==============================="
file="example2.fasta"
starts=$(grep -o "ATG" "$file" | wc -l)
ser=$(grep -o "S" "$file" | wc -l)
arg=$(grep -o "R" "$file" | wc -l)
stops=$(grep -o -E "TAA|TAG|TGA" "$file" | wc -l)

echo "ATG (M): $starts"
echo "Serine (S): $ser"
echo "Arginine (R): $arg"
echo "Stops (*): $stops"

sed -E 's/ATG/M/g; s/TAA|TAG|TGA/*/g' "$file" > converted.fasta
echo "--- Original ---"
cat "$file"
echo "--- Converted ---"
cat converted.fasta
echo

echo "==============================="
echo "Bonus II: Copy non-.txt files"
echo "==============================="
for file in MultiN.fastq corrupted.fq example2.fasta eukaryotes.tsv; do
    if [[ $file == *.txt ]]; then
        echo "Skipping $file"
    else
        cp "$file" "${file}.txt"
        echo "Created ${file}.txt"
    fi
done
echo

