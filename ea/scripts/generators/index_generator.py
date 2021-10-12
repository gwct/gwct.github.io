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
			<img id="name_img" src="img/me/main-logo.png">
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
			<h3>
				My name is Ellie Armstrong and I am a postdoctoral fellow at Washington State University in 
				<a href="https://labs.wsu.edu/genomes/" target="_blank">Joanna Kelley's lab</a>. I recently earned my PhD at Stanford with 
				<a href="https://hadlylab.stanford.edu/" target="_blank">Elizabeth Hadly</a>, and <a href="http://petrov.stanford.edu/" target="_blank">Dmitri Petrov</a>.
			</h3>

			<p>
				Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, 
				quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum 
				dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.
			</p>
		</div>
		<div class="col-2-24" id="margin"></div>
	</div>

	<div class="row">
		<div class="col-24-24" id="sep_div"></div>
	</div>

	<div class="row" id="email_row">
		<div class="col-9-24" id="email-margin"></div>
		<div class="col-6-24" id="email-col">
			<img id="contact" src="img/contact/contact.png">
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
title = "Ellie Armstrong"

head = RC.readHead(title, pagefile);
nav = RC.readNav(pagefile);
links = RC.readLinks();
footer = RC.readFooter();

outfilename = "../../" + pagefile;

with open(outfilename, "w") as outfile:
    outfile.write(html_template.format(head=head, nav=nav, links=links, footer=footer));