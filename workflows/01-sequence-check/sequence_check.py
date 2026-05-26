from pathlib import Path

fasta_file = Path("data/raw/example_sequence.fasta")

print("ViroFlow-101: Sequence Check")
print(f"Input file: {fasta_file}")

if fasta_file.exists():
    print("Status: FASTA file found")

    sequences = {}
    current_name = None
    current_sequence = ""

    with open(fasta_file, "r") as file:
        for line in file:
            line = line.strip()

            if line.startswith(">"):
                if current_name is not None:
                    sequences[current_name] = current_sequence

                current_name = line.replace(">", "")
                current_sequence = ""
            else:
                current_sequence = current_sequence + line

        if current_name is not None:
            sequences[current_name] = current_sequence

    print(f"Number of sequences: {len(sequences)}")
    print("Sequence lengths:")

    for name, sequence in sequences.items():
        print(f"- {name}: {len(sequence)} bases")

else:
    print("Status: FASTA file NOT found")
