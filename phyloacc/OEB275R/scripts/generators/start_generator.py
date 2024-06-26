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
   	<div class="row" id="header">Getting started</div>

    <div class="row" id="body-row">
        <div class="col-3-24" id="side-nav-cont">
            <div id="side-nav">
                <span id="side-header">Page contents</span>
                <ul>
                    <li><a href="start.html#start">Getting started</a></li>
                    <li><a href="start.html#cannon">Connecting to Cannon</a></li>
                    <li><a href="start.html#env">Loading the PhyloAcc environment</a></li>
                    <li><a href="start.html#project">Creating a project folder</a></li>
                </ul>
            </div>
        </div>

        <div class="col-21-24" id="main-cont">

            <!-- ------- BEGIN SECTION ------- -->

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
                            <p>
                                Hello! Today we'll be going through some hands-on activities to help you get familiar with how PhyloAcc is run and how it can be used to
                                identify genomic elements that have experienced accelerated evolution.
                            </p>

                            <p>
                                This course will have 2 parts: one where we are on the server and running commands and another where we download some pre-run data to analyze with R.
                            </p>

                            <p>
                                Most of our work in the first part of the course will be done as bash commands typed in the Terminal. Throughout this walkthrough, commands will be presented
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

                            <!--
                            <p>Commands that you should run will have a <span style="background-color:#c6ecd9;">green background</span>. We will also provide some commands that are beneficial
                                to see, but do not necessarily need to be run using a <span style="background-color:#ffb3b3;">red background</span>, like so:

                            <center><pre class="cmd-ne"><code>this is an example command that won't be run</code></pre></center>

                            <p>Additionally, one of the most important and often overlooked parts of bioinformatics analyses is to simply look at ones data.
                                There will be several points where we stop to look at the output of a given program or command. When we do, a snippet
                                of the output will be presented in the walkthrough as follows:
                            </p>
                            -->

                            <pre class="text"><code>Here is some made up output.
Looking at your data is very important!
You can catch problems before you use the data in later analyses.</code></pre>
                        </div>
                        <div class="col-2-24" id="inner-margin"></div>
                    </div>
                </div>
            </div>

            <!-- -------- END SECTION -------- -->

            <!-- ------- BEGIN SECTION ------- -->

            <a class="internal-link" name="cannon"></a>
            <div class="row" id="section-header-cont">
                <div class="col-24-24" id="section-header-row">
                    <div id="section-header">Loading the PhyloAcc environment</div>
                </div>
            </div>
            <div class="row" id="section-cont">
                <div class="col-24-24" id="section-col">
                    <div class="row" id="section-row">
                        <div class="col-2-24" id="inner-margin"></div>
                        <div class="col-20-24" id="section-content">

                            <p>
                                If you want to follow along by running the commands, the first thing you should do if you haven't done 
                                so is to connect to Cannon, our cluster, such that you can run commands from a terminal. There are different ways to do this, but the easiest thing 
                                would to just open up Terminal (on Mac) or PowerShell (on Windows) and run the following command:
                            </p>

                            <center><pre class="cmd"><code>ssh [your user name]@login.rc.fas.harvard.edu</code></pre></center>

                            <p>
                                This should prompt you for your password and 2-factor authentication code, at which point you should see something like this:
                            </p>

                            <div class="row" id="img-row">
                                <div class="col-5-24" id="margin"></div>
                                <div class="col-14-24" id="img-col">
                                    <img id="res-img" src="img/cannon.png">
                                    <center><span class="fig-caption">Figure 1.1: Cannon right after logging in.</span></center>
                                </div>
                                <div class="col-5-24" id="margin"></div>
                            </div>


                            <p>
                                In addition to logging on to the server as above, we're also going to start an interactive session on one of the compute nodes
                                so that we don't bog down any of the login nodes trying to run PhyloAcc:
                            </p>

                            <center><pre class="cmd"><code>salloc -p test --mem 12g -c 8 -t 0-02:00</code></pre></center>

                            <div class="table-cont">
                                <table class="cmd-table">
                                    <thead><th class="tcol-1">Command line parameter</th><th class="tcol-2">Description</th></thead>
                                    <tr>
                                        <td class="tcol-1">salloc</td>
                                        <td class="tcol-2">The job scheduling command to allocate an interactive session.</td>
                                    </tr>
                                    <tr>
                                        <td class="tcol-1">-p</td>
                                        <td class="tcol-2">The option to specify which partition we want our job to run on, in this case the <b>test</b> partition.</td>
                                    </tr>
                                    <tr>
                                        <td class="tcol-1">--mem 12g</td>
                                        <td class="tcol-2">The option to specify how much memory to allocate to our job, in this case the 12 gigabytes.</td>
                                    </tr>        
                                    <tr>
                                        <td class="tcol-1">-t 0-02:00</td>
                                        <td class="tcol-2">The option to specify how much time to allocate to our job, in this case the 2 hours.</td>
                                    </tr>                                                                      
                                </table>
                            </div>                            


                        </div>
                        <div class="col-2-24" id="inner-margin"></div>
                    </div>
                </div>
            </div>

            <!-- -------- END SECTION -------- -->

            <!-- ------- BEGIN SECTION ------- -->

            <a class="internal-link" name="env"></a>
            <div class="row" id="section-header-cont">
                <div class="col-24-24" id="section-header-row">
                    <div id="section-header">Loading the PhyloAcc environment</div>
                </div>
            </div>
            <div class="row" id="section-cont">
                <div class="col-24-24" id="section-col">
                    <div class="row" id="section-row">
                        <div class="col-2-24" id="inner-margin"></div>
                        <div class="col-20-24" id="section-content">                       

                            <p>
                                Once logged in, we'll load the PhyloAcc package. I've pre-made a <code class="inline">conda</code> environment with 
                                PhyloAcc installed in it. To load it, first load Anaconda:
                            </p>

                            <center><pre class="cmd"><code>module load Anaconda3</code></pre></center>

                            <div class="table-cont">
                                <table class="cmd-table">
                                    <thead><th class="tcol-1">Command line parameter</th><th class="tcol-2">Description</th></thead>
                                    <tr>
                                        <td class="tcol-1">module</td>
                                        <td class="tcol-2">The cluster's module system that contains pre-installed software.</td>
                                    </tr>
                                    <tr>
                                        <td class="tcol-1">load</td>
                                        <td class="tcol-2">The module sub-command telling it we want to load a package.</td>
                                    </tr>
                                    <tr>
                                        <td class="tcol-1">Anaconda3</td>
                                        <td class="tcol-2">The name of the package we want to load.</td>
                                    </tr>                                    
                                </table>
                            </div>

                            <p>Next, load my pre-made environment</p>

                            <center><pre class="cmd"><code>source activate /n/holylfs05/LABS/informatics/Everyone/phyloacc-data/workshop-20221027/env/phyloacc-workshop</code></pre></center>
                            
                            <div class="table-cont">
                                <table class="cmd-table">
                                    <thead><th class="tcol-1">Command line parameter</th><th class="tcol-2">Description</th></thead>
                                    <tr>
                                        <td class="tcol-1">source</td>
                                        <td class="tcol-2">The conda command to run scripts.</td>
                                    </tr>
                                    <tr>
                                        <td class="tcol-1">activate</td>
                                        <td class="tcol-2">The conda script to run which activates environments</td>
                                    </tr>
                                    <tr>
                                        <td class="tcol-1">/n/holylfs05/LABS/informatics/Everyone/phyloacc-data/workshop-20221027/env/phyloacc-workshop</td>
                                        <td class="tcol-2">The path to the environment we want to load.</td>
                                    </tr>
                                </table>
                            </div>

                            <p>
                                Then, let's make sure everything loaded correctly by running a check:
                            </p>

                            <center><pre class="cmd"><code>phyloacc.py --depcheck</code></pre></center>

                            <div class="table-cont">
                                <table class="cmd-table">
                                    <thead><th class="tcol-1">Command line parameter</th><th class="tcol-2">Description</th></thead>
                                    <tr>
                                        <td class="tcol-1">phyloacc.py</td>
                                        <td class="tcol-2">The main interface for PhyloAcc.</td>
                                    </tr>
                                    <tr>
                                        <td class="tcol-1">--depcheck</td>
                                        <td class="tcol-2">An option that tells PhyloAcc to check dependency paths.</td>
                                    </tr>                                    
                                </table>
                            </div>       

                            <p>
                                When you do this, you should hopefully see something like this, with both binaries reporting PASSED statuses:
                            </p>

                            <pre class="text"><code># --depcheck set: CHECKING DEPENDENCY PATHS AND EXITING.

   PROGRAM          PATH                STATUS
   -------------------------------------------
   phyloacc         PhyloAcc-ST         PASSED
   phyloacc-gt      PhyloAcc-GT         PASSED

# All dependencies PASSED.</code></pre>

                        <p>
                            If you don't see this, or one or both of the checks failed, please let me know.
                        </p>

                        </div>
                        <div class="col-2-24" id="inner-margin"></div>
                    </div>
                </div>
            </div>

            <!-- -------- END SECTION -------- -->

            <!-- ------- BEGIN SECTION ------- -->

            <a class="internal-link" name="project"></a>
            <div class="row" id="section-header-cont">
                <div class="col-24-24" id="section-header-row">
                    <div id="section-header">Creating a project directory</div>
                </div>
            </div>
             <div class="row" id="section-cont">
                <div class="col-24-24" id="section-col">
                    <div class="row" id="section-row">
                        <div class="col-2-24" id="inner-margin"></div>
                        <div class="col-20-24" id="section-content">                    

                            <p>
                                To keep things organized, let's make a new folder specifically for this workshop. First let's make sure you're in your
                                home directory:
                            </p>

                            <center><pre class="cmd"><code>cd ~</code></pre></center>

                            <div class="table-cont">
                                <table class="cmd-table">
                                    <thead><th class="tcol-1">Command line parameter</th><th class="tcol-2">Description</th></thead>
                                    <tr>
                                        <td class="tcol-1">cd</td>
                                        <td class="tcol-2">The Linux change directory</td>
                                    </tr>
                                    <tr>
                                        <td class="tcol-1">phyloacc-workshop</td>
                                        <td class="tcol-2">The path to the directory you want to change to. In this case, ~ is a shortcut
                                            meaning "your home directory".</td>
                                    </tr>
                                </table>
                            </div>

                            <p>
                                And this will create a folder in your
                                home directory, but feel free to do it anywhere you like.
                            </p>

                            <center><pre class="cmd"><code>mkdir phyloacc-workshop</code></pre></center>

                            <div class="table-cont">
                                <table class="cmd-table">
                                    <thead><th class="tcol-1">Command line parameter</th><th class="tcol-2">Description</th></thead>
                                    <tr>
                                        <td class="tcol-1">mkdir</td>
                                        <td class="tcol-2">The Linux create directory command</td>
                                    </tr>
                                    <tr>
                                        <td class="tcol-1">phyloacc-workshop</td>
                                        <td class="tcol-2">The name of the directory you want to create</td>
                                    </tr>
                                </table>
                            </div>

                            <p>
                                Finally let's enter our new directory so any files we create will be put in it:
                            </p>

                            <center><pre class="cmd"><code>cd phyloacc-workshop</code></pre></center>

                            <div class="table-cont">
                                <table class="cmd-table">
                                    <thead><th class="tcol-1">Command line parameter</th><th class="tcol-2">Description</th></thead>
                                    <tr>
                                        <td class="tcol-1">cd</td>
                                        <td class="tcol-2">The Linux change directory</td>
                                    </tr>
                                    <tr>
                                        <td class="tcol-1">phyloacc-workshop</td>
                                        <td class="tcol-2">The path to the directory you want to change to.</td>
                                    </tr>
                                </table>
                            </div>

                            <p>Now, let's move on to <a href="marine-mammals.html">an intro to our data</a></p>

                        </div>
                        <div class="col-2-24" id="inner-margin"></div>
                    </div>
                </div>
            </div>

            <!-- -------- END SECTION -------- -->

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
                <a href="marine-mammals.html">Next&nbsp;&gt;</a>
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
title = "PhyloAcc OEB275R - " + year

head = RC.readHead(title);
nav = RC.readNav(pagefile);
footer = RC.readFooter();

outfilename = "../../" + pagefile;

with open(outfilename, "w") as outfile:
    outfile.write(html_template.format(head=head, nav=nav, footer=footer));