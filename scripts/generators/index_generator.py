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

	<div class="pure-g" id="top_grid">
		<div class="pure-u-24-24" id="hero">
			<img class="pure_img" id="name_img" src="img/me/name5.png">
		</div>
	</div>

	<div class="pure-g" id="main_div_bio">
		<!-- <div class="pure-u-24-24" id="header">Bio</div> -->
		<div class="pure-u-24-24" id="sep_div"></div>

		<div class="pure-u-1-24" id="margin"></div>
		<div class="pure-u-5-24" id="bio_pic_container">
			<div class="pure_img" id="bio_pic"></div>
		</div>
		<div class="pure-u-1-24" id="margin"></div>
		<div class="pure-u-15-24" id="bio_text">
			<h3 align="justify">Hi! I am a postdoctoral research associate in the Division of Biological Sciences at the University of Montana under 
			the advisement of <a href="http://www.thegoodlab.org/" target="_blank">Jeff Good</a>.</h3> I previously studied at Indiana University with 
				<a href="http://www.indiana.edu/~hahnlab/" target="_blank">Matt Hahn</a>.
			<p align="justify">I'm excited to understand the processes and patterns of molecular evolution by using genomics and phylogenetics, and working 
				through some of the problems that vast amounts of genomic data has presented. To this end, I have worked on modeling mutation rate variation 
				in mammals, detecting convergent evolution on genomic data, and analyzing gene families in a number of species. I contributed to latest 
				version of <a href="https://hahnlab.github.io/CAFE/" target="_blank">CAFE</a> to account for error in gene family analysis, and I developed 
				the program <a href="https://gwct.github.io/grampa" target="_blank" id="doi_link">GRAMPA</a> to study polyploidy in the context of gene tree 
				topologies. <!-- I also have an interest in the biology of extremophiles.</p> --> I also wrote the program 
				<a href="https://gwct.github.io/referee" target="_blank" id="doi_link">Referee</a> to annotate genome assemblies with quality scores.</p>
			<p align="justify">Outside of the lab, I have a passion for 
				<span id="hidden">do<img src="img/me/jenny.jpg"></span><span id="hidden">gs<img src="img/me/momo.jpg"></span>
				 and </span><span id="hidden">animals<img src="img/me/pip.jpg"></span> 
				 in general. <!-- I volunteer every weekend at the local animal shelter to try and help
				out. --> I also enjoy being active and doing 
				<span id="hidden"> puzzles<img src="img/me/puzzles.jpg"></span> with my partner!</p>

			<!-- <p>Contact: grthomas [at] indiana [dot] edu</p> -->
			<div class="pure-u-2-24" id="margin"></div>
		</div>

        <!--<div class="pure-u-10-24" id="margin"></div>	-->
        <div class="pure-u-24-24"><center><img class="pure_img" id="contact" src="img/contact/cont.png"></center></div>
        <!--<div class="pure-u-10-24" id="margin"></div>-->

		<div class="pure-u-24-24" id="sep_div"></div>

		<div class="pure-u-6-24" id="margin"></div>	
        {links}
		<div class="pure-u-6-24" id="margin"></div>
	</div>

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