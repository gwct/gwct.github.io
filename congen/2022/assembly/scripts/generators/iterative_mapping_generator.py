############################################################
# For ConGen2020 site, 08.20
# This generates the file "iterative-mapping.html"
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

    {banner}

    <a class="internal-link" name="ref-bias"></a>
   	<div class="row" id="header">Iterative Read Mapping</div>

    <div class="row" id="body-row">
        <div class="col-3-24" id="side-nav-cont">
            <div id="side-nav">
                <span id="side-header">Page contents</span>
                <ul>
                    <li><a href="iterative-mapping.html#ref-bias">Reference bias</a></li>
                    <li><a href="iterative-mapping.html#pseudo-it">Iterative mapping with pseudo-it</a></li>
                    <li><a href="iterative-mapping.html#iters">Reference bias reduction</a></li>
                </ul>
            </div>
        </div>

        <div class="col-21-24" id="main-cont">
            <div class="row" id="top-row-cont">
                <div class="col-24-24" id="top-row"></div>
            </div>

            <div class="row" id="section-header-cont">
                <div class="col-24-24" id="section-header-row">
                    <div id="section-header">Reference bias</div>
                </div>
            </div>
            <div class="row" id="section-cont">
                <div class="col-24-24" id="section-col">
                    <div class="row" id="section-row">
                        <div class="col-2-24" id="inner-margin"></div>
                        <div class="col-20-24" id="section-content">

                            <p>Reference bias occurs during read mapping and causes the mapped reads to more closely resemble the reference genome than it actually does. This happens because alignment programs
                                inherently favor alignments with a greater number of matches and with read mapping we are aligning sequences that do not match. Conceptually, this is well defined. But other than 
                                <a href="https://doi.org/10.1093/gbe/evx034" target="_blank">Sarver et al. 2017</a>, little has been done to directly quantify the effects of reference bias. 
                                However, we can layout some expectations:
                            </p>

                            <ol>
                                <li>Reference bias will lead to lower divergence estimates between the reference species and the mapped species.</li>
                                <li>When mapping multiple species to a single reference, all species will appear to be more similar with respect to sequence.</li>
                                <li>Reference bias can lead to false negatives in downstream analyses.</li>
                            </ol>

                            <p>Briefly, reference bias occurs because some reads remain unmapped during the read mapping process. This can happen because they contain many sequencing errors (red below) OR because
                                they contain many actual variants (green below):
                            </p>

                            <div class="row" id="img-row">
                                <div class="col-4-24" id="margin"></div>
                                <div class="col-16-24" id="img-col">
                                    <img id="res-img" src="img/iterative-mapping-1.png">
                                    <center><span class="fig-caption">Figure 5.1: Unmapped reads can be reads containing errors (dark red) and/or variants (green).</span></center>
                                </div>
                                <div class="col-4-24" id="margin"></div>
                            </div>

                            <p>All of those unmapped reads with variants lead to our final consensus sequence looking more like the reference than it should.</p>

                        </div>
                        <div class="col-2-24" id="inner-margin"></div>
                    </div>
                </div>
            </div>

            <a class="internal-link" name="pseudo-it"></a>
            <div class="row" id="section-header-cont">
                <div class="col-24-24" id="section-header-row">
                    <div id="section-header">Iterative read mapping with <a href="https://github.com/goodest-goodlab/pseudo-it" target="_blank">pseudo-it</a></div>
                </div>
            </div>
            <div class="row" id="section-cont">
                <div class="col-24-24" id="section-col">
                    <div class="row" id="section-row">
                        <div class="col-2-24" id="inner-margin"></div>
                        <div class="col-20-24" id="section-content">

                            <p>Pseudo-it is software designed to mitigate the effects of reference bias by using an iterative mapping approach to generate pseudo-reference assemblies. It performs the following
                                steps:
                            </p>

                            <ol>
                                <li>Map reads to a <b>reference</b> genome.</li>
                                <li>Call variants based on the mapped reads.</li>
                                <li>Generate a consensus sequence using the called variants.</li>
                                <li>Repeat the process, but instead of mapping reads to the <b>reference</b>, map them to the newly generated <b>consensus</b> sequence.</li>
                            </ol>

                            <p>The idea here is to generate a sequence that incorporates the variation that has been mapped to allow mapping of the reads that were previously too divergent:</p>

                            <div class="row" id="img-row">
                                <div class="col-4-24" id="margin"></div>
                                <div class="col-16-24" id="img-col">
                                    <img id="res-img" src="img/iterative-mapping-2.png">
                                    <center><span class="fig-caption">Figure 5.2: Iterative mapping incorporates mapped variation to allow for more reads to be mapped.</span></center>
                                </div>
                                <div class="col-4-24" id="margin"></div>
                            </div>

                            <p>The first version of this software (<a href="https://doi.org/10.1093/gbe/evx034" target="_blank">Sarver et al. 2017</a>) used BWA to map reads and GATK 3. to call variants. 
                                It was shown to increase estimated divergence in a set of mouse exomes:</p>
                
                            <div class="row" id="img-row">
                                <div class="col-6-24" id="margin"></div>
                                <div class="col-12-24" id="img-col">
                                    <img id="res-img" src="img/sarver-fig1.png">
                                    <center><span class="fig-caption">Figure 5.3: Divergence increases (A) and bias decreases (B) over iterations of mapping in several mouse species when mapping to the same reference genome 
                                        (<a href="https://doi.org/10.1093/gbe/evx034" target="_blank">Sarver et al. 2017</a>).</span></center>
                                </div>
                                <div class="col-6-24" id="margin"></div>
                            </div>               

                            <p>The newest version that we'll be using today will still use BWA, but is upgraded to use GATK 4 and incorporates indels in the final pseudo-assembly. Let's try it out!</p>

                            <p>First, let's navigate back to the main project directory:</p>

                            <center><pre class="cmd"><code>cd ..</code></pre></center>

                            <div class="table-cont">
                                <table class="cmd-table">
                                    <thead><th class="tcol-1">Command line parameter</th><th class="tcol-2">Description</th></thead>
                                    <tr>
                                        <td class="tcol-1">cd</td><td class="tcol-2">The Linux change directory command.</td>
                                    </tr>
                                    <tr>
                                        <td class="tcol-1">..</td><td class="tcol-2">The path to the directory you want to change to. <code class="inline">..</code> is a shortcut that means "one directory up".</td>
                                    </tr>
                                </table> 
                            </div>

                            <p>And now we can run <code class="inline">psuedo-it</code> on <em>D. pseudoobscura</em> chromosome 2 with two iterations:</p>

                            <center><pre class="cmd"><code>pseudo_it -ref dmel-3R-reference/Drosophila_melanogaster.BDGP6.28.dna.chromosome.3R.fa -pe1 dpse-chr2-reads/illumina/pse-chr2_1.fastq.gz -pe2 dpse-chr2-reads/illumina/pse-chr2_2.fastq.gz -i 2 -p 4 -o dpse-pseudo-it</code></pre></center>

                            <div class="table-cont">
                                <table class="cmd-table">
                                    <thead><th class="tcol-1">Command line parameter</th><th class="tcol-2">Description</th></thead>
                                    <tr>
                                        <td class="tcol-1">pseudo_it</td><td class="tcol-2">Call the <code class="inline">pseudo_it</code> program.</td>
                                    </tr>
                                    <tr>
                                        <td class="tcol-1">-ref dmel-3R-reference/Drosophila_melanogaster.BDGP6.28.dna.chromosome.3R.fa</td><td class="tcol-2">Tells <code class="inline">pseudo_it</code> the path to the
                                        reference genome to which we are mapping. In this case, we'll be mapping to <em>D. melanogaster</em> chromosome 3R.</td>
                                    </tr>
                                    <tr>
                                        <td class="tcol-1">-pe1 dpse-chr2-reads/illumina/pse-chr2_1.fastq.gz</td><td class="tcol-2">Tells <code class="inline">pseudo_it</code> the path to the file containing the first pairs of reads.</td>
                                    </tr>
                                    <tr>
                                        <td class="tcol-1">-pe2 dpse-chr2-reads/illumina/pse-chr2_2.fastq.gz</td><td class="tcol-2">Tells <code class="inline">pseudo_it</code> the path to the file containing the second pairs of reads.</td>
                                    </tr>
                                    <tr>
                                        <td class="tcol-1">-i 2</td><td class="tcol-2">This option sets <code class="inline">pseudo_it</code> to run 2 iterations.</td>
                                    </tr>
                                    <tr>
                                        <td class="tcol-1">-p 4</td><td class="tcol-2">This option tells <code class="inline">pseudo_it</code> to use 4 cores when mapping and calling variants. 
                                            For a whole genome, I would recommend 4 cores per chromosomes</td>
                                    </tr>
                                    <tr>
                                        <td class="tcol-1">-o dpse-pseudo-it</td><td class="tcol-2">This tells <code class="inline">pseudo_it</code> the desired output directory. This directory will be created if it does not exist.</td>
                                    </tr>                    
                                </table> 
                            </div>

                            <p>This will perform the steps outlined above twice (mapping, variant calling, consensus) and will save the relevant files for each iteration, including a final consensus FASTA file as
                                a pseudo-assembly. You can explore the output folder <code class="inline">dpse-pesudo-it</code> to see what's there. You can view its progress on the screen as it runs.
                            </p>

                            <p>Note that this runs an entire gamut of mapping, variant calling, and consensus sequence generation, which can take a very long time (about 1 week for a mammalian whole genome with 4 iterations
                                and 4 cores per chromosome). Even for our single chromosome from <em>D. pseudoobscura</em> this would take over an hour. So let's go ahead and cancel this run by hitting
                                <code class="inline">&lt;ctrl&gt;+c</code> while the Terminal is selected.
                            </p>

                                <div id="msg_cont">
                                    <div id="msg">
                                        <div id="msg_banner">Tip - Cancelling command line programs</div>
                                        <div id="msg_text">
                                            <p>
                                                Sometimes you'll start a command and realize something is wrong or decide you want to do something else, so you'll want to <b>cancel</b> the command.
                                                In a bash terminal this is done with the following keystroke:
                                            </p>

                                            <center><code class="inline">&lt;ctrl&gt;+c</code></center>

                                            <p>But be careful not to stop a program you want to keep running!</p>

                                            <p></p>
                                        </div>
                                    </div>
                                </div>
                                <p></p>                       

                        </div>
                        <div class="col-2-24" id="inner-margin"></div>
                    </div>
                </div>
            </div>
        
            <a class="internal-link" name="iters"></a>
            <div class="row" id="section-header-cont">
                <div class="col-24-24" id="section-header-row">
                    <div id="section-header">Quantifying the reduction in reference bias</div>
                </div>
            </div>
            <div class="row" id="section-cont">
                <div class="col-24-24" id="section-col">
                    <div class="row" id="section-row">
                        <div class="col-2-24" id="inner-margin"></div>
                        <div class="col-20-24" id="section-content">

                            <p>In order to see how <code class="inline">pseudo-it</code> has reduced reference bias, we would first need to generate the consensus sequence after <b>one iteration</b>:</p>

                            <center><pre class="cmd-ne"><code>pseudo_it -ref dmel-3R-reference/Drosophila_melanogaster.BDGP6.28.dna.chromosome.3R.fa -pe1 dpse-chr2-reads/illumina/pse-chr2_1.fastq.gz -pe2 dpse-chr2-reads/illumina/pse-chr2_2.fastq.gz -i 1 -p 4 -resume dpse-pseudo-it</code></pre></center>

                            <div class="table-cont">
                                <table class="cmd-table">
                                    <thead><th class="tcol-1">Command line parameter</th><th class="tcol-2">Description</th></thead>
                                    <tr>
                                        <td class="tcol-1">pseudo_it</td><td class="tcol-2">Call the <code class="inline">pseudo_it</code> program.</td>
                                    </tr>
                                    <tr>
                                        <td class="tcol-1">-ref dmel-3R-reference/Drosophila_melanogaster.BDGP6.28.dna.chromosome.3R.fa</td><td class="tcol-2">Tells <code class="inline">pseudo_it</code> the path to the
                                        reference genome to which we are mapping. In this case, we'll be mapping to <em>D. melanogaster</em> chromosome 3R.</td>
                                    </tr>
                                    <tr>
                                        <td class="tcol-1">-pe1 dpse-2-reads/illumina/pse-chr2_1.fastq.gz</td><td class="tcol-2">Tells <code class="inline">pseudo_it</code> the path to the file containing the first pairs of reads.</td>
                                    </tr>
                                    <tr>
                                        <td class="tcol-1">-pe2 dpse-2-reads/illumina/pse-chr2_2.fastq.gz</td><td class="tcol-2">Tells <code class="inline">pseudo_it</code> the path to the file containing the second pairs of reads.</td>
                                    </tr>
                                    <tr>
                                        <td class="tcol-1">-i 1</td><td class="tcol-2">This option sets <code class="inline">pseudo_it</code> to run 1 iteration.</td>
                                    </tr>
                                    <tr>
                                        <td class="tcol-1">-p 4</td><td class="tcol-2">This option tells <code class="inline">pseudo_it</code> to use 4 cores when mapping and calling variants.
                                            For a whole genome, I would recommend 4 cores per chromosomes</td>
                                    </tr>
                                    <tr>
                                        <td class="tcol-1">-resume dpse-pseudo-it</td><td class="tcol-2">Using the <code class="inline">resume</code> flag tells <code class="inline">pseudo_it</code> that some of the files have already been generated in this
                                            directory and it will try to resume the pipeline. In this case, we've already mapped reads for the first iteration so it shouldn't need to do that again.</td>
                                    </tr>                    
                                </table> 
                            </div>

                            <p>However, since this would also take some time, we'll just move forward with the provided expected output in <code class="inline">dpse-pseudo-it</code>.</p>
                            
                            <p>Remember, reference bias makes mapped reads look more similar to the reference that expected, so we can outline a couple of expectations to test:</p>

                            <ol>
                                <li>More reads should map to the second iteration.</li>
                                <li>The consensus sequence from the second iteration should appear to be more diverged.</li>
                            </ol>

                            <a name="more-reads"></a>	
                            <h3>01. More reads should map to the second iteration</h3>

                                <p>This is fairly easy to check with <code class="inline">samtools flagstat</code>. First, we can run flagstat on the BAM file from the first iteration:</p>

                                <center><pre class="cmd"><code>samtools flagstat expected-outputs/dpse-pseudo-it/iter-01/bam/merged-rg-mkdup-iter-01.bam.gz</code></pre></center>

                                <div class="table-cont">
                                    <table class="cmd-table">
                                        <thead><th class="tcol-1">Command line parameter</th><th class="tcol-2">Description</th></thead>
                                        <tr>
                                            <td class="tcol-1">samtools</td><td class="tcol-2">Call the <code class="inline">samtools</code> program.</td>
                                        </tr>
                                        <tr>
                                            <td class="tcol-1">flagstat</td><td class="tcol-2">Use the <code class="inline">flagstat</code> sub-program implemented within <code class="inline">samtools</code>.</td>
                                        </tr>
                                        <tr>
                                            <td class="tcol-1">expected-outputs/dpse-pseudo-it/iter-01/bam/merged-rg-mkdup-iter-01.bam.gz</td><td class="tcol-2">The path to the input BAM file.</td>
                                        </tr>
                                    </table>
                                </div>

                                <p>This results in the following output:</p>

                                <pre class="text"><code>404438 + 0 mapped (37.53% : N/A)</code></pre> 
                                
                                <p>Now let's check the second iteration:</p>

                                <center><pre class="cmd"><code>samtools flagstat expected-outputs/dpse-pseudo-it/iter-02/bam/merged-rg-mkdup-iter-02.bam.gz</code></pre></center>

                                <div class="table-cont">
                                    <table class="cmd-table">
                                        <thead><th class="tcol-1">Command line parameter</th><th class="tcol-2">Description</th></thead>
                                        <tr>
                                            <td class="tcol-1">samtools</td><td class="tcol-2">Call the <code class="inline">samtools</code> program.</td>
                                        </tr>
                                        <tr>
                                            <td class="tcol-1">flagstat</td><td class="tcol-2">Use the <code class="inline">flagstat</code> sub-program implemented within <code class="inline">samtools</code>.</td>
                                        </tr>
                                        <tr>
                                            <td class="tcol-1">expected-outputs/dpse-pseudo-it/iter-02/bam/merged-rg-mkdup-iter-02.bam.gz</td><td class="tcol-2">The path to the input BAM file.</td>
                                        </tr>
                                    </table>
                                </div>

                                <pre class="text"><code>420425 + 0 mapped (38.97% : N/A)</code></pre>

                                <p>A modest increase in this example, but an increase nonetheless.</p>

                                <p>Another effect of more reads mapping is that we should have higher average read depth per iteration. Recall that with our original mappings (one iteration), we calculated
                                    an average read depth on this chromosome of <b>3.95</b>, even though our expected coverage based on the Lander/Waterman equation was about <b>5</b>. Let's see if our
                                    iterative mapping has improved read depth.
                                </p>

                                <p>Then, like before, let's run <code class="inline">samtools depth</code> on our BAM file:</p>

                                <center><pre class="cmd"><code>samtools depth expected-outputs/dpse-pseudo-it/iter-02/bam/merged-rg-mkdup-iter-02.bam.gz > dpse2-to-dmel3R-pi2-depth.tab</code></pre></center>
                
                                <div class="table-cont">
                                    <table class="cmd-table">
                                        <thead><th class="tcol-1">Command line parameter</th><th class="tcol-2">Description</th></thead>
                                        <tr>
                                            <td class="tcol-1">samtools</td><td class="tcol-2">Call the <code class="inline">samtools</code> program.</td>
                                        </tr>
                                        <tr>
                                            <td class="tcol-1">depth</td><td class="tcol-2">Use the <code class="inline">depth</code> sub-program within <code class="inline">samtools</code>.</td>
                                        </tr>
                                        <tr>
                                            <td class="tcol-1">expected-outputs/dpse-pseudo-it/iter-02/bam/merged-rg-mkdup-iter-02.bam.gz</td><td class="tcol-2">The input BAM/SAM file.</td>
                                        </tr>
                                        <tr>
                                            <td class="tcol-1">&gt;</td><td class="tcol-2">This redirects the output that would have been printed to the screen to a file instead.</td>
                                        </tr>
                                        <tr>
                                            <td class="tcol-1">dpse2-to-dmel3R-pi2-depth.tab</td><td class="tcol-2">The desired output file</td>
                                        </tr>
                                    </table>
                                </div>

                                <p>And let's calculate average depth with our custom R script:</p>

                                <center><pre class="cmd"><code>Rscript scripts/depth_plot.r dpse2-to-dmel3R-pi2-depth.tab</code></pre></center>
                
                                <div class="table-cont">
                                    <table class="cmd-table">
                                        <thead><th class="tcol-1">Command line parameter</th><th class="tcol-2">Description</th></thead>
                                        <tr>
                                            <td class="tcol-1">Rscript</td><td class="tcol-2">Invokes R to run the script.</td>
                                        </tr>
                                        <tr>
                                            <td class="tcol-1">../scripts/depth_plot.r</td><td class="tcol-2">The path to the script.</td>
                                        </tr>
                                        <tr>
                                            <td class="tcol-1">dpse2-to-dmel3R-pi2-depth.tab</td><td class="tcol-2">The input file.</td>
                                        </tr>
                                    </table>
                                </div>

                                <p>This will generate a read depth histogram (<code class="inline">depth-hist.png</code>) and tell us the average read depth:
                                </p>

                                <pre class="text"><code># Avg. read depth: 4.174893</code></pre> 

                                <p>Again, a modest increase from 3.95, but a step in the right direction, showing that iterative mapping improves read depth.</p>
                            
                            <a name="lower-pi"></a>	
                            <h3>02. The consensus sequence from the second iteration should appear to be more diverged.</h3>

                                <p>There are many ways to calculate divergence. We'll use the simplest one: the percent identity, or the number of sites that match between the alignment of two sequences.
                                    To do that we'll first need to generate some alignments.
                                </p>

                                <p>To generate alignments between these two chromosomes, we'll actually be using a long-read mapper called <a href="https://github.com/lh3/minimap2" target="_blank">minimap2</a>.
                                    I've found this program useful for generating between species chromosome alignments.
                                </p>

                                <p>Next, let's use <code class="inline">minimap2</code> to generate an alignment between the first iteration of mapping and the original <em>D. melanogaster</em> 3R reference:</p>

                                <center><pre class="cmd"><code>minimap2 -x asm10 dmel-3R-reference/Drosophila_melanogaster.BDGP6.28.dna.chromosome.3R.fa expected-outputs/dpse-pseudo-it/iter-01/fa/iter-01-final.fa > alignments/dpse-2-pi-1-to-dmel3.paf</code></pre></center>

                                <div class="table-cont">
                                    <table class="cmd-table">
                                        <thead><th class="tcol-1">Command line parameter</th><th class="tcol-2">Description</th></thead>
                                        <tr>
                                            <td class="tcol-1">minimap2</td><td class="tcol-2">Call the <code class="inline">minimap2</code> program.</td>
                                        </tr>
                                        <tr>
                                            <td class="tcol-1">-x asm10</td><td class="tcol-2">Set this to indicate assembly-to-reference mapping.</td>
                                        </tr>
                                        <tr>
                                            <td class="tcol-1">dmel-3R-reference/Drosophila_melanogaster.BDGP6.28.dna.chromosome.3R.fa</td><td class="tcol-2">The path to the reference genome FASTA file. 
                                                In this case, <em>D. melanogaster</em> chromosome 3R.</td>
                                        </tr>
                                        <tr>
                                            <td class="tcol-1">expected-outputs/dpse-pseudo-it/iter-01/fa/iter-01-final.fa</td><td class="tcol-2">The path to the assembly FASTA file. In this case, the consensus sequence of <em>D. pseudoobscura</em>
                                                after <b>one</b> iteration of mapping.</td>
                                        </tr>
                                        <tr>
                                            <td class="tcol-1">&gt;</td><td class="tcol-2">This redirects the output that would have been printed to the screen to a file instead.</td>
                                        </tr>
                                        <tr>
                                            <td class="tcol-1">alignments/dpse-2-pi-1-to-dmel3.paf</td><td class="tcol-2">The desired output file.</td>
                                        </tr>
                                    </table> 
                                </div>

                                <p><code class="inline">minimap2</code> output can be formatted in two ways, the BAM format we are familiar with or PAF, the pairwise alignment format. I believe this format is unique to 
                                    <code class="inline">minimap2</code>, but is simply a tab-delimited file that contains informationo about blocks that have been aligned, such as sequence ID, start position, number of
                                    matching bases, etc.
                                </p>

                                <p>Let's take a look at this particular PAF file:</p>

                                <center><pre class="cmd"><code>less -S alignments/dpse-2-pi-1-to-dmel3.paf</code></pre></center>

                                <div class="table-cont">
                                    <table class="cmd-table">
                                        <thead><th class="tcol-1">Command line parameter</th><th class="tcol-2">Description</th></thead>
                                        <tr>
                                            <td class="tcol-1">less</td><td class="tcol-2">A Linux text file viewer (use space to scroll down, b to scroll up, and q to exit)</td>
                                        </tr>
                                        <tr>
                                            <td class="tcol-1">-S</td><td class="tcol-2">Turn off line-wrapping within less (use the left and right arrow keys to scroll left and right).</td>
                                        </tr>
                                        <tr>
                                            <td class="tcol-1">alignments/dpse-2-pi-1-to-dmel3.paf</td><td class="tcol-2">The path to the file you want to view</td>
                                        </tr>
                                    </table>
                                </div>

                                <pre class="text"><code>3R      32168558        50522   32168555        +       3R      32079331        50522   32079328        30591593        32177084        60      tp:A:P  cm:i:3034393    s1:i:30543658   s2:i:25089      dv:f:0.0028 rl:i:147655
3R      32168558        5       44485   +       3R      32079331        5       44485   23645   44480   60      tp:A:P  cm:i:2055       s1:i:23645      s2:i:3382       dv:f:0.0000     rl:i:147655</code></pre> 

                                <p>This shows that between the <em>D. pesudoobscura</em> pseudo-reference of chromosome 2 and the <em>D. melanogaster</em> reference of 
                                    chromosome 3R there are two large blocks that could be confidently aligned (one block per line).</p>

                                <p>The following table explains the PAF columns explicitly:</p>

                                <div class="row" id="img-row">
                                    <div class="col-8-24" id="margin"></div>
                                    <div class="col-8-24" id="img-col">
                                        <img id="res-img" src="img/paf-cols.png">
                                        <center><span class="fig-caption">Figure 5.4: The column definitions of PAF files. <a href="https://github.com/lh3/miniasm/blob/master/PAF.md" target="_blank">Source</a>.</span></center>
                                    </div>
                                    <div class="col-8-24" id="margin"></div>
                                </div>

                                <p>Conveniently, this tells us the number of matches (column 10) and total number of sites (column 11) per alignment block. We can use this to quickly calculate the percent identity from
                                    a PAF file. We've provided a custom python script, <code class="inline">div_est.py</code> that does this. Let's run this script on the <code class="inline">alignments/dpse-2-pi-1-to-dmel3.paf</code>
                                    file.
                                </p>

                                <center><pre class="cmd"><code>python3 scripts/div_est.py alignments/dpse-2-pi-1-to-dmel3.paf</code></pre></center>
                
                                <div class="table-cont">
                                    <table class="cmd-table">
                                        <thead><th class="tcol-1">Command line parameter</th><th class="tcol-2">Description</th></thead>
                                        <tr>
                                            <td class="tcol-1">python3</td><td class="tcol-2">Invokes <code class="inline">python3</code> to run the script.</td>
                                        </tr>
                                        <tr>
                                            <td class="tcol-1">scripts/div_est.py</td><td class="tcol-2">The path to the script.</td>
                                        </tr>
                                        <tr>
                                            <td class="tcol-1">alignments/dpse-2-pi-1-to-dmel3.paf</td><td class="tcol-2">The input file.</td>
                                        </tr>
                                    </table>
                                </div>

                                <p>This should simply print the percent identity to the screen:</p>

                                <pre class="text"><code># Percent matching bases: 95.015</code></pre>

                                <p>95.015% identity after one iteration of mapping. What about after two iterations? Remember, reference bias makes mapped reads look more like the reference than
                                    expected, so we would expect % identity to DECREASE if we are improving on reference bias.
                                </p>

                                <p>Next, run <code class="inline">minimap2</code> on the second iteration of mapping:

                                <center><pre class="cmd"><code>minimap2 -x asm10 dmel-3R-reference/Drosophila_melanogaster.BDGP6.28.dna.chromosome.3R.fa expected-outputs/dpse-pseudo-it/iter-02/fa/iter-02-final.fa > alignments/dpse-2-pi-2-to-dmel3.paf</code></pre></center>

                                <div class="table-cont">
                                    <table class="cmd-table">
                                        <thead><th class="tcol-1">Command line parameter</th><th class="tcol-2">Description</th></thead>
                                        <tr>
                                            <td class="tcol-1">minimap2</td><td class="tcol-2">Call the <code class="inline">minimap2</code> program.</td>
                                        </tr>
                                        <tr>
                                            <td class="tcol-1">-x asm10</td><td class="tcol-2">Set this to indicate assembly-to-reference mapping.</td>
                                        </tr>
                                        <tr>
                                            <td class="tcol-1">-x asm10</td><td class="tcol-2">Set this to indicate assembly-to-reference mapping.</td>
                                        </tr>
                                        <tr>
                                            <td class="tcol-1">dmel-3R-reference/Drosophila_melanogaster.BDGP6.28.dna.chromosome.3R.fa</td><td class="tcol-2">The path to the reference genome FASTA file. 
                                                In this case, <em>D. melanogaster</em> chromosome 3R.</td>
                                        </tr>
                                        <tr>
                                            <td class="tcol-1">expected-outputs/dpse-pseudo-it/iter-02/fa/iter-02-final.fa</td><td class="tcol-2">The path to the assembly FASTA file. In this case, the consensus sequence of <em>D. pseudoobscura</em>
                                                after <b>two</b> iterations of mapping.</td>
                                        </tr>
                                        <tr>
                                            <td class="tcol-1">&gt;</td><td class="tcol-2">This redirects the output that would have been printed to the screen to a file instead.</td>
                                        </tr>
                                        <tr>
                                            <td class="tcol-1">alignments/dpse-2-pi-2-to-dmel3.paf</td><td class="tcol-2">The desired output file.</td>
                                        </tr>
                                    </table> 
                                </div>       
                                
                                <p>And then again let's calculate % identity:</p>

                                <center><pre class="cmd"><code>python3 scripts/div_est.py alignments/dpse-2-pi-2-to-dmel3.paf</code></pre></center>
                
                                <div class="table-cont">
                                    <table class="cmd-table">
                                        <thead><th class="tcol-1">Command line parameter</th><th class="tcol-2">Description</th></thead>
                                        <tr>
                                            <td class="tcol-1">python3</td><td class="tcol-2">Invokes <code class="inline">python3</code> to run the script.</td>
                                        </tr>
                                        <tr>
                                            <td class="tcol-1">scripts/div_est.py</td><td class="tcol-2">The path to the script.</td>
                                        </tr>
                                        <tr>
                                            <td class="tcol-1">alignments/dpse-2-pi-2-to-dmel3.paf</td><td class="tcol-2">The input file.</td>
                                        </tr>
                                    </table>
                                </div>

                                <pre class="text"><code># Percent matching bases: 94.541</code></pre>

                                <p>Compared to the previous 95.015%, the % identity has decreased with an iteration of mapping as expected. This means we are likely capturing more variation in this 
                                    version of the pseudo-reference.</p>

                                <h3>This brings us to <a href="end.html">the end</a> of our workshop. Thanks for attending!</h3>

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
                <a href="mapping.html">&lt;&nbsp;Previous</a>    
            </div>
        </div>
        <div class="col-12-24" id="nav-margin"></div>
        <div class="col-6-24" id="nav-btn-cont">
            <!-- <div class="nav-btn">
                <a href="assembly.html">Next&nbsp;&gt;</a>
            </div> -->
        </div>
        <div class="col-3-24" id="nav-btn-margin"></div>
    </div>

    {footer}
</body>
"""

######################
# Main block
######################
pagefile = "iterative-mapping.html";
print("Generating " + pagefile + "...");
year = RC.getYear();
title = "ConGen" + year + " - Assembly Workshop"

head = RC.readHead(title);
nav = RC.readNav(pagefile);
banner = RC.readPrevBanner(year, "assembly");
footer = RC.readFooter();

outfilename = "../../" + pagefile;

with open(outfilename, "w") as outfile:
    outfile.write(html_template.format(head=head, nav=nav, banner=banner, footer=footer));