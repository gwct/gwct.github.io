#!/usr/bin/python
############################################################
# UVU Genomics teaching demo, 01.2021
############################################################

import sys, os, gzip, argparse

############################################################
# Options

parser = argparse.ArgumentParser(description="FASTQ quality score counts");
parser.add_argument("-i", dest="input", help="An input FASTQ file.", default=False);
parser.add_argument("-o", dest="output", help="Desired output file name.", default=False);
parser.add_argument("--overwrite", dest="overwrite", help="If the output file already exists and you wish to overwrite it, set this option.", action="store_true", default=False);
args = parser.parse_args();
# IO options

if not args.input or not os.path.isfile(args.input):
    sys.exit(" * ERROR 1: Please enter valid FASTQ file (-i).");

if not args.output:
    args.output = "fastq-count.txt";

if os.path.isfile(args.output) and not args.overwrite:
    sys.exit( " * Error 2: Output file (" + args.output + ") already exists! Explicity specify --overwrite to overwrite it and its contents.");
# Input option parsing and error checking.

score_counts = {};
for i in range(0,42):
    score_counts[chr(i+33)] = { 'score' : str(i), 'prob-err' : str(10**(-i/10)), 'count' : 0 };
# Initializing count dictionary.

num_reads = 0;
for line in gzip.open(args.input):
    line = line.decode().strip();
    if line[0] == "@":
        read_line = 0;
        num_reads += 1;
    else:
        read_line += 1;

    if read_line == 3:
        for score in line:
            score_counts[score]['count'] += 1;
print("Total reads: " + str(num_reads));
# Counting quality scores.

with open(args.output, "w") as outfile:
    headers = ["Phred score" ,"Error probability" ,"Number of bases with score"];
    outfile.write("\t".join(headers) + "\n");

    for score in score_counts:
        outline = [ score_counts[score]['score'], score_counts[score]['prob-err'], str(score_counts[score]['count']) ];
        print("\t".join(outline));
        outfile.write("\t".join(outline) + "\n");
# Write the output file.
