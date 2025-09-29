#!/bin/bash

var1="Methionine"
var2="Leucine"
var3="Cysteine"
var4="Alanine"
var5="Valine"

echo $var1
echo $var2
echo $var3
echo $var4
echo $var5

total_length=$((${#var1} + ${#var2} + ${#var3} + ${#var4} + ${#var5}))

echo "Total length: $total_length"

echo "---------------------------------------------------------------"

start="ATG"
stop1="TAA"
stop2="TAG"
stop3="TGA"

start_count=$(grep -v "^>" example2.fasta | grep "^$start" | wc -l)

stop_count=$(grep -v "^>" example2.fasta | egrep "$stop1$|$stop2$|$stop3$" | wc -l)

echo "Number of start codons ($start): $start_count"
echo "Number of stop codons ($stop1, $stop2, $stop3): $stop_count"

echo "---------------------------------------------------------------"

echo "Username: "

whoami

echo "Current directory: "

pwd

echo "Root directory: "
ROOT


echo "Date and time: "

date

echo "---------------------------------------------------------------"


echo "1. gunzip file.gz → Uncompress"

echo "2. tar -zxvf file.tar.gz → Uncompress"

echo "3. zip file.zip file.txt file1.txt → Compress"

echo "4. tar -zcvf file.tar.gz file.txt file1.txt → Compress"

echo "---------------------------------------------------------------"

aminos=(Methionine Leucine Cysteine Alanine Valine Tyrosine Proline)
echo "to delete Alanine: unset aminos[3]"
echo "to print the aminos from cysteine to tyrosine: ${aminos[@]:2:4}"
echo "to add histidine to the array: aminos+=("Histidine")"

echo "---------------------------------------------------------------"

echo "to count how many times the name 'abdul' is left: grep -oP "abdul\s+chi" doppelganger_names.txt | wc -l"
echo "the count: "
grep -oP "abdul\s+chi" doppelganger_names.txt | wc -l

echo "---------------------------------------------------------------"

echo "legal variable name: myVariable=10"
echo "illegal variable name: 3variable=10"
echo "---------------------------------------------------------------"
echo "to compile: chmod +x script.sh"
echo "to run a bash script: bash script.sh"
echo "---------------------------------------------------------------"
echo "bonus 1: "
aminos=(Methionine Leucine Cysteine Alanine Valine Tyrosine Proline)

for amino in "${aminos[@]}"
do
  echo $amino
done
