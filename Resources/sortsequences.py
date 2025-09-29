#!/usr/bin.python3

#function that counts the number of sequences in a file
def count_sequence(filename):
	with open(filename, 'r') as infile:
		seqs = infile.read()
		numseqs = seqs.count(">")
		print("Number of sequences: ", numseqs)


#function that sorts headers into list items and writes them into a new file
def sortheaders(filename):
	with open(filename, 'r') as infile:
		headerlist = []

		for line in infile.readlines():
			if line.startswith(">"):
				headerlist.append(line.strip('\n'))
	return headerlist


#function that sorts sequences into list items and writes them into a new file
def sortseqs(filename):
	with open(filename, 'r') as infile:
		seqlist = []
		seq = ""

		for line in infile.readlines():
			if not line.startswith(">"):
				seq += line.strip('\n')
			elif line.startswith(">") and len(seq) > 0:
				seqlist.append(seq)
				seq = ""
		#the code in this statement executes when the loop reaches the end of the file
		else:
			seqlist.append(seq)
	print("List of seqs: ", seqlist)
	return seqlist


#function that counts ATs in each item in seqlist
def count_AT(seq): #takes list as parameter
	
	countA = seq.count("A")
	countT = seq.count("T")
	strresult = "The number of A is ", countA, " and the number of T is ", countT
	return strresult

#counting # of seqs
count_sequence("lab2.fna")
sortseqs("lab2.fna")

#prints the list of headers
print("List of headers: ", sortheaders("lab2.fna"))

#writes each header in the list into a file
outfile = open("example2_headers.txt", 'w')

headerlist = sortheaders("lab2.fna")
seqlist = sortseqs("lab2.fna")

for header in headerlist:
	outfile.write(header)
	outfile.write("\n")
print("headers written to: example2_headers.txt")

#writes each seq in the list into a file
outfile = open("example2_seqs.txt", 'w')

#prints each sequence in the sequence list into a new file
for seq in seqlist:
        outfile.write(seq)
        outfile.write("\n")
print("seqs written to: example2_seqs.txt")

# prints each header and corresponding AT content
for i in range(0, 4):
	print(headerlist[i],": ", count_AT(seqlist[i]))
	

