from pathlib import Path

fasta_file = Path("data/raw/example_sequence.fasta")

print("ViroFlow-101: Sequence Check")
print(f"Input file: {fasta_file}")

if fasta_file.exists():
    print("Status: FASTA file found")

    sequence_count = 0
    sequence_names = []

    with open(fasta_file, "r") as file:
        for line in file:
            line = line.strip()

            if line.startswith(">"):
                sequence_count = sequence_count + 1
                sequence_name = line.replace(">", "")
                sequence_names.append(sequence_name)

    print(f"Number of sequences: {sequence_count}")
    print("Sequence names:")

    for name in sequence_names:
        print(f"- {name}")

else:
    print("Status: FASTA file NOT found")
