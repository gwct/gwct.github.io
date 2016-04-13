import sys

def htmlPrep():
	template = """
	<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
	<html xmlns="http://www.w3.org/1999/xhtml">
	<head>
		<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
		<title>i5k - Arthropod Phylogeny</title>
		<link rel="stylesheet" href="table_style.css" type="text/css" media="screen" />
	</head>

	<body>

		<h1>{header}</h1>

		<h3>Significantly changing families:</h3>

		<p><b>Bold</b> text indicates lineage specific changes.</p>
		<table>
			<tr><th>Family ID</th><th>GO link</th></tr>
			{table}
		</table>
	</body>
	</html>
	"""
	return template;

##################################

infilename = "infiles/dupliphy_sig.txt";
lsfilename = "infiles/dupliphy_sig_ls.txt";

inlines = open(infilename).readlines();
lslines = open(lsfilename).readlines();
i = 1;
for line in inlines:
	if line[0] == "#":
		continue;
	print i;
	fams = [];
	node = "";

	line = line.strip().split("\t");
	node = line[0][:line[0].index(" ")].replace("<","").replace(">","");
	

	html = htmlPrep();
	outfilename = node + "_fams.html";

	if node.isdigit():
		header = "Node " + node;
	else:
		header = node;

	if len(line) < 2:
		table = "<tr><td>No siginificant changes found on this branch.</td></tr>";
		
	else:
		fams = line[1].split(",");
		lsfams = [];
		table = "";

		for lsline in lslines:
			if lsline[0] == "#":
				continue;
			lsline = lsline.strip().split("\t");
			lsnode = lsline[0][:lsline[0].index(" ")].replace("<","").replace(">","");
			if lsnode == node and len(lsline) > 1:
				lsfams = lsline[1].split(",");
		

		for fam in fams:
			if fam in lsfams:
				fam = "<b>" + fam + "</b>";
			table += "<tr><td>" + fam + "</td><td></td></tr>"

	outfile = open(outfilename, "w");
	outfile.write(html.format(header=header, table=table));
	outfile.close();
	i = i + 1;
	#sys.exit();


#<tr><td>EOG8CC6J2*</td><td></td></tr>