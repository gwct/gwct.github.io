############################################################
# For ConGen2020 site, 08.20
# This generates the file "mapping.html"
############################################################

import sys, os
sys.path.append(os.path.abspath('../lib/'))
import read_chunks as RC

######################
# HTML template
######################

html_template = """
<!doctype html>
    {head}

<body>
    {nav}

    {banner}

    {main}

    {footer}
</body>
"""

######################
# Main block
######################
pagefile = "mapping.html";
print("Generating " + pagefile + "...");
year = RC.getYear();
title = "ConGen" + year + " - Assembly Workshop"

head = RC.readHead(title);
nav = RC.readNav(pagefile);
banner = "";
#banner = RC.readPrevBanner(year, "assembly");
main = RC.readMapping();
footer = RC.readFooter();

outfilename = "../../" + pagefile;

with open(outfilename, "w") as outfile:
    outfile.write(html_template.format(head=head, nav=nav, main=main, banner=banner, footer=footer));