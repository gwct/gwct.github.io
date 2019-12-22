############################################################
# For personal site, 11.19
# This generates the file "research.html"
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

    <div class="pure-g" id="main_div_res">
        <div class="pure-u-24-24" id="header">Research</div>

        <div class="pure-u-2-24" id="margin"></div>
        <div class="pure-u-20-24 section_header_cont"><h1><div class="section_header">Mutation rate variation</div></h1></div>
        <div class="pure-u-2-24" id="margin"></div>

        <div class="pure-u-2-24" id="margin"></div>
        <div class="pure-u-10-24" id="research_text">
            <p align="justify">Mutations play a key role in disease and in the long-term evolution of populations. That means the rate at which mutations
                    arise can have big impacts on both an individual and a species. Mutation rates have been shown to vary between species and
                    even within species depending on the genomic context of the mutation and the age of the sample. I'm interested in what causes
                    this variation and what we can learn about rates of substitution between species by studying it.</p>		
        </div>
        <div class="pure-u-2-24" id="margin"></div>
        <div class="pure-u-8-24" id="research_pic_container">
            <div id="research_pic_1"></div>
        </div>
        <div class="pure-u-2-24" id="margin"></div>

        <div class="pure-u-24-24" id="sep_div"></div>

        <div class="pure-u-2-24" id="margin"></div>
        <div class="pure-u-20-24 section_header_cont"><h1><div class="section_header">Molecular convergence</div></h1></div>
        <div class="pure-u-2-24" id="margin"></div>

        <div class="pure-u-2-24" id="margin"></div>
        <div class="pure-u-10-24" id="research_text">
            <p align="justify">Convergent evolution occurs when distantly related lineages evolve to share the same trait. A general assumption is that
                    for a trait to converge in multiple lineages, it must be adaptive. That means convergent evolution provides a great opportunity
                    to study adaptation. Until recently, convergent	evolution was only observed at the phenotypic level (i.e. the defensive quills
                    on the porcupine, echidna, and hedgehog). But with whole genome sequences available for many species we can now study convergent evolution
                    at the molecular level and ask whether it can be linked to convergence at the phenotypic level. However, we've discovered that
                    convergent amino acid substitutions occur all the time by chance in nature. This makes it difficult to pick out which convergent
                    changes are actually special. I've done work in this area to develop methods to detect molecular convergence while avoiding many
                    pitfalls that come from high levels of background convergence.</p>		
        </div>
        <div class="pure-u-2-24" id="margin"></div>
        <div class="pure-u-8-24" id="research_pic_container">
            <div id="research_pic_2"></div>
        </div>
        <div class="pure-u-2-24" id="margin"></div>

        <div class="pure-u-24-24" id="sep_div"></div>

        <div class="pure-u-2-24" id="margin"></div>
        <div class="pure-u-20-24 section_header_cont"><h1><div class="section_header">Gene family evolution</div></h1></div>
        <div class="pure-u-2-24" id="margin"></div>

        <div class="pure-u-2-24" id="margin"></div>
        <div class="pure-u-10-24" id="research_text">	
            <p align="justify">Another type of mutation is deletion or duplication of long stretches of DNA. This can lead to gene duplication
                    or loss which can play a key role in the functional evolution between species. I have helped develop the latest version of 
                    <a href="https://hahnlab.github.io/CAFE/" target="_blank">CAFE</a> by devising a method to estimate annotation and assembly 
                    error for gene count data. I have also delved into the study of whole genome duplications by developing a method to properly
                    identify and place polyploidization events on phylogeny. This method has been implemented in the software 
                    <a href="https://gwct.github.io/grampa" target="_blank">GRAMPA</a>. Finally, I led the phylogenetic and gene family analysis for the 
                    <a href="http://i5k.github.io/" target="_blank">i5K</a> pilot project. This is the largest gene family analysis to date 
                    and yielded a wealth of information as a resource for Arthropod researchers.</p>		
        </div>
        <div class="pure-u-2-24" id="margin"></div>
        <div class="pure-u-8-24" id="research_pic_container">
            <div id="research_pic_3"></div>
        </div>
        <div class="pure-u-2-24" id="margin"></div>

		<div class="pure-u-24-24" id="sep_div"></div>

		<div class="pure-u-6-24" id="margin"></div>	
        {links}
        <div class="pure-u-6-24" id="margin"></div>
    </div>

    {footer}
</body>
"""

######################
# Main block
######################
pagefile = "research.html";
print("Generating " + pagefile + "...");
title = "Gregg Thomas - Research"

head = RC.readHead(title, pagefile);
nav = RC.readNav(pagefile);
links = RC.readLinks();
footer = RC.readFooter();

outfilename = "../../" + pagefile;

with open(outfilename, "w") as outfile:
    outfile.write(html_template.format(head=head, nav=nav, links=links, footer=footer));