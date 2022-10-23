############################################################
# For ConGen2020 site, 08.20
# This generates the file "index.html"
############################################################

import sys, os
#sys.path.append('..')
import lib.read_chunks as RC

######################
# HTML template
######################

html_template = """
<!doctype html>
    {head}

<body>

    <div class="row" id="top_grid">
        <div class="row" id="bg-col-row">
            <div class="col-24-24" id="bg-col-col">

                <div class="row" id="header-row">
                    <div class="col-24-24" id="header-col">
                        <center><a href="https://phyloacc.github.io/">PhyloAcc</a> courses</center>
                    </div>
                </div>

                <div class="row" id="link-row">

                    <div class="col-10-24" id="inner-margin"></div>
                    <div class="col-4-24" id="btm-link"><a href="OEB275R/index.html">OEB275R - Fall 2022</a></div>
                    <div class="col-10-24" id="inner-margin"></div>

                </div>

            </div>
        </div>
	</div>

    {footer}
</body>
</html>
"""

######################
# Main block
######################
pagefile = "index.html";
print("Generating " + pagefile + "...");
title = "PhyloAcc courses"

head = RC.readHead(title);
nav = RC.readNav(pagefile);
footer = RC.readFooter();

outfilename = pagefile;

with open(outfilename, "w") as outfile:
    outfile.write(html_template.format(head=head, nav=nav, footer=footer));