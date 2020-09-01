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

    <a class="internal-link" name="top"></a>
    <div class="row" id="header">Genome assembly</div>

    <div class="row" id="body-row">
        <div class="col-3-24" id="side-nav-cont">
            <div id="side-nav">
                <span id="side-header">Page contents</span>
                <ul>
                    <li><a href="assembly.html#top">Intro</a></li>
                    <li><a href="assembly.html#spades">Short read assembly with SPAdes</a></li>
                    <li><a href="assembly.html#flye">Long read assembly with Flye</a></li>
                    <li><a href="assembly.html#asm-qual">Assembly quality</a></li>
                </ul>
            </div>
        </div>

        <div class="col-21-24" id="main-cont">
            <div class="row" id="section-cont">
                <div class="col-24-24" id="section-col">
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

                            <!-- <p>As we discussed in the lecture, there are a couple differences between assembling short-reads and assembling long-reads. First, the underlying representation of the contig assembly
                                graph. Short reads can employ a de Bruijn graph based approach that uses k-mers to further break down the reads to find overlaps. This has the advantage of preventing pairwise
                                comparisons of all reads, which is computationally intensive. The de Bruijn graph can also use Eulerian path algorithms, which are easier to solve, and employ error-correction
                                based on structures in the assembly graph (i.e. bubbles and tips).</p>

                            <p>While long read assemblies can be done using de Bruijn graph based approaches, -->

                            <p>Today, we'll be using both long and short reads to assemble the <em>D. pseudoobscura</em> genome and then using several metrics to assess the resulting assemblies.</p>

                        </div>
                        <div class="col-2-24" id="inner-margin"></div>
                    </div>
                </div>
            </div>    

            <a class="internal-link" name="spades"></a>
            <div class="row" id="section-header-cont">
                <div class="col-24-24" id="section-header-row">
                    <div id="section-header">Assembly with short reads with <a href="https://github.com/ablab/spades/" target="_blank">SPAdes</a></div>
                </div>
            </div>
            <div class="row" id="section-cont">
                <div class="col-24-24" id="section-col">
                    <div class="row" id="section-row">
                        <div class="col-2-24" id="inner-margin"></div>
                        <div class="col-20-24" id="section-content">

                            <p>SPAdes is a de Bruijn graph based assembler that can handle many types of data, both short and long reads. It is highly automated, and combines results from graphs built from multiple
                                values of k. SPAdes, while relatively fast among genome assemblers, still takes a while to run, so today we'll be running one assembly of <em>D. pseudoobscura</em> on short reads only
                                and compare it to a pre-made assembly that uses both long and short reads.

                            <p>Let's start by generating the short read assembly:

                            <center><pre class="cmd"><code>spades.py -1 /dpse-2-reads/illumina/chr2-1mil_1.fastq.gz -2 /dpse-2-reads/illumina/chr2-1mil_1.fastq.gz -o assemblies/spades-illumina -t 16 --isolate</code></pre></center>

                            <div class="table-cont">
                                <table class="cmd-table">
                                    <thead><th class="tcol-1">Command line parameter</th><th class="tcol-2">Description</th></thead>
                                    <tr>
                                        <td class="tcol-1">spades.py</td><td class="tcol-2">Call the main SPAdes interface script.</td>
                                    </tr>
                                    <tr>
                                        <td class="tcol-1">-1 /dpse-2-reads/illumina/chr2-1mil_1.fastq.gz</td><td class="tcol-2">The path to the first read-pair file.</td>
                                    </tr>
                                    <tr>
                                        <td class="tcol-1">-2 /dpse-2-reads/illumina/chr2-1mil_2.fastq.gz</td><td class="tcol-2">The path to the second read-pair file.</td>
                                    </tr>
                                    <tr>
                                        <td class="tcol-1">-o assemblies/spades-illumina/</td><td class="tcol-2">The path to the desired output directory.</td>
                                    </tr>
                                    <tr>
                                        <td class="tcol-1">-t 16</td><td class="tcol-2">The number of threads SPAdes can use.</td>
                                    </tr>
                                    <tr>
                                        <td class="tcol-1">--isolate</td><td class="tcol-2">--isolate</td>
                                    </tr>
                                </table> 
                            </div>

                            <p>This will build the SPAdes assembly from the Illumina short reads. It should take about XX minutes to run.</p>

                            <p>SPAdes creates many output files within the specified output directory, including assemblies for multiple k-values. The final assembly will be constructed by comparing
                                portions of each of the k-mer graphs and selecting the most resolved regions
                            </p>

                            <p>The final assembly will be in the file <code class="inline">scaffolds.fasta</code>

                        </div>
                        <div class="col-2-24" id="inner-margin"></div>
                    </div>
                </div>
            </div>

            <a class="internal-link" name="asm-qual"></a>
            <div class="row" id="section-header-cont">
                <div class="col-24-24" id="section-header-row">
                    <div id="section-header">Assessing assembly quality</div>
                </div>
            </div>
            <div class="row" id="section-cont">
                <div class="col-24-24" id="section-col">
                    <div class="row" id="section-row">
                        <div class="col-2-24" id="inner-margin"></div>
                        <div class="col-20-24" id="section-content">

                        <p>One of the main goals for a genome assembly program is to produce assembly scaffolds approaching chromosome length. This is difficult because repeats can often form 
                            unresolvable portions of the underlying assembly graph that prevent the extension of a sequence. This means genome assemblies can be highly fragmented.</p>

                        <p><a href="https://doi.org/10.1186/2047-217X-2-10" target="_blank">Assemblathon</a> was a competition to assess genome assemblers in 2013. They have helpfully made available
                            some of the scripts they use to quantify final genome assemblies in their <a href="https://doi.org/10.1186/2047-217X-2-10" target="_blank">github repository</a>. We will 
                            use one of their scripts to gather some basic statistics about the genome assembly we just produced:
                        </p>

                        <center><pre class="cmd"><code>perl /usr/bin/assemblathon_stats.pl assemblies/illumina-only-spades/scaffolds.fasta > assemblies/illumina-assemblathon.txt</code></pre></center>

                        <div class="table-cont">
                            <table class="cmd-table">
                                <thead><th class="tcol-1">Command line parameter</th><th class="tcol-2">Description</th></thead>
                                <tr>
                                    <td class="tcol-1">perl</td><td class="tcol-2">Invoke <code class="inline">perl</code> to run a script.</td>
                                </tr>
                                <tr>
                                    <td class="tcol-1">/usr/bin/assemblathon_stats.pl</td><td class="tcol-2">The path to the <code class="inline">perl</code> script to run.</td>
                                </tr>
                                <tr>
                                    <td class="tcol-1">assemblies/illumina-only-spades/scaffolds.fasta</td><td class="tcol-2">The input FASTA file containing a genome assembly.</td>
                                </tr>
                                <tr>
                                    <td class="tcol-1">&gt;</td><td class="tcol-2">This redirects the output from the command specified before it into the file specified after it.</td>
                                </tr>
                                <tr>
                                    <td class="tcol-1">-t 16</td><td class="tcol-2">The number of threads SPAdes can use.</td>
                                </tr>
                                <tr>
                                    <td class="tcol-1">assemblies/illumina-assemblathon.txt</td><td class="tcol-2">The desired output file.</td>
                                </tr>
                            </table> 
                        </div>                        

                        <p>This should produce the file <code class="inline">assemblies/illumina-assemblathon.txt</code> which contains several statistics about the assembly</p>

                        <p>Let's take a look at this file:</p>
                        
                            <center><pre class="cmd"><code>less -S assemblies/illumina-assemblathon.txt</code></pre></center>
            
                            <div class="table-cont">
                                <table class="cmd-table">
                                    <thead><th class="tcol-1">Command line parameter</th><th class="tcol-2">Description</th></thead>
                                    <tr>
                                        <td class="tcol-1">less</td><td class="tcol-2">A Linux text file viewer 
                                            (use <code class="inline">&lt;up arrow&gt;</code> and <code class="inline">&lt;down arrow&gt;</code> to scroll up and down by one line 
                                            or <code class="inline">&lt;space&gt;</code> and <code class="inline">b</code> 
                                            to scroll up and down by one page, resepectively. Type <code class="inline">q</code> to exit)</td>
                                    </tr>
                                    <tr>
                                        <td class="tcol-1">-S</td><td class="tcol-2">Turn off line-wrapping within <code class="inline">less</code> 
                                            (use the <code class="inline">&lt;left arrow&gt;</code> and <code class="inline">&lt;right arrow&gt;</code> to scroll left and right).</td>
                                    </tr>
                                    <tr>
                                        <td class="tcol-1">assemblies/illumina-assemblathon.txt</td><td class="tcol-2">The path to the file you want to view</td>
                                    </tr>
                                </table>
                            </div>




                        </div>
                        <div class="col-2-24" id="inner-margin"></div>
                    </div>
                </div>
            </div>

        </div>
    </div>

    <div class="row" id="btm-nav">
        <div class="col-3-24" id="nav-bnt-margin"></div>
        <div class="col-6-24" id="nav-btn-cont">
            <div class="nav-btn">
                <a href="reads.html">&lt;&nbsp;Previous</a>    
            </div>
        </div>
        <div class="col-6-24" id="nav-margin"></div>
        <div class="col-6-24" id="nav-btn-cont">
            <div class="nav-btn">
                <a href="mapping.html">Next&nbsp;&gt;</a>
            </div>
        </div>
        <div class="col-3-24" id="nav-btn-margin"></div>
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