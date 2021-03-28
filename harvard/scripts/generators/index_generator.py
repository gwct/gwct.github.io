############################################################
# For ConGen2020 site, 08.20
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

    <div class="row" id="section-cont">
        <div class="col-4-24" id="outer-margin"></div>
        <div class="col-16-24" id="section-col">
            <div class="row" id="section-row">
                <div class="col-2-24" id="inner-margin"></div>
                <div class="col-20-24" id="section-content">
                    
                    <div id="sep_div"></div>
                    <div class="row" id="img-row">
                        <div class="col-6-24" id="margin"></div>
                        <div class="col-12-24" id="img-col">
                            <img id="main-img" src="img/logo-1.png">
                            <!-- <center><span class="fig-caption">Figure 1.1: The RStudio interface for running commands and browsing files.</span></center>  -->
                        </div>
                        <div class="col-6-24" id="margin"></div>
                    </div>          

                    <h1>Welcome to the Harvard FAS Bioinformatics workshops page.</h1>
                        <p>
                            This page will host all resourcess for the workshops, including lecture slides, worksheets, and links to relevant readings.
                            I also aim to provide helpful resources, such as definitions of common terms or file formats you might come across
                            on the <a href="terms.html">Terminology</a> page and lists of <a href="programs.html">Programs</a> that we will use.
                        </p>
                </div>
                <div class="col-2-24" id="inner-margin"></div>
            </div>
        </div>
        <div class="col-4-24" id="outer-margin"></div>
    </div>

    <a name="desc"></a>
    <div class="row" id="section-header-cont">
        <div class="col-4-24" id="outer-margin"></div>
        <div class="col-16-24" id="section-header-row">
            <div id="section-header">Course description</div>
        </div>
        <div class="col-4-24" id="outer-margin"></div>
    </div>
    <div class="row" id="section-cont">
        <div class="col-4-24" id="outer-margin"></div>
        <div class="col-16-24" id="section-col">
            <div class="row" id="section-row">
                <div class="col-2-24" id="inner-margin"></div>
                <div class="col-20-24" id="section-content">

                    <p>
                        During this workshop, we will be learning about read mapping and reference bias, and how to mitigate reference bias through iterative mapping using
                        pseudo-it.
                    </p>

                    <a name="prereqs"></a>
                    <h3>Prerequisites</h3>
                    <p>
                        A basic familiarity with command line interfaces. All other software will be pre-installed on your machines.
                    </p>

                </div>
                <div class="col-2-24" id="inner-margin"></div>
            </div>
        </div>
        <div class="col-4-24" id="outer-margin"></div>
    </div>

    <a name="instructors"></a>
    <div class="row" id="section-header-cont">
        <div class="col-4-24" id="outer-margin"></div>
        <div class="col-16-24" id="section-header-row">
            <div id="section-header">Instructors</div>
        </div>
        <div class="col-4-24" id="outer-margin"></div>
    </div>
    <div class="row" id="section-cont">
        <div class="col-4-24" id="outer-margin"></div>
        <div class="col-16-24" id="section-col">
            <div class="row" id="section-row">
                <div class="col-2-24" id="inner-margin"></div>
                <div class="col-20-24" id="section-content">

                    <div id="sep_div"></div>

                    <div class="row" id="instructor">
                        <div class="col-4-24" id="inst-img-cont">
                            <img id="inst-img" src="img/gt.jpg">
                        </div>
                        <div class="col-20-24" id="inst-text">
                            <p><a href="https://gwct.github.io/" target="_blank">Gregg Thomas</a> is a postdoctoral researcher in <a href="http://www.thegoodlab.org/" target="_blank">Jeff Good's</a>
                                lab at the University of Montana. Gregg studies molecular evolution to determine what forces drive divergence and adaptation between species. He earned his doctorate
                                at Indiana University studying how mutation rates evolve in primates, patterns of gene gain and loss in arthropods, and molecular convergence. He currently studies
                                phylogenetics and molecular evolution of murine rodents.
                            </p>
                        </div>
                    </div>

                    <div id="sep_div"></div>

                </div>
                <div class="col-2-24" id="inner-margin"></div>
            </div>
        </div>
        <div class="col-4-24" id="outer-margin"></div>
    </div>

    <a name="nav"></a>
    <div class="row" id="section-header-cont">
        <div class="col-4-24" id="outer-margin"></div>
        <div class="col-16-24" id="section-header-row">
            <div id="section-header">Getting started</div>
        </div>
        <div class="col-4-24" id="outer-margin"></div>
    </div>
    <div class="row" id="section-cont">
        <div class="col-4-24" id="outer-margin"></div>
        <div class="col-16-24" id="section-col">
            <div class="row" id="section-row">
                <div class="col-2-24" id="inner-margin"></div>
                <div class="col-20-24" id="section-content">
                    <p>
                        Today we'll be working on read mapping:
                    </p>

                    <center><h2><a href="start.html" id="start-btn">Start workshop</a></h2></center>

                    <div id="sep_div"></div>
                    <!-- <div class="row" id="link-row">
                        <div class="col-4-24" id="btm-link"><a href="reads.html">Reads</a></div>
                        <div class="col-3-24" id="inner-margin"></div>
                        <div class="col-4-24" id="btm-link"><a href="assembly.html">Assembly</a></div>
                        <div class="col-3-24" id="inner-margin"></div>
                        <div class="col-4-24" id="btm-link"><a href="mapping.html">Mapping</a></div>
                        <div class="col-3-24" id="inner-margin"></div>
                        <div class="col-4-24" id="btm-link"><a href="iterative-mapping.html">Iterative mapping</a></div>
                    </div> -->
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
pagefile = "index.html";
print("Generating " + pagefile + "...");
title = "Harvard Bioinformatics"

head = RC.readHead(title);
nav = RC.readNav(pagefile);
footer = RC.readFooter();

outfilename = "../../" + pagefile;

with open(outfilename, "w") as outfile:
    outfile.write(html_template.format(head=head, nav=nav, footer=footer));