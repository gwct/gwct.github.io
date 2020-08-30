############################################################
# For ConGen2020 site, 08.20
# This generates the file "assembly.html"
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

    <div class="row" id="header">Genome assembly</div>

    <div class="row" id="body-row">
        <div class="col-3-24" id="side-nav-cont">
            <div id="side-nav">
                <span id="side-header">Page contents</span>
                <ul>
                    <li><a href="assembly.html#top">Intro</a></li>
                    <li><a href="assembly.html#spades">Short read assembly with SPAdes</a></li>
                    <li><a href="assembly.html#flye">Long read assembly with Flye</a></li>
                    <li><a href="assembly.html#asm-qual">Assembly quality</a></li>
                </ul>
            </div>
        </div>

        <div class="col-21-24" id="main-cont">
            <a class="internal-link" name="top"></a>
            <div class="row" id="section-cont">
                <div class="col-24-24" id="section-col">
                    <div class="row" id="section-row">
                        <div class="col-2-24" id="inner-margin"></div>
                        <div class="col-20-24" id="section-content">

                            <p><em>de novo</em> Genome assembly is the process by which overlapping sequence reads are pieced back together to form longer, contiguous sequences
                                for analysis:
                            </p>
                
                            <div class="row" id="img-row">
                                <div class="col-4-24" id="margin"></div>
                                <div class="col-16-24" id="img-col">
                                    <img id="res-img" src="img/assembly-flow-2.png">
                                    <center><span class="fig-caption">Figure 3.1: Genome assembly usually proceeds in steps that connect progressively longer segments of sequence.</span></center>
                                </div>
                                <div class="col-4-24" id="margin"></div>
                            </div>       
                            
                            <p>Many factors can play a role in the ultimate success of a genome assembly, including sequencing error rate, heterozygosity of the target genome, length of the target genome,
                                and number and length of reads sequenced.
                            </p>
                
                            <p>Today, we'll be using both long and short reads to assemble the <em>D. pseudoobscura</em> genome and then using several metrics to assess the resulting assemblies.</p>

                        </div>
                        <div class="col-2-24" id="inner-margin"></div>
                    </div>
                </div>
            </div>    

            <a class="internal-link" name="spades"></a>
            <div class="row" id="section-header-cont">
                <div class="col-24-24" id="section-header-row">
                    <div id="section-header">Assembly with short reads with <a href="https://github.com/ablab/spades/" target="_blank">SPAdes</a></div>
                </div>
            </div>
            <div class="row" id="section-cont">
                <div class="col-24-24" id="section-col">
                    <div class="row" id="section-row">
                        <div class="col-2-24" id="inner-margin"></div>
                        <div class="col-20-24" id="section-content">

                        <p>Content

                        </div>
                        <div class="col-2-24" id="inner-margin"></div>
                    </div>
                </div>
            </div>

            <a class="internal-link" name="flye"></a>
            <div class="row" id="section-header-cont">
                <div class="col-24-24" id="section-header-row">
                    <div id="section-header">Assembly with long reads with <a href="https://github.com/fenderglass/Flye/" target="_blank">Flye</a></div>
                </div>
            </div>
            <div class="row" id="section-cont">
                <div class="col-24-24" id="section-col">
                    <div class="row" id="section-row">
                        <div class="col-2-24" id="inner-margin"></div>
                        <div class="col-20-24" id="section-content">

                        <p>Content

                        </div>
                        <div class="col-2-24" id="inner-margin"></div>
                    </div>
                </div>
            </div>

            <a class="internal-link" name="asm-qual"></a>
            <div class="row" id="section-header-cont">
                <div class="col-24-24" id="section-header-row">
                    <div id="section-header">Assessing assembly quality</div>
                </div>
            </div>
            <div class="row" id="section-cont">
                <div class="col-24-24" id="section-col">
                    <div class="row" id="section-row">
                        <div class="col-2-24" id="inner-margin"></div>
                        <div class="col-20-24" id="section-content">

                        <p>Content

                        </div>
                        <div class="col-2-24" id="inner-margin"></div>
                    </div>
                </div>
            </div>

        </div>
    </div>

    <div class="row" id="btm-nav">
        <div class="col-3-24" id="nav-bnt-margin"></div>
        <div class="col-6-24" id="nav-btn-cont">
            <div class="nav-btn">
                <a href="reads.html">&lt;&nbsp;Previous</a>    
            </div>
        </div>
        <div class="col-6-24" id="nav-margin"></div>
        <div class="col-6-24" id="nav-btn-cont">
            <div class="nav-btn">
                <a href="mapping.html">Next&nbsp;&gt;</a>
            </div>
        </div>
        <div class="col-3-24" id="nav-btn-margin"></div>
    </div>

    {footer}
</body>
"""

######################
# Main block
######################
pagefile = "assembly.html";
print("Generating " + pagefile + "...");
title = "ConGen2020 - Assembly Workshop"

head = RC.readHead(title);
nav = RC.readNav(pagefile);
#main = RC.readMapping();
footer = RC.readFooter();

outfilename = "../../" + pagefile;

with open(outfilename, "w") as outfile:
    outfile.write(html_template.format(head=head, nav=nav, footer=footer));