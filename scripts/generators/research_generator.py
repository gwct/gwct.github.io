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
		<div class="pure-u-20-24" id="res_text">
            <!-- <div class="pure-u-2-24" id="margin"></div> -->
            <div id="res_intro_cont">
                <p id="res_intro">
                    My main research interests center around how changes in DNA sequences play a role in adapation. Molecular evolution 
                    &mdash; the changes that accrue in the DNA sequence of a population or species over time &mdash; can be driven by many 
                    factors, including evolution of the mutation rate, natural selection, and life history variation between 
                    species. Additionally, false inferences of molecular change can be caused by systematic error in the genome 
                    sequencing and comparative pipelines, and unaccounted phylogenetic discordance. Using phylogenetics and 
                    comparative genomics, I am interested in studying adaptation by identifying general patterns of molecular 
                    evolution and specific links between molecular changes and phenotypes. In the process, I develop 
                    <a href="links.html" style="color:#FF994B;">software</a> 
                    to solve specific problems and to help account for systematic errors through the genomic workflow.

                    Below I outline some of the specific ways I have pursued these goals up to this point!
                </p>
            </div>
            
            <div class="section_header_cont"><div class="section_header">Mutation rate variation</div></div>
            <div class="pure-g">
                <div class="pure-u-2-24" id="margin"></div>
                <div class="pure-u-20-24" id="res_row">
                    <div id="res_desc">
                        <span>
                            Mutations play a key role in disease and in the long-term evolution of populations. That 
                            means the rate at which mutations arise can have big impacts on both an individual and a 
                            species. Mutation rates have been shown to vary between species and even within species 
                            depending on the genomic context of the mutation and the age of the sample. I'm interested 
                            in what causes this variation and what we can learn about rates of substitution between 
                            species by studying it.
                        </span>
                    </div>
                    <div id="res_img_cont">
                        <img class="pure-img" id="res_img" src="img/research/fig3.png">
                    </div>
                </div>
                <div class="pure-u-2-24" id="margin"></div>
            </div>

            <div class="pure-u-24-24" id="sep_div"></div>

            <div class="section_header_cont"><div class="section_header">Molecular convergence</div></div>
            <div class="pure-g">
                <div class="pure-u-2-24" id="margin"></div>
                <div class="pure-u-20-24" id="res_row">
                    <div id="res_desc">
                        <span>
                            Convergent evolution occurs when distantly related lineages evolve to share the same trait. A 
                            general assumption is that for a trait to converge in multiple lineages, it must be adaptive. 
                            That means convergent evolution provides a great opportunity to study adaptation. Until 
                            recently, convergent evolution was only observed at the phenotypic level (i.e. the defensive 
                            quills on the porcupine, echidna, and hedgehog). But with whole genome sequences available for 
                            many species we can now study convergent evolution at the molecular level and ask whether it 
                            can be linked to convergence at the phenotypic level. However, we've discovered that convergent 
                            amino acid substitutions occur all the time by chance in nature. This makes it difficult to pick 
                            out which convergent changes are actually adaptive. I've done work in this area to develop 
                            methods to detect molecular convergence while avoiding many pitfalls that come from high levels 
                            of background convergence.
                        </span>
                    </div>
                    <div id="res_img_cont">
                        <img class="pure-img" id="res_img" src="img/research/conv4.png">
                    </div>
                </div>
                <div class="pure-u-2-24" id="margin"></div>
            </div>

            <div class="pure-u-24-24" id="sep_div"></div>

            <div class="section_header_cont"><div class="section_header">Gene family evolution</div></div>
            <div class="pure-g">
                <div class="pure-u-2-24" id="margin"></div>
                <div class="pure-u-20-24" id="res_row">
                    <div id="res_desc">
                        <span>
                            Gene duplications and losses can open up new avenues for adaptation by changing the selective 
                            constraints and expression levels of genes. I have helped develop the latest version of 
                            <a href="https://hahnlab.github.io/CAFE/" target="_blank">CAFE</a> by devising a method to 
                            estimate annotation and assembly error for gene count data. I have also delved into the study 
                            of whole genome duplications by developing a method to properly identify and place polyploidization 
                            events on phylogeny. This method has been implemented in the software 
                            <a href="https://gwct.github.io/grampa" target="_blank">GRAMPA</a>. Finally, I led the phylogenetic 
                            and gene family analysis for the <a href="http://i5k.github.io/" target="_blank">i5K</a> pilot 
                            project. This is the largest gene family analysis to date and yielded a wealth of information as 
                            a resource for Arthropod researchers.
                        </span>
                    </div>
                    <div id="res_img_cont">
                        <img class="pure-img" id="res_img" src="img/research/gfam3.png">
                    </div>
                </div>
                <div class="pure-u-2-24" id="margin"></div>
            </div>
        </div>

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