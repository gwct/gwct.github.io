############################################################
# For ConGen2020 site, 08.20
# This generates the file "end.html"
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

    <div class="row" id="section-cont">
        <div class="col-4-24" id="outer-margin"></div>
        <div class="col-16-24" id="section-col">
            <div class="row" id="section-row">
                <div class="col-2-24" id="inner-margin"></div>
                <div class="col-20-24" id="section-content">
                    <h1>Thank you for attending the read mapping workshop!</h1>

                    <div class="row" id="img-row">
                        <div class="col-7-24" id="margin"></div>
                        <div class="col-10-24" id="img-col">
                            <img id="res-img" src="img/pooh-meme.png">
                            <center><span class="fig-caption">Source unknown.</span></center>
                        </div>
                        <div class="col-7-24" id="margin"></div>
                    </div>

                    <p>Be sure to check out the <a href="programs.html">Programs</a> and <a href="terms.html">Terms</a> pages, and the slides for the lecture
                        and the workshop are available on the <a href="links.html">Links</a> page.</p>

                    <p>&nbsp;</p>
                    <p>&nbsp;</p>

                </div>
                <div class="col-2-24" id="inner-margin"></div>
            </div>
        </div>
        <div class="col-4-24" id="outer-margin"></div>
    </div>


    {footer}
</body>
</html>
"""

######################
# Main block
######################
pagefile = "end.html";
print("Generating " + pagefile + "...");
title = "Harvard Bioinformatics"

head = RC.readHead(title);
nav = RC.readNav(pagefile);
footer = RC.readFooter();

outfilename = "../../" + pagefile;

with open(outfilename, "w") as outfile:
    outfile.write(html_template.format(head=head, nav=nav, footer=footer));