############################################################
# For ConGen2020 site, 08.20
# This generates the file "reads.html"
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

<a class="internal-link" name="intro"></a>
<div class="row" id="header">Getting started</div>

    <div class="row" id="body-row">
        <div class="col-3-24" id="side-nav-cont">
            <div id="side-nav">
                <span id="side-header">Page contents</span>
                <ul>
                    <li><a href="start.html#intro">Introduction</a></li>
                    <li><a href="start.html#drosophila">Drosophila data</a></li>
                    <li><a href="start.html#prep">Project prep</a></li>
                </ul>
            </div>
        </div>

        <div class="col-21-24" id="main-cont">
            <div class="row" id="top-row-cont">
                <div class="col-24-24" id="top-row"></div>
            </div>

            <div class="row" id="top-row-cont">
                <div class="col-24-24" id="top-row"></div>
            </div>

            <div class="row" id="section-header-cont">
                <div class="col-24-24" id="section-header-row">
                    <div id="section-header">Introduction</div>
                </div>
            </div>
            <div class="row" id="section-cont">
                <div class="col-24-24" id="section-col">
                    <div class="row" id="section-row">
                        <div class="col-2-24" id="inner-margin"></div>
                        <div class="col-20-24" id="section-content">
                                <p>
                                    Welcome to the FAS Bioinformatics workshop on read mapping!
                                </p>

                                <p>
                                    Today we'll be going over common file formats and encodings that deal with <b>raw sequence data</b> that you would receive from a
                                    sequencing machine, company, or database. Our goal is to become familiar with handling these formats, and knowing what to do with them
                                    once we have them.
                                </p>

                                <h3>The command line</h3>

                                <p>
                                    We'll be running commands on your machine's text-based command prompt. This can be opened by navigating to the program from your
                                    start menu, and should look something like this:
                                </p>

                                <div class="row" id="img-row">
                                    <div class="col-4-24" id="margin"></div>
                                    <div class="col-16-24" id="img-col">
                                        <img id="res-img" src="img/cmd.png">
                                        <center><span class="fig-caption">Figure 1.1: A typical command prompt.</span></center>
                                    </div>
                                    <div class="col-4-24" id="margin"></div>
                                </div>

                                <p>
                                    Most of our work today will be done as commands typed into a command line. Throughout this walkthrough, commands will be presented
                                    as follows:
                                </p>

                                <center><pre class="cmd"><code>this is an example command</code></pre></center>

                                <p>Following each command will be a table that goes through and explains each part of the command explicitly:</p>

                                <div class="table-cont">
                                    <table class="cmd-table">
                                        <thead><th class="tcol-1">Command line parameter</th><th class="tcol-2">Description</th></thead>
                                        <tr>
                                            <td class="tcol-1">this</td><td class="tcol-2">An example program</td>
                                        </tr>
                                        <tr>
                                            <td class="tcol-1">is</td><td class="tcol-2">An example option used in the example program</td>
                                        </tr>
                                        <tr>
                                            <td class="tcol-1">an</td><td class="tcol-2">An example option used in the example program</td>
                                        </tr>
                                        <tr>
                                            <td class="tcol-1">example</td><td class="tcol-2">An example option used in the example program</td>
                                        </tr>
                                        <tr>
                                            <td class="tcol-1">command</td><td class="tcol-2">An example option used in the example program</td>
                                        </tr>
                                    </table>
                                </div>

                                <p>
                                    The goal of providing these tables is to break-down some of the 'black box' that command line tools can sometimes feel like.
                                    Hopefully this is helpful. If not, feel free to skip over these tables when you see them!
                                </p>

                                <div id="msg_cont">
                                    <div id="msg">
                                        <div id="msg_banner">Tip - Help menus</div>
                                        <div id="msg_text">
                                            <p>
                                                A general convention among command-line software is to provide a help menu for programs that lists common options.
                                                In moset cases, these can be viewed from the command line with the <code class="inline">-h</code> or 
                                                <code class="inline">--help</code> options as follows:
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

                                <p>
                                    Commands that you should run will have a <span style="background-color:#c6ecd9;">green background</span>. We will also provide some commands that are beneficial
                                    to see, but do not necessarily need to be run using a <span style="background-color:#ffb3b3;">red background</span>, like so:
                                </p>

                                <center><pre class="cmd-ne"><code>this is an example command that won't be run</code></pre></center>

                                <p>
                                    Additionally, one of the most important and often overlooked parts of bioinformatics analyses is to simply look at one's data.
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
                            <p>
                                Today we'll be working with short reads from the relatively small 150Mb genome from <em>Drosophila pseudoobscura</em>. 
                                Many times we will limit our data to just chromosome 2 (32Mb) of </em>D. pseudoobscura</em> to speed up run times even more.
                            </p>

                            <p>
                                <em>D. pseudoobscura</em> is a species of fruit fly that diverged from the well known <em>D. melanogaster</em> model species roughly 50
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
                                <li>Looking at sequences in FASTA and FASTQ format.</li>
                                <li>Mapping reads to a reference genome</li>
                                <li>Learning about reference bias in read mapping, and mitigating it with pseudo-it</li>
                                <!-- <li>Learning about quality score encodings in sequence reads and converting between various encodings.</li>
                                <li>Assessing read quality with the FastQC software.</li>
                                <li><b>ASSIGNMENT</b>: Writing a script to assess base quality on our own.</li> -->
                            </ol>
                        </div>
                        <div class="col-2-24" id="inner-margin"></div>
                    </div>
                </div>
            </div>

            <a class="internal-link" name="prep"></a>
            <div class="row" id="section-header-cont">
                <div class="col-24-24" id="section-header-row">
                    <div id="section-header">Preparing Your Project</div>
                </div>
            </div>
            <div class="row" id="section-cont">
                <div class="col-24-24" id="section-col">
                    <div class="row" id="section-row">
                        <div class="col-2-24" id="inner-margin"></div>
                        <div class="col-20-24" id="section-content">
                            <h3>Copying input data</h3>

                            <p>The data we'll be working with today are mainly sequences in FASTA and FASTQ format (more on those in a moment). The input 
                                files are located on the server at <code class="inline">/home/gwct/workshops/mapping-workshop/</code>. Let's make a copy of this 
                                directory in our home directory so we don't have to worry about that path anymore. First, make sure you are in your home directory:
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

                            <center><pre class="cmd"><code>cp -r /home/gwct/workshops/mapping-workshop/ .</code></pre></center>

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
                                        <td class="tcol-1">/home/gwct/workshops/mapping-workshop/</td><td class="tcol-2">The path to the directory you want to copy.</td>
                                    </tr>
                                    <tr>
                                        <td class="tcol-1">.</td><td class="tcol-2">The path to the new copy. In bash, <code class="inline">.</code> is a shortcut meaning
                                            "the same name." So this will copy the directory to our current location with the name <code class="inline">mapping-workshop</code></td>
                                    </tr>
                                </table>
                            </div>            

                            <p>Let's move into this folder with <code class="inline">cd</code> again since we'll spend the rest of the workshop here:</p>

                            <center><pre class="cmd"><code>cd mapping-workshop</code></pre></center>

                            <div class="table-cont">
                                <table class="cmd-table">
                                    <thead><th class="tcol-1">Command line parameter</th><th class="tcol-2">Description</th></thead>
                                    <tr>
                                        <td class="tcol-1">cd</td><td class="tcol-2">The Linux change directory command</td>
                                    </tr>
                                    <tr>
                                        <td class="tcol-1">mapping-workshop</td><td class="tcol-2">The path to the directory you want to change to.</td>
                                    </tr>
                                </table>
                            </div>                                      
                            
                            <p>
                                And now we can look at what is in that folder with the <code class="inline">ls</code> command.
                            </p>

                            <center><pre class="cmd"><code>ls</code></pre></center>
                            <div class="table-cont">
                                <table class="cmd-table">
                                    <thead><th class="tcol-1">Command line parameter</th><th class="tcol-2">Description</th></thead>
                                    <tr>
                                        <td class="tcol-1">ls</td><td class="tcol-2">The Linux list directory command to view the files in a folder. 
                                            Shows files in current folder by default.</td>
                                    </tr>
                                </table>
                            </div>

                            <p>You should see the following folders listed</p>

                            <div class="table-cont">
                                <table class="norm-table">
                                    <thead><th class="tcol-1">Folder</th><th class="tcol-2">Description</th></thead>
                                    <tr>
                                        <td class="tcol-1"><code class="inline">data/</code></td><td class="tcol-2">A folder containing the <em>Drosophila</em> 
                                            data used in this lab.</td>
                                    </tr>
                                    <tr>
                                        <td class="tcol-1"><code class="inline">expected-outputs/</code></td><td class="tcol-2">The folder where you will write and run scripts.
                                            Pre-generated outputs for today's activities.
                                    </tr>
                                    <tr>
                                        <td class="tcol-1"><code class="inline">scripts/</code></td><td class="tcol-2">The folder where you will write and run scripts.
                                            Any pre-made scripts will also be located here.
                                    </tr>
                                </table>
                            </div> 

                            <p>
                                Let's also take a look at what's in the <code class="inline">data</code> folder so we know what we'll be working with:
                            </p>


                            <center><pre class="cmd"><code>ls data/</code></pre></center>
                            <div class="table-cont">
                                <table class="cmd-table">
                                    <thead><th class="tcol-1">Command line parameter</th><th class="tcol-2">Description</th></thead>
                                    <tr>
                                        <td class="tcol-1">ls</td><td class="tcol-2">The Linux list directory command to view the files in a folder. Shows files in current folder by default.</td>
                                    </tr>
                                    <tr>
                                        <td class="tcol-1">data/</td><td class="tcol-2">By default, ls lists the contents of the current directory. You can also supply a path to another
                                            directory, such as the data folder, to list it's contents.
                                        </td>
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
                                </table>
                            </div> 

                            <div id="msg_cont">
                                <div id="msg">
                                    <div id="msg_banner">Tip - Pre-generated outputs</div>
                                    <div id="msg_text">
                                        <p>
                                            We have tried to anticipate the expected outputs from the commands we run today. If you get behind or stuck on something, try moving on to the next
                                            step by adding <code class="inline">expected-outputs/</code> to the beginning of the path for input of the next command.
                                            Feel free to ask us for help for any specific command.
                                        </p>

                                        <p></p>
                                    </div>
                                </div>
                            </div>

                            <h3>Preparing output directories</h3>

                            <p>
                                I like to try and think ahead about what outputs my project will produce and make those directories early on, which helps me plan out my workflows. 
                            </p>
                            
                            <p>
                                Today we'll be mapping sequence reads from our sample to a reference genome. Let's make an output directory for them as well:
                            </p>

                            <center><pre class="cmd"><code>mkdir mapped-reads</code></pre></center>
            
                            <div class="table-cont">
                                <table class="cmd-table">
                                    <thead><th class="tcol-1">Command line parameter</th><th class="tcol-2">Description</th></thead>
                                    <tr>
                                        <td class="tcol-1">mkdir</td><td class="tcol-2">The Linux make directory command</td>
                                    </tr>
                                    <tr>
                                        <td class="tcol-1">mapped-reads</td><td class="tcol-2">The desired name of the new directory.</td>
                                    </tr>
                                </table>
                            </div>

                            <p>
                                And we'll be doing some pairwise sequence alignments to compare different read mapping runs, so let's make a folder for
                                those outputs:
                            </p>

                            <center><pre class="cmd"><code>mkdir alignments</code></pre></center>
            
                            <div class="table-cont">
                                <table class="cmd-table">
                                    <thead><th class="tcol-1">Command line parameter</th><th class="tcol-2">Description</th></thead>
                                    <tr>
                                        <td class="tcol-1">mkdir</td><td class="tcol-2">The Linux make directory command</td>
                                    </tr>
                                    <tr>
                                        <td class="tcol-1">alignments</td><td class="tcol-2">The desired name of the new directory.</td>
                                    </tr>
                                </table>
                            </div>

                            <h4>
                                Next we'll be talking about <a href="reads.html">raw sequence data and their formats.</a>
                            </h4>

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
            <!-- <div class="nav-btn">
                <a href="start.html">&lt;&nbsp;Previous</a>    
            </div> -->
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
"""

######################
# Main block
######################
pagefile = "start.html";
print("Generating " + pagefile + "...");
title = "Getting started - Harvard Bioinformatics"

head = RC.readHead(title);
nav = RC.readNav(pagefile);
footer = RC.readFooter();

outfilename = "../../" + pagefile;

with open(outfilename, "w") as outfile:
    outfile.write(html_template.format(head=head, nav=nav, footer=footer));