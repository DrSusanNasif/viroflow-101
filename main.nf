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
process REVERSE_COMPLEMENT {
    publishDir "results", mode: "copy"

    input:
    path fasta_file

    output:
    path "reverse_complement.txt"

    script:
    """
    python3 ${projectDir}/bin/reverse_complement.py ${fasta_file} > reverse_complement.txt
    """
}


workflow {
    fasta_ch = Channel.fromPath(params.fasta)
    SUMMARIZE_FASTA(fasta_ch)
    REVERSE_COMPLEMENT(fasta_ch)
}