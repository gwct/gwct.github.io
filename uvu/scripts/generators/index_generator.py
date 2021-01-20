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

                    <h1>Welcome to Genomics at Utah Valley University (teaching demo).</h1>
                        <p>This web page hosts the syllabus, class resources, and lab assignments for the course.</p>
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
                        <b>Genomics</b> is the modern scientific field that uses the sequences of whole genomes to reveal the function and molecular variation encoded in DNA and the relationships 
                        between living organisms. These advances are enabled by the ability to sequence whole genomes quickly and at low-cost. Genome sequencing 
                        and analysis has become a fundamental and essential aspect of many biological research questions. This strictly computational course is 
                        designed to provide a narrative description of modern genomics workflows from sequencing to genome assembly to genome analysis. Starting 
                        from the raw data received from a genome sequencer, we will study the underlying data encodings, methods, and algorithms of genomic software, 
                        using hands-on, computer-lab based discussions and activities, providing students with first-hand experience running and implementing these methods.
                    </p>

                    <a name="prereqs"></a>
                    <h3>Prerequisites</h3>
                    <p>
                        Familiarity with command-line interfaces, some programming experience, basic understanding of probability and statistics. All of these skills can be learned
                        in the Practical Computing for Biology course.
                    </p>

                    <a name="struct"></a>
                    <h3>Course Structure</h3>
                    <p>
                        This course meets twice a week in a computer lab, and consists of a combination of short lectures, group discussion, and hands-on lab applications. 
                        Each week, the topic will be introduced with a brief overview in a lecture before we break into small groups for more in-depth discussion. The second 
                        class instructional period of the week will be devoted to a hands-on application as a lab. Following a brief discussion of the lab workflow, students 
                        will begin work on the lab with the opportunity to raise and troubleshoot issues during class time. Students will then be responsible for completing 
                        the assignment by the end of the week.  
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
                                at Indiana University studying how mutations rates evolve in primates.
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
                    <p>
                        This page will host all resources for the class, including lecture slides, worksheets, readings, and lab assignments.
                        I also aim to provide helpful resources, such as definitions of common terms or file formats you might come across
                        on the <a href="terms.html">Terminology</a> page and lists of <a href="programs.html">Programs</a> that we will use.
                    </p>

                    <p>
                        A really good place to get started if you have any questions is the Syllabus page:
                    </p>

                    <center><h2><a href="syllabus.html" id="start-btn">Syllabus</a></h2></center>

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
title = "UVU Genomics"

head = RC.readHead(title);
nav = RC.readNav(pagefile);
footer = RC.readFooter();

outfilename = "../../" + pagefile;

with open(outfilename, "w") as outfile:
    outfile.write(html_template.format(head=head, nav=nav, footer=footer));