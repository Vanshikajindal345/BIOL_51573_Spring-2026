#!/usr/bin/env python3


#read_fasta: this will open and read the input the covid.fasta file. If you look at that file,
#you’ll see that you need to skip the first line (we’ve done this) and strip the newline character
#(we’ve done this, too) from each line containing DNA information. Return the DNA string in a
#variable called genome_sequence.

#filename = "data/covid_genome/covid.fasta"
# we rae 
# we have the functions without defining then they will show the error so thats why putting the print statements

def read_fasta(fasta_file):
    genome_sequence = ""

# now we will open the fileby using the with open functions 
# everytime I am writing i will do the sanity ckecks using the print statmenst
# make. avariabel to store the genome sequence
    with open(fasta_file, "r") as file:
        lines = file.readlines()

        for line in lines[1:]:   # skip header # if line starts with the > like the first line : if line.startswith(">"):
            genome_sequence += line.strip()
# How do we add sequence together += and strip the line using the strip function
# search from the google always what function we needed to do that specific thing 
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
            # i used the delimiter that is \ so thats why its in the bracket created a line 
            # as long as line is the split so we can grab the pieces together 
            ## we want the three parts of this file if I get a list if 3 is the start and 4 is the end 
            #def read_gff(gff3_file):
            #with open(gff3_file, "r") as g:
            # create a csv reader object
            #reader = csv.reader(g, delimiter='\t')
            cols = line.strip().split("\t")

            # Columns 4 and 5 → start and end 
            # call it as the attributes 
            # indexing we will use the start and end coordinates we use the zero base numbering 
            # in the python if the end coordinate is the 3 but for slicing 
            # lets say first gff starts the file from 1 but python 0 
            # in python = gff-1
            # for teh end is like GFFe

            start = int(cols[3])
            end = int(cols[4])

            # correct sequence extraction
            sequence = genome_sequence[start-1:end]

            attributes = cols[8]
            seq_id = attributes.split("ID=")[1].split(";")[0]

            # append to LIST 
            features.append((seq_id, sequence))

    return features


# read the file line by line 
# for line in reader:
# start = int(line[3]) - 1
# end = int(line[4]) # we dont have to change the end cord because how pythin slices
# features_seq = genome_sequence[start:end]
# print (start end, len(features_seq), atts)
# all this is to get the 
    
#write_output: usethetheextractedsequenceandsequenceIDtoprinteachfeature(i.e., eachline
#from the GFF3 file). Every sequence should be written out to the same file, covid_genes.fasta.
#The output should be in FASTA format, similar to what was in covid.fasta. Here’s a subset of
#the output:

def write_output(features):
    with open("covid_genes.fasta", "w") as outfile:
        for seq_id, sequence in features:
            outfile.write(f">{seq_id}\n")
            outfile.write(f"{sequence}\n")

# biopython they have a function to read the fasta file replace with that the and use taht 