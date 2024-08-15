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
                    <center>
                        <h1>
                            Welcome to the virtual <a href="https://www.umt.edu/ces/conferences/congen/" target="_blank">ConGen2024</a> Introduction to Bioinformatics workshop!
                        </h1>
                        <p>
                            This web page will guide you through the activities we have planned for you today!
                        </p>
                    </center>
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
                            <img id="inst-img" src="img/rs.jpg">
                        </div>
                        <div class="col-20-24" id="inst-text">
                            <p>
                                <a href="https://renaschweizer.org/" target="_blank">Rena Schweizer</a>: Rena is a Research Entomologist with the USDA Agricultural 
                                Research Service Pollinating Insects Research Unit, where she is working on conservation genomics of U.S. native bees. In her research, 
                                Rena integrates genomics, population genetics, bioinformatics, and physiology to evaluate the conservation status of wildlife populations 
                                and study evolution. 
                            </p>
                        </div>
                    </div>

                    <!--
                    <div class="row" id="instructor">
                        <div class="col-4-24" id="inst-img-cont">
                            <img id="inst-img" src="img/gt.jpg">
                        </div>
                        <div class="col-20-24" id="inst-text">
                            <p>
                                <a href="https://gwct.github.io/" target="_blank">Gregg Thomas</a>: A bioinformatics scientist in the
                                <a href="https://informatics.fas.harvard.edu/" target="_blank">FAS Informatics group</a> at Harvard University and recent postdoc in
                                <a href="http://www.thegoodlab.org/" target="_blank">Jeff Good's lab</a> lab at the University of Montana. Gregg uses and develops
                                computational methods to study molecular evolution and phylogenetics to determine what forces drive divergence and adaptation between species.
                            </p>
                        </div>
                    </div>
                    -->

                    <div id="sep_div"></div>

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
                        If you come across a term or file format you don't recognize, check the <a href="terms.html">Terminology</a> page to see if it's listed there.
                        A table of useful programs and their use-cases has been compiled as a resource under the <a href="programs.html">Programs</a> link. Finally, some other links,
                        including to workshops from previous years (though they are mostly identical), have been organized in the <a href="links.html">Links</a> page.
                    </p>

                    <p>Use the links below to start and navigate to various parts of the workshop.</p>

                    <center><h1><a href="start.html" id="start-btn">Get Started</a></h1></center>

                    <div class="row" id="link-row">
                        <div class="col-4-24" id="btm-link"><a href="organization.html">Project Organization</a></div>
                        <div class="col-1-24" id="inner-margin"></div>
                        <div class="col-4-24" id="btm-link"><a href="commands.html">Command Concepts</a></div>
                        <div class="col-1-24" id="inner-margin"></div>
                        <div class="col-4-24" id="btm-link"><a href="macaque-svs.html">Macaque SVs</a></div>
                        <div class="col-1-24" id="inner-margin"></div>
                        <div class="col-4-24" id="btm-link"><a href="wolf-snps.html">Wolf SNPs</a></div>
                        <div class="col-1-24" id="inner-margin"></div>
                        <div class="col-4-24" id="btm-link"><a href="advanced.html">Advanced Topics</a></div>
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
title = "ConGen" + year + " - Intro to Bioinformatics"

head = RC.readHead(title);
nav = RC.readNav(pagefile);
banner = "";
#banner = RC.readPrevBanner(year, "bioinformatics");
footer = RC.readFooter();

outfilename = "../../" + pagefile;

with open(outfilename, "w") as outfile:
    outfile.write(html_template.format(head=head, nav=nav, banner=banner, footer=footer));