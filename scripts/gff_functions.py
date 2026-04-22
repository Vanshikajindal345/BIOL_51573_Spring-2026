#!/usr/bin/env python3


#read_fasta: this will open and read the input the covid.fasta file. If you look at that file,
#you’ll see that you need to skip the first line (we’ve done this) and strip the newline character
#(we’ve done this, too) from each line containing DNA information. Return the DNA string in a
#variable called genome_sequence.

#filename = "data/covid_genome/covid.fasta"
# we rae 

def read_fasta(fasta_file):
    genome_sequence = ""

    with open(fasta_file, "r") as file:
        lines = file.readlines()

        for line in lines[1:]:   # skip header 
            genome_sequence += line.strip()

    return genome_sequence

#read_gff: this will read and parse covid_genes.gff3. See here for an introduction to GFF files.
#Use the begin and end coordinates (cols 4 and 5, respectively) of each feature in the genome (i.e.,
#each line in the GFF3 file) to extract that specific sequence out of the genome sequence. This
#function will need the name of the GFF3 file and the ‘genome_sequence’ string. This function
#will also need to extract the sequence ID, which is the information from the last column that
#follows “ID=”. So the sequence ID for the first gene is “cds-YP_009724389.1”, the second gene
#is “cds-YP_009725295.1”, and so on

# filename = "data/covid_genome/covid_genes.gff3"


def read_gff(gff_file, genome_sequence):
    features = []

    with open(gff_file, "r") as file:
        for line in file:
            if line.startswith("#"):
                continue
            
            # it means it creates the list of the genome
            cols = line.strip().split("\t")

            # Columns 4 and 5 → start and end
            start = int(cols[3])
            end = int(cols[4])

            # correct sequence extraction
            sequence = genome_sequence[start-1:end]

            attributes = cols[8]
            seq_id = attributes.split("ID=")[1].split(";")[0]

            # append to LIST 
            features.append((seq_id, sequence))

    return features
    
#write_output: usethetheextractedsequenceandsequenceIDtoprinteachfeature(i.e., eachline
#from the GFF3 file). Every sequence should be written out to the same file, covid_genes.fasta.
#The output should be in FASTA format, similar to what was in covid.fasta. Here’s a subset of
#the output:

def write_output(features):
    with open("covid_genes.fasta", "w") as outfile:
        for seq_id, sequence in features:
            outfile.write(f">{seq_id}\n")
            outfile.write(f"{sequence}\n")