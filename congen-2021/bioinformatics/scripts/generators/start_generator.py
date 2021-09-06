############################################################
# For ConGen2020 site, 08.20
# This generates the file "start.html"
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

    <a class="internal-link" name="start"></a>
   	<div class="row" id="header">Introduction to Bioinformatics workshop</div>

    <div class="row" id="body-row">
        <div class="col-3-24" id="side-nav-cont">
            <div id="side-nav">
                <span id="side-header">Page contents</span>
                <ul>
                    <li><a href="start.html#start">Getting started</a></li>
                    <li><a href="start.html#downloading">Downloading the project</a></li>
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
                                <p>Hello! Today we'll be going through some hands-on activities to help you get familiar with how many bioinformatics tasks can be done directly from the command line.</p>

                                <p>The first thing you should do if you haven't done so is connect to the ConGen server. We'll be working exclusively in the RStudio browser interface that 
                                    you should be familiar with by now, but if you have questions or problems at any point please feel free to ask! Just in case, here's an annotated 
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

            <a class="internal-link" name="downloading"></a>
            <div class="row" id="section-header-cont">
                <div class="col-24-24" id="section-header-row">
                    <div id="section-header">Downloading the project</div>
                </div>
            </div>
            <div class="row" id="section-cont">
                <div class="col-24-24" id="section-col">
                    <div class="row" id="section-row">
                        <div class="col-2-24" id="inner-margin"></div>
                        <div class="col-20-24" id="section-content">
                            <p>Today we'll be doing some basic bioinformatics tasks from the command line. We'll get to the specifics of the data later, but for now
                                please download the project template we've provided on github.
                            </p>

                            <p>First, make sure you're in your home directory. If you're not, or you're not sure if you are, run the command:</p>

                            <center><pre class="cmd"><code>cd ~</code></pre></center>

                            <div class="table-cont">
                                <table class="cmd-table">
                                    <thead><th class="tcol-1">Command line parameter</th><th class="tcol-2">Description</th></thead>
                                    <tr>
                                        <td class="tcol-1">cd</td><td class="tcol-2">The Linux change directory command</td>
                                    </tr>
                                    <tr>
                                        <td class="tcol-1">~</td><td class="tcol-2">The path to the directory you want to change to. ~ is a shortcut for
                                        "the current user's home directory."</td>
                                    </tr>
                                </table>
                            </div>

                            <p>Next, download the project repository using <code class="inline">git</code>:</p>

                            <center><pre class="cmd"><code>git clone https://github.com/gwct/congen-2021-bioinformatics.git</code></pre></center>
                            
                            <div class="table-cont">
                                <table class="cmd-table">
                                    <thead><th class="tcol-1">Command line parameter</th><th class="tcol-2">Description</th></thead>
                                    <tr>
                                        <td class="tcol-1">git</td><td class="tcol-2">A cross platform program for vesrion control and syncing of software 
                                        and data projects.</td>
                                    </tr>
                                    <tr>
                                        <td class="tcol-1">clone</td><td class="tcol-2">The git sub-program to make download an exact copy of a repository.</td>
                                    </tr>
                                    <tr>
                                        <td class="tcol-1">https://github.com/gwct/congen-2021-bioinformatics.git</td>
                                        <td class="tcol-2">The URL of the project repository. This can be found on the webpage of the repository.</td>
                                    </tr>
                                </table>
                            </div>

                            <p>
                                Git is very powerful software for sharing your projects and used commonly to share code and data from scientific papers, 
                                but we won't talk about it much today other than using the <code class="inline">clone</code> command to download the project. 
                                You don't need a github account to clone a repository, but you do need git installed on your computer to do so.
                            </p>

                            <div id="msg_cont">
                                <div id="msg">
                                    <div id="msg_banner">Tip - More info about git</div>
                                    <div id="msg_text">
                                        <p>
                                            If you're interested in learning more about git there are a ton of guides and docs out there for you to search for. To get
                                            started, we've put together a couple of how-tos for understanding git basics here:
                                        </p>

                                        <center><a href="https://github.com/goodest-goodlab/good-protocols/tree/main/how-tos" target="_blank">git how-tos</a></center>

                                        <p></p>
                                    </div>
                                </div>
                            </div>

                            <p>
                                After the clone command completes, you should now have a folder in your home directory called <code class="inline">congen-2021-bioinformatics</code>.
                                Make sure it's there with <code class="inline">ls</code>:
                            </p>

                            <center><pre class="cmd"><code>ls</code></pre></center>

                            <div class="table-cont">
                                <table class="cmd-table">
                                    <thead><th class="tcol-1">Command line parameter</th><th class="tcol-2">Description</th></thead>
                                    <tr>
                                        <td class="tcol-1">ls</td><td class="tcol-2">The Linux list directory contents command. With no other options given,
                                            this lists the contents of the current directory.</td>
                                    </tr>
                                </table>
                            </div>                            

                            <p>And next change into that directory:</p>

                            <center><pre class="cmd"><code>cd congen-2021-bioinformatics</code></pre></center>

                            <div class="table-cont">
                                <table class="cmd-table">
                                    <thead><th class="tcol-1">Command line parameter</th><th class="tcol-2">Description</th></thead>
                                    <tr>
                                        <td class="tcol-1">cd</td><td class="tcol-2">The Linux change directory command</td>
                                    </tr>
                                    <tr>
                                        <td class="tcol-1">~</td><td class="tcol-2">The path to the directory you want to change to.</td>
                                    </tr>
                                </table>
                            </div>

                            <p>Using this project template data, we'll be performing the following tasks today:</p>

                            <ol>
                                <li>Talking about project organization, common commands, and text editors and work setups.</li>
                                <li>Introducing common bioinformatics file formats.</li>
                                <li>Using the command line to do a basic analysis of structural variation in a sample of 32 Rhesus macaques and
                                    of SNPs in 35 gray wolves.</li>
                                <li>Time permitting, briefly touch on some next steps in developing more advanced bioinformatics skills</li>
                            </ol>

                            <p>Now, let's move on to <a href="organization.html">Project Organization</a></p>

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
                <a href="organization.html">Next&nbsp;&gt;</a>
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
title = "ConGen2021 - Intro to Bioinformatics"

head = RC.readHead(title);
nav = RC.readNav(pagefile);
footer = RC.readFooter();

outfilename = "../../" + pagefile;

with open(outfilename, "w") as outfile:
    outfile.write(html_template.format(head=head, nav=nav, footer=footer));