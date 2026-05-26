from pathlib import Path

fasta_file = Path("data/raw/example_sequence.fasta")

print("ViroFlow-101: Sequence Check")
print(f"Input file: {fasta_file}")

if fasta_file.exists():
    print("Status: FASTA file found")

    sequence_count = 0

    with open(fasta_file, "r") as file:
        for line in file:
            if line.startswith(">"):
                sequence_count = sequence_count + 1

    print(f"Number of sequences: {sequence_count}")

else:
    print("Status: FASTA file NOT found")
