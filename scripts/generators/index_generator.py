############################################################
# For personal site, 11.19
# This generates the file "index.html"
############################################################

import sys, os
sys.path.append('..')
import lib.read_chunks as RC

######################
# HTML template
######################

html_template = """
<!doctype html>
    {head}

<body>
    {nav}

<div class="row" id="top_grid">
		<div class="col-24-24" id="hero">
			<div id="name_img_cont">
				<img id="name_img" src="img/me/name5.png">
			</div>
		</div>
	</div>

	<div class="row">
		<div class="col-24-24" id="sep_div"></div>
	</div>

	<div class="row" id="bio_row">
		<div class="col-1-24" id="margin"></div>
		<div class="col-5-24" id="bio_pic_container">
			<div id="bio_pic"></div>
		</div>
		<div class="col-1-24" id="margin"></div>
		<div class="col-15-24" id="bio_text">
			<h3>Hi! I am a Bioinformatics Scientist in the <a href="https://informatics.fas.harvard.edu/" target="_blank">FAS Informatics Group</a> at
					Harvard University.</h3>
					
			<p>I was recently a postdoctoral researcher at the University of Montana in <a href="http://www.thegoodlab.org/" target="_blank">Jeff Good's lab</a>,
				and I studied at Indiana University under the advisement of <a href="http://www.indiana.edu/~hahnlab/" target="_blank">Matt Hahn</a>.</p>
			<p>I'm excited to understand the processes and patterns of molecular evolution by using genomics and phylogenetics, and working 
				through some of the problems that vast amounts of genomic data has presented. To this end, I have worked on modeling mutation rate variation 
				in mammals, detecting convergent evolution on genomic data, and analyzing gene families in a number of species. I contributed to latest 
				version of <a href="https://hahnlab.github.io/CAFE/" target="_blank">CAFE</a> to account for error in gene family analysis, and I developed 
				the program <a href="https://gwct.github.io/grampa" target="_blank" id="doi_link">GRAMPA</a> to study polyploidy in the context of gene tree 
				topologies. <!-- I also have an interest in the biology of extremophiles.</p> --> I also wrote the program 
				<a href="https://gwct.github.io/referee" target="_blank" id="doi_link">Referee</a> to annotate genome assemblies with quality scores.</p>
			<p>Outside of the lab, I have a passion for 

				<span>do<img class="hidden_img" src="img/me/jenny.jpg"></span><span>gs<img class="hidden_img" src="img/me/momo.jpg"></span> 
				and <span>animals<img class="hidden_img" src="img/me/pip.jpg"></span> 
				in general. <!-- I volunteer every weekend at the local animal shelter to try and help
				out. --> I also enjoy being active and doing 
				<span> puzzles<img class="hidden_img" src="img/me/puzzles.jpg"></span> with my partner!</p>
		</div>
		<div class="col-2-24" id="margin"></div>
	</div>

	<div class="row">
		<div class="col-24-24" id="sep_div"></div>
	</div>

	<div class="row" id="email_row">
		<div class="col-9-24" id="email-margin"></div>
		<div class="col-6-24" id="email-col">
			<img id="contact" src="img/contact/cont.png">
		</div>
		<div class="col-9-24" id="email-margin"></div>
	</div>

	{links}

    {footer}
</body>
"""

######################
# Main block
######################
pagefile = "index.html";
print("Generating " + pagefile + "...");
title = "Gregg Thomas"

head = RC.readHead(title, pagefile);
nav = RC.readNav(pagefile);
links = RC.readLinks();
footer = RC.readFooter();

outfilename = "../../" + pagefile;

with open(outfilename, "w") as outfile:
    outfile.write(html_template.format(head=head, nav=nav, links=links, footer=footer));