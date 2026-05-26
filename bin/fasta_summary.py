# fasta_summary.py
# A beginner-friendly script to summarize a viral FASTA file

import sys

fasta_file = sys.argv[1]

sequence_name = ""
sequence = ""

with open(fasta_file, "r") as file:
    for line in file:
        line = line.strip()

        if line.startswith(">"):
            sequence_name = line[1:]
        else:
            sequence += line.upper()

length = len(sequence)

a_count = sequence.count("A")
t_count = sequence.count("T")
g_count = sequence.count("G")
c_count = sequence.count("C")

gc_content = ((g_count + c_count) / length) * 100

print("Genome summary")
print("--------------")
print(f"Sequence name: {sequence_name}")
print(f"Genome length: {length} nucleotides")
print(f"A count: {a_count}")
print(f"T count: {t_count}")
print(f"G count: {g_count}")
print(f"C count: {c_count}")
print(f"GC content: {gc_content:.2f}%")
