#!/usr/bin/env nextflow

/*
ViroFlow-101
A beginner-friendly Nextflow workflow for summarizing a viral FASTA file.
*/

process SUMMARIZE_FASTA {

    publishDir "results", mode: "copy"
    
    input:
    path fasta_file

    output:
    path "genome_summary.txt"

    script:
    """
    python3 ${projectDir}/bin/fasta_summary.py ${fasta_file} > genome_summary.txt
    """
}

workflow {
    fasta_ch = Channel.fromPath("data/test_virus.fasta")
    SUMMARIZE_FASTA(fasta_ch)
}
