#!/usr/bin/env python3
sequence = input("Enter a DNA sequence: ")
sequence = sequence.upper()
a_count = sequence.count("A")
t_count = sequence.count("T")
total_length = len(sequence)
if total_length > 0:
    at_content = (a_count + t_count) / total_length * 100
else:
    at_content = 0

print("Number of A's:", a_count)
print("Number of T's:", t_count)
print("AT content:", round(at_content, 2), "%")