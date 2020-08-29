############################################################
# For ConGen2020 site, 08.20
# This generates the file "links.html"
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

    <div class="row">
        <div class="col-4-24" id="margin"></div>
        
        <div class="col-16-24" id="main_content">

        	<!--<div class="row" id="section-header-row">
                <div class="col-24-24" id="section_header">ConGen2020</div>
	        </div>-->

            <ul id="links-list">
                <li><a href="https://www.umt.edu/ces/conferences/congen/" target="_blank">ConGen2020</a></li>

            </ul>
            <div id="sep_div"></div>
        </div>
        <div class="col-4-24" id="margin"></div>
    </div>

    {footer}
</body>
"""

######################
# Main block
######################
pagefile = "links.html";
print("Generating " + pagefile + "...");
title = "ConGen2020 - Assembly Workshop"

head = RC.readHead(title);
nav = RC.readNav(pagefile);
footer = RC.readFooter();

outfilename = "../../" + pagefile;

with open(outfilename, "w") as outfile:
    outfile.write(html_template.format(head=head, nav=nav, footer=footer));