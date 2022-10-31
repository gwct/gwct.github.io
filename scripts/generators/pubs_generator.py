############################################################
# For personal site, 11.19
# This generates the file "pubs.html"
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

	<a class="internal-link" name="pubs"></a>
    <div class="row" id="header">Publications</div>

	<!--
    <div class="row" id="section-header-row">
        <div class="col-2-24" id="margin"></div>
        <div class="col-20-24" id="section_header">Pre-prints</div>
        <div class="col-2-24" id="margin"></div>
	</div>
	<div class="row" id="pub-row"></div>
	<div class="col-2-24" id="margin"></div>
	<div class="col-20-24" id="pub">
		<ul id="presents">
			<p>
				<span class="pub_title">The evolution of widespread recombination suppression on the Dwarf Hamster (<em>Phodopus</em>) X chromosome</span>
				</br>&nbsp;&nbsp;Moore EC, <b>Thomas GWC</b>, Mortimer S, Kopania EEK, Hunnicut KE, Clare-Salzer ZJ, Larson EL, Good JM. 
				2022.
				<em>bioRxiv</em>.
				</br>&nbsp;&nbsp;doi: <a href="https://doi.org/10.1101/2021.11.15.468705" target="_blank" id="doi_link">10.1101/2021.11.15.468705</a>
			</p>
		</ul>
	</div>
	<div class="col-2-24" id="margin"></div>
	-->

    <div class="row" id="section-header-row">
        <div class="col-2-24" id="margin"></div>
        <div class="col-20-24" id="section_header">2022</div>
        <div class="col-2-24" id="margin"></div>
	</div>
	<div class="row" id="pub-row"></div>
	<div class="col-2-24" id="margin"></div>
	<div class="col-20-24" id="pub">
		<ul id="presents">
			<p>
				<span class="pub_title">The evolution of widespread recombination suppression on the Dwarf Hamster (<em>Phodopus</em>) X chromosome</span>
				</br>&nbsp;&nbsp;Moore EC, <b>Thomas GWC</b>, Mortimer S, Kopania EEK, Hunnicut KE, Clare-Salzer ZJ, Larson EL, Good JM. 
				2022.
				<em>Genome Biology & Evolution</em>.
				14(6):evac080.
				</br>&nbsp;&nbsp;doi: <a href="https://doi.org/10.1093/gbe/evac080" target="_blank" id="doi_link">10.1093/gbe/evac080</a>
			</p>
		</ul>
	</div>
	<div class="col-2-24" id="margin"></div>

    <div class="row" id="section-header-row">
        <div class="col-2-24" id="margin"></div>
        <div class="col-20-24" id="section_header">2021</div>
        <div class="col-2-24" id="margin"></div>
	</div>
	<div class="row" id="pub-row"></div>
	<div class="col-2-24" id="margin"></div>
	<div class="col-20-24" id="pub">
		<ul id="presents">
			<p>
				<span class="pub_title">Origins and long-term patterns of copy-number variation in rhesus macaques</span>
				</br>&nbsp;&nbsp;<b>Thomas GWC</b>, Wang RJ, Nguyen J, Harris RA, Raveendran M, Rogers J, Hahn MW. 
				2021. 
				<em>Molecular Biology & Evolution</em>.
				38(4):1460-1471.
				</br>&nbsp;&nbsp;doi: <a href="https://doi.org/10.1093/molbev/msaa303" target="_blank" id="doi_link">10.1093/molbev/msaa303</a>
				</br>&nbsp;&nbsp;Resources: <a href="https://github.com/gwct/macaque-cnv-figs" target="_blank">Figures</a>
			</p>

			<p>
				<span class="pub_title">Genus-wide characterization of bumblebee genomes reveals variation associated with key ecological and behavioral traits of pollinators</span>
				</br>&nbsp;&nbsp;Sun C, Huang J, ... <b>Thomas GWC</b>, ..., Hahn MW, ..., Mueller RL. 
				2021. 
				<em>Molecular Biology & Evolution</em>.
				38(2):486-501.
				</br>&nbsp;&nbsp;doi: <a href="https://doi.org/10.1093/molbev/msaa240 " target="_blank" id="doi_link">10.1093/molbev/msaa240</a>
			</p>
		</ul>
	</div>
	<div class="col-2-24" id="margin"></div>

    <div class="row" id="section-header-row">
        <div class="col-2-24" id="margin"></div>
        <div class="col-20-24" id="section_header">2020</div>
        <div class="col-2-24" id="margin"></div>
	</div>
	<div class="row" id="pub-row"></div>
	<div class="col-2-24" id="margin"></div>
	<div class="col-20-24" id="pub">
		<ul id="presents">
			<p>
				<span class="pub_title">Paternal age in rhesus macaques is positively associated with germline mutation accumulation but not with measures of offspring sociability</span>
				</br>&nbsp;&nbsp;Wang RJ, <b>Thomas GWC</b>, Raveendran M, Harris RA, Doddapaneni H, Muzny DM, Capitanio JP, Radivojac P, Rogers J, Hahn MW. 
				2020.
				<em>Genome Research</em>. 
				30:826-834.
				</br>&nbsp;&nbsp;doi: <a href="https://doi.org/10.1101/gr.255174.119" target="_blank" id="doi_link">10.1101/gr.255174.119</a>
			</p>

			<p>
				<span class="pub_title">Gene content evolution in the arthropods</span>
				<!-- <p><span class="pub_title">The genomic basis of Arthropod diversity</span> -->
				</br>&nbsp;&nbsp;<b>Thomas GWC</b>, Dohmen E, Hughes DST, Murali SC, Poelchau M, Glastad K, The i5K Phylogenomics Consortium,
					</br>&nbsp;&nbsp;Chipman AD, Waterhouse RM, Bornberg-Bauer E, Hahn MW, Richards S. 
				2020. 
				<em>Genome Biology</em>. 
				21(15). 
				</br>&nbsp;&nbsp;doi: <a href="https://doi.org/10.1186/s13059-019-1925-7" target="_blank" id="doi_link">10.1186/s13059-019-1925-7</a>
				</br>&nbsp;&nbsp;Resources: <a href="https://arthrofam.org" target="_blank">ArthroFam website</a>
			</p>
		</ul>
	</div>
	<div class="col-2-24" id="margin"></div>

    <div class="row" id="section-header-row">
        <div class="col-2-24" id="margin"></div>
        <div class="col-20-24" id="section_header">2019</div>
        <div class="col-2-24" id="margin"></div>
	</div>
	<div class="row" id="pub-row"></div>
	<div class="col-2-24" id="margin"></div>
	<div class="col-20-24" id="pub">
		<ul id="presents">
			<p>
				<span class="pub_title">Tissue-specific expression profiles and positive selection analysis in the tree swallow (<em>Tachycineta bicolor</em>) using a <em>de novo</em> transcriptome assembly</span>
				</br>&nbsp;&nbsp;Bentz AB, <b>Thomas GWC</b>, Rusch DB, Rosvall KA. 
				2019. 
				<em>Scientific Reports</em>. 
				9:15849.
				</br>&nbsp;&nbsp;doi: <a href="https://doi.org/10.1038/s41598-019-52312-4" target="_blank" id="doi_link">10.1038/s41598-019-52312-4</a>
			</p>

			<p>
				<span class="pub_title">Referee: reference genome quality scores</span>
				</br>&nbsp;&nbsp;<b>Thomas GWC</b> and Hahn MW. 2019. 
				<em>Genome Biology and Evolution</em>. 
				11(5):1483-1486.
				</br>&nbsp;&nbsp;doi: <a href="https://doi.org/10.1093/gbe/evz088" target="_blank" id="doi_link">10.1093/gbe/evz088</a>
				</br>&nbsp;&nbsp;Software: <a href="https://gwct.github.io/referee" target="_blank">Referee</a>
			</p>

			<p>
				<span class="pub_title">The comparative genomics and complex population history of <em>Papio</em> baboons</span>
				</br>&nbsp;&nbsp;Rogers J, <b>The Baboon Genome Analysis Consortium</b>. 
				2019. 
				<em>Science Advances</em>. 
				5(1).
				</br>&nbsp;&nbsp;doi: <a href="https://doi.org/10.1126/sciadv.aau6947" target="_blank" id="doi_link">10.1126/sciadv.aau6947</a>
			</p>

			<p>
				<span class="pub_title">Evolution of salivary glue genes in Drosophila species</span>
				</br>&nbsp;&nbsp;Da Lage JL, <b>Thomas GWC</b>, Bonneau M, Courtier-Orgogozo V. 
				2019. 
				<em>BMC Evolutionary Biology</em>. 
				19(36).
				</br>&nbsp;&nbsp;doi: <a href="https://doi.org/10.1186/s12862-019-1364-9" target="_blank" id="doi_link">10.1186/s12862-019-1364-9</a>
				</br>&nbsp;&nbsp;Resources: <a href="http://dx.doi.org/10.6084/m9.figshare.5450602" target="_blank">FigShare Drosophila 25 species phylogeny</a>
			</p>

			<p>
				<span class="pub_title">Comparative analyses identify genomic features potentially involved in the evolution of birds-of-paradise</span>
				</br>&nbsp;&nbsp;Prost S, Armstrong EE, Nylander J, <b>Thomas GWC</b>, Suh A, Petersen B, Dalen L, Benz BW, Blom MPK,
					</br>&nbsp;&nbsp;Palkopoulou E, Ericson PGP, Irestedt M. 
				2019. 
				<em>GigaScience</em>. 8(5). 
				</br>&nbsp;&nbsp;doi: <a href="https://doi.org/10.1093/gigascience/giz003" target="_blank" id="doi_link">10.1093/gigascience/giz003</a>
				</br>&nbsp;&nbsp;Resources: <a href="https://cafe-portal.gitlab.io/bop/" target="_blank">Website</a>
			</p>
		</ul>
	</div>
	<div class="col-2-24" id="margin"></div>

	<div class="row" id="section-header-row">
        <div class="col-2-24" id="margin"></div>
        <div class="col-20-24" id="section_header">2018</div>
        <div class="col-2-24" id="margin"></div>
	</div>
	<div class="row" id="pub-row"></div>
	<div class="col-2-24" id="margin"></div>
	<div class="col-20-24" id="pub">
		<ul id="presents">
			<p>
				<span class="pub_title">Reproductive longevity predicts mutation rates in primates</span>
				</br>&nbsp;&nbsp;<b>Thomas GWC</b>, Wang RJ, Puri A, Harris RA, Raveendran M, Hughes DST, Murali SC, Williams LE,
					</br>&nbsp;&nbsp;Doddapaneni H, Muzny DM, Gibbs RA, Abee CR, Galinski MR, Worley KC, Rogers J, Radivojac P, Hahn MW. 
				2018. 
				<em>Current Biology</em>. 
				28(19):3193-3197. 
				</br>&nbsp;&nbsp;doi: <a href="https://doi.org/10.1016/j.cub.2018.08.050" target="_blank" id="doi_link">10.1016/j.cub.2018.08.050</a>
				</br>&nbsp;&nbsp;Resources: <a href="https://gwct.github.io/owl-monkey/" target="_blank">Website</a> / <a href="https://github.com/gwct/owl-monkey" target="_blank">Github repo</a>
			</p>

			<p>
				<span class="pub_title">Clonal polymorphism and high heterozygosity in the celibate genome of the Amazon molly</span>
				</br>&nbsp;&nbsp;Warren WC, García-Pérez R, ..., <b>Thomas GWC</b>, ..., Hahn MW, ..., Schartl M. 
				2018. 
				<em>Nature Ecology and Evolution</em>. 
				2:669–679.
				</br>&nbsp;&nbsp;doi: <a href="https://doi.org/10.1038/s41559-018-0473-y" target="_blank" id="doi_link">10.1038/s41559-018-0473-y</a>
			</p>

			<p>
				<span class="pub_title">A model species for agricultural pest genomics: the genome of the Colorado potato beetle, <em>Leptinotarsa decemlineata</em> (Coleoptera: Chrysomelidae)</span>
				</br>&nbsp;&nbsp;Schoville SD, Chen YH, ..., <b>Thomas GWC</b>, ..., Richards S. 
				2018. 
				<em>Scientific Reports</em>. 
				8(1931).
				</br>&nbsp;&nbsp;doi: <a href="https://doi.org/10.1038/s41598-018-20154-1" target="_blank" id="doi_link">10.1038/s41598-018-20154-1</a>
			</p>

			<p>
				<span class="pub_title">Sooty mangabey genome sequence provides insight into AIDS resistance in a natural SIV host</span>
				</br>&nbsp;&nbsp;Palesch D, Bosinger SE, ..., <b>Thomas GWC</b>, Hahn MW, ..., Silvestri G. 
				2018. 
				<em>Nature</em>. 
				553:77-81.
				</br>&nbsp;&nbsp;doi: <a href="https://doi.org/doi:10.1038/nature25140" target="_blank" id="doi_link">10.1038/nature25140</a>
			</p>
		</ul>
	</div>
	<div class="col-2-24" id="margin"></div>

	<div class="row" id="section-header-row">
        <div class="col-2-24" id="margin"></div>
        <div class="col-20-24" id="section_header">2017</div>
        <div class="col-2-24" id="margin"></div>
	</div>
	<div class="row" id="pub-row"></div>
	<div class="col-2-24" id="margin"></div>
	<div class="col-20-24" id="pub">
		<ul id="presents">
			<p>
				<span class="pub_title">Gene-tree reconciliation with MUL-trees to resolve polyploidy events</span>
				</br>&nbsp;&nbsp;<b>Thomas GWC</b>, Ather SA, and Hahn MW. 
				2017. 
				<em>Systematic Biology.</em> 
				66(6):1007-1018.
				</br>&nbsp;&nbsp;doi: <a href="https://doi.org/10.1093/sysbio/syx044" target="_blank" id="doi_link">10.1093/sysbio/syx044</a>
				</br>&nbsp;&nbsp;Software: <a href="https://gwct.github.io/grampa" target="_blank">GRAMPA</a>
			</p>

			<p>
				<span class="pub_title">The effects of increasing the number of taxa on inferences of molecular convergence</span>
				</br>&nbsp;&nbsp;<b>Thomas GWC</b>, Hahn MW, and Hahn Y. 
				2017. 
				<em>Genome Biology and Evolution.</em> 
				9(1):213-221.
				</br>&nbsp;&nbsp;doi: <a href="http://dx.doi.org/10.1093/gbe/evw306" target="_blank">10.1093/gbe/evw306</a>
				</br>&nbsp;&nbsp;Software: <a href="https://github.com/gwct/gwct" target="_blank">GWCT</a>
			</p>
		</ul>
	</div>
	<div class="col-2-24" id="margin"></div>

	<div class="row" id="section-header-row">
        <div class="col-2-24" id="margin"></div>
        <div class="col-20-24" id="section_header">2015</div>
        <div class="col-2-24" id="margin"></div>
	</div>
	<div class="row" id="pub-row"></div>
	<div class="col-2-24" id="margin"></div>
	<div class="col-20-24" id="pub">
		<ul id="presents">
			<p>
				<span class="pub_title">The genome of the vervet (Chlorocebus aethiops sabaeus)</span>
				</br>&nbsp;&nbsp;Warren WC, <b>The Vervet Genome Consortium</b>, Freimer NB. 
				2015. 
				<em>Genome Research.</em> 
				25(12):1921-1933.
				</br>&nbsp;&nbsp;doi: <a href="http://dx.doi.org/10.1101/gr.192922.115" target="_blank">10.1101/gr.192922.115</a>
			</p>

			<p>
				<span class="pub_title">Determining the null model for detecting adaptive convergence from genomic data: a case study using echolocating mammals</span>
				</br>&nbsp;&nbsp;<b>Thomas GWC</b> and Hahn MW. 
				2015. 
				<em>Molecular Biology and Evolution.</em> 
				32(5):1232-1236.
				</br>&nbsp;&nbsp;doi: <a href="http://dx.doi.org/10.1093/molbev/msv013" target="_blank">10.1093/molbev/msv013</a>
			</p>

			<p>
				<span class="pub_title">Convergent evolution of the genomes of marine mammals</span>
				</br>&nbsp;&nbsp;Foote AD*, Liu Y*, <b>Thomas GWC*</b>, Vinař T*, et al. 
				2015. 
				<em>Nature Genetics.</em> 
				47(3):272-275.
				</br>&nbsp;&nbsp;doi: <a href="http://dx.doi.org/doi:10.1038/ng.3198" target="_blank">doi:10.1038/ng.3198</a>
			</p>

			<p>
				<span class="pub_title">Highly evolvable malaria vectors: the genomes of 16 Anopheles mosquitoes</span>
				</br>&nbsp;&nbsp;Neafsey DE, Waterhouse RM, <b>The Anopheles Genome Consortium</b>, Besansky NJ. 
				2015. 
				<em>Science.</em> 
				347(6217):1258522
				</br>&nbsp;&nbsp;doi: <a href="http://dx.doi.org/10.1126/science.1258522" target="_blank">10.1126/science.1258522</a>
			</p>
		</ul>
	</div>
	<div class="col-2-24" id="margin"></div>

	<div class="row" id="section-header-row">
        <div class="col-2-24" id="margin"></div>
        <div class="col-20-24" id="section_header">2014</div>
        <div class="col-2-24" id="margin"></div>
	</div>
	<div class="row" id="pub-row"></div>
	<div class="col-2-24" id="margin"></div>
	<div class="col-20-24" id="pub">
		<ul id="presents">
			<p>
				<span class="pub_title">Comparative analysis of the domestic cat genome reveals genetic signatures underlying feline biology and domestication</span>
				</br>&nbsp;&nbsp;Montague MJ ... <b>Thomas GWC</b>, Hahn MW ... Warren WC. 
				2014. 
				<em>PNAS.</em> 
				111(48):17230-17235.
				</br>&nbsp;&nbsp;doi: <a href="http://dx.doi.org/10.1073/pnas.1410083111" target="_blank">10.1073/pnas.1410083111</a>
			</p>

			<p>
				<span class="pub_title">Gibbon genome and the fast karyotype evolution of small apes</span>
				</br>&nbsp;&nbsp;Carbone L, <b>The Gibbon Genome Consortium</b>, Gibbs RA. 
				2014. 
				<em>Nature.</em> 
				513(7517):295-201.
				</br>&nbsp;&nbsp;doi: <a href="http://dx.doi.org/10.1038/nature13679" target="_blank">10.1038/nature13679</a>
			</p>
		</ul>
	</div>
	<div class="col-2-24" id="margin"></div>

	<div class="row" id="section-header-row">
        <div class="col-2-24" id="margin"></div>
        <div class="col-20-24" id="section_header">2013</div>
        <div class="col-2-24" id="margin"></div>
	</div>
	<div class="row" id="pub-row"></div>
	<div class="col-2-24" id="margin"></div>
	<div class="col-20-24" id="pub">
		<ul id="presents">
			<p>
				<span class="pub_title">The human mutation rate is increasing, even as it slows</span>
				</br>&nbsp;&nbsp;<b>Thomas GWC</b> and Hahn MW. 
				2013. 
				<em>Molecular Biology and Evolution.</em> 
				31(2):253-257.
				</br>&nbsp;&nbsp;doi: <a href="http://dx.doi.org/10.1093/molbev/mst218" target="_blank">10.1093/molbev/mst218</a>
			</p>

			<p>
				<span class="pub_title">Estimating gene gain and loss rates in the presence of error in genome assembly and annotation using CAFE 3</span>
				</br>&nbsp;&nbsp;Han MV, <b>Thomas GWC</b>, Lugo-Martinez J, and Hahn MW. 
				2013. 
				<em>Molecular Biology and Evolution.</em> 
				30(8):1987-1997.
				</br>&nbsp;&nbsp;doi: <a href="http://dx.doi.org/10.1093/molbev/mst100" target="_blank">10.1093/molbev/mst100</a>
			</p>
		</ul>
	</div>
	<div class="col-2-24" id="margin"></div>
	
	<a class="internal-link" name="talks"></a>
	<div class="row" id="header">Presentations</div>
	<div class="col-2-24" id="margin"></div>
	<div class="col-20-24" id="pub">
		<ul id="presents">
			<p>
				<span class="pub_title">Prioritizing loci for ILS-aware rate analyses using phylogenetic concordance factors</span>
				</br>&nbsp;&nbsp;Society of Molecular Biology and Evolution Global Symposium 2 (Sustainability, Equity, and Efficiency in Computational Biology) - 
				2022.07.12 -
				Virtual -
				Contributed Talk - 
				<a href="slides/2022.07.12-SMBE-phyloacc.pptx">Slides</a>
			</p>

			<p>
				<span class="pub_title">Prioritizing loci for ILS-aware rate analyses using phylogenetic concordance factors</span>
				</br>&nbsp;&nbsp;Evolution Conference - 
				2022.06.27 -
				Cleveland, OH -
				Contributed Talk - 
				<a href="slides/2022.06.27-Evolution-phyloacc.pptx">Slides</a>
			</p>

			<p>
				<span class="pub_title">Speciation and introgression across the most species-rich radiation in mammals</span>
				</br>&nbsp;&nbsp;Population, Evolutionary, and Quantitative Genetics Conference - 
				2022.06.09 -
				Pacific Grove, CA -
				Platform Talk - 
				<a href="slides/2022.06.09-PEQG-rodent-introgression.pptx">Slides</a>
			</p>

			<p>
				<span class="pub_title">Patterns of genomic variation across the tree of life</span>
				</br>&nbsp;&nbsp;UMass Lowell Departmental Seminar - 
				2022.03.25 -
				Lowell, MA -
				Invited Talk - 
				<a href="slides/2022.03.25-UMass-Lowell-comparative.pptx">Slides</a>
			</p>

			<p>
				<span class="pub_title">Patterns of genomic variation across the tree of life</span>
				</br>&nbsp;&nbsp;Harvard Museum of Comparative Zoology Lunchtime Seminar -
				2022.03.21 - 
				Cambridge, MA -
				Invited Talk - 
				<a href="slides/2022.03.21-MCZ-comparative.pptx">Slides</a>
			</p>

			<p>
				<span class="pub_title">Pedigree sequencing and mutation rate variation in primates</span>
				</br>&nbsp;&nbsp;American Association of Biological Anthropologists - 
				2021.04.15 -
				Virtual - 
				Invited Talk - 
				<a href="slides/2021.04.15-AABA-mutation-rates.pptx">Slides</a>
			</p>

			<p>
				<span class="pub_title">Patterns of molecular evolution in Arthropods (with Elias Dohmen)</span>
				</br>&nbsp;&nbsp;Arthropod Genomics Symposium - 
				2020.07.21 -
				Virtual - 
				Invited Talk - 
				<a href="slides/2020.07.21-AGS-i5k.pptx">Slides</a>
			</p>

			<p>
				<span class="pub_title">Reproductive longevity predicts mutation rates in primates</span>
				</br>&nbsp;&nbsp;Population, Evolutionary, and Quantitative Genetics Conference - 
				2018.05.15
				Madison, WI - 
				Platform Talk - 
				<a href="slides/2018.05.15-PEQG-owlmonkey.pptx">Slides</a>
			</p>

			<p>
				<span class="pub_title">The evolution of the genes and genomes of 76 arthropod species</span>
				</br>&nbsp;&nbsp;Evolution Conference - 
				2017.06.26
				Portland, OR - 
				Regular Talk - 
				<a href="slides/2017.06.26-Evolution-i5k.pptx">Slides</a> (14 minute version)
			</p>

			<p>
				<span class="pub_title">The evolution of the genes and genomes of 76 arthropod species</span>
				</br>&nbsp;&nbsp;Arthropod Genomics Symposium - 
				2017.06.09 -
				South Bend, IN - 
				Invited Talk - 
				<a href="slides/2017.06.09-AGS-i5k.pptx">Slides</a> (20 minute version)
			</p>

			<p>
				<span class="pub_title">Gene tree reconciliation with MUL-trees for polyploid analysis</span>
				</br>&nbsp;&nbsp;Evolution Conference - 
				2016.06.19 -
				Austin, TX - 
				Regular Talk - 
				<a href="slides/2016.06.19-Evolution-GRAMPA.pptx">Slides</a>
			</p>

			<p>
				<span class="pub_title">Accounting for sequencing error in phylogenetics</span>
				</br>&nbsp;&nbsp;Society of Systematic Biologists - 
				2015.05.21 -
				Ann Arbor, MI - 
				Lightning Talk - 
				<a href="slides/2015.05.21-SSB-Error.pptx">Slides</a>
			</p>

			<p>
				<span class="pub_title">Inferring molecular convergence from genomic data</span>
				</br>&nbsp;&nbsp;Midwest Ecology and Evolution Conference - 
				2015.03.28 -
				Bloomington, IN - 
				Contributed Talk - 
				<a href="slides/2015.03.28-MEEC-Convergence.pptx">Slides</a>
			</p>

			<p>
				<span class="pub_title">Convergent evolution of the genomes of marine mammals</span>
				</br>&nbsp;&nbsp;Society of Molecular Biology and Evolution - 
				2014.06.12 -
				San Juan, PR - 
				Contributed Talk - 
				<a href="slides/2014.06.12-SMBE-MarineMammals.pptx">Slides</a>
			</p>
		</ul>
	</div>
	<div class="col-2-24" id="margin"></div>

	<a class="internal-link" name="posters"></a>
	<div class="row" id="header">Posters</div>
	<div class="col-2-24" id="margin"></div>
	<div class="col-20-24" id="pub">
		<ul id="presents">
			<p>
				<span class="pub_title">Molecular and morphological evolution across the most species-rich radiation in mammals</span>
				</br>&nbsp;&nbsp;Evolution Conference - 
				2022.06.27 -
				Cleveland, OH -
				<a href="posters/2022.06.27-Evolution-murine.png">Poster</a>
			</p>

			<p>
				<span class="pub_title">Causes and consequences of structural variation in the <em>Macaca mulatta</em> genome (first author <b>Jelena Nguyen</b>)</span>				
				</br>&nbsp;&nbsp;Center of Excellence for Women & Technology Research Experience for Undergraduates Symposium - 
				2019.04.12 -
				Bloomington, IN -
				<a href="posters/2019.04.12-CEWiT-macaque.png">Poster</a>
			</p>

			<p>
				<span class="pub_title">Convergent evolution of the genomes of marine mammals</span>
				</br>&nbsp;&nbsp;Genetics, Cellular, and Molecular Sciences Symposium - 
				2014.06.05 -
				Bloomington, IN -
				<a href="posters/2014.06.05-GCMS-Symposium-convergence.jpg">Poster</a>
			</p>
		</ul>
	</div>
	<div class="col-2-24" id="margin"></div>

	<a class="internal-link" name="workshops"></a>
	<div class="row" id="header">Workshops</div>
	<div class="col-2-24" id="margin"></div>
	<div class="col-20-24" id="pub">
		<ul id="presents">
			<p>
				<span class="pub_title">Bayesian estimation of substitution rates with <a href="https://phyloacc.github.io/" target="_blank">PhyloAcc</a></span>
				</br>&nbsp;&nbsp;OEB275R Fall 2022 - Comparative Genomics: Phylogenetic Approaches to Linking Genomes and Phenotypes - 
				Harvard University, Cambridge, MA -
				<a href="https://gwct.github.io/phyloacc/" target="_blank">Workshop website</a>
			</p>	

			<p>
				<span class="pub_title">Introduction to Bioinformatics (with <a href="https://renaschweizer.org/" target="_blank">Rena Schweizer</a>)</span>
				</br>&nbsp;&nbsp;ConGen 2022: Population Genomic Data Analysis Course/Workshop - 
				Virtual - 
				<a href="https://gwct.github.io/congen/bioinformatics/" target="_blank">Workshop website</a>
			</p>			

			<p>
				<span class="pub_title">Genome Assembly (led by Ellie Armstrong)</span>
				</br>&nbsp;&nbsp;ConGen 2022: Population Genomic Data Analysis Course/Workshop - 
				Virtual - 
				<a href="congen/assembly/slides/congen-assembly-lecture.pptx">Slides</a> - 
				<a href="https://gwct.github.io/congen/assembly/" target="_blank">Workshop website</a>
			</p>

			<p>
				<span class="pub_title">Introduction to Bioinformatics (with <a href="https://renaschweizer.org/" target="_blank">Rena Schweizer</a>)</span>
				</br>&nbsp;&nbsp;ConGen 2021: Population Genomic Data Analysis Course/Workshop - 
				Virtual - 
				<a href="https://gwct.github.io/congen/2021/bioinformatics/" target="_blank">Workshop website</a>
			</p>			

			<p>
				<span class="pub_title">Genome Assembly (with Ellie Armstrong)</span>
				</br>&nbsp;&nbsp;ConGen 2021: Population Genomic Data Analysis Course/Workshop - 
				Virtual - 
				<a href="congen/2021/assembly/slides/congen-assembly-lecture.pptx">Slides</a> - 
				<a href="https://gwct.github.io/congen/2021/assembly/" target="_blank">Workshop website</a>
			</p>

			<p>
				<span class="pub_title">Genome Assembly (with Ellie Armstrong)</span>
				</br>&nbsp;&nbsp;ConGen 2020: Population Genomic Data Analysis Course/Workshop - 
				Virtual - 
				<a href="congen/2020/slides/congen-assembly-lecture.pptx">Slides</a> - 
				<a href="https://gwct.github.io/congen/2020/" target="_blank">Workshop website</a>
			</p>
		</ul>
	</div>
	<div class="col-2-24" id="margin"></div>	

	<a class="internal-link" name="other"></a>
	<div class="row" id="header">Other Content</div>
	<div class="col-2-24" id="margin"></div>
	<div class="col-20-24" id="pub">
		<ul id="presents">
			<p>
				<span class="pub_title">Drosophila 25 species phylogeny.</span>
				</br>&nbsp;&nbsp;Thomas GWC, Hahn MW. 2017. <a href="https://figshare.com/articles/Drosophila_25_species_phylogeny/5450602" target="_blank">FigShare fileset</a>.
				</br>&nbsp;&nbsp;doi: <a href="http://dx.doi.org/10.6084/m9.figshare.5450602" target="_blank">10.6084/m9.figshare.5450602</a>
			</p>
		</ul>
	</div>
	<div class="col-2-24" id="margin"></div>

    {links}

    {footer}
</body>
"""

######################
# Main block
######################
pagefile = "pubs.html";
print("Generating " + pagefile + "...");
title = "Gregg Thomas - Publications"

head = RC.readHead(title, pagefile);
nav = RC.readNav(pagefile);
links = RC.readLinks();
footer = RC.readFooter();

outfilename = "../../" + pagefile;

with open(outfilename, "w", encoding='utf-8') as outfile:
    outfile.write(html_template.format(head=head, nav=nav, links=links, footer=footer));