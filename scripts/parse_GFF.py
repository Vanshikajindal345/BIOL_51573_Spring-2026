#!/usr/bin/env python3

import argparse
import gff_functions



# Create argument parser
def get_args():
    parser = argparse.ArgumentParser(description="Parse FASTA files")

    parser.add_argument("fasta_file", help="Genome FASTA file")
    parser.add_argument("gff_file", help="Genome gff3 file")
    
    return parser.parse_args()
    # Read files
def main():
    args = get_args()
    genome_sequence = gff_functions.read_fasta(args.fasta_file)

    # extract sequences from gff
    sequences = gff_functions.read_gff(args.gff_file, genome_sequence)

    # Write output
    print("Genome length:", len(genome_sequence))
    print("complete.")
    gff_functions.write_output(sequences)

#set the env for the script
#is it main(), or this a module being called by something else?
if __name__ == "__main__":
    main()
