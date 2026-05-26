# ViroFlow-101

A beginner-friendly bioinformatics project for exploring a viral genome using Python and Nextflow.

## Project goal

This project teaches beginners how to analyze a simple viral FASTA file and generate a basic genome summary.

## What this workflow does

The workflow reads a viral genome sequence and reports:

- sequence name
- genome length
- number of A, T, G, and C nucleotides
- GC content

## Project structure

```text
viroflow-101/
├── data/
│   └── test_virus.fasta
├── bin/
│   └── fasta_summary.py
├── results/
│   └── .gitkeep
├── main.nf
├── nextflow.config
└── README.md
