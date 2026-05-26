from pathlib import Path

fasta_file = Path("data/raw/example_sequence.fasta")
output_file = Path("workflows/01-sequence-check/outputs/sequence_summary.txt")
allowed_letters = set("ATGCN")

print("ViroFlow-101: Sequence Check")
print(f"Input file: {fasta_file}")

summary_lines = []

summary_lines.append("ViroFlow-101: Sequence Check")
summary_lines.append(f"Input file: {fasta_file}")

if fasta_file.exists():
    print("Status: FASTA file found")
    summary_lines.append("Status: FASTA file found")

    sequences = {}
    current_name = None
    current_sequence = ""

    with open(fasta_file, "r") as file:
        for line in file:
            line = line.strip().upper()

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
    print("Sequence checks:")

    summary_lines.append(f"Number of sequences: {len(sequences)}")
    summary_lines.append("Sequence checks:")

    for name, sequence in sequences.items():
        suspicious_letters = set(sequence) - allowed_letters

        print(f"- {name}: {len(sequence)} bases")
        summary_lines.append(f"- {name}: {len(sequence)} bases")

        if suspicious_letters:
            print(f"  Warning: suspicious letters found: {suspicious_letters}")
            summary_lines.append(f"  Warning: suspicious letters found: {suspicious_letters}")
        else:
            print("  Status: sequence letters look OK")
            summary_lines.append("  Status: sequence letters look OK")

else:
    print("Status: FASTA file NOT found")
    summary_lines.append("Status: FASTA file NOT found")

with open(output_file, "w") as file:
    file.write("\n".join(summary_lines))

print(f"Summary saved to: {output_file}")
