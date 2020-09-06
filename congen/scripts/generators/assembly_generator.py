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
                    <li><a href="assembly.html#asm-qual">Assembly quality with N50</a></li>
                    <li><a href="assembly.html#busco">Assembly completeness with BUSCO</a></li>
                    <li><a href="assembly.html#index">Preparing assembly for analysis</a></li>
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
                    <div id="section-header">Assembly short reads with <a href="https://github.com/ablab/spades/" target="_blank">SPAdes</a></div>
                </div>
            </div>
            <div class="row" id="section-cont">
                <div class="col-24-24" id="section-col">
                    <div class="row" id="section-row">
                        <div class="col-2-24" id="inner-margin"></div>
                        <div class="col-20-24" id="section-content">

                            <p>SPAdes is a de Bruijn graph based assembler that can handle many types of data, both short and long reads, and can scaffold contigs together using read pairs or pre-assembled contigs.
                                It is highly automated, and combines results from graphs built from multiple values of k. SPAdes, while relatively fast among genome assemblers, still takes a while to run, 
                                so today we'll be running one assembly of <em>D. pseudoobscura</em> on short reads only and compare it to a pre-made assembly that uses both long and short reads.

                            <p>Let's start by generating the short read assembly:

                            <center><pre class="cmd"><code>spades.py -1 dpse-chr2-reads/illumina-subsample/chr2-1mil_1.fastq.gz -2 dpse-chr2-reads/illumina-subsample/chr2-1mil_2.fastq.gz -k 77 -o assemblies/spades-illumina-chr2-k77 -t 4 --isolate</code></pre></center>

                            <div class="table-cont">
                                <table class="cmd-table">
                                    <thead><th class="tcol-1">Command line parameter</th><th class="tcol-2">Description</th></thead>
                                    <tr>
                                        <td class="tcol-1">spades.py</td><td class="tcol-2">Call the main SPAdes interface script.</td>
                                    </tr>
                                    <tr>
                                        <td class="tcol-1">-1 dpse-chr2-reads/illumina/chr2-1mil_1.fastq.gz</td><td class="tcol-2">The path to the first read-pair file.</td>
                                    </tr>
                                    <tr>
                                        <td class="tcol-1">-2 dpse-chr2-reads/illumina/chr2-1mil_2.fastq.gz</td><td class="tcol-2">The path to the second read-pair file.</td>
                                    </tr>                                    
                                    <tr>
                                        <td class="tcol-1">-k 77</td><td class="tcol-2">The <em>k</em>-mer value. The length of sub-string overlaps used to construct the de Bruijn graph.</td>
                                    </tr>
                                    <tr>
                                        <td class="tcol-1">-o assemblies/spades-illumina-chr2-k77</td><td class="tcol-2">The path to the desired output directory.</td>
                                    </tr>
                                    <tr>
                                        <td class="tcol-1">-t 4</td><td class="tcol-2">The number of threads SPAdes can use. The default value is 16, but since there are 4 of us to a server we'll
                                            limit it to 4.</td>
                                    </tr>
                                    <tr>
                                        <td class="tcol-1">--isolate</td><td class="tcol-2">--isolate</td>
                                    </tr>
                                </table> 
                            </div>

                            <p>This will build the SPAdes assembly from the Illumina short reads. It should take about 4 minutes to run.</p>

                            <p>SPAdes creates many output files within the specified output directory. Normally, this would include assemblies for multiple k-values. 
                                The final assembly would be constructed by comparing portions of each of the <em>k</em>-mer graphs and selecting the most resolved regions. However,
                                due to time constraints, we have limited <code class="inline">spades</code> to one value of <em>k</em>=77.
                            </p>

                            <p>Recall that <em>k</em> is the length of the sub-strings used to construct the de Bruijn graph. Reads a broken up into all possible strings of length <em>k</em>.
                                Counterintuitively, this actually leads to smaller graphs than the overlap graphs, which use full reads, because in the de Bruijn graph, identical overlaps (repeats) are
                                collapsed into a single node:
                            </p>

                            <div class="row" id="img-row">
                                <div class="col-8-24" id="margin"></div>
                                <div class="col-8-24" id="img-col">
                                    <img id="res-img" src="img/pevzner-2001.png">
                                    <center><span class="fig-caption">Figure 3.2: Figure 2 from <a href="https://doi.org/10.1073/pnas.171285098" target="_blank">Pevzner 2001</a>
                                        showing how repeats are compacted in a de Bruijn graph.</span></center>
                                </div>
                                <div class="col-8-24" id="margin"></div>
                            </div>                                   

                            <p>Selection of <em>k</em> is critical. A <em>k</em> that is too low will mean your graph will have too many collapsed repeats and be unresolvable. Imagine a
                                <em>k</em>=2, which would essentially be a graph made up of the 4 nucleotides looping back on themselves. On the other hand, a <em>k</em> that is too high
                                could lead to graphs with too few overlaps, making the assembly of longer contigs impossible. Fortunately, most modern assembly algorithms (including SPAdes)
                                optimize over many values of <em>k</em>, obviating the need for <em>k</em>-mer selection by the user.
                            </p>

                            <p>The final assembly for this run will be in the file <code class="inline">assemblies/spades-illumina-chr2-k77/scaffolds.fasta</code>

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

                            <p>Here are some important statistics to consider when assessing a fragmented assembly:</p>

                            <div class="table-cont">
                                <table class="norm-table">
                                    <thead><th class="tcol-1">Statistic</th><th class="tcol-2">Description</th></thead>
                                    <tr>
                                        <td class="tcol-1"><code class="inline">Total assembly size</code></td><td class="tcol-2">The sum of the length of all contigs. 
                                            If you have an expected genome size from a closely related organism or other analysis, this can help determine how much of the genome you have assembled.</td>
                                    </tr>
                                    <tr>
                                        <td class="tcol-1"><code class="inline">N50</code></td><td class="tcol-2">The length, N, of the scaffold/contig such that 50% ofo the 
                                            assembly is contained in scaffolds of length N and longer. In other words, at least half of the nucleotides in the assembly belongs to contigs with the 
                                            N50 length or longer.</td>
                                    </tr>
                                    <tr>
                                        <td class="tcol-1"><code class="inline">L90</code></td><td class="tcol-2">The number of scaffolds that make up 90% of the assembly. Ideally close to the
                                            number of chromosomes in the sequenced organism.</td>
                                    </tr>
                                    <tr>
                                        <td class="tcol-1"><code class="inline">Number of Ns</code></td><td class="tcol-2">Bases that can't be confidently called, especially near contig junctions within
                                            scaffolds, are represented by Ns in the FASTA assembly file. Counting the total number of Ns can give you an idea of how well contigs were joined together
                                            into scaffolds.</td>
                                    </tr>
                                </table>
                            </div>

                            <p><code class="inline">N50</code> can be a little tricky to understand, luckily the Molecular Ecologist blog
                                has a <a href="https://www.molecularecologist.com/2017/03/whats-n50/" target="_blank">simple explainer post</a>, that has the following figure:

                            <div class="row" id="img-row">
                                <div class="col-6-24" id="margin"></div>
                                <div class="col-12-24" id="img-col">
                                    <img id="res-img" src="img/n50.png">
                                    <center><span class="fig-caption">Figure 3.2: Scaffold N50. Source: 
                                        <a href="https://www.molecularecologist.com/2017/03/whats-n50/" target="_blank">Molecular Ecologist</a></span></center>
                                </div>
                                <div class="col-6-24" id="margin"></div>
                            </div>

                            <p><code class="inline">L90</code> is similar, but using number of scaffolds instead of scaffold length.</p>

                            <p>These statistics are relatively easy to calculate, but there are also tools that can summarize these and more for a given assembly.
                                <a href="https://doi.org/10.1186/2047-217X-2-10" target="_blank">Assemblathon</a> was a competition to assess genome assemblers in 2013. They have helpfully made available
                                some of the scripts they use to quantify final genome assemblies in their <a href="https://doi.org/10.1186/2047-217X-2-10" target="_blank">github repository</a>. We will 
                                use one of their scripts to gather some basic statistics about a genome assembly.
                            </p>

                            <p>Instead of using the assembly we just produced, which is only of a single chromosome, we've provided several <em>D. pseudoobscura</em> genomes to compare in the
                                <code class="inline">expected-outputs/assemblies/</code> folder. Let's run the <code class="inline">assemblathon</code> script on one of them:
                            </p>

                            <center><pre class="cmd"><code>perl /usr/bin/assemblathon_stats.pl expected-outputs/assemblies/spades-illumina-only/scaffolds.fasta > assemblies/spades-illumina-only-assemblathon.txt</code></pre></center>

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
                                        <td class="tcol-1">expected-outputs/assemblies/illumina-only-spades/scaffolds.fasta</td><td class="tcol-2">The input FASTA file containing a genome assembly.</td>
                                    </tr>
                                    <tr>
                                        <td class="tcol-1">&gt;</td><td class="tcol-2">This redirects the output from the command specified before it into the file specified after it.</td>
                                    </tr>
                                    <tr>
                                        <td class="tcol-1">assemblies/spades-illumina-only-assemblathon.txt</td><td class="tcol-2">The desired output file.</td>
                                    </tr>
                                </table> 
                            </div>                        

                            <p>This should produce the file <code class="inline">assemblies/spades-illumina-only-assemblathon.txt</code> which contains several statistics about the assembly</p>

                            <p>Let's take a look at this file:</p>
                            
                            <center><pre class="cmd"><code>less -S assemblies/spades-illumina-only-assemblathon.txt</code></pre></center>
            
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
                                        <td class="tcol-1">assemblies/spades-illumina-only-assemblathon.txt</td><td class="tcol-2">The path to the file you want to view</td>
                                    </tr>
                                </table>
                            </div>

                            <p>This should display a nice table of statstics:</p>

                            <pre class="text"><code>---------------- Information for assembly 'assemblies/illumina-only-spades/scaffolds.fasta' ----------------


                                         Number of scaffolds     133829
                                     Total size of scaffolds  159563605
                                            Longest scaffold     656252
                                           Shortest scaffold         78
                                 Number of scaffolds > 1K nt       7924   5.9%
                                Number of scaffolds > 10K nt       2178   1.6%
                               Number of scaffolds > 100K nt        357   0.3%
                                 Number of scaffolds > 1M nt          0   0.0%
                                Number of scaffolds > 10M nt          0   0.0%
                                          Mean scaffold size       1192
                                        Median scaffold size        109
                                         N50 scaffold length      65232
                                          L50 scaffold count        626
                                                 scaffold %A      27.22
                                                 scaffold %C      22.57
                                                 scaffold %G      22.66
                                                 scaffold %T      27.43
                                                 scaffold %N       0.12
                                         scaffold %non-ACGTN       0.00
                             Number of scaffold non-ACGTN nt          0</code></pre>

                            <p>We know that <em>D. pseudoobscura</em> has a genome size of roughly 150Mb in 6 chromosomes. So the assembly size of <code class="inline">159563605</code>
                                is about right, but we've only been able to resolve <code class="inline">133829</code> scaffolds. No where near the 6 chromosomes we would ideally want.
                                Such a fragmented assembly could make annotation difficult with genes likely being split between scaffolds, and analysis of structural variation impossible.
                            </p>

                            <p>What about some other assemblies? We've provided several more assemblies of <em>D. pseudoobscura</em> in the <code class="list">expected-outputs/assemblies/</code> folder,
                                including a SPAdes assembly with long reads (PacBio + Nanopore), a <a href="https://github.com/fenderglass/Flye/" target="_blank">Flye</a>
                                assembly with just PacBio reads and a Flye assembly with just Nanopore reads. The assemblathon output files are there as well, but the statistics we've talked about
                                are summarized in the following table, as well as the latest published <em>D. pseudoobscura</em> genome on the SRA:
                            </p>

                            <div class="table-cont">
                                <table class="norm-table">
                                    <thead>
                                        <th>Statistic</th><th><a href="https://www.ncbi.nlm.nih.gov/assembly/GCF_009870125.1/" target="_blank">SRA assembly</a> (PacBio/Canu)</th>
                                        <th>SPAdes (Illumina only)</th>
                                        <th>SPAdes (PacBio+Nanopore)</th>
                                        <th>Flye (PacBio)</th>
                                        <th>Flye (Nanopore)</th>
                                    </thead>
                                    <tr>
                                        <td>Number of scaffolds</td>
                                        <td>70</td>
                                        <td>133829</td>
                                        <td>122980</td>
                                        <td>239</td>
                                        <td>1321</td>
                                    </tr>
                                    <tr>
                                        <td>Assembly size</td>
                                        <td>163282969</td>
                                        <td>159563605</td>
                                        <td>159513481</td>
                                        <td>158355727</td>
                                        <td>151695649</td>
                                    </tr>
                                    <tr>
                                        <td>Scaffold N50</td>
                                        <td>32422566</td>
                                        <td>65232</td>
                                        <td>110786</td>
                                        <td>17300572</td>
                                        <td>5886457</td>
                                    </tr>
                                    <tr>
                                        <td>L90</td>
                                        <td>NA</td>
                                        <td>12954</td>
                                        <td>7018</td>
                                        <td>15</td>
                                        <td>70</td>
                                    </tr>
                                    <tr>
                                        <td>% Ns</td>
                                        <td>NA</td>
                                        <td>0.12</td>
                                        <td>0.05</td>
                                        <td>0.00</td>
                                        <td>0.00</td>
                                    </tr>
                                </table>
                            </div>
                        
                            <p>Clearly the long read assemblies with the long read assembler (Flye) have higher N50s and fewer scaffolds than the SPAdes assemblies. Note that this doesn't mean SPAdes
                                is "worse" than Flye, it just means that for this type of data Flye is producing more contiguous assemblies. Also note that none of these assemblies alone produce scaffolds
                                approaching the SRA assembly for <em>D. pseudoobscura</em> (PacBio/Canu), which has only 70 scaffolds, most assigned to one of the 6 chromosomes.
                            </p>

                        </div>
                        <div class="col-2-24" id="inner-margin"></div>
                    </div>
                </div>
            </div>

            <a class="internal-link" name="busco"></a>
            <div class="row" id="section-header-cont">
                <div class="col-24-24" id="section-header-row">
                    <div id="section-header">Annotation quality with <a href="https://busco.ezlab.org/" target="_blank">BUSCO</a></div>
                </div>
            </div>
            <div class="row" id="section-cont">
                <div class="col-24-24" id="section-col">
                    <div class="row" id="section-row">
                        <div class="col-2-24" id="inner-margin"></div>
                        <div class="col-20-24" id="section-content">

                            <p>BUSCO, short for Benchmarking sets of Universal Single-Copy Orthologs, can help to assess the completeness of your genome with respect to gene content.
                                It does so by comparing gene sequences of well annotated species closely related to your species of interest to determine the number of Complete, Duplicated,
                                Fragmented, and Missing genes present in an assembly among a set of universal orthologs.
                            </p>

                            <p>You'll learn more about BUSCO in the next session, but for now we'll just take a look at a sample output from our SPAdes assemblies.</p>

                            <div class="row" id="img-row">
                                <div class="col-7-24" id="margin"></div>
                                <div class="col-10-24" id="img-col">
                                    <img id="res-img" src="img/busco-short.png">
                                    <center><span class="fig-caption">Figure 3.3: BUSCO results for the short read SPAdes assembly.</span></center>
                                </div>
                                <div class="col-7-24" id="margin"></div>
                            </div>     

                            <p></p>

                            <div class="row" id="img-row">
                                <div class="col-7-24" id="margin"></div>
                                <div class="col-10-24" id="img-col">
                                    <img id="res-img" src="img/busco-long.png">
                                    <center><span class="fig-caption">Figure 3.4: BUSCO results for the long read SPAdes assembly.</span></center>
                                </div>
                                <div class="col-7-24" id="margin"></div>
                            </div>     

                            <p>What we can see here is that, despite the short read assembly being much more fragmented, we still recover 98% of the universal copy orthologs,
                                identical to the long read alignment. Depending on the questions you are asking, short read assemblies may be sufficient.
                            </p>

                        </div>
                        <div class="col-2-24" id="inner-margin"></div>
                    </div>
                </div>
            </div>

            <a class="internal-link" name="index"></a>
            <div class="row" id="section-header-cont">
                <div class="col-24-24" id="section-header-row">
                    <div id="section-header">Preparing your assembly for analysis</div>
                </div>
            </div>
            <div class="row" id="section-cont">
                <div class="col-24-24" id="section-col">
                    <div class="row" id="section-row">
                        <div class="col-2-24" id="inner-margin"></div>
                        <div class="col-20-24" id="section-content">

                            <p>Now that we have a FASTA file that contains our genome assembly, and we know roughly how complete it is from a technical (N50) and biological (BUSCO)
                                perspective, we're ready to use it for analysis. Many downstream analyses require an assembly FASTA to be <b>indexed</b>. There are several types of 
                                indices and I usually make all of them for any assembly I work with. These indices are made with <code class="inline>samtools faidx</code>,
                                <code class="inline>bwa index</code>, and <code class="inline">picard CreateSequenceDictionary</code>.
                            </p>

                            <p>All of these are simple to generate. Today we'll just generate the <code class="inline">samtools faidx</code> for our pre-generated SPAdes Illumina assembly:</p>

                            <center><pre class="cmd"><code>samtools faidx expected-outputs/assemblies/spades-illumina-only/scaffolds.fasta</code></pre></center>
            
                            <div class="table-cont">
                                <table class="cmd-table">
                                    <thead><th class="tcol-1">Command line parameter</th><th class="tcol-2">Description</th></thead>
                                    <tr>
                                        <td class="tcol-1">samtools</td><td class="tcol-2">Call the <code class="inline">samtools</code> program</td>
                                    </tr>
                                    <tr>
                                        <td class="tcol-1">faidx</td><td class="tcol-2">Call the <code class="inline">faidx</code> sub-program within <code class="inline">samtools</code></td>
                                    </tr>
                                    <tr>
                                        <td class="tcol-1">expected-outputs/assemblies/spades-illumina-only/scaffolds.fasta</td><td class="tcol-2">The path to the FASTA file to index</td>
                                    </tr>
                                </table>
                            </div>

                            <p>This should run fairly quickly and will produce the file <code class="inline">expected-outputs/assemblies/spades-illumina-only/scaffolds.fasta.fai</code> file that we can look at</p>

                            <center><pre class="cmd"><code>less -S expected-outputs/assemblies/spades-illumina-only/scaffolds.fasta.fai</code></pre></center>
            
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
                                        <td class="tcol-1">expected-outputs/assemblies/spades-illumina-only/scaffolds.fasta/scaffolds.fasta.fai</td><td class="tcol-2">The path to the file you want to view</td>
                                    </tr>
                                </table>
                            </div>

                            <pre class="text"><code>NODE_1_length_656252_cov_29.014074      656252  36      60      61
NODE_2_length_575306_cov_27.441711      575306  667262  60      61
NODE_3_length_562891_cov_29.873761      562891  1252193 60      61
NODE_4_length_438072_cov_30.397365      438072  1824502 60      61
NODE_5_length_388373_cov_29.564742      388373  2269912 60      61
NODE_6_length_381978_cov_29.826266      381978  2664794 60      61
NODE_7_length_364204_cov_28.969093      364204  3053175 60      61
NODE_8_length_351331_cov_28.605180      351331  3423486 60      61
NODE_9_length_348425_cov_29.467863      348425  3780709 60      61
NODE_10_length_333664_cov_29.009230     333664  4134979 60      61
NODE_11_length_325795_cov_29.005299     325795  4474242 60      61
NODE_12_length_315498_cov_28.812061     315498  4805504 60      61
NODE_13_length_304746_cov_29.743095     304746  5126298 60      61
NODE_14_length_301147_cov_28.087172     301147  5436161 60      61
NODE_15_length_300141_cov_28.878596     300141  5742365 60      61
NODE_16_length_291038_cov_28.065040     291038  6047546 60      61
NODE_17_length_279739_cov_29.975989     279739  6343472 60      61
NODE_18_length_267631_cov_28.541939     267631  6627911 60      61
NODE_19_length_262557_cov_28.861460     262557  6900040 60      61</code></pre>

                            <p><code class="inline">.fai</code> files are pretty straightforward. They contain tab-delimited columns with information for one scaffold on each row. Column 1
                                indicates the scaffold name, Column 2 the length, Column 3 a byte index, Column 4 the number of bases per line, and Column 5 the number of bytes per line
                            </p>

                            <p>Other indices that we won't generate directly today include the BWA index files, which make it easier to map reads to an assembly:

                            <center><pre class="cmd-ne"><code>bwa index assemblies/spades-illumina/scaffolds.fasta</code></pre></center>
            
                            <div class="table-cont">
                                <table class="cmd-table">
                                    <thead><th class="tcol-1">Command line parameter</th><th class="tcol-2">Description</th></thead>
                                    <tr>
                                        <td class="tcol-1">bwa</td><td class="tcol-2">Call the <code class="inline">bwa</code> program</td>
                                    </tr>
                                    <tr>
                                        <td class="tcol-1">index</td><td class="tcol-2">Call the <code class="inline">index</code> sub-program within <code class="inline">bwa</code></td>
                                    </tr>
                                    <tr>
                                        <td class="tcol-1">assemblies/spades-illumina/scaffolds.fasta</td><td class="tcol-2">The path to the FASTA file to index</td>
                                    </tr>
                                </table>
                            </div>                            

                            <p>And the Picard Dictionary file, which used by variant callers such as GATK and other programs:

                            <center><pre class="cmd-ne"><code>Picard CreateSequenceDictionary I=assemblies/spades-illumina/scaffolds.fasta O=assemblies/spades-illumina/scaffolds.dict</code></pre></center>
            
                            <div class="table-cont">
                                <table class="cmd-table">
                                    <thead><th class="tcol-1">Command line parameter</th><th class="tcol-2">Description</th></thead>
                                    <tr>
                                        <td class="tcol-1">picard</td><td class="tcol-2">Call the <code class="inline">picard</code> program</td>
                                    </tr>
                                    <tr>
                                        <td class="tcol-1">CreateSequenceDictionary</td><td class="tcol-2">Call the <code class="inline">CreateSequenceDictionary</code> 
                                            sub-program within <code class="inline">picard</code></td>
                                    </tr>
                                    <tr>
                                        <td class="tcol-1">I=assemblies/spades-illumina/scaffolds.fasta</td><td class="tcol-2">The path to the FASTA file</td>
                                    </tr>
                                    <tr>
                                        <td class="tcol-1">O=assemblies/spades-illumina/scaffolds.dict</td><td class="tcol-2">The path to the desired output file</td>
                                    </tr>
                                </table>
                            </div>

                            <p>After you've generated and assessed the quality of your assembly, the next step is usually annotation. This usually means figuring out where repeats
                                are in the assembly and classifying their types, and figuring out where the genes in the assembly are. There are many ways to do this, enough to fill
                                up a separate workshop, so we won't be covering annotation today.</p>

                            <p>Next we will talk about an alternate to de novo genome assembly: reference guided assembly with <a href="mapping.html">read mapping</a>...

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