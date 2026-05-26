# ViroFlow-101

A beginner-friendly bioinformatics project for exploring a viral genome using Python and Nextflow.

## Current status

This repository currently contains:

- a test viral FASTA file
- a beginner Python script to summarize the FASTA sequence
- a simple Nextflow workflow
- a basic project configuration file

Next step: test the workflow locally or in a cloud/web environment.

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
