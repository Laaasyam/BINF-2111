#!/usr/bin/env python3
import argparse

protein = "vlspadknvww"
print("=== PART I ===")
print("1. Uppercase sequence:", protein.upper())
print("2. Valines (V):", protein.upper().count("V"))
print("3. Tryptophans (W):", protein.upper().count("W"))
print("4. Length:", len(protein))
print("5. W → G:", protein.upper().replace("W", "G"))


nuc = "GAATTCAGTAGATAGTAAGGAATTCTATGTATGTAGGCGCGCGTGCGCGTGCGCGGAATTC"
print("\n=== PART II ===")
print("6. AT repeats:", nuc.count('AT'))
print("   GC repeats:", nuc.count('GC'))
print("7. EcoR1 sites (AATTC):", nuc.count('AATTC'))

parts = nuc.split("GAATTC")
print("8. Sequences post EcoR1 cutting:")
for i, p in enumerate(parts, 1):
    print("   Fragment", i, ":", p)

a, t, g, c = nuc.count('A'), nuc.count('T'), nuc.count('G'), nuc.count('C')
total = len(nuc)
print(f"9. AT content: {((a+t)/total)*100:.2f}%")
print(f"   GC content: {((g+c)/total)*100:.2f}%")
print("10. RNA sequence (T→U):", nuc.replace('T', 'U'))


print("Bonus 1")
def run_bonus_protein(file):
    seq = ""
    for line in open(file):
        if not line.startswith(">"):
            seq += line.strip().lower()
    print("\n=== BONUS I ===")
    print("Sequence (lowercase):", seq)
    print("Valines (v):", seq.count("v"))
    print("Tryptophans (w):", seq.count("w"))
    print("Length:", len(seq))
    print("W → G:", seq.replace("w", "g"))
    polar = "stnqcy"
    print("Polar neutral amino acids:", sum(seq.count(a) for a in polar))


print("Bonus 2")
def run_bonus_nucleotide(file):
    seq = ""
    for line in open(file):
        if not line.startswith(">"):
            seq += line.strip().upper()
    complement = seq.translate(str.maketrans("ATGC", "TACG"))
    print("\n=== BONUS II ===")
    print("Sequence:", seq)
    print("Complement:", complement)


if __name__ == "__main__":
    
    default_protein = "CoV_furin_seq.faa"
    default_nuc = "RW2.fna"

    print("\n=== Running Bonuses Automatically ===")
    run_bonus_protein(default_protein)
    run_bonus_nucleotide(default_nuc)

