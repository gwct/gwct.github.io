############################################################
# For ConGen2020 site, 08.20
# This generates the file "reads.html"
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
pagefile = "reads.html";
print("Generating " + pagefile + "...");
title = "ConGen2020 - Assembly Workshop"

head = RC.readHead(title);
nav = RC.readNav(pagefile);
banner = RC.readPrevBanner("2020", "assembly");
main = RC.readReads();
footer = RC.readFooter();

outfilename = "../../" + pagefile;

with open(outfilename, "w") as outfile:
    outfile.write(html_template.format(head=head, nav=nav, banner=banner, main=main, footer=footer));