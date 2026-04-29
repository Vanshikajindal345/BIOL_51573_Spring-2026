#!/usr/bin/env python3

import argparse
import gff_functions

# he mentioned to use the use the argparse function and then need to define the 
# def main():
#   gff_functions.read_gff()
#   gff_functions

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
    # in order to read the read fasta how do we get the file args.fatsa and we expect to return to the genome sequence read_fasta(args.fasta_file)

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


# copy the command line fibonacci file and the modified
#def get_args():
###------------- accept and parse command line arguments
# create an argument parser object
    #parser = argparse.ArgumentParser(description="Get feature sequence from a GFF file from a gff file and corresposnding genome file")

    # add a positional argument, in this case, the position in the fasta and gff file
    #parser.add_argument("fasta", help="Name of genome file in FASTA format", type=str)
    #parser.add_argument("gff3", help="Name of genome file in GFF3 format", type=str)

    # parse the arguments and return in two steps
    #args = parser.parse_args()
    #return args
