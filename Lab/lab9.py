#!/usr/bin/env python3


# ---------- PART 1 ----------
count = 0
with open("example2.fasta", "r") as file:
    for line in file:
        if line.startswith(">"):
            count += 1
print(f"There are {count} sequences in example2.fasta.\n")


# ---------- PART 2 ----------
def read_fasta(filename):
    """Reads FASTA and returns list of sequences."""
    sequences = []
    seq = ""
    with open(filename, "r") as f:
        for line in f:
            if line.startswith(">"):
                if seq:
                    sequences.append(seq)
                    seq = ""
            else:
                seq += line.strip()
        if seq:
            sequences.append(seq)
    return sequences


sequences = read_fasta("example2.fasta")

# a. Count AT and GC repeats
for seq in sequences:
    at_repeats = seq.count("AT")
    gc_repeats = seq.count("GC")
    print(f"AT repeats: {at_repeats}, GC repeats: {gc_repeats}")

# b. Length of each sequence
for i, seq in enumerate(sequences, start=1):
    print(f"Sequence {i} length: {len(seq)}")

# c. Count EcoR1 sites (GAATTC)
for seq in sequences:
    eco_sites = seq.count("GAATTC")
    print(f"EcoR1 sites found: {eco_sites}")

# d. Replace every T with U and save to new file
with open("RNAconverted.fna", "w") as new_file:
    for seq in sequences:
        rna = seq.replace("T", "U")
        new_file.write(rna + "\n")
print("All T's replaced with U and saved to RNAconverted.fna.")

# e. Count AT and GC content (percent)
for seq in sequences:
    a = seq.count("A")
    t = seq.count("T")
    g = seq.count("G")
    c = seq.count("C")
    total = len(seq)
    at_content = ((a + t) / total) * 100
    gc_content = ((g + c) / total) * 100
    print(f"AT content: {at_content:.2f}%, GC content: {gc_content:.2f}%\n")


# ---------- PART 3 ----------
# a. Join the sequence into one line (ignore header)
with open("pUC19c.fasta", "r") as f:
    lines = f.readlines()[1:]
    sequence = "".join(line.strip() for line in lines)
print(f"Joined pUC19c sequence length: {len(sequence)} bases.")

# b. Count number of SmaI sites (CCCGGG)
sma_sites = sequence.count("CCCGGG")
print(f"Number of SmaI sites in pUC19c: {sma_sites}")

# c. AT and GC content
a = sequence.count("A")
t = sequence.count("T")
g = sequence.count("G")
c = sequence.count("C")
total = len(sequence)
at_content = ((a + t) / total) * 100
gc_content = ((g + c) / total) * 100
print(f"AT content: {at_content:.2f}%, GC content: {gc_content:.2f}%")

# d. NEBcutter instructions
print("""
To visualize the SmaI site:
1. Go to https://nc3.neb.com/NEBcutter/
2. Click 'File' and upload pUC19c.fasta
3. Click 'Submit'
4. Take a screenshot of the plasmid map
5. Click the SmaI site to see its location (Site at ___)
6. Take a screenshot of the site info
""")

print("The site is located at 412.")

