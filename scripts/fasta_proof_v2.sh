#!/usr/bin/env bash
set -euo pipefail

INPUT="data/test_virus.fasta"
OUTDIR="results/bash_proof"
REPORT="$OUTDIR/report_v2.txt"
SEQUENCE="$OUTDIR/sequence_only.txt"

mkdir -p "$OUTDIR"

echo "Processing file: $INPUT"

grep -v '^>' "$INPUT" | tr 'a-z' 'A-Z' | tr -cd 'ATGCN' > "$SEQUENCE"

SEQ=$(cat "$SEQUENCE")
LENGTH=${#SEQ}

{
  echo "Bash FASTA proof v2"
  echo "-------------------"
  echo "Input file: $INPUT"
  echo ""
  echo "Clean sequence:"
  echo "$SEQ"
  echo ""
  echo "Sequence length: $LENGTH"
  echo ""
  echo "Base counts:"
} > "$REPORT"

for BASE in A T G C N
do
  COUNT=$(echo "$SEQ" | tr -cd "$BASE" | wc -c)
  echo "$BASE: $COUNT" >> "$REPORT"
done

G_COUNT=$(echo "$SEQ" | tr -cd 'G' | wc -c)
C_COUNT=$(echo "$SEQ" | tr -cd 'C' | wc -c)

GC=$(awk -v g="$G_COUNT" -v c="$C_COUNT" -v len="$LENGTH" 'BEGIN { printf "%.2f", ((g+c)/len)*100 }')

echo "" >> "$REPORT"
echo "GC content: $GC%" >> "$REPORT"

echo "Done. Report created at: $REPORT"
