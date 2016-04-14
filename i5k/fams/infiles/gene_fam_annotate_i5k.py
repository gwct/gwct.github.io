#!/usr/bin/python
#############################################################################
# Gene family annotation lookup with GO terms.
#
# Gregg Thomas
# Feb. 2016
#############################################################################

import sys, os, platform, argparse, core

############################################
#Function Definitions
############################################
def optParse(errorflag):
#This function handles the command line options.

	parser = argparse.ArgumentParser(description="Gene family annotation lookup with GO terms.");

	parser.add_argument("-i", dest="input_file", help="A tab delimited file containing on each line the gene family ID in the first column and all GO terms associated with that family.");
	parser.add_argument("-f", dest="fam_list", help="A comma delimited list of gene families for which you wish to look up GO terms. Enter 'all' to retrieve all families in input file.");
	parser.add_argument("-q", dest="query_list", help="A comma delimted list of words or terms to search for in the families retrieved with -f.", default="");

	args = parser.parse_args();

	if errorflag == 0:
		if args.input_file == None or args.fam_list == None:
			core.errorout(1, "All options must be specified.");
			optParse(1);

		return args.input_file, args.fam_list.split(","), args.query_list.split(",");

	elif errorflag == 1:
		parser.print_help();
		sys.exit();

######################

def printFams(fdict):
	# for fam in fdict:
	# 	print "Family ID: " + fam;
	# 	for gt in fdict[fam]:
	# 		for g in range(len(gt)):
	# 			if g == 0:
	# 				print "\t" + gt[g];
	# 			else:
	# 				print "\t\t" + gt[g];
	for fam in fdict:
		fam = str(fam);
		i = 0;
		for gt in fdict[fam]:
			if i == 0:
				i = i + 1;
				continue;
			outline = fam + "\t";
			for g in gt:
				outline = outline + g + "\t";
			print outline;
			i = i + 1;

######################

def querySearch(fdict, qlist):
	pdict = {};
	for q in qlist:
		for fam in fdict:
			for gt in fdict[fam]:
				for g in gt:
					if any(v in g for v in [q, q.title(), q.upper(), q.lower()]):
						pdict[fam] = fdict[fam];

	printFams(pdict);

############################################
#Main Block
############################################

infilename, famlist, querylist = optParse(0);
# Getting the input parameters.

gofilename = "go.obo";

# print "# =======================================================================";
# print "#\t\t\tGene Family Annotation Lookup";
# print "#\t\t\t" + core.getDateTime()
# print "# Input gene family annotation file:\t" + infilename;
# print "# GO term database location:\t\t" + gofilename;
# print "# ---------";
# print "# Looking up GO terms for the following families:";
# for each in famlist:
# 	print "# " + each;
# print "# ---------";
# if querylist != [""]:
# 	print "# Looking for the following phrases in above families:"
# 	for each in querylist:
# 		print "# " + each;
# 	print "# ---------";
# print "# Looking up annotations...\n"

if famlist[0].lower() == "all":
	famlist = [f.split("\t")[0] for f in open(infilename)];

# if len(famlist) > 100:
# 	if len(famlist) > 1000:
# 		print "# WARNING: Looking up more than 1000 families... this will take a very long time.\n"
# 	else:
# 		print "# WARNING: Looking up more than 100 families... this may take a while.\n"

famdict = {};

for fam in famlist:
	famdict[fam] = [];
	famline = "";
	for line in open(infilename):
		line = line.strip().split();
		if line[0] == fam:
			famline = line;
			break;

	if famline == "":
		continue;

	famline.pop(0);
	for goterm in famline:
		golist = [];
		golist.append(goterm);
		gofile = open(gofilename, "r");	
		for line in gofile:
			if line.strip() == "id: " + goterm:
				line = gofile.next();
				while "[Term]" not in line:
					if any(l in line for l in ["name:","namespace:","def:"]):				
						golist.append(line.strip());
					line = gofile.next();
				famdict[fam].append(golist);
				break;
		gofile.close();

	if len(famdict) > 100:
		if querylist != [""]:
			querySearch(famdict, querylist);
		else:
			printFams(famdict);
		famdict = {};
		# print "# Continuing lookup...\n"
	
if querylist != [""]:
	querySearch(famdict, querylist);
else:
	printFams(famdict);

# print "\n# Done!";
# print "# =======================================================================";