############################################################
# For Harvard interview, 03.21
# Takes a PAF file from minimap and calculates % identity
############################################################

import sys

if len(sys.argv) < 2:
    sys.exit("ERROR: No input file provided.\nUSAGE: python div_est.py <input file in PAF>")

infilename = sys.argv[1];

matches, total = 0,0;
for line in open(infilename):
    line = line.strip().split("\t");
    matches += int(line[9]);
    total += int(line[10]);

perc_ident = (matches / total ) * 100;

print("# Percent matching bases: " + str(round(perc_ident, 3)));