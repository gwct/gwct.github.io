############################################################
# For personal site, 11.19
# This generates the file "research.html"
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

    <div class="row" id="header">Research</div>

    <div class="row" id="reasearch-intro-row">
        <div class="col-2-24" id="margin"></div>
        <div class="col-20-24">
            <div id="res-intro-cont">
                <p id="res-intro">
                    Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, 
                    quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum 
                    dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.
                </p>
            </div>
        </div>
        <div class="col-2-24" id="margin"></div>
    </div>

    <div class="row" id="section-header-row">
        <div class="col-2-24" id="margin"></div>
        <div class="col-20-24" id="section_header">Reasearch topic 1</div>
        <div class="col-2-24" id="margin"></div>
    </div>

    <div class="row" id="res-section">
        <div class="col-4-24" id="margin"></div>
        <div class="col-8-24" id="res-text">
            Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, 
			quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum 
			dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.
        </div>
        <div class="col-8-24" id="res-img-col">
            <img id="res-img" src="img/placeholder.png">
        </div>
        <div class="col-4-24" id="margin"></div>
    </div>

    <div class="row">
		<div class="col-24-24" id="sep_div"></div>
	</div>

    <div class="row" id="section-header-row">
        <div class="col-2-24" id="margin"></div>
        <div class="col-20-24" id="section_header">Research topic 2</div>
        <div class="col-2-24" id="margin"></div>
    </div>
    
    <div class="row" id="res-section">
        <div class="col-4-24" id="margin"></div>
        <div class="col-8-24" id="res-text">
            Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, 
			quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum 
			dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.
        </div>
        <div class="col-8-24" id="res-img-col">
            <img id="res-img" src="img/placeholder.png">
        </div>
        <div class="col-4-24" id="margin"></div>
    </div>

    <div class="row">
		<div class="col-24-24" id="sep_div"></div>
	</div>

    <div class="row" id="section-header-row">
        <div class="col-2-24" id="margin"></div>
        <div class="col-20-24" id="section_header">Research topic 3</div>
        <div class="col-2-24" id="margin"></div>
    </div>


    <div class="row" id="res-section">
        <div class="col-4-24" id="margin"></div>
        <div class="col-8-24" id="res-text">
            Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, 
			quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum 
			dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.
        </div>
        <div class="col-8-24" id="res-img-col">
            <img id="res-img" src="img/placeholder.png">
        </div>
        <div class="col-4-24" id="margin"></div>
    </div>

    <div class="row">
		<div class="col-24-24" id="sep_div"></div>
	</div>

    {links}

    {footer}
</body>
"""

######################
# Main block
######################
pagefile = "research.html";
print("Generating " + pagefile + "...");
title = "Ellie Armstrong - Research"

head = RC.readHead(title, pagefile);
nav = RC.readNav(pagefile);
links = RC.readLinks();
footer = RC.readFooter();

outfilename = "../../" + pagefile;

with open(outfilename, "w") as outfile:
    outfile.write(html_template.format(head=head, nav=nav, links=links, footer=footer));