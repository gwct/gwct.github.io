############################################################
# For ConGen2020 site, 08.20
# This generates the file "index.html"
############################################################

import sys, os
sys.path.append(os.path.abspath('lib/'))
import read_chunks as RC

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

                <div class="row" id="congen-row">
                    <div class="col-24-24" id="congen-col">
                        <center><a href="https://www.umt.edu/ces/conferences/congen/">ConGen 2024</a></center>
                    </div>
                </div>

                <div class="row" id="link-row">

                    <div class="col-6-24" id="inner-margin"></div>
                    <div class="col-4-24" id="btm-link"><a href="bioinformatics/index.html">Intro to Bioinformatics</a></div>
                    <div class="col-4-24" id="inner-margin"></div>
                    <div class="col-4-24" id="btm-link"><a href="assembly/index.html">Assembly Workshop</a></div>
                    <div class="col-6-24" id="inner-margin"></div>

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
title = "ConGen2024"

head = RC.readHead(title);
nav = RC.readNav(pagefile);
footer = RC.readFooter();

outfilename = pagefile;

with open(outfilename, "w") as outfile:
    outfile.write(html_template.format(head=head, nav=nav, footer=footer));