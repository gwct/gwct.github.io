############################################################
# For personal site, 11.19
# This generates the file "archive.html"
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

	<div class="row" id="header">Updates</div>

    <div class="row" id="section-header-row">
        <div class="col-2-24" id="margin"></div>
        <div class="col-20-24" id="section_header">July 2, 2024 &nbsp;</div>
        <div class="col-2-24" id="margin"></div>
	</div>
	<div class="row" id="pub-row"></div>
	<div class="col-2-24" id="margin"></div>
	<div class="col-20-24" id="arc_entry">
		<ul>
			<p>
				The past year has been busy! From teaching and developing more workshops here in the <a href="https://informatics.fas.harvard.edu/" target="_blank">Informatics Group</a>
                (and helping to update the website!), to seeing friends and showing a poster about <a href="https://phyloacc.github.io/" target="_blank">PhyloAcc</a> at this year's 
                <a href="https://genetics-gsa.org/tagc/" target="_blank">TAGC in Washington D.C</a>, and to <a href="pubs.html" target="_blank">finishing up several projects</a>.
			</p>
            
            <p>
				On top of that, I just welcomed my son, Wesley, into the world on June 20! With that being said, I'll be on leave for the next few months to get to know him.
            </p>
		</ul>
	</div>
	<div class="col-2-24" id="margin"></div>    
    
    <div class="row" id="section-header-row">
        <div class="col-2-24" id="margin"></div>
        <div class="col-20-24" id="section_header">July 2, 2023 &nbsp;</div>
        <div class="col-2-24" id="margin"></div>
	</div>
	<div class="row" id="pub-row"></div>
	<div class="col-2-24" id="margin"></div>
	<div class="col-20-24" id="arc_entry">
		<ul>
			<p>
				It was great to see old friends and meet new people at the Evolution 2023 meeting in Albuquerque, New Mexico!
			</p>
            
            <p>
				I gave a talk on the effects of divergence on the effectiveness of read mapping and subsequent variant calling. You can check out the slides from my talk 
                <a href="file:///C:/bin/gwct.github.io/pubs.html#talks">here</a>.
            </p>
		</ul>
	</div>
	<div class="col-2-24" id="margin"></div>

    
    <div class="row" id="section-header-row">
        <div class="col-2-24" id="margin"></div>
        <div class="col-20-24" id="section_header">April 6, 2023 &nbsp;</div>
        <div class="col-2-24" id="margin"></div>
	</div>
	<div class="row" id="pub-row"></div>
	<div class="col-2-24" id="margin"></div>
	<div class="col-20-24" id="arc_entry">
		<ul>
			<p>
				I helped teach a series of workshops over 4 weeks in March with my colleagues in the <a href="https://informatics.fas.harvard.edu/" target="_blank">Informatics Group</a> here at Harvard.
				We covered topics ranging from an introduction to the R programming language and the tidyverse, to common bioinformatics files and tools, and working with conda environments and
				a HPC. I look forward to developing these workshops in the future, possibly into a full semester-long course.
			</p>
		</ul>
	</div>
	<div class="col-2-24" id="margin"></div>

    <div class="row" id="section-header-row">
        <div class="col-2-24" id="margin"></div>
        <div class="col-20-24" id="section_header"><img src="img/me/jack.png" style="height:24px;width:24px"/>ctober 31, 2022 &nbsp;</div>
        <div class="col-2-24" id="margin"></div>
	</div>
	<div class="row" id="pub-row"></div>
	<div class="col-2-24" id="margin"></div>
	<div class="col-20-24" id="arc_entry">
		<ul>
			<p>
				I was happy to give a <a href="https://gwct.github.io/phyloacc/OEB275R/" target="_blank">workshop</a> this week demonstrating 
				<a href="https://phyloacc.github.io/" target="_blank">PhyloAcc</a> in
				<a href="https://edwards.oeb.harvard.edu/people/scott-v-edwards" target="_blank">Prof. Scott Edwards'<a> 
				<a href="https://canvas.harvard.edu/courses/106414" target="_blank">comparative genomics class</a>.
			</p>
		</ul>
	</div>
	<div class="col-2-24" id="margin"></div>

    <div class="row" id="section-header-row">
        <div class="col-2-24" id="margin"></div>
        <div class="col-20-24" id="section_header">July 13, 2022</div>
        <div class="col-2-24" id="margin"></div>
	</div>
	<div class="row" id="pub-row"></div>
	<div class="col-2-24" id="margin"></div>
	<div class="col-20-24" id="arc_entry">
		<ul>
			<p>
				After my talks in the spring, I launched a summer tour, giving talks and posters at multiple conferences! The tour dates were:

				<ul>
					<li>
						June 07 - PEQG (Pacific Grove, CA): Speciation and introgression across the most species-rich radiation in mammals
					</li>

					<li>
						June 27 - Evolution (Cleveland, OH): Prioritizing loci for ILS-aware rate analyses using phylogenetic concordance factors (Phylogenetic Methods IV)
					</li>

					<li>
						June 27 - Evolution (Cleveland, OH): Molecular and morphological evolution across the most species-rich radiation in mammals (Poster board 105) 
					</li>

					<li>
						June 12 - SMBE GS2 (Virtual): Prioritizing loci for ILS-aware rate analyses using phylogenetic concordance factors
					</li>															
				</ul>
			</p>

			<p>
				SMBE GS2 was really unique, focusing on <a href="http://www.smbe.org/smbe/MEETINGS/SMBEeverywhere/GS2.aspx" target="_blank">Sustainability, Equity, and Efficiency in Computational Biology</a>,
				which is something I'm really interested in and that our field now has the capability and need to focus on. I learned about some nice tools from Jason Grealey and colleagues
				(<a href="https://doi.org/10.1093/molbev/msac034" target="_blank">The carbon footprint of bioinformatics</a>) like
				<a href="http://green-algorithms.org/" target="_blank">Green algorithms</a> and 
				<a href="https://github.com/Llannelongue/GreenAlgorithms4HPC" target="_blank">GreenAlgorithms4HPC</a> to quantify the energy use and carbon footprint of the programs we run.
			</p>

			<p>
				You can check out the slides from my talks on the <a href="pubs.html">Publications & Talks</a> page.
			</p>

		</ul>
	</div>
	<div class="col-2-24" id="margin"></div>


    <div class="row" id="section-header-row">
        <div class="col-2-24" id="margin"></div>
        <div class="col-20-24" id="section_header">January 29, 2022</div>
        <div class="col-2-24" id="margin"></div>
	</div>
	<div class="row" id="pub-row"></div>
	<div class="col-2-24" id="margin"></div>
	<div class="col-20-24" id="arc_entry">
		<ul>
			<p>
				After moving to MA and settling in last semester, I'm looking forward to giving a couple seminars this spring. First,
				I'll be talking at the <a href="https://mcz.harvard.edu/seminars" target="_blank">lunchtime seminar</a> at the Museum of 
				Comparative Zoology here at Harvard on March 21. Later that week, on March 25, I'll be talking about my work at UMass Lowell's
				<a href="https://www.uml.edu/Sciences/biology/News/colloquia.aspx" target="_blank">weekly biology seminar</a>. Thanks to 
				<a href="https://darencard.net/" target="_blank">Daren Card</a> (MCZ) and 
				<a href="http://www.jessicagarb.science/" target="_blank">Jessica Garb</a> (UMass Lowell) for the invitations!
			</p>

			<p>
				I'm also looking forward to presenting my work at some conferences this summer. More on that soon!
			</p>
		</ul>
	</div>
	<div class="col-2-24" id="margin"></div>

    <div class="row" id="section-header-row">
        <div class="col-2-24" id="margin"></div>
        <div class="col-20-24" id="section_header">October 12, 2021</div>
        <div class="col-2-24" id="margin"></div>
	</div>
	<div class="row" id="pub-row"></div>
	<div class="col-2-24" id="margin"></div>
	<div class="col-20-24" id="arc_entry">
		<ul>
			<p>
				In September I taught at this year's online	<a href="https://www.umt.edu/ces/conferences/congen/" target="_blank">ConGen</a> population genomics workshop.
				This year I taught two workshops.
			</p>

			<ul>
				<li>
					<a href="https://gwct.github.io/congen-2021/bioinformatics/" target="_blank">Introduction to Bioinformatics</a> with 
					<a href="https://renaschweizer.org/" target="_blank">Rena Schweizer</a>
				</li>

				<li>
					<a href="https://gwct.github.io/congen-2021/assembly/" target="_blank">Genome Assembly</a> with Ellie Armstrong					
				</li>
			</ul>

			<p>	
				I'm really grateful to be working with such great people!
			</p>
		</ul>
	</div>
	<div class="col-2-24" id="margin"></div>

    <div class="row" id="section-header-row">
        <div class="col-2-24" id="margin"></div>
        <div class="col-20-24" id="section_header">July 25, 2021</div>
        <div class="col-2-24" id="margin"></div>
	</div>
	<div class="row" id="pub-row"></div>
	<div class="col-2-24" id="margin"></div>
	<div class="col-20-24" id="arc_entry">
		<ul>
			<p>
				This April I attended <a href="https://physanth.org/" target="_blank">AABA's</a> virtual meeting and gave a talk about primate mutation rates. I summarized
				all that we have learned about the rate at which mutations accumulate in primates, and how this changes for different types of mutations. Check out
				the slides <a href="slides/2021.04.15-AABA-mutation-rates.pptx" download>here</a>!
			</p>

			<p>	
				Importantly, at the beginning of July I started a position as a Bioinformatics Scientist at Harvard University! I'm really excited about this position 
				because I'll have both the freedom to pursue research and the stability of a staff position. I'll be working in 
				<a href="https://scholar.harvard.edu/tsackton/home" target="_blank">Tim Sackton's</a> <a href="https://informatics.fas.harvard.edu/" target="_blank">group</a> 
				on a range of comparative and population genomics questions and software development. For now, I'm working remotely still in Missoula, but will be moving
				to Cambridge in September, and I'm really looking forward to working with the scientists at Harvard!
			</p>
		</ul>
	</div>
	<div class="col-2-24" id="margin"></div>


    <div class="row" id="section-header-row">
        <div class="col-2-24" id="margin"></div>
        <div class="col-20-24" id="section_header">August 18, 2020</div>
        <div class="col-2-24" id="margin"></div>
	</div>
	<div class="row" id="pub-row"></div>
	<div class="col-2-24" id="margin"></div>
	<div class="col-20-24" id="arc_entry">
		<ul>
			<p>
				In September, I will be giving a workshop on genome assembly with <a href="http://elliearmstrong.mystrikingly.com/" target="_blank">Ellie Armstrong</a> at this year's online
				<a href="https://www.umt.edu/ces/conferences/congen/" target="_blank">ConGen</a>.
			</p>
		</ul>
	</div>
	<div class="col-2-24" id="margin"></div>


    <div class="row" id="section-header-row">
        <div class="col-2-24" id="margin"></div>
        <div class="col-20-24" id="section_header">July 20, 2020</div>
        <div class="col-2-24" id="margin"></div>
	</div>
	<div class="row" id="pub-row"></div>
	<div class="col-2-24" id="margin"></div>
	<div class="col-20-24" id="arc_entry">
		<ul>
			<p>
				Earlier this summer I was awarded the Indiana University Graduate School Distinguished Ph.D. Disseratation award! I am so honored and excited to have been chosen for this award!
				The graduate school has since nominated my dissertation for the Council of Graduate Schools Distinguished Dissertation award.
			</p>

			<p>
				On July 21, 2020 I will be giving a talk at the <a href="http://i5k.github.io/ags2020" target="_blank">vitrual Arthropod Genomics Symposium</a> regarding our 
				<a href="https://doi.org/10.1186/s13059-019-1925-7" target="_blank">recent publication</a> of the i5K pilot project. I'll be summarizing our results from this
				broad comparative study.
			</p>
		</ul>
	</div>
	<div class="col-2-24" id="margin"></div>

    <div class="row" id="section-header-row">
        <div class="col-2-24" id="margin"></div>
        <div class="col-20-24" id="section_header">May 30, 2020</div>
        <div class="col-2-24" id="margin"></div>
	</div>
	<div class="row" id="pub-row"></div>
	<div class="col-2-24" id="margin"></div>
	<div class="col-20-24" id="arc_entry">
		<ul>
			<p>
				Our <a href="https://doi.org/10.1101/gr.255174.119" target="_blank">paper</a> regarding mutation rates in rhesus macaques was featured on
				Luddy School of Informatics news website! Great work led by Richard Wang.
			</p>

			<p>
				<a href="https://luddy.indiana.edu/news/story.html?story=Hahn-Precision-Health-Initiative-researchers-publish-study-on-impact-of-paternal-age-on-offspring-mutation" target="_blank">Read more</a>
			</p>

			<p>-------</p>

			<p>
				I was excited to be asked to talk about my dissertation work on mutation rates in primates at this year's <a href="https://physanth.org/" target="_blank">AAPA</a>
				meeting, however this meeting was cancelled due to the COVID pandemic. Instead I will be uploading slides for this talk to their website in the near future.
			</p>
		</ul>
	</div>
	<div class="col-2-24" id="margin"></div>

    <div class="row" id="section-header-row">
        <div class="col-2-24" id="margin"></div>
        <div class="col-20-24" id="section_header">December 26, 2019</div>
        <div class="col-2-24" id="margin"></div>
	</div>
	<div class="row" id="pub-row"></div>
	<div class="col-2-24" id="margin"></div>
	<div class="col-20-24" id="arc_entry">
		<ul>
			<p>
				I recently (Nov. 1, 2019) gave a <a href="http://www.cooper-lab.org/chalk.html" target="_blank">CHALK</a> talk to my colleagues here
				at the University of Montana about my reasearch (past and future). It was a great learning experience for me to give a talk in this format.
			</p>

			<p>
				Jeff and I also recently (Nov. 10-13, 2019) visited the <a href="https://www.lsu.edu/mns/" target="_blank">LSU Museum of Natural Science</a> 
				to discuss upcoming collaborations with rodent specialists <a href="https://esselstyn.github.io/" target="_blank">Jake Esselstyn</a>, 
				<a href="https://museumsvictoria.com.au/about-us/staff/natural-sciences/terrestrial-zoology/dr-kevin-rowe/" target="_blank">Kevin Rowe</a>,
				and <a href="https://scholar.google.com/citations?user=iVRhKXQAAAAJ&hl=en&oi=ao" target="_blank">Carl Hutter</a>.
				This was a great opportunity to spend time with these scientists in the Museum and meet others at LSU!
			</p>
		</ul>
	</div>
	<div class="col-2-24" id="margin"></div>

    <div class="row" id="section-header-row">
        <div class="col-2-24" id="margin"></div>
        <div class="col-20-24" id="section_header">August 2, 2019</div>
        <div class="col-2-24" id="margin"></div>
	</div>
	<div class="row" id="pub-row"></div>
	<div class="col-2-24" id="margin"></div>
	<div class="col-20-24" id="arc_entry">
		<ul>
			<p>
				On July 1, 2019 I successfully defended my dissertation! It is titled 
				<a href="https://scholarworks.iu.edu/dspace/handle/2022/23333" target="_blank">The causes of mutation and substitution rate variation in primates</a>
				and is available open access at that link thanks to <a href="https://scholarworks.iu.edu/" target="_blank">IUScholarWorks</a>.
			</p>

			<p>
				I have subsequently moved to the <a href="http://hs.umt.edu/dbs/">University of Montana</a> in Missoula to start my postdoc work in 
				<a href="http://www.thegoodlab.org/" target="_blank">Jeff Good's lab</a>. Here I'll continue to work on some of the fundamental questions
				of phylogenetics and genome evolution using the great model system of murine rodents!
			</p>
		</ul>
	</div>
	<div class="col-2-24" id="margin"></div>

    <div class="row" id="section-header-row">
        <div class="col-2-24" id="margin"></div>
        <div class="col-20-24" id="section_header">August 9, 2018</div>
        <div class="col-2-24" id="margin"></div>
	</div>
	<div class="row" id="pub-row"></div>
	<div class="col-2-24" id="margin"></div>
	<div class="col-20-24" id="arc_entry">
		<ul>
			<p>
				On September 5th, I'll be hosting the <a href="http://i5k.github.io/webinar" target="_blank">i5K webinar</a>
				and discussing our work on the i5K pilot project to examine genome evolution across 76 species of Arthropods.
			</p>

			<p>
				Check out the pre-print of the paper on <a href="https://www.biorxiv.org/content/early/2018/08/04/382945" target="_blank">bioRxiv</a>!
			</p>
		</ul>
	</div>
	<div class="col-2-24" id="margin"></div>

    <div class="row" id="section-header-row">
        <div class="col-2-24" id="margin"></div>
        <div class="col-20-24" id="section_header">June 13, 2018</div>
        <div class="col-2-24" id="margin"></div>
	</div>
	<div class="row" id="pub-row"></div>
	<div class="col-2-24" id="margin"></div>
	<div class="col-20-24" id="arc_entry">
		<ul>
			<p>
				I have been featured in an article on IU's IT News & Events for my use of the 
				high-performance computing clusters to perform large-scale genomic analyses!
			</p>

			<p>
				<a href="https://itnews.iu.edu/articles/2018/IU%20doctoral%20student%20explores%20the%20history%20of%20life%20on%20Earth%20.php" target="_blank">Read More</a>
			</p>
		</ul>
	</div>
	<div class="col-2-24" id="margin"></div>

    <div class="row" id="section-header-row">
        <div class="col-2-24" id="margin"></div>
        <div class="col-20-24" id="section_header">June 9, 2017</div>
        <div class="col-2-24" id="margin"></div>
	</div>
	<div class="row" id="pub-row"></div>
	<div class="col-2-24" id="margin"></div>
	<div class="col-20-24" id="arc_entry">
		<ul>
			<p>
				I will also be giving my talk about my work with the i5k project at Evolution 
				this year in Portland. My talk is in the 'Phylogenomics 1' session at 8:30AM on Monday June 26.
			</p>
		</ul>
	</div>
	<div class="col-2-24" id="margin"></div>

    <div class="row" id="section-header-row">
        <div class="col-2-24" id="margin"></div>
        <div class="col-20-24" id="section_header">January 31, 2017</div>
        <div class="col-2-24" id="margin"></div>
	</div>
	<div class="row" id="pub-row"></div>
	<div class="col-2-24" id="margin"></div>
	<div class="col-20-24" id="arc_entry">
		<ul>
			<p>
				I have been invited to speak at the Arthropod Genomics Symposium at Notre Dame University in June.
				I'll be talking about my work in the i5k initiative on large scale gene family analysis. My first invited talk!
			</p>
		</ul>
	</div>
	<div class="col-2-24" id="margin"></div>

    <div class="row" id="section-header-row">
        <div class="col-2-24" id="margin"></div>
        <div class="col-20-24" id="section_header">May 20, 2016</div>
        <div class="col-2-24" id="margin"></div>
	</div>
	<div class="row" id="pub-row"></div>
	<div class="col-2-24" id="margin"></div>
	<div class="col-20-24" id="arc_entry">
		<ul>
			<p>
				I'll be giving a talk at this year's
				<a href="http://www.evolutionmeetings.org/evolution-2016---austin-texas.html" target="_blank"> Evolution Meeting</a> in Austin.
			</p>

			<p>
				<b>UPDATE: June 11, 2016</b> -- The title of my talk is "Gene tree reconciliation using MUL-trees resolves polyploidy events" and will
				be on Sunday June 19 at 9:15AM in the Phylogenetics methods development 3 symposium (MR5).
			</p>

			<p>
				Check out the pre-print of the paper on <a href="http://biorxiv.org/content/early/2016/06/10/058149" target="_blank">bioRxiv</a>!
			</p>
		</ul>
	</div>
	<div class="col-2-24" id="margin"></div>

    <div class="row" id="section-header-row">
        <div class="col-2-24" id="margin"></div>
        <div class="col-20-24" id="section_header">April 02, 2016</div>
        <div class="col-2-24" id="margin"></div>
	</div>
	<div class="row" id="pub-row"></div>
	<div class="col-2-24" id="margin"></div>
	<div class="col-20-24" id="arc_entry">
		<ul>
			<p>
				I was recently featured in a spotlight on the IU School of Informatics website!
			</p>

			<p>
				<a href="http://www.informatics.indiana.edu/graduate/spotlights/Gregg-Thomas.html" target="_blank">Read More</a>
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
pagefile = "archive.html";
print("Generating " + pagefile + "...");
title = "Gregg Thomas - Updates"

head = RC.readHead(title, pagefile);
nav = RC.readNav(pagefile);
links = RC.readLinks();
footer = RC.readFooter();

outfilename = "../../" + pagefile;

with open(outfilename, "w") as outfile:
    outfile.write(html_template.format(head=head, nav=nav, links=links, footer=footer));