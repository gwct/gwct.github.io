############################################################
# For ConGen2020 site, 08.20
# This generates the file "reads.html"
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

    {main}

    {footer}
</body>
"""

######################
# Main block
######################
pagefile = "reads.html";
print("Generating " + pagefile + "...");
title = "ConGen2021 - Assembly Workshop"

head = RC.readHead(title);
nav = RC.readNav(pagefile);
main = RC.readReads();
footer = RC.readFooter();

outfilename = "../../" + pagefile;

with open(outfilename, "w") as outfile:
    outfile.write(html_template.format(head=head, nav=nav, main=main, footer=footer));