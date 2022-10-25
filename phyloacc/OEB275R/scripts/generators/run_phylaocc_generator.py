############################################################
# For ConGen2021 site, 08.21
# This generates the file "wolf-snps.html"
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

    <a class="internal-link" name="pipeline"></a>
   	<div class="row" id="header">Running PhyloAcc</div>

    <div class="row" id="body-row">
        <!--
        <div class="col-3-24" id="side-nav-cont">
            <div id="side-nav">
                <span id="side-header">Page contents</span>
                <ul>
                    <li><a href="run-phyloacc.html#pipeline">PhyloAcc pipeline</a></li>
                    <li><a href="run-phyloacc.html#batch">Running a single batch</a></li>
                    <li><a href="run-phyloacc.html#gather">Gathering outputs</a></li>
                </ul>
            </div>
        </div>
        -->

        <div class="col-24-24" id="main-cont">

            <!-- ------- BEGIN SECTION ------- -->

            <div class="row" id="top-row-cont">
                <div class="col-24-24" id="top-row"></div>
            </div>
            <div class="row" id="section-header-cont">
                <div class="col-24-24" id="section-header-row">
                    <div id="section-header">The PhyloAcc pipeline</div>
                </div>
            </div>

            <div class="row" id="section-cont">
                <div class="col-24-24" id="section-col">
                    <div class="row" id="section-row">
                        <div class="col-2-24" id="inner-margin"></div>
                        <div class="col-20-24" id="section-content">
                            <p>
                                As we described, PhyloAcc now implements a model that accounts for <b>phylogenetic discordance</b> in the input loci. This results
                                in more accurate estimates of substitution rates.
                            </p>

                            <p>
                                Unfortunately, these models also take MUCH longer to run. That, combined with the fact that we have hundreds of thousands of
                                loci can lead to exorbitant run times. For example, our full mammal dataset would take <b>years</b> to run if we ran
                                the gene tree model on each locus one at a time.
                            </p>

                            <p>
                                Fortunately, we can come up with ways to speed things up:
                            </p>

                            <ul>
                                <li>Not every locus may need to be run with the gene tree model, so we use <b>site concordance factors</b> to determine which PhyloAcc
                                    model should be used for each locus</li>
                                
                                <li>We <b>batch</b> loci to be run in parallel on the cluster with <a href="https://snakemake.readthedocs.io/en/stable/" target="_blank">snakemake</a>.
                            </ul>

                            <p>
                                All that is to say that this slightly changes how we run PhyloAcc in the latest version:
                            </p>

                            <div class="row" id="img-row">
                                <div class="col-4-24" id="margin"></div>
                                <div class="col-16-24" id="img-col">
                                    <img id="res-img" src="img/phyloacc-pipeline.png">
                                    <center><span class="fig-caption">Figure 3.1: The PhyloAcc v2.0 pipeline with pre-processing interface and snakemake.</span></center>
                                </div>
                                <div class="col-4-24" id="margin"></div>
                            </div>

                            <p>
                                First, we will run our loci through the batching interface:
                            </p>

                            <center><pre class="cmd"><code>phyloacc.py -d /n/holylfs05/LABS/informatics/Everyone/phyloacc-data/mammal-input-accelerated/seq/ -m /n/holylfs05/LABS/informatics/Everyone/phyloacc-data/mammal-input-accelerated/mammal_acc1.mod -t "turTru2;orcOrc1;odoRosDiv1;lepWed1;triMan1" -g "monDom5;sarHar1;macEug2;ornAna1" -r st -burnin 1000 -mcmc 10000 -n 4 -batch 25 -part "shared" -time 4 -o phyloacc-batch-st</code></pre></center>

                            <div class="table-cont">
                                <table class="cmd-table">
                                    <thead><th class="tcol-1">Command line parameter</th><th class="tcol-2">Description</th></thead>
                                    <tr>
                                        <td class="tcol-1">phyloacc.py</td><td class="tcol-2">The PhyloAcc batching command</td>
                                    </tr>
                                    <tr>
                                        <td class="tcol-1">-d /n/holylfs05/LABS/informatics/Everyone/phyloacc-data/mammal-input-accelerated/seq/</td>
                                        <td class="tcol-2">{co}-d{cc} is the PhyloAcc option for the input directory with aligned sequences and
                                            {co}/n/holylfs05/LABS/informatics/Everyone/phyloacc-data/mammal-input-accelerated/seq/{cc} is the path
                                            to that directory for our data.</td>
                                    </tr>
                                    <tr>
                                        <td class="tcol-1">-m /n/holylfs05/LABS/informatics/Everyone/phyloacc-data/mammal-input-accelerated/mammal_acc1.mod</td>
                                        <td class="tcol-2">{co}-m{cc} is the PhyloAcc option for the input mod file with the neutral rates and phylogeny and 
                                            {co}/n/holylfs05/LABS/informatics/Everyone/phyloacc-data/mammal-input-accelerated/mammal_acc1.mod{cc} is the path
                                            to that file for our data.</td>
                                    </tr>                                    
                                    <tr>
                                        <td class="tcol-1">-t "turTru2;orcOrc1;odoRosDiv1;lepWed1;triMan1"</td>
                                        <td class="tcol-2">{co}-t{cc} is the PhyloAcc option to set the target branches and
                                        "turTru2;orcOrc1;odoRosDiv1;lepWed1;triMan1" are the marine mammal species in the tree.</td>
                                    </tr>
                                    <tr>
                                        <td class="tcol-1">-g "monDom5;sarHar1;macEug2;ornAna1"</td>
                                        <td class="tcol-2">{co}-g{cc} is the PhyloAcc option to set the outgroup branches and
                                        "monDom5;sarHar1;macEug2;ornAna1" are the outgroups in the mammal tree.</td>
                                    </tr>                                                                        
                                    <tr>
                                        <td class="tcol-1">-r st</td>
                                        <td class="tcol-2">This means we want all loci to be run with the species tree model.</td>
                                    </tr>
                                    <tr>
                                        <td class="tcol-1">-burnin 1000</td>
                                        <td class="tcol-2">This specifies the number of MCMC cycles to be discarded as burnin for each batch</td>
                                    </tr>
                                    <tr>
                                        <td class="tcol-1">-mcmc 10000</td>
                                        <td class="tcol-2">This specifies the total number of MCMC cycles for each batch</td>
                                    </tr>
                                    <tr>
                                        <td class="tcol-1">-n 4</td>
                                        <td class="tcol-2">The number of processes this script should use.</td>
                                    </tr>
                                    <tr>
                                        <td class="tcol-1">-batch 50</td>
                                        <td class="tcol-2">The number of loci per batch.</td>
                                    </tr>
                                    <tr>
                                        <td class="tcol-1">-part "shared"</td>
                                        <td class="tcol-2">The partition on the cluster to run batches.</td>
                                    </tr>
                                    <tr>
                                        <td class="tcol-1">-time 4</td>
                                        <td class="tcol-2">The time limit for each batch in hours.</td>
                                    </tr>
                                    <tr>
                                        <td class="tcol-1">-o phyloacc-batch-st</td>
                                        <td class="tcol-2">{co}-o{cc} is the PhyloAcc option to specify where files are output and
                                            {co}phyloacc-batch-st{cc} is the path we have chosen. This directory will be created if it doesn't exist.</td>
                                    </tr>                                                                                                                                                                                                                                                                                                                                                                                                           
                                </table>
                            </div> 

                            <p>
                                This should run in a few seconds, and when it's done it should have created several files and folders in the {co}phyloacc-batch-st{cc}
                                directory, including a <a href="data/st-test-branches/phyloacc-pre-run-summary.html" target="blank">summary HTML file</a>.
                            </p>

                            <p>
                                Note that all of our batches are for the species tree model. If we were to run this in <b>adaptive mode</b> with {co}-r adaptive{cc}, 
                                the program would also calculate concordance factors and run some loci with the gene tree model and some through the species tree 
                                model based on them.
                            </p>

                            <p>
                                Compare the <a href="data/adaptive-test-branches/phyloacc-pre-run-summary.html" target="_blank">summary of an <b>adaptive</b> run</a> to the species tree run above.
                            </p>             

                            <p>
                                If we were performing a real analysis, we would execute the snakemake command printed out when we ran the batching script, which would submit the
                                batches to the cluster. But since we don't have that much time, I've pre-run these loci through the pipeline with both the species tree and gene tree
                                model for us to compare and analyze.
                            </p>

                            <p>
                                Then, after all the PhyloAcc batches have been run by the server, their outputs need to be summarized and gathered back into a single location. For this, 
                                PhyloAcc containes a post-processing script, {co}phyloacc_post.py{cc}, that also <a href="data/st-target-branches/phyloacc-results.html" target="_blank">summarizes the results</a> 
                                and importantly creates the {co}elem_lik.txt{cc} output table, which we'll analyze in detail after we 
                                <a href="">download the pre-run data...</a>
                            </p>

                        </div>
                        <div class="col-2-24" id="inner-margin"></div>
                    </div>
                </div>
            </div>

            <!-- -------- END SECTION -------- -->

            <!--      
            <a class="internal-link" name="batch"></a>
            <div class="row" id="section-header-cont">
                <div class="col-24-24" id="section-header-row">
                    <div id="section-header">Running a single locus with the species tre model</div>
                </div>
            </div>

            <div class="row" id="section-cont">
                <div class="col-24-24" id="section-col">
                    <div class="row" id="section-row">
                        <div class="col-2-24" id="inner-margin"></div>
                        <div class="col-20-24" id="section-content">

                            <p>
                                If we were performing a real analysis, we would execute the snakemake command printed out when we ran the batching script, which would submit the
                                batches to the cluster. But since we don't have that much time, lets just run a single locus through PhyloAcc to get an idea of what its doing:
                            </p>

                            <center><pre class="cmd-ne"><code>vcftools &lt;options&gt; &lt;input file&gt;{cc}</pre></center>

                            <div class="table-cont">
                                <table class="cmd-table">
                                    <thead><th class="tcol-1">Command line parameter</th><th class="tcol-2">Description</th></thead>
                                    <tr>
                                        <td class="tcol-1">vcftools</td><td class="tcol-2">A program for working with variant calls in VCF format</td>
                                    </tr>
                                    <tr>
                                        <td class="tcol-1">&lt;options&gt;</td><td class="tcol-2">Analysis specific run options</td>
                                    </tr>
                                    <tr>
                                        <td class="tcol-1">&lt;input file&gt;</td><td class="tcol-2">The path to the file you want to run on</td>
                                    </tr>
                                </table>
                            </div>
                                
                        </div>
                        <div class="col-2-24" id="inner-margin"></div>
                    </div>
                </div>
            </div>
            -->

            <!--   
            <a class="internal-link" name="gather"></a>
            <div class="row" id="section-header-cont">
                <div class="col-24-24" id="section-header-row">
                    <div id="section-header">Gathering outputs</div>
                </div>
            </div>

            <div class="row" id="section-cont">
                <div class="col-24-24" id="section-col">
                    <div class="row" id="section-row">
                        <div class="col-2-24" id="inner-margin"></div>
                        <div class="col-20-24" id="section-content">

                            <p>
                                After all the PhyloAcc batches have been run by the server, their outputs need to be summarized and gathered back into a single location. For this, 
                                PhyloAcc containes a post-processing script, {co}phyloacc_post.py{cc}, that also <a href="" target="_blank">summarizes the results</a> and importantly
                                creates the {co}elem_lik.txt{cc} output table, which we'll analyze in detail after we download some pre-run data...
                            </p>

                        </div>
                        <div class="col-2-24" id="inner-margin"></div>
                    </div>
                </div>
            </div>    
            --> 

        </div>
    </div>

    <div class="row" id="btm-nav">
        <div class="col-3-24" id="nav-bnt-margin"></div>
        <div class="col-6-24" id="nav-btn-cont">
            <div class="nav-btn">
                <a href="marine-mammals.html">&lt;&nbsp;Previous</a>    
            </div>
        </div>
        <div class="col-6-24" id="nav-margin"></div>
        <div class="col-6-24" id="nav-btn-cont">
            <div class="nav-btn">
                <a href="phyloacc-results.html">Next&nbsp;&gt;</a>
            </div>
        </div>
        <div class="col-3-24" id="nav-btn-margin"></div>
    </div>

    {footer}

</body>
</html>
"""

######################
# Main block
######################
pagefile = "run-phyloacc.html";
print("Generating " + pagefile + "...");
year = RC.getYear();
title = "PhyloAcc OEB275R - " + year;


head = RC.readHead(title);
nav = RC.readNav(pagefile);
footer = RC.readFooter();

outfilename = "../../" + pagefile;

with open(outfilename, "w") as outfile:
    outfile.write(html_template.format(head=head, nav=nav, footer=footer, co="<code class='inline'>", cc="</code>"));