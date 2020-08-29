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

    <div class="row" id="section-cont">
        <div class="col-4-24" id="outer-margin"></div>
        <div class="col-16-24" id="section-col">
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
        <div class="col-4-24" id="outer-margin"></div>
    </div>    

    <a name="spades"></a>
    <div class="row" id="section-header-cont">
        <div class="col-4-24" id="outer-margin"></div>
        <div class="col-16-24" id="section-header-row">
            <div id="section-header">Assembly with short reads with <a href="https://github.com/ablab/spades/" target="_blank">SPAdes</a></div>
        </div>
        <div class="col-4-24" id="outer-margin"></div>
    </div>

    <div class="row" id="section-cont">
        <div class="col-4-24" id="outer-margin"></div>
        <div class="col-16-24" id="section-col">
            <div class="row" id="section-row">
                <div class="col-2-24" id="inner-margin"></div>
                <div class="col-20-24" id="section-content">

                   <p>Content

                </div>
                <div class="col-2-24" id="inner-margin"></div>
            </div>
        </div>
        <div class="col-4-24" id="outer-margin"></div>
    </div>

    <a name="flye"></a>
    <div class="row" id="section-header-cont">
        <div class="col-4-24" id="outer-margin"></div>
        <div class="col-16-24" id="section-header-row">
            <div id="section-header">Assembly with long reads with <a href="https://github.com/fenderglass/Flye/" target="_blank">Flye</a></div>
        </div>
        <div class="col-4-24" id="outer-margin"></div>
    </div>

    <div class="row" id="section-cont">
        <div class="col-4-24" id="outer-margin"></div>
        <div class="col-16-24" id="section-col">
            <div class="row" id="section-row">
                <div class="col-2-24" id="inner-margin"></div>
                <div class="col-20-24" id="section-content">

                   <p>Content

                </div>
                <div class="col-2-24" id="inner-margin"></div>
            </div>
        </div>
        <div class="col-4-24" id="outer-margin"></div>
    </div>

    <a name="asm-qual"></a>
    <div class="row" id="section-header-cont">
        <div class="col-4-24" id="outer-margin"></div>
        <div class="col-16-24" id="section-header-row">
            <div id="section-header">Assessing assembly quality</div>
        </div>
        <div class="col-4-24" id="outer-margin"></div>
    </div>

    <div class="row" id="section-cont">
        <div class="col-4-24" id="outer-margin"></div>
        <div class="col-16-24" id="section-col">
            <div class="row" id="section-row">
                <div class="col-2-24" id="inner-margin"></div>
                <div class="col-20-24" id="section-content">

                   <p>Content

                </div>
                <div class="col-2-24" id="inner-margin"></div>
            </div>
        </div>
        <div class="col-4-24" id="outer-margin"></div>
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