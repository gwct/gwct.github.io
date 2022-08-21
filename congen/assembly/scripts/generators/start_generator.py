############################################################
# For ConGen2020 site, 08.20
# This generates the file "start.html"
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

    <a class="internal-link" name="start"></a>
   	<div class="row" id="header">Genome assembly workshop</div>

    <div class="row" id="body-row">
        <div class="col-3-24" id="side-nav-cont">
            <div id="side-nav">
                <span id="side-header">Page contents</span>
                <ul>
                    <li><a href="start.html#start">Getting started</a></li>
                    <li><a href="start.html#drosophila">Drosophila data</a></li>
                    <li><a href="start.html#io">Input files & output prep</a></li>
                </ul>
            </div>
        </div>

        <div class="col-21-24" id="main-cont">

            <div class="row" id="top-row-cont">
                <div class="col-24-24" id="top-row"></div>
            </div>
            <div class="row" id="section-header-cont">
                <div class="col-24-24" id="section-header-row">
                    <div id="section-header">Getting started</div>
                </div>
            </div>

            <div class="row" id="section-cont">
                <div class="col-24-24" id="section-col">
                    <div class="row" id="section-row">
                        <div class="col-2-24" id="inner-margin"></div>
                        <div class="col-20-24" id="section-content">
                                <p>Hello! Today we'll be going through some hands-on activities to help you get familiar with the steps involved in genome assembly and quality assessment.</p>

                                <p>The first thing you should do if you haven't done so is connect to the ConGen server. We'll be working exclusively in the RStudio browser interface that 
                                    you should be familiar with by now, but if you have questions or problems at any point please feel free to ask! Just in case, here's a annotated 
                                    picture of roughly what you should be seeing right now. If you are seeing something drastically different or something that you don't understand, let us know.
                                </p>

                                <div class="row" id="img-row">
                                    <!-- <div class="col-2-24" id="margin"></div> -->
                                    <div class="col-24-24" id="img-col">
                                        <img id="res-img" src="img/congen-interface.png">
                                        <center><span class="fig-caption">Figure 1.1: The RStudio interface for running commands and browsing files.</span></center>
                                    </div>
                                    <!-- <div class="col-2-24" id="margin"></div> -->
                                </div>

                                <p>Most of our work will be done as bash commands typed in the Terminal provided by RStudio. Throughout this walkthrough, commands will be presented
                                    as follows:
                                </p>

                                <center><pre class="cmd"><code>this is an example command</code></pre></center>

                                <p>Following each command will be a table that goes through and explains each part of the command explicitly:</p>

                                <div class="table-cont">
                                    <table class="cmd-table">
                                        <thead><th class="tcol-1">Command line parameter</th><th class="tcol-2">Description</th></thead>
                                        <tr>
                                            <td class="tcol-1">this</td><td class="tcol-2">An example command</td>
                                        </tr>
                                        <tr>
                                            <td class="tcol-1">is</td><td class="tcol-2">An example option used in the example command</td>
                                        </tr>
                                        <tr>
                                            <td class="tcol-1">an</td><td class="tcol-2">An example option used in the example command</td>
                                        </tr>
                                        <tr>
                                            <td class="tcol-1">example</td><td class="tcol-2">An example option used in the example command</td>
                                        </tr>
                                        <tr>
                                            <td class="tcol-1">command</td><td class="tcol-2">An example option used in the example command</td>
                                        </tr>
                                    </table>
                                </div>

                                <p>The goal of providing these tables is to break-down some of the 'black box' that command line tools can sometimes feel like.
                                    Hopefully this is helpful. If not, feel free to skip over these tables when you see them!</p>

                                <div id="msg_cont">
                                    <div id="msg">
                                        <div id="msg_banner">Tip - Help menus</div>
                                        <div id="msg_text">
                                            <p>
                                                A general convention among command-line software is to provide a help menu for programs that lists common options. These can generally
                                                viewed from the command line with the <code class="inline">-h</code> option as follows:
                                            </p>

                                            <center><code class="inline">&lt;program&gt; -h</code> &nbsp;<em>-or-</em>&nbsp; <code class="inline">&lt;program&gt; &lt;sub-program&gt; -h</code></center>

                                            <p>For Linux commands, documentation is generally available with the <code class="inline">man</code> command (man is short for manual):</p>

                                            <center><code class="inline">man &lt;command&gt;</code></center>

                                            <p><code class="inline">man</code> opens a text viewer that can be navigated with the arrow keys and exited simply by typing <code class="inline">q</code>.
                                                If you're ever stuck or want to know more about a program's options, try these!
                                            </p>
                                            <p></p>
                                        </div>
                                    </div>
                                </div>

                                <p>Commands that you should run will have a <span style="background-color:#c6ecd9;">green background</span>. We will also provide some commands that are beneficial
                                    to see, but do not necessarily need to be run using a <span style="background-color:#ffb3b3;">red background</span>, like so:

                                <center><pre class="cmd-ne"><code>this is an example command that won't be run</code></pre></center>

                                <p>Additionally, one of the most important and often overlooked parts of bioinformatics analyses is to simply look at ones data.
                                    There will be several points where we stop to look at the output of a given program or command. When we do, a snippet
                                    of the output will be presented in the walkthrough as follows:
                                </p>

                                <pre class="text"><code>Here is some made up output.
Looking at your data is very important!
You can catch problems before you use the data in later analyses.</code></pre>
                        </div>
                        <div class="col-2-24" id="inner-margin"></div>
                    </div>
                </div>
            </div>

            <a class="internal-link" name="drosophila"></a>
            <div class="row" id="section-header-cont">
                <div class="col-24-24" id="section-header-row">
                    <div id="section-header">Drosophila data</div>
                </div>
            </div>
            <div class="row" id="section-cont">
                <div class="col-24-24" id="section-col">
                    <div class="row" id="section-row">
                        <div class="col-2-24" id="inner-margin"></div>
                        <div class="col-20-24" id="section-content">
                            <p>Today we'll be talking about genome assembly. While the programs that perform the various steps of assembly have greatly improved over
                                the past few years, genome assembly is still generally a slow, multi-step process. Given that, we'll be working with a smaller 150Mb
                                genome from <em>Drosophila pseudoobscura</em>. Many times we will limit our data to just chromosome 2 (32Mb) of </em>D. pseudoobscura</em> to speed up
                                run times even more.
                            </p>

                            <p><em>D. pseudoobscura</em> is a species of fruit fly that diverged from the well known <em>D. melanogaster</em> model species roughly 50
                                million years ago. <em>D. pseudoobscura</em> chromosome 2 is homologous to <em>D. melanogaster</em> chromosome arm 3R.
                            </p>

                            <div class="row" id="img-row">
                                <div class="col-4-24" id="margin"></div>
                                <div class="col-16-24" id="img-col">
                                    <img id="res-img" src="img/drosophila.png">
                                    <center><span class="fig-caption">Figure 1.2: Drosophila phylogeny and homology between chromosome arms. 
                                        From <a href="https://www.genetics.org/content/179/3/1601" target="blank">Schaeffer et al. 2008</a></span></center>
                                </div>
                                <div class="col-4-24" id="margin"></div>
                            </div>

                            <p>Using these data, we'll be performing the following tasks today:</p>

                            <ol>
                                <li>Assembling the <em>D. pseudoobscura</em> genome and assessing the quality of said assembly.</li>
                                <li>Mapping reads from <em>D. pseudoobscura</em> chromosome 2 to <em>D. melanogaster</em> chromosome 3R.</li>
                                <li>Assessing how iterative mapping of reads from <em>D. pseudoobscura</em> chromosome 2 to <em>D. melanogaster</em> affects divergence estimates.</li>
                            </ol>
                        </div>
                        <div class="col-2-24" id="inner-margin"></div>
                    </div>
                </div>
            </div>

            <a class="internal-link" name="io"></a>
            <div class="row" id="section-header-cont">
                <div class="col-24-24" id="section-header-row">
                    <div id="section-header">Input files & output prep</div>
                </div>
            </div>

            <div class="row" id="section-cont">
                <div class="col-24-24" id="section-col">
                    <div class="row" id="section-row">
                        <div class="col-2-24" id="inner-margin"></div>
                        <div class="col-20-24" id="section-content">

                            <h3>Copying input data</h3>

                            <p>The data we'll be working with today are mainly sequences in FASTA and FASTQ format (more on those in a moment). The input files are located on the server at
                                <code class="inline">~/instructor_materials/Gregg_Thomas/congen-assembly/</code>. Let's make a copy of this directory in our home directory so we don't 
                                have to worry about that path anymore. First, make sure you are in your home directory:
                            </p>

                            <center><pre class="cmd"><code>cd ~</code></pre></center>

                            <div class="table-cont">
                                <table class="cmd-table">
                                    <thead><th class="tcol-1">Command line parameter</th><th class="tcol-2">Description</th></thead>
                                    <tr>
                                        <td class="tcol-1">cd</td><td class="tcol-2">The Linux change directory command</td>
                                    </tr>
                                    <tr>
                                        <td class="tcol-1">~</td><td class="tcol-2">The path to the directory you want to change to. In bash, 
                                            <code class="inline">~</code> is a shortcut meaning "the current user's home directory."</td>
                                    </tr>
                                </table>
                            </div>                                
                            
                            <p>Now let's make a copy of the data directory:</p>

                            <center><pre class="cmd"><code>cp -r instructor_materials/Gregg_Thomas/congen-assembly/ .</code></pre></center>

                            <div class="table-cont">
                                <table class="cmd-table">
                                    <thead><th class="tcol-1">Command line parameter</th><th class="tcol-2">Description</th></thead>
                                    <tr>
                                        <td class="tcol-1">cp</td><td class="tcol-2">The Linux copy command</td>
                                    </tr>
                                    <tr>
                                        <td class="tcol-1">-r</td><td class="tcol-2">Recursively copy all files in a directory.</td>
                                    </tr>
                                    <tr>
                                        <td class="tcol-1">instructor_materials/Gregg_Thomas/congen-assembly/</td><td class="tcol-2">The path to the directory you want to copy.</td>
                                    </tr>
                                    <tr>
                                        <td class="tcol-1">.</td><td class="tcol-2">The path to the new copy. In bash, <code class="inline">.</code> is a shortcut meaning
                                            "the same name." So this will copy the directory to our current location with the name <code class="inline">congen-assembly</code></td>
                                    </tr>
                                </table>
                            </div>            

                            <p>Let's move into this folder with <code class="inline">cd</code> again since we'll spend the rest of the workshop here:</p>

                            <center><pre class="cmd"><code>cd congen-assembly</code></pre></center>

                            <div class="table-cont">
                                <table class="cmd-table">
                                    <thead><th class="tcol-1">Command line parameter</th><th class="tcol-2">Description</th></thead>
                                    <tr>
                                        <td class="tcol-1">cd</td><td class="tcol-2">The Linux change directory command</td>
                                    </tr>
                                    <tr>
                                        <td class="tcol-1">congen-assembly</td><td class="tcol-2">The path to the directory you want to change to.</td>
                                    </tr>
                                </table>
                            </div>                                      
                            
                            <p>
                                And now we can look at what is in that folder with the <code class="inline">ls</code> command. Make sure you've
                                selected your Terminal window and type the following:
                            </p>

                            <center><pre class="cmd"><code>ls</code></pre></center>
                            <div class="table-cont">
                                <table class="cmd-table">
                                    <thead><th class="tcol-1">Command line parameter</th><th class="tcol-2">Description</th></thead>
                                    <tr>
                                        <td class="tcol-1">ls</td><td class="tcol-2">The Linux list directory command to view the files in a folder. Shows files in current folder by default.</td>
                                    </tr>
                                </table>
                            </div>

                            <p>You should see the following folders listed</p>

                            <div class="table-cont">
                                <table class="norm-table">
                                    <thead><th class="tcol-1">Folder</th><th class="tcol-2">Description</th></thead>
                                    <tr>
                                        <td class="tcol-1"><code class="inline">dmel-3R-reference/</code></td><td class="tcol-2">A folder containing the <em>D. melanogaster</em> chromosome 3R sequence file and its indices.</td>
                                    </tr>
                                    <tr>
                                        <td class="tcol-1"><code class="inline">dpse-chr2-reads/</code></td><td class="tcol-2">A folder containing Illumina short reads for <em>D. pseudoobscura</em>.</td>
                                    </tr>
                                    <tr>
                                        <td class="tcol-1"><code class="inline">expected-outputs/</code></td><td class="tcol-2">Pre-run outputs for all the programs we run today. 
                                            If you get stuck or something takes too long, look for the expected output here</td>
                                    </tr>
                                    <tr>
                                        <td class="tcol-1"><code class="inline">scripts/</code></td><td class="tcol-2">A few supplementary scripts for data analysis.</td>
                                    </tr>
                                </table>
                            </div> 

                            <div id="msg_cont">
                                <div id="msg">
                                    <div id="msg_banner">Tip - Pre-generated outputs</div>
                                    <div id="msg_text">
                                        <p>
                                            We have tried to anticipate the expected outputs from the commands we run today. If you get behind or stuck on something, try moving on to the next
                                            step by adding <code class="inline">expected-outputs/</code> to the beginning of the path for input you were expected to generate for the next command.
                                            Feel free to ask us for help for any specific command.
                                        </p>

                                        <p></p>
                                    </div>
                                </div>
                            </div>                       

                            <h3>Preparing output directories</h3>

                            <p>I like to try and think ahead about what outputs my project will produce and make those directories early on, which helps me plan out my workflows. 
                                Today we'll be generating assemblies, read mappings, and alignments, so let's prepare an output directory for each of those tasks.
                            </p>

                            <center><pre class="cmd"><code>mkdir alignments</code></pre></center>

                            <div class="table-cont">
                                <table class="cmd-table">
                                    <thead><th class="tcol-1">Command line parameter</th><th class="tcol-2">Description</th></thead>
                                    <tr>
                                        <td class="tcol-1">mkdir</td><td class="tcol-2">The Linux make directory command</td>
                                    </tr>
                                    <tr>
                                        <td class="tcol-1">alignments</td><td class="tcol-2">The name of the directory where we will generate and store our alignments for comparing assemblies and read mappings</td>
                                    </tr>
                                </table>
                            </div>

                            <center><pre class="cmd"><code>mkdir assemblies</code></pre></center>

                            <div class="table-cont">
                                <table class="cmd-table">
                                    <thead><th class="tcol-1">Command line parameter</th><th class="tcol-2">Description</th></thead>
                                    <tr>
                                        <td class="tcol-1">mkdir</td><td class="tcol-2">The Linux make directory command</td>
                                    </tr>
                                    <tr>
                                        <td class="tcol-1">assemblies</td><td class="tcol-2">The name of the directory where we will generate and store our assemblies</td>
                                    </tr>
                                </table>
                            </div>

                            <center><pre class="cmd"><code>mkdir mapped-reads</code></pre></center>

                            <div class="table-cont">
                                <table class="cmd-table">
                                    <thead><th class="tcol-1">Command line parameter</th><th class="tcol-2">Description</th></thead>
                                    <tr>
                                        <td class="tcol-1">mkdir</td><td class="tcol-2">The Linux make directory command</td>
                                    </tr>
                                    <tr>
                                        <td class="tcol-1">mapped-reads</td><td class="tcol-2">The name of the directory where we will generate and store our read mappings</td>
                                    </tr>
                                </table>
                            </div>

                            <p>We'll also be running the program FastQC, which requires a pre-made output directory:

                            <center><pre class="cmd"><code>mkdir fastqc-output</code></pre></center>
            
                            <div class="table-cont">
                                <table class="cmd-table">
                                    <thead><th class="tcol-1">Command line parameter</th><th class="tcol-2">Description</th></thead>
                                    <tr>
                                        <td class="tcol-1">mkdir</td><td class="tcol-2">The Linux make directory command</td>
                                    </tr>
                                    <tr>
                                        <td class="tcol-1">fastqc-output</td><td class="tcol-2">The desired name of the new directory.</td>
                                    </tr>
                                </table>
                            </div>                            

                            <p>Some other programs we run will create their own output directories. We should now be ready to run the commands to generate assemblies 
                                and read mappings. But first, let's get familiar with our input data, <a href="reads.html">sequences and reads...</a>
                            </p>
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
                <a href="index.html">&lt;&nbsp;Previous</a>    
            </div>
        </div>
        <div class="col-6-24" id="nav-margin"></div>
        <div class="col-6-24" id="nav-btn-cont">
            <div class="nav-btn">
                <a href="reads.html">Next&nbsp;&gt;</a>
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
pagefile = "start.html";
print("Generating " + pagefile + "...");
year = RC.getYear();
title = "ConGen" + year + " - Assembly Workshop"

head = RC.readHead(title);
nav = RC.readNav(pagefile);
footer = RC.readFooter();

outfilename = "../../" + pagefile;

with open(outfilename, "w") as outfile:
    outfile.write(html_template.format(head=head, nav=nav, footer=footer));