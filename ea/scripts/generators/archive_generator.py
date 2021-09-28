############################################################
# For personal site, 11.19
# This generates the file "archive.html"
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

	<div class="row" id="header">Updates</div>

    <div class="row" id="section-header-row">
        <div class="col-2-24" id="margin"></div>
        <div class="col-20-24" id="section_header">September 25, 2021</div>
        <div class="col-2-24" id="margin"></div>
	</div>
	<div class="row" id="pub-row"></div>
	<div class="col-2-24" id="margin"></div>
	<div class="col-20-24" id="arc_entry">
		<ul>
			<p>
				I recently defended my dissertation on Comparative and Population Genomics of the Big Cats!
			</p>

			<p>
				I will be starting a postdoctoral fellowship in the <a href="https://labs.wsu.edu/genomes/" target="_blank">Kelley lab</a>
				at Washington State University!
			</p>
		</ul>
	</div>
	<div class="col-2-24" id="margin"></div>


    <div class="row" id="section-header-row">
        <div class="col-2-24" id="margin"></div>
        <div class="col-20-24" id="section_header">August 18, 2021</div>
        <div class="col-2-24" id="margin"></div>
	</div>
	<div class="row" id="pub-row"></div>
	<div class="col-2-24" id="margin"></div>
	<div class="col-20-24" id="arc_entry">
		<ul>
			<p>In September, I will be giving a workshop on genome assembly with <a href="https://gwct.github.io/" target="_blank">Gregg Thomas</a> at this year's online
			<a href="https://www.umt.edu/ces/conferences/congen/" target="_blank">ConGen</a>.</p>
		</ul>
	</div>
	<div class="col-2-24" id="margin"></div>


    <div class="row" id="section-header-row">
        <div class="col-2-24" id="margin"></div>
        <div class="col-20-24" id="section_header">July 20, 2020</div>
        <div class="col-2-24" id="margin"></div>
	</div>
	<div class="row" id="pub-row"></div>
	<div class="col-2-24" id="margin"></div>
	<div class="col-20-24" id="arc_entry">
		<ul>
			<p>
				Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, 
				quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum 
				dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.
			</p>
		</ul>
	</div>
	<div class="col-2-24" id="margin"></div>

    <div class="row" id="section-header-row">
        <div class="col-2-24" id="margin"></div>
        <div class="col-20-24" id="section_header">May 30, 2020</div>
        <div class="col-2-24" id="margin"></div>
	</div>
	<div class="row" id="pub-row"></div>
	<div class="col-2-24" id="margin"></div>
	<div class="col-20-24" id="arc_entry">
		<ul>
			<p>
				Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, 
				quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum 
				dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.
			</p>

			<p><a href="#">Read more</a></p>

			<p>-------</p>

			<p>
				Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, 
				quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum 
				dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.
			</p>
		</ul>
	</div>
	<div class="col-2-24" id="margin"></div>

    {links}

    {footer}
</body>
"""

######################
# Main block
######################
pagefile = "archive.html";
print("Generating " + pagefile + "...");
title = "Ellie Armstrong - Updates"

head = RC.readHead(title, pagefile);
nav = RC.readNav(pagefile);
links = RC.readLinks();
footer = RC.readFooter();

outfilename = "../../" + pagefile;

with open(outfilename, "w") as outfile:
    outfile.write(html_template.format(head=head, nav=nav, links=links, footer=footer));