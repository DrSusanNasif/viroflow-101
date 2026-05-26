from pathlib import Path

fasta_file = Path("data/raw/example_sequence.fasta")

print("ViroFlow-101: Sequence Check")
print(f"Input file: {fasta_file}")

if fasta_file.exists():
    print("Status: FASTA file found")
else:
    print("Status: FASTA file NOT found")
