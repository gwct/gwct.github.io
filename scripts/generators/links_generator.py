############################################################
# For personal site, 11.19
# This generates the file "links.html"
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

   	<div class="row" id="header">Software & Links</div>
	<div class="row">
		<div class="col-24-24" id="sep_div"></div>
	</div>

	<div class="row" id="link-section">
		<div class="col-4-24" id="margin"></div>
		<div class="col-2-24" id="link-img-col">
			<a href="https://gwct.github.io/referee/" id="link-img-link" target="_blank">
				<img class="pure-img" id="link-img" src="img/logo/ref-link-logo.png">
			</a>
		</div>

		<div class="col-14-24" id="link-text">
				<b><a href="https://gwct.github.io/referee/" target="_blank">Reference assembly quality scores</a></b></br>
				Using genotype likelihoods from reads mapped back to an assembly, Referee assigns a quality score 
				to every position of that assembly. Developed in 
				<a href="https://doi.org/10.1093/gbe/evz088" target="_blank">Thomas and Hahn 2019</a>.
		</div>
		<div class="col-4-24" id="margin"></div>
	</div>

	<div class="row" id="link-section">
		<div class="col-4-24" id="margin"></div>
		<div class="col-2-24" id="link-img-col">
			<a href="https://gwct.github.io/grampa/" id="link-img-link" target="_blank">
				<img class="pure-img" id="link-img" src="img/logo/grampa-link-logo.png">
			</a>
		</div>

		<div class="col-14-24" id="link-text">
			<b><a href="https://gwct.github.io/grampa/" target="_blank">Gene-tree Reconciliation Algorithm with MUL-trees for Polyploid Analysis</a></b></br>
				Software to identify polyploidy events given a species tree and a set of gene trees. Can count 
				duplications and losses in the presence of polyploidy and differentiate between auto- and 
				allopolyploidy events. Developed in 
				<a href="https://doi.org/10.1093/sysbio/syx044" target="_blank">Thomas et al. 2017</a>.
		</div>
		<div class="col-4-24" id="margin"></div>
	</div>

	<div class="row" id="link-section">
		<div class="col-4-24" id="margin"></div>
		<div class="col-2-24" id="link-img-col">
			<a href="https://gwct.github.io/gwct/" id="link-img-link" target="_blank">
				<img class="pure-img" id="link-img" src="img/logo/gwct-link-logo.png">
			</a>
		</div>

		<div class="col-14-24" id="link-text">
			<b><a href="https://github.com/gwct/gwct" target="_blank">Genome-Wide Convergence Tester</a></b></br>
				These scripts and earlier versions of them were used in 
				<a href="http://dx.doi.org/doi:10.1038/ng.3198" target="_blank">Foote et al. 2015</a>, 
				<a href="http://dx.doi.org/10.1093/molbev/msv013" target="_blank">Thomas and Hahn 2015</a>, 
				and <a href="http://dx.doi.org/10.1093/gbe/evw306" target="_blank">Thomas et al. 2017</a> 
				to count convergent and divergent substitutions in a phylogeny.
		</div>
		<div class="col-4-24" id="margin"></div>
	</div>

	<div class="row" id="link-section">
		<div class="col-4-24" id="margin"></div>
		<div class="col-2-24" id="link-img-col">
			<a href="https://gwct.github.io/core/" id="link-img-link" target="_blank">
				<img class="pure-img" id="link-img" src="img/logo/core-link-logo-2.png">
			</a>
		</div>

		<div class="col-14-24" id="link-text">
			<b><a href="https://github.com/gwct/core" target="_blank">COde for Romps in Evolutionary data</a></b></br>
				My personal scripts and libraries for manipulating sequence data, phylogenetic trees, and other things.
		</div>
		<div class="col-4-24" id="margin"></div>
	</div>

	<div class="row" id="section-header-row">
		<div class="col-2-24" id="margin"></div>
		<div class="col-20-24" id="section_header">Software I have contributed to</div>
		<div class="col-2-24" id="margin"></div>
	</div>

	<div class="row" id="link-section">
		<div class="col-4-24" id="margin"></div>
		<div class="col-2-24" id="link-img-col">
			<a href="https://hahnlab.github.io/CAFE/" id="link-img-link" target="_blank">
				<img class="pure-img" id="link-img" src="img/logo/cafe-link-logo.png">
			</a>
		</div>

		<div class="col-14-24" id="link-text">
			<b><a href="https://hahnlab.github.io/CAFE/" target="_blank">Computational Analysis of Gene Family Evolution</a></b></br>	
				Software developed in the Hahn lab to estimate rates of gene family evolution and 
				reconstruct ancestral gene counts.
		</div>
		<div class="col-4-24" id="margin"></div>
	</div>

	<div class="row" id="section-header-row">
		<div class="col-2-24" id="margin"></div>
		<div class="col-20-24" id="section_header">Project resources</div>
		<div class="col-2-24" id="margin"></div>
	</div>

	<div class="row" id="link-section">
		<div class="col-4-24" id="margin"></div>
		<div class="col-2-24" id="link-img-col">
			<a href="https://arthrofam.org" id="link-img-link" target="_blank">
				<img class="pure-img" id="link-img" src="img/logo/i5k-link-logo.png">
			</a>
		</div>

		<div class="col-14-24" id="link-text">
			<b><a href="https://arthrofam.org" target="_blank">ArthroFam.org</a></b></br>
				A website I built to browse phylogenetic, gene family, and protein domain results of 76 arthropod species as part of the 
				<a href="https://doi.org/10.1101/382945" target="_blank" id="doi_link">i5K pilot project</a>.
		</div>
		<div class="col-4-24" id="margin"></div>
	</div>

	<div class="row" id="link-section">
		<div class="col-4-24" id="margin"></div>
		<div class="col-2-24" id="link-img-col">
			<a href="https://github.com/gwct/macaque-cnv-figs" id="link-img-link" target="_blank">
				<img class="pure-img" id="link-img" src="img/logo/macaque-link-logo.png">
			</a>
		</div>

		<div class="col-14-24" id="link-text">
			<b><a href="https://github.com/gwct/macaque-cnv-figs" target="_blank">Macaque CNVs</a></b></br>
				Code and data used to produce the figures in our rhesus macaque CNV 
				<a href="https://doi.org/10.1101/749416" target="_blank" id="doi_link">paper</a>.
		</div>
		<div class="col-4-24" id="margin"></div>
	</div>

	<div class="row" id="link-section">
		<div class="col-4-24" id="margin"></div>
		<div class="col-2-24" id="link-img-col">
			<a href="https://gwct.github.io/owl-monkey/" id="link-img-link" target="_blank">
				<img class="pure-img" id="link-img" src="img/logo/om-link-logo.png">
			</a>
		</div>

		<div class="col-14-24" id="link-text">
			<b><a href="https://gwct.github.io/owl-monkey/" target="_blank">Owl monkey mutations</a> - 
				<a href="https://github.com/gwct/owl-monkey" target="_blank">Github</a></b></br>
				A markdown document to accompany our <a href="https://doi.org/10.1101/382945" target="_blank" id="doi_link">paper</a> 
				on mutation rates in owl monkeys. Goes through our analyses and provides code for reproducible figures.
		</div>
		<div class="col-4-24" id="margin"></div>
	</div>

	<div class="row" id="link-section">
		<div class="col-4-24" id="margin"></div>
		<div class="col-2-24" id="link-img-col">
			<a href="http://dx.doi.org/10.6084/m9.figshare.5450602" id="link-img-link" target="_blank">
				<img class="pure-img" id="link-img" src="img/logo/drosophila-link-logo.png">
			</a>
		</div>

		<div class="col-14-24" id="link-text">
			<b><a href="http://dx.doi.org/10.6084/m9.figshare.5450602" target="_blank">Drosophila 25 species phylogeny</a></b></br>
				A FigShare micro-publication of the 25 species Drosophila phylogeny 
				that was used to study gene families across the genus, in particular 
				<a href="https://doi.org/10.1186/s12862-019-1364-9" target="_blank" id="doi_link">salivary glue genes</a>.
		</div>
		<div class="col-4-24" id="margin"></div>
	</div>

	<div class="row" id="link-section">
		<div class="col-4-24" id="margin"></div>
		<div class="col-2-24" id="link-img-col">
			<a href="https://cafe-portal.gitlab.io/bop/" id="link-img-link" target="_blank">
				<img class="pure-img" id="link-img" src="img/logo/bop-link-logo.png">
			</a>
		</div>

		<div class="col-14-24" id="link-text">
			<b><a href="https://cafe-portal.gitlab.io/bop/" target="_blank">Birds-of-paradise gene families</a></b></br>
				Results of gene family analyses in several species of birds-of-paradise. 
				<a href="https://doi.org/10.1093/gigascience/giz003" target="_blank" id="doi_link">Paper</a>.
		</div>
		<div class="col-4-24" id="margin"></div>
	</div>		

	<div class="row" id="section-header-row">
		<div class="col-2-24" id="margin"></div>
		<div class="col-20-24" id="section_header">People</div>
		<div class="col-2-24" id="margin"></div>
	</div>

	<div class="row" id="link-section">
		<div class="col-4-24" id="margin"></div>
		<div class="col-2-24" id="link-img-col">
			<a href="http://www.thegoodlab.org/" id="link-img-link" target="_blank">
				<img class="pure-img" id="link-img" src="img/logo/good-link-logo.png">
			</a>
		</div>

		<div class="col-14-24" id="link-text">
			<b><a href="http://www.thegoodlab.org/" target="_blank">Good lab</a></b></br>
				My postdoc advisor.
		</div>
		<div class="col-4-24" id="margin"></div>
	</div>		

	<div class="row" id="link-section">
		<div class="col-4-24" id="margin"></div>
		<div class="col-2-24" id="link-img-col">
			<a href="http://www.indiana.edu/~hahnlab/" id="link-img-link" target="_blank">
				<img class="pure-img" id="link-img" src="img/logo/mwh-link-logo.png">
			</a>
		</div>

		<div class="col-14-24" id="link-text">
			<b><a href="http://www.indiana.edu/~hahnlab/" target="_blank">Hahn lab</a></b></br>
				My PhD advisor.
		</div>
		<div class="col-4-24" id="margin"></div>
	</div>	

	<div class="row" id="section-header-row">
		<div class="col-2-24" id="margin"></div>
		<div class="col-20-24" id="section_header">Helpful software from others</div>
		<div class="col-2-24" id="margin"></div>
	</div>

	<div class="row other_link_row">
		<div class="col-4-24 other_link_margin" id="margin"></div>
		<div class="col-2-24 other_link"><a href="https://blast.ncbi.nlm.nih.gov/Blast.cgi?PAGE_TYPE=BlastDocs&DOC_TYPE=Download" target="_blank">BLAST</a></div>
		<div class="col-2-24 other_link"><a href="http://micans.org/mcl/" target="_blank">MCL</a></div>
		<div class="col-2-24 other_link"><a href="http://www.drive5.com/muscle/" target="_blank">MUSCLE</a></div>
		<div class="col-2-24 other_link"><a href="https://github.com/smirarab/pasta" target="_blank">PASTA</a></div>
		<div class="col-2-24 other_link"><a href="http://wasabiapp.org/software/prank/" target="_blank">PRANK</a></div>
		<div class="col-2-24 other_link"><a href="https://bioweb.supagro.inra.fr/macse/" target="_blank">MACSE</a></div>
		<div class="col-2-24 other_link"><a href="http://sco.h-its.org/exelixis/software.html" target="_blank">RAxML</a></div>
		<div class="col-2-24 other_link"><a href="http://www.iqtree.org/" target="_blank">IQ-Tree</a></div>
		<div class="col-4-24 other_link_margin" id="margin"></div>
	</div>
	<div class="row other_link_row">
		<div class="col-4-24 other_link_margin" id="margin"></div>
		<div class="col-2-24 other_link"><a href="https://github.com/smirarab/ASTRAL" target="_blank">ASTRAL</a></div>
		<div class="col-2-24 other_link"><a href="https://sourceforge.net/projects/r8s/" target="_blank">r8s</a></div>
		<div class="col-2-24 other_link"><a href="http://cegg.unige.ch/newick_utils" target="_blank">Newick Utilities</a></div>
		<div class="col-2-24 other_link"><a href="http://doua.prabi.fr/software/seaview" target="_blank">SeaView</a></div>
		<div class="col-2-24 other_link"><a href="http://tree.bio.ed.ac.uk/software/figtree/" target="_blank">FigTree</a></div>
		<div class="col-2-24 other_link"><a href="https://guangchuangyu.github.io/software/ggtree/" target="_blank">ggtree</a></div>
		<div class="col-2-24 other_link"><a href="http://abacus.gene.ucl.ac.uk/software/paml.html" target="_blank">PAML</a></div>
		<div class="col-2-24 other_link"><a href="http://www.cs.cmu.edu/~durand/Notung/" target="_blank">Notung</a></div>
		<div class="col-4-24 other_link_margin" id="margin"></div>
	</div>
	<div class="row other_link_row">
		<div class="col-4-24 other_link_margin" id="margin"></div>
		<div class="col-2-24 other_link"><a href="https://github.com/arvestad/jprime" target="_blank">JPrIME</a></div>
		<div class="col-2-24 other_link"><a href="https://github.com/lh3/bwa" target="_blank">BWA</a></div>
		<div class="col-2-24 other_link"><a href="https://broadinstitute.github.io/picard/" target="_blank">Picard</a></div>
		<div class="col-2-24 other_link"><a href="http://www.htslib.org/" target="_blank">Samtools</a></div>
		<div class="col-2-24 other_link"><a href="http://www.popgen.dk/angsd/index.php/ANGSD" target="_blank">ANGSD</a></div>
		<div class="col-2-24 other_link"><a href="https://software.broadinstitute.org/gatk/" target="_blank">GATK</a></div>
		<div class="col-2-24 other_link"><a href="https://github.com/arq5x/lumpy-sv" target="_blank">Lumpy</a></div>
		<div class="col-2-24 other_link"><a href="https://github.com/hall-lab/svtyper" target="_blank">SVTyper</a></div>
		<div class="col-4-24 other_link_margin" id="margin"></div>
	</div>		

    {links}

    {footer}
</body>
"""

######################
# Main block
######################
pagefile = "links.html";
print("Generating " + pagefile + "...");
title = "Gregg Thomas - Links"

head = RC.readHead(title, pagefile);
nav = RC.readNav(pagefile);
links = RC.readLinks();
footer = RC.readFooter();

outfilename = "../../" + pagefile;

with open(outfilename, "w") as outfile:
    outfile.write(html_template.format(head=head, nav=nav, links=links, footer=footer));