############################################################
# For personal site, 11.19
# This generates the file "pubs.html"
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
			<p><span class="pub_title">Origins and long-term patterns of copy-number variation in rhesus macaques</span>
			</br>&nbsp;&nbsp;<b>Thomas GWC</b>, Wang RJ, Nguyen J, Harris RA, Raveendran M, Rogers J, Hahn MW. 2019. <em>bioRxiv</em>.
			</br>&nbsp;&nbsp;doi: <a href="https://doi.org/10.1101/749416" target="_blank" id="doi_link">10.1101/749416</a>
			</br>&nbsp;&nbsp;Resources: <a href="https://github.com/gwct/macaque-cnv-figs" target="_blank">Figures</a></p>
		</ul>
	</div>
	<div class="col-2-24" id="margin"></div>
	-->

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
				<span class="pub_title">Highly contiguous assemblies of 101 drosopholid genomes</span>
				</br>&nbsp;&nbsp;Kim BY, ..., <b>Armstrong EE</b>, ..., Petrov D.
				2021. 
				<em>eLife.</em> 
				10:e66405.
				</br>&nbsp;&nbsp;doi: <a href="https://doi.org/10.7554/eLife.66405" target="_blank">10.7554/eLife.66405</a>
			</p>

			<p>
				<span class="pub_title">Recent evolutionary history of tigers highlights contrasting roles of genetic drift and selection</span>
				</br>&nbsp;&nbsp;<b>Armstrong EE</b>, ..., Ramakrishnan U.
				2021. 
				<em>Molecular Biology and Evolution.</em> 
				38(6):2366-2379.
				</br>&nbsp;&nbsp;doi: <a href="https://doi.org/10.1093/molbev/msab032" target="_blank">10.1093/molbev/msab032</a>
			</p>

			<p>
				<span class="pub_title">Widespread introgression across a phylogeny of 155 <em>Drosophila</em> genomes</span>
				</br>&nbsp;&nbsp;Suvorov A, ..., <b>Armstrong EE</b>, ..., Comeault AA.
				2021. 
				<em>bioRxiv</em> 
				</br>&nbsp;&nbsp;doi: <a href="https://doi.org/10.1101/2020.12.14.422758" target="_blank">10.1101/2020.12.14.422758</a>
			</p>
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
				<span class="pub_title">Characterization of P=orodiginine pathway in marine sponge-associated <em>Pseudoalteromonas</em> sp. PPB1 in Hilo, Hawai‘i</span>
				</br>&nbsp;&nbsp;Sakai-Kawada FE, Ip CG, Hagiwara KA, Nguyen H-YX, Yakym C-JAV, Helmkampf M, <b>Armstrong EE</b>, Awaya JD.
				2020. 
				<em>Frontiers in Sustainable Food Systems</em> 
				18:3.
				</br>&nbsp;&nbsp;doi: <a href="https://doi.org/10.3389/fsufs.2020.600201" target="_blank">10.3389/fsufs.2020.600201</a>
			</p>

			<p>
				<span class="pub_title">Long live the king: chromosome-level assembly of the lion (<em>Penthera leo</em>) using linked-read, Hi-C, and long-read data</span>
				</br>&nbsp;&nbsp;<b>Armstrong EE</b>, Taylor RW, Miller D, Kaelin CB, Barsh GS, Hadly EA, Petrov D.
				2020. 
				<em>BMC Biology.</em> 
				4:600201.
				</br>&nbsp;&nbsp;doi: <a href="https://doi.org/10.1186/s12915-019-0734-5" target="_blank">10.1186/s12915-019-0734-5</a>
			</p>

			<p>
				<span class="pub_title">A holobiont view of island biogeography: unraveling patterns driving the nascent diversification of a Hawaiian spider and its microbial associates</span>
				</br>&nbsp;&nbsp;<b>Armstrong EE</b>, Perez-Lamarque B, Bi K, Chen C, Becking LE, Lim JY, Linderoth T, Krehenwinkel H, Gillespie R.
				2020. 
				<em>bioRxiv.</em> 
				</br>&nbsp;&nbsp;doi: <a href="https://doi.org/10.1101/2020.12.07.414961" target="_blank">10.1101/2020.12.07.414961</a>
			</p>
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
				<span class="pub_title">Horizontal transfer of bacterial cytolethal distending toxin B genes to insects</span>
				</br>&nbsp;&nbsp;Verster KI, Wisecaver JH, Karageorgi M, Duncan RP, Gloss AD, <b>Armstrong EE</b>, Price DK, Menon AR, Ali ZM, Whiteman NK.
				2019. 
				<em>Molecular Biology and Evolution.</em> 
				36(10):2105-2110.
				</br>&nbsp;&nbsp;doi: <a href="https://doi.org/10.1093/molbev/msz146" target="_blank">10.1093/molbev/msz146</a>
			</p>

			<p>
				<span class="pub_title">Comparative analyses identify genomic features potentially involved in the evolution of birds-of-paradise.</span>
				</br>&nbsp;&nbsp;Prost S, <b>Armstrong EE</b>, ..., Irestedt M.
				2019. 
				<em>GigaScience.</em> 
				8(5):giz003.
				</br>&nbsp;&nbsp;doi: <a href="https://doi.org/10.1093/gigascience/giz003" target="_blank">10.1093/gigascience/giz003</a>
			</p>

			<p>
				<span class="pub_title">Cost-effective assembly of the African wild dog (<em>Lycaon pictus</em>) genome using linked reads</span>
				</br>&nbsp;&nbsp;<b>Armstrong EE</b>, Taylor RW, Prost S, Blinston P, van der Meer E, Madizkanda H, Mufute O, Mandisodza-Chikerema R, Stuelpnagel J, Sillero-Zubiri C, Petrov D.
				2019. 
				<em>GigaScience.</em> 
				8(2):giy124.
				</br>&nbsp;&nbsp;doi: <a href="https://doi.org/10.1093/gigascience/giy124" target="_blank">10.1093/gigascience/giy124</a>
			</p>

			<p>
				<span class="pub_title">Evolution of herbivory remodels a <em>Drosophila</em> genome</span>
				</br>&nbsp;&nbsp;Gloss AD, ...,  <b>Armstrong EE</b>, ..., Whiteman NK.
				2019. 
				<em>bioRxiv</em> 
				</br>&nbsp;&nbsp;doi: <a href="https://doi.org/10.1101/767160" target="_blank">10.1101/767160</a>
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
				<span class="pub_title">Draft genome sequence and annotation of the lichen-forming fungus <em>Arthonia radiata</em></span>
				</br>&nbsp;&nbsp;<b>Armstrong EE</b>, Prost S, Ertz D, Westberg M, Frisch A, Bendiskby M.
				2018. 
				<em>Genome Announcements.</em> 
				6(14):e00281-18.
				</br>&nbsp;&nbsp;doi: <a href="https://doi.org/10.1128/genomeA.00281-18" target="_blank">10.1128/genomeA.00281-18</a>
			</p>

			<p>
				<span class="pub_title">Rapid divergence of mussel populations despite incomplete barriers to dispersal</span>
				</br>&nbsp;&nbsp;Maas DL, Prost S, Bi K, Smith LL, <b>Armstrong EE</b> Aji LP, Toha AHA, Gillespie RG, Becking LE. 
				2018. 
				<em>Molecular Ecology.</em> 
				27(7):1556-1571.
				</br>&nbsp;&nbsp;doi: <a href="https://doi.org/10.1111/mec.14556" target="_blank">10.1111/mec.14556</a>
			</p>
		</ul>
	</div>
	<div class="col-2-24" id="margin"></div>

	<div class="row" id="section-header-row">
        <div class="col-2-24" id="margin"></div>
        <div class="col-20-24" id="section_header">2016</div>
        <div class="col-2-24" id="margin"></div>
	</div>
	<div class="row" id="pub-row"></div>
	<div class="col-2-24" id="margin"></div>
	<div class="col-20-24" id="pub">
		<ul id="presents">
			<p>
				<span class="pub_title">Draft genome sequence of marine spong symbiont <em>Pseudoalteromonas luteoviolace</em> IPB1, isolated from Hilo, Hawaii</span>
				</br>&nbsp;&nbsp;Sakai-Kawada FE, Yakym CJ, Helmkampf M, Hagiwara K, Ip CG, Antonio BJ, <b>Armstrong EE</b>, Ulloa WJ, Awaya JD. 
				2016. 
				<em>Genome Announcements.</em> 
				4(5):e01002-16.
				</br>&nbsp;&nbsp;doi: <a href="https://doi.org/10.1128/genomeA.01002-16" target="_blank">10.1128/genomeA.01002-16</a>
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
				<span class="pub_title">Community assembly on isolated islands: macroecology meets evolution</span>
				</br>&nbsp;&nbsp;Rominger AJ, ..., Armstrong EE, ..., Gillespie RG. 
				2015. 
				<em>Global Ecology and Biogeography.</em> 
				25(7):769-780.
				</br>&nbsp;&nbsp;doi: <a href="https://doi.org/10.1111/geb.12341" target="_blank">10.1111/geb.12341</a>
			</p>
		</ul>
	</div>
	<div class="col-2-24" id="margin"></div>
		
	<div class="row" id="header">Presentations</div>
	<div class="col-2-24" id="margin"></div>
	<div class="col-20-24" id="pub">
		<ul id="presents">
			<p>
				<span class="pub_title">Pedigree sequencing and mutation rate variation in primates</span>
				</br>&nbsp;&nbsp;American Association of Biological Anthropologists 2021 - 
				Virtual - 
				Invited Talk - 
				<a href="#">Slides</a>
			</p>

			<p>
				<span class="pub_title">Patterns of molecular evolution in Arthropods (with Elias Dohmen)</span>
				</br>&nbsp;&nbsp;Arthropod Genomics Symposium 2020 - 
				Virtual - 
				Invited Talk - 
				<a href="#">Slides</a></p>
		</ul>
	</div>
	<div class="col-2-24" id="margin"></div>

	<div class="row" id="header">Workshops</div>
	<div class="col-2-24" id="margin"></div>
	<div class="col-20-24" id="pub">
		<ul id="presents">
			<p>
				<span class="pub_title">Genome Assembly (with <a href="http://gwct.github.io" target="_blank">Gregg Thomas</a>)</span>
				</br>&nbsp;&nbsp;ConGen 2021: Population Genomic Data Analysis Course/Workshop - 
				Virtual - 
				<a href="congen/slides/congen-assembly-lecture.pptx">Slides</a> -
				<a href="https://gwct.github.io/congen-2021/assembly/" target="_blank">Workshop website</a>
			</p>

			<p>
				<span class="pub_title">Feline and Canine Genomics Workshop (with Elinor Karlsson)</span>
				</br>&nbsp;&nbsp;Plant and Animal Genome XXVIII Conference - 
				<a href="https://pag.confex.com/pag/xxviii/meetingapp.cgi/Session/5947" target="_blank">Synopsis</a>
			</p>

			<p>
				<span class="pub_title">Genome Assembly (with <a href="http://gwct.github.io" target="_blank">Gregg Thomas</a>)</span>
				</br>&nbsp;&nbsp;ConGen 2020: Population Genomic Data Analysis Course/Workshop - 
				Virtual - 
				<a href="congen/slides/congen-assembly-lecture.pptx">Slides</a> -
				<a href="https://gwct.github.io/congen/" target="_blank">Workshop website</a>
			</p>
		</ul>
	</div>
	<div class="col-2-24" id="margin"></div>	

	<!-- <div class="row" id="header">Other Content</div>
	<div class="col-2-24" id="margin"></div>
	<div class="col-20-24" id="pub">
		<ul id="presents">
			<p>
			<span class="pub_title">Drosophila 25 species phylogeny.</span>
			</br>&nbsp;&nbsp;Thomas GWC, Hahn MW. 
			2017. 
			<a href="https://figshare.com/articles/Drosophila_25_species_phylogeny/5450602" target="_blank">FigShare fileset</a>.
			</br>&nbsp;&nbsp;doi: <a href="http://dx.doi.org/10.6084/m9.figshare.5450602" target="_blank">10.6084/m9.figshare.5450602</a></p>
		</ul>
	</div>
	<div class="col-2-24" id="margin"></div> -->

    {links}

    {footer}
</body>
"""

######################
# Main block
######################
pagefile = "pubs.html";
print("Generating " + pagefile + "...");
title = "Ellie Armstrong - Publications"

head = RC.readHead(title, pagefile);
nav = RC.readNav(pagefile);
links = RC.readLinks();
footer = RC.readFooter();

outfilename = "../../" + pagefile;

with open(outfilename, "w", encoding='utf-8') as outfile:
    outfile.write(html_template.format(head=head, nav=nav, links=links, footer=footer));