# GeneFlow
A Python based bioinformatics tool for DNA sequence validation, composition analysis, ORF detection, transcription, and translation.

## Overview
GeneFlow is a beginner-developed Python tool designed to perform basic
DNA sequence analysis and demonstrate fundamental concepts of molecular
biology and programming.

The tool takes a DNA sequence as input and performs validation,
composition analysis, ORF detection, transcription, and translation.

## Features
- DNA sequence validation
- DNA sequence length calculation
- A, T, G, and C base counting
- GC% and AT% calculation
- Open Reading Frame (ORF) detection
- Transcription of DNA to mRNA
- Translation of mRNA into an amino acid sequence

## Technologies Used
- Python 3
- Python dictionaries
- Loops and conditional statements
- String manipulation
- Basic bioinformatics concepts

## Input
GeneFlow uses a DNA sequence provided through `input_dna.txt`.

The sequence should contain standard DNA bases: A, T, G, C

## How to Run
1. Download or clone this repository.
2. Place your DNA sequence in `input_dna.txt`.
3. Run `GeneFlow.py` using Python 3.
4. The program will display the sequence analysis results.

## Example
Input: ATGCATGCGTAA

GeneFlow analyzes the sequence and reports information including
sequence length and compositions, ORFs, mRNA sequences, and translated amino acid chains.

Output :

 Entered sequence is a Valid DNA
 
 The length of the sequence is : 12
 
 The number of Adenine bases in the sequence is : 4
 
 The number of Thymine bases in the sequence is : 3

 The number of Guanine bases in the sequence is : 3
 
 The number of Cytosine bases in the sequence is : 2

 AT Percentage is :58.33%

 GC Percentage is :41.67%
 
 The ORF sequence is : ATGCATGCGTAA

 ORF Starts from : 1

 ORF Ends at : 12

 Length of the ORF is : 12

 The Transcribed mRNA sequence is : AUGCAUGCGUAA

The Translated Amino acid chain is : Met-His-Ala

## Project Status
GeneFlow is an ongoing learning project. Future improvements may
include FASTA file support, additional sequence analysis features,
and improved input handling.

## Author
AyushBiotech
