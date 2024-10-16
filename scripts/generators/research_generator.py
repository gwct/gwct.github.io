############################################################
# For personal site, 11.19
# This generates the file "research.html"
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

    <div class="row" id="header">Research</div>

    <div class="row" id="reasearch-intro-row">
        <div class="col-2-24" id="margin"></div>
        <div class="col-20-24">
            <div id="res-intro-cont">
                <p id="res-intro">
                    My main research interests center around how changes in DNA sequences play a role in adaptation. Molecular evolution 
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

                <p id="res-intro">
                    As I strive for high quality and reproducible research on my own, I also want to pass on what I learn by teaching best practices 
                    in bioinformatics, encompassing data science skills, programming and software development, and computational scientific communication. 
                    I develop courses and <a href="copngen-2021/bioinformatics/" style="color:#FF994B;">workshops</a> to try to convey these concepts to biologists at any 
                    computational skill level, with an emphasis on access and equity. It is my hope that in teaching these skills, students and those 
                    that I mentor can make the most of them in their own research. Many of the underlying skills in bioinformatics are widely applicable 
                    to data science, giving students the ability to translate these skills into many possible domains and career paths.
                </p>
            </div>
        </div>
        <div class="col-2-24" id="margin"></div>
    </div>

    <div class="row" id="section-header-row">
        <div class="col-2-24" id="margin"></div>
        <div class="col-20-24" id="section_header">Mutation rate variation</div>
        <div class="col-2-24" id="margin"></div>
    </div>

    <div class="row" id="res-section">
        <div class="col-4-24" id="margin"></div>
        <div class="col-8-24" id="res-text">
            Mutations play a key role in disease and in the long-term evolution of populations. That 
            means the rate at which mutations arise can have big impacts on both an individual and a 
            species. Mutation rates have been shown to vary between species and even within species 
            depending on the genomic context of the mutation and the age of the sample. I'm interested 
            in what causes this variation and what we can learn about rates of substitution between 
            species by studying it.
        </div>
        <div class="col-8-24" id="res-img-col">
            <img id="res-img" src="img/research/fig3.png">
        </div>
        <div class="col-4-24" id="margin"></div>
    </div>

    <div class="row">
		<div class="col-24-24" id="sep_div"></div>
	</div>

    <div class="row" id="section-header-row">
        <div class="col-2-24" id="margin"></div>
        <div class="col-20-24" id="section_header">Comparative genomics</div>
        <div class="col-2-24" id="margin"></div>
    </div>
    
    <div class="row" id="res-section">
        <div class="col-4-24" id="margin"></div>
        <div class="col-8-24" id="res-text">
            Comparing genomes between related species in the context of their phylogeny provides us the opportunity
            to ask and answer questions about how these species evolved at the molecular level. Using comparative genomics
            we can study patterns such as substitution rate variation, convergent molecular evolution (right, bottom), gene family
            evolution (see below), gene expression and much more. I aim to uncover these patterns across the tree of
            life. I have done large-scale comparative studies in primates and insects, and I am now working on similar studies
            in rodents and turtles. And I am working on software to account for reference bias in read mapping.
            
            <div class="row" id="section-header-row">
                <div class="col-24-24" id="res-sub-header">Convergent evolution</div>
            </div>

            <div class="row" id="res-sub-section">
                <div class="col-24-24" id="res-text">           
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
                </div>
            </div>
            
            <div class="row" id="section-header-row">
                <div class="col-24-24" id="res-sub-header">Gene family evolution</div>
            </div>

            <div class="row" id="res-sub-section">
                <div class="col-24-24" id="res-text">
                    Gene duplications and losses can open up new avenues for adaptation by changing the selective 
                    constraints and expression levels of genes. I have helped develop the latest version of 
                    <a href="https://hahnlab.github.io/CAFE/" target="_blank">CAFE</a> by devising a method to 
                    estimate annotation and assembly error for gene count data. I have also delved into the study 
                    of whole genome duplications by developing a method to properly identify and place polyploidization 
                    events on phylogeny. This method has been implemented in the software 
                    <a href="https://gwct.github.io/grampa" target="_blank">GRAMPA</a>. Finally, I led the phylogenetic 
                    and gene family analysis for the <a href="http://i5k.github.io/" target="_blank">i5K</a> 
                    pilot project (right, top). This is the largest gene family analysis to date and yielded a wealth of information as 
                    a resource for Arthropod researchers.
                </div>
            </div>

            <div class="row" id="section-header-row">
                <div class="col-24-24" id="res-sub-header">Phylogenetic discordance</div>
            </div>

            <div class="row" id="res-sub-section">
                <div class="col-24-24" id="res-text">
                    A large part of comparative genomics is phylogenetics. Besides uncovering the relationships among species,
                    the phylogeny provides the framework for us to ask and answer many of the interesting biological questions 
                    in comparative datasets. I am interested in studying patterns of phylogenetic discordance over time and 
                    across the genome and developing methods to account for it in comparative analyses. Specifically, in recent 
                    work we have found that phylogenies inferred from windows along the genome are more similar the closer they are. 
                    This discordance poses problems when inferring changes on a single species tree: if the underlying data do not follow 
                    that tree, evolutionary events will be mismapped. To account for this in comparative studies,  I am developing methods to prune 
                    large phylogenies to maxmize their concordance with underlying gene trees, estimate substitution rates more accurately
                     on a species tree, and estimating substitution rates in a Bayesian framework while accounting for discordance.
                </div>
            </div>

        </div>
        <div class="col-8-24" id="res-img-col">
            <div class="row" id="res-img-row">
                <div class="col-24-24" id="res-img-cont">
                    <img id="res-img-i5k" src="img/research/i5k1.png">
                </div>
                <div class="col-24-24" id="res-img-sep"></div>
                <div class="col-24-24" id="res-img-cont">
                    <img id="res-img" src="img/research/conv4.png">
                </div>
                <!--
                <div class="col-24-24" id="res-img-sep"></div>
                <div class="col-24-24" id="res-img-cont">
                    <img id="res-img" src="img/research/gfam3.png">
                </div>
                -->
            </div>
        </div>
        <div class="col-4-24" id="margin"></div>
    </div>

    <div class="row">
		<div class="col-24-24" id="sep_div"></div>
	</div>

    {links}

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