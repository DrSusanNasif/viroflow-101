#!/usr/bin/env bash

INPUT="data/test_virus.fasta"
OUTDIR="results/bash_proof"

mkdir -p "$OUTDIR"

echo "Processing file: $INPUT"

echo "Original file content:" > "$OUTDIR/report.txt"
cat "$INPUT" >> "$OUTDIR/report.txt"

echo "" >> "$OUTDIR/report.txt"
echo "File statistics:" >> "$OUTDIR/report.txt"
wc "$INPUT" >> "$OUTDIR/report.txt"

echo "" >> "$OUTDIR/report.txt"
echo "Sequence only:" >> "$OUTDIR/report.txt"
cat "$INPUT" | tr 'a-z' 'A-Z' | tr -cd 'ATGCN' >> "$OUTDIR/report.txt"

echo "" >> "$OUTDIR/report.txt"
echo "Done. Report created at: $OUTDIR/report.txt"
