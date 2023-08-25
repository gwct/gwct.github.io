############################################################
# For ConGen2020 site, 08.20
# This generates the file "index.html"
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

    <div class="row" id="section-cont">
        <div class="col-4-24" id="outer-margin"></div>
        <div class="col-16-24" id="section-col">
            <div class="row" id="section-row">
                <div class="col-2-24" id="inner-margin"></div>
                <div class="col-20-24" id="section-content">
                    <h1>Welcome to the virtual <a href="https://www.umt.edu/ces/conferences/congen/" target="_blank">ConGen2022</a> genome assembly workshop!</h1>
                        <p>This web page will guide you through the genome assembly and read mapping activities we have planned for you today!</p>
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

                    <!--
                    <div id="sep_div"></div>

                    <div class="row" id="instructor">
                        <div class="col-4-24" id="inst-img-cont">
                            <img id="inst-img" src="img/gt.jpg">
                        </div>
                        <div class="col-20-24" id="inst-text">
                            <p><a href="https://gwct.github.io/" target="_blank">Gregg Thomas</a>: A bioinformatics scientist in the
                                <a href="https://informatics.fas.harvard.edu/" target="_blank">FAS Informatics group</a> at Harvard University and recent postdoc in
                                <a href="http://www.thegoodlab.org/" target="_blank">Jeff Good's lab</a> lab at the University of Montana. Gregg uses and develops
                                computational methods to study molecular evolution and phylogenetics to determine what forces drive divergence and adaptation between species.
                            </p>
                        </div>
                    </div>
                    -->

                    <div id="sep_div"></div>

                    <div class="row" id="instructor">
                        <div class="col-4-24" id="inst-img-cont">
                            <img id="inst-img" src="img/ea.jpg">
                        </div>
                        <div class="col-20-24" id="inst-text">
                            <p>Ellie Armstrong: A recent PhD at Stanford University co-advised by
                                <a href="http://petrov.stanford.edu/" target="_blank">Dmitri Petrov</a> and <a href="https://web.stanford.edu/group/hadlylab/" target="_blank">Liz Hadley</a>.
                                Ellie works on conservation genetics of big cats, and published the 
                                <a href="https://bmcbiol.biomedcentral.com/articles/10.1186/s12915-019-0734-5" target="_blank">genome assembly of the lion</a> and will soon be starting a postdoc at
                                Washington State University with <a href="https://labs.wsu.edu/genomes/" target="_blank">Joanna Kelley</a>.
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
            <div id="section-header">Navigation</div>
        </div>
        <div class="col-4-24" id="outer-margin"></div>
    </div>
    <div class="row" id="section-cont">
        <div class="col-4-24" id="outer-margin"></div>
        <div class="col-16-24" id="section-col">
            <div class="row" id="section-row">
                <div class="col-2-24" id="inner-margin"></div>
                <div class="col-20-24" id="section-content">
                    <p>In the nav bar at the top of the page you'll find links to navigate this workshop and to resources we've compiled. Come back to this page any time by clicking 
                        the <a href="#">Intro</a> link above. Go to the first page of the workhop by clicking on the <a href="start.html">Workshop</a> link above or the link below.
                        If you come across a term or file format you don't recognize, check the <a href="terms">Terminology</a> page to see if it's listed there.
                        A table of useful programs and their use-cases has been compiled as a resource under the <a href="programs.html">Programs</a> link. Finally, some other links have
                        been organized in the <a href="links.html">Links</a> page.
                    </p>

                    <p>Use the links below to start and navigate to various parts of the workshop.</p>

                    <center><h1><a href="start.html" id="start-btn">Get Started</a></h1></center>

                    <div class="row" id="link-row">
                        <div class="col-4-24" id="btm-link"><a href="reads.html">Reads</a></div>
                        <div class="col-3-24" id="inner-margin"></div>
                        <div class="col-4-24" id="btm-link"><a href="assembly.html">Assembly</a></div>
                        <div class="col-3-24" id="inner-margin"></div>
                        <div class="col-4-24" id="btm-link"><a href="mapping.html">Mapping</a></div>
                        <div class="col-3-24" id="inner-margin"></div>
                        <div class="col-4-24" id="btm-link"><a href="iterative-mapping.html">Iterative mapping</a></div>
                    </div>
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
year = RC.getYear();
title = "ConGen" + year + " - Assembly Workshop"

head = RC.readHead(title);
nav = RC.readNav(pagefile);
banner = RC.readPrevBanner(year, "assembly");
footer = RC.readFooter();

outfilename = "../../" + pagefile;

with open(outfilename, "w") as outfile:
    outfile.write(html_template.format(head=head, nav=nav, banner=banner, footer=footer));