#!/usr/bin/python
print('Content-type: text/plain\n')
#############################################################################
# Gene family annotation lookup with GO terms.
#
# Gregg Thomas
# Feb. 2016
#############################################################################

import sys, os, cgi, argparse

############################################
#Function Definitions
############################################
def printFams(fdict):
	for fam in fdict:
		fam = str(fam);
		i = 0;
		if fdict[fam] == []:
			print fam + "\tNo GO Terms found.";
		for gt in fdict[fam]:
			if i == 0:
				i = i + 1;
				continue;
			outline = fam + "\t";
			if len(gt) == 0:
				outline += "No GO Terms found.";
			for g in gt:
				outline += g + "\t";
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

#infilename, famlist, querylist = optParse(0);
# Getting the input parameters.

infilename = "i5k_go_mult.txt";
gofilename = "go.obo";

form = cgi.FieldStorage();
famlist = form.getlist('infams');
querylist = "";

# print "# =======================================================================";

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
	
#if querylist != [""]:
#	querySearch(famdict, querylist);
#else:
printFams(famdict);

# print "\n# Done!";
# print "# =======================================================================";
