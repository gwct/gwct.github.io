############################################################
# For personal site, 11.19
# This generates the file "archive.html"
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

	<div class="pure-g" id="main_div_arc">
		<div class="pure-u-24-24" id="header">Updates</div>
		<div class="pure-u-2-24" id="margin"></div>
		<div class="pure-u-20-24" id="arc_text">
			<div id="arc_entry">
				<div class="section_header_cont"><div class="section_header">December 26, 2019</div></div>
				<ul>
					<p>I recently (Nov. 1, 2019) gave a <a href="http://www.cooper-lab.org/chalk.html" target="_blank">CHALK</a> talk to my colleagues here
						at the University of Montana about my reasearch (past and future). It was a great learning experience for me to give a talk in this format.</p>

					<p>Jeff and I also recently (Nov. 10-13, 2019) visited the <a href="https://www.lsu.edu/mns/" target="_blank">LSU Museum of Natural Science</a> 
						to discuss upcoming collaborations with rodent specialists <a href="https://esselstyn.github.io/" target="_blank">Jake Esselstyn</a>, 
						<a href="https://museumsvictoria.com.au/about-us/staff/natural-sciences/terrestrial-zoology/dr-kevin-rowe/" target="_blank">Kevin Rowe</a>,
						and <a href="https://scholar.google.com/citations?user=iVRhKXQAAAAJ&hl=en&oi=ao" target="_blank">Carl Hutter</a>.
						This was a great opportunity to spend time with these scientists in the Museum and meet others at LSU!</p>
				</ul>
			</div>
			<div class="pure-u-24-24" id="arc_sep_div"></div>

			<div id="arc_entry">
				<div class="section_header_cont"><div class="section_header">August 2, 2019</div></div>
				<ul>
					<p>On July 1, 2019 I successfully defended my dissertation! It is titled 
						<a href="https://scholarworks.iu.edu/dspace/handle/2022/23333" target="_blank">The causes of mutation and substitution rate variation in primates</a>
						and is available open access at that link thanks to <a href="https://scholarworks.iu.edu/" target="_blank">IUScholarWorks</a>.</p>

					<p>I have subsequently moved to the <a href="http://hs.umt.edu/dbs/">University of Montana</a> in Missoula to start my postdoc work in 
						<a href="http://www.thegoodlab.org/" target="_blank">Jeff Good's lab</a>. Here I'll continue to work on some of the fundamental questions
						of phylogenetics and genome evolution using the great model system of murine rodents!</p>
				</ul>
			</div>
			<div class="pure-u-24-24" id="arc_sep_div"></div>
	
			<div id="arc_entry">
				<div class="section_header_cont"><div class="section_header">August 9, 2018</div></div>
				<ul>
					<p>On September 5th, I'll be hosting the <a href="http://i5k.github.io/webinar" target="_blank">i5K webinar</a>
					and discussing our work on the i5K pilot project to examine genome evolution across 76 species of Arthropods.</p>
					<p>Check out the pre-print of the paper on <a href="https://www.biorxiv.org/content/early/2018/08/04/382945" target="_blank">bioRxiv</a>!</p>
				</ul>
			</div>
			<div class="pure-u-24-24" id="arc_sep_div"></div>

			<div id="arc_entry">
				<div class="section_header_cont"><div class="section_header">June 13, 2018</div></div>
				<ul>
					<p>I have been featured in an article on IU's IT News & Events for my use of the 
					high-performance computing clusters to perform large-scale genomic analyses!</p>
					<p><a href="https://itnews.iu.edu/articles/2018/IU%20doctoral%20student%20explores%20the%20history%20of%20life%20on%20Earth%20.php" target="_blank">Read More</a></p>
				</ul>
			</div>
			<div class="pure-u-24-24" id="arc_sep_div"></div>

			<div id="arc_entry">
				<div class="section_header_cont"><div class="section_header">May 8, 2018</div></div>
				<ul>
				 	<p>I will be giving a talk at <a href="http://conferences.genetics-gsa.org/peqg/2018/index" target="_blank">PEQG</a> 
					this year about my recent work on mutation rates in primates! My talk is Tuesday, May 15 at 12:30PM.</p>
				</ul>
			</div>
			<div class="pure-u-24-24" id="arc_sep_div"></div>

			<div id="arc_entry">
				<div class="section_header_cont"><div class="section_header">June 9, 2017</div></div>
				<ul>
					<p>I will also be giving my talk about my work with the i5k project at Evolution 
					this year in Portland. My talk is in the 'Phylogenomics 1' session at 8:30AM on Monday June 26.</p>
				</ul>
			</div>
			<div class="pure-u-24-24" id="arc_sep_div"></div>

			<div id="arc_entry">
				<div class="section_header_cont"><div class="section_header">January 31, 2017</div></div>
				<ul>
					<p>I have been invited to speak at the Arthropod Genomics Symposium at Notre Dame University in June.
					I'll be talking about my work in the i5k initiative on large scale gene family analysis. My first invited talk!</p>
				</ul>
			</div>
			<div class="pure-u-24-24" id="arc_sep_div"></div>

			<div id="arc_entry">
				<div class="section_header_cont"><div class="section_header">May 20, 2016</div></div>
				<ul>
					<p>I'll be giving a talk at this year's
					<a href="http://www.evolutionmeetings.org/evolution-2016---austin-texas.html" target="_blank"> Evolution Meeting</a> in Austin.</p>

					<p><b>UPDATE: June 11, 2016</b> -- The title of my talk is "Gene tree reconciliation using MUL-trees resolves polyploidy events" and will
					be on Sunday June 19 at 9:15AM in the Phylogenetics methods development 3 symposium (MR5).</p>

					<p>Check out the pre-print of the paper on <a href="http://biorxiv.org/content/early/2016/06/10/058149" target="_blank">bioRxiv</a>!</p>
				</ul>
			</div>
			<div class="pure-u-24-24" id="arc_sep_div"></div>

			<div id="arc_entry">
				<div class="section_header_cont"><div class="section_header">April 02, 2016</div></div>
				<ul>
					<p>I was recently featured in a spotlight on the IU School of Informatics website!</p>
					<p><a href="http://www.informatics.indiana.edu/graduate/spotlights/Gregg-Thomas.html" target="_blank">Read More</a></p>
				</ul>
			</div>
			<div class="pure-u-24-24" id="arc_sep_div"></div>

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