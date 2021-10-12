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

   	<div class="row" id="header">Links</div>
	<div class="row">
		<div class="col-24-24" id="sep_div"></div>
	</div>

	<div class="row" id="section-header-row">
		<div class="col-2-24" id="margin"></div>
		<div class="col-20-24" id="section_header">People</div>
		<div class="col-2-24" id="margin"></div>
	</div>

		<div class="row" id="link-section">
			<div class="col-4-24" id="margin"></div>
			<div class="col-2-24" id="link-img-col">
				<!-- <a href="http://www.thegoodlab.org/" id="link-img-link" target="_blank">
					<img class="pure-img" id="link-img" src="img/logo/good-link-logo.png">
				</a> -->
			</div>

			<div class="col-14-24" id="link-text">
				<b><a href="https://labs.wsu.edu/genomes/" target="_blank">Kelley lab</a></b></br>
					My postdoc advisor.
			</div>
			<div class="col-4-24" id="margin"></div>
		</div>

		<div class="row" id="link-section">
			<div class="col-4-24" id="margin"></div>
			<div class="col-2-24" id="link-img-col">
				<!-- <a href="http://www.thegoodlab.org/" id="link-img-link" target="_blank">
					<img class="pure-img" id="link-img" src="img/logo/good-link-logo.png">
				</a> -->
			</div>

			<div class="col-14-24" id="link-text">
				<b><a href="https://hadlylab.stanford.edu/" target="_blank">Hadly lab</a></b></br>
					One of my PhD advisors.
			</div>
			<div class="col-4-24" id="margin"></div>
		</div>

		<div class="row" id="link-section">
			<div class="col-4-24" id="margin"></div>
			<div class="col-2-24" id="link-img-col">
				<!-- <a href="http://www.thegoodlab.org/" id="link-img-link" target="_blank">
					<img class="pure-img" id="link-img" src="img/logo/good-link-logo.png">
				</a> -->
			</div>

			<div class="col-14-24" id="link-text">
				<b><a href="http://petrov.stanford.edu/" target="_blank">Petrov lab</a></b></br>
					One of my PhD advisors.
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
title = "Ellie Armstrong - Links"

head = RC.readHead(title, pagefile);
nav = RC.readNav(pagefile);
links = RC.readLinks();
footer = RC.readFooter();

outfilename = "../../" + pagefile;

with open(outfilename, "w") as outfile:
    outfile.write(html_template.format(head=head, nav=nav, links=links, footer=footer));