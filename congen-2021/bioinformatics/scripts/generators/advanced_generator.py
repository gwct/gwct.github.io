

############################################################
# For ConGen2021 site, 08.21
# This generates the file "advanced.html"
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

    <a class="internal-link" name="profiles"></a>
   	<div class="row" id="header">Overview of advanced topics</div>

    <div class="row" id="body-row">
        <div class="col-3-24" id="side-nav-cont">
            <div id="side-nav">
                <span id="side-header">Page contents</span>
                <ul>
					<li><a href="advanced.html#profiles">Profiles</a></li>
					<li><a href="advanced.html#multiplex">Terminal multiplexers</a></li>
					<li><a href="advanced.html#conda">Installing software with conda</a></li>
					<li><a href="advanced.html#clusters">Clusters</a></li>
					<li><a href="advanced.html#parallel">GNU parallel</a></li>
					<li><a href="advanced.html#snakemake">Snakemake</a></li>
                    <li><a href="advanced.html#search">Online resources</a></li>
                    <li><a href="advanced.html#other">Other stuff</a></li>
                </ul>
            </div>
        </div>

        <div class="col-21-24" id="main-cont">


            <div class="row" id="top-row-cont">
                <div class="col-24-24" id="top-row"></div>
            </div>

            <div class="row" id="section-cont">
                <div class="col-24-24" id="section-col">
                    <div class="row" id="section-row">
                        <div class="col-1-24" id="inner-margin"></div>
                        <div class="col-22-24" id="section-content">

                            <p>
                                What we've covered is a brief introduction about basic command line skills to get started in data science and bioinformatics. Besides
                                practicing the things we've covered, such as memorizing your file system, figuring out your project organization and how you interact
                                with text files, and command and scripting syntax, there are many other skills that can further enhance your data science workflows.
                                These skills and tools all build upon what we've introduced today, and could fill entire workshops themselves, so for now we will
                                only provide a brief overview of these tools, but are happy to answer questions about them later!
                            </p>

                        </div>
                        <div class="col-1-24" id="inner-margin"></div>
                    </div>
                </div>
            </div>
            
            <!-- ------- BEGIN SECTION ------- -->

            <div class="row" id="section-header-cont">
                <div class="col-24-24" id="section-header-row">
                    <div id="section-header">Profiles</div>
                </div>
            </div>

            <div class="row" id="section-cont">
                <div class="col-24-24" id="section-col">
                    <div class="row" id="section-row">
                        <div class="col-2-24" id="inner-margin"></div>
                        <div class="col-20-24" id="section-content">
                        
                        <p>
                            As you start connecting to remote servers to work more, you may find yourself doing a lot of tasks at startup, like loading the
                            programs you need to do your work or setting up shortcuts. Luckily, there is a way to automate this with {co}profiles{cc}.
                        </p>

                        <p>
                            {co}Profiles{cc} are text files that exist in your home directory. They have specific names such that the operating system knows
                            that they should be interpreted as <b>scripts</b>, meaning they contain a list of commands. These scripts are run automatically
                            when a user logs in, so any tasks you find yourself doing often at start-up or otherwise, you can put in these files so they
                            are done automatically.
                        </p>

                        <p>
                            In {co}bash{cc} (the common Unix shell program we are using), these files are {co}.bashrc{cc}, {co}.bash_profile{cc}, and {co}.profile{cc}.
                            Note that all of them have a period ({co}.{cc}) preceding their name, which means that these are hidden files and won't show up in the file
                            system unless explicitly told to. You can see what hidden files you have in your home directory by typing:
                        </p>

                        <center><pre class="cmd"><code>ls -a ~{cc}</pre></center>

                        <div class="table-cont">
                            <table class="cmd-table">
                                <thead><th class="tcol-1">Command line parameter</th><th class="tcol-2">Description</th></thead>
                                <tr>
                                    <td class="tcol-1">ls</td><td class="tcol-2">The Linux list directory contents command</td>
                                </tr>
                                <tr>
                                    <td class="tcol-1">-a</td><td class="tcol-2">This option tells {co}ls{cc} to list ALL files</td>
                                </tr>
                                <tr>
                                    <td class="tcol-1">~</td><td class="tcol-2">A preset shortcut to your home directory path</td>
                                </tr>
                            </table>
                        </div> 

                        <p>
                            When I do this on our server, I see both a {co}.bashrc{cc} and {co}.profile{cc} file. If these files don't exist on the server you use to work,
                            you can create them! If they do exist, don't be surprised to see commands already in them, as the OS may automatically put some in. As you
                            learn more about profiles, you can decide whether to keep these commands in yours or not.
                        </p>

                        <p>
                            Once you've located or created your profile, you can add any commands to it you want to be executed at login!
                        </p>

                        <p>
                            Read more about {co}profiles{cc}:
                            <ul>
                                <li><a href="https://www.linuxfordevices.com/tutorials/linux/bashrc-and-bash-profile" target="_blank">
                                    Understanding Linux .bashrc and .bash_profile files</a></li>
                                <li><a href="https://www.baeldung.com/linux/bashrc-vs-bash-profile-vs-profile" target="_blank">
                                    Difference Between .bashrc, .bash-profile, and .profile</a></li>
                                <li><a href="https://linuxhint.com/simple-guide-to-create-open-edit-bash-profile/" target="_blank">
                                    A Simple Guide to Create, Open, and Edit bash_profile</a></li>
                            </ul>
                        </p>

                        </div>
                        <div class="col-2-24" id="inner-margin"></div>
                    </div>
                </div>
            </div>

            <!-- -------- END SECTION -------- -->

            <!-- ------- BEGIN SECTION ------- -->

            <a class="internal-link" name="multiplex"></a>
            <div class="row" id="section-header-cont">
                <div class="col-24-24" id="section-header-row">
                    <div id="section-header">Terminal multiplexers</div>
                </div>
            </div>

            <div class="row" id="section-cont">
                <div class="col-24-24" id="section-col">
                    <div class="row" id="section-row">
                        <div class="col-2-24" id="inner-margin"></div>
                        <div class="col-20-24" id="section-content">
                        
                            <p>
                                The phrase <b>terminal multiplexer</b> definitely sounds advanced and cool, but they are actually really simple and can help 
                                streamline your bioinformatics work.
                            </p>

                            <p>
                                A terminal multiplexer is simply a program that allows you to open another terminal within your currently running terminal, kind of
                                like having multiple tabs open in a browser. What's even better though is that, <b>the second terminal will continue to run even if
                                you disconnect</b>. This is obviously great because it allows you to start a command that may take a while and come back to it later
                                without having to worry about losing your work. Or you could start a command on your lab at work, suspend the multiplexed terminal, disconnect,
                                walk home, reconnect, and resume the terminal to check on your progress! In essence, it allows you to run commands in the background
                                (similar to <a href="https://www.geeksforgeeks.org/nohup-command-in-linux-with-examples/" target="_blank">nohup &</a>, which we're not
                                even covering because multiplexers are so much better), but also allows you to easily resume and interact with the process running.
                            </p>

                            <p>
                                There are serveal <a href="https://en.wikipedia.org/wiki/Terminal_multiplexer" target="_blank">terminal multiplexers</a> available
                                for Linux and Mac, but the two most-used ones are:
                                <ol>
                                    <li><a href="https://www.gnu.org/software/screen/" target="_blank">
                                        screen</a></li>
                                    <li><a href="https://github.com/tmux/tmux/wiki" target="_blank">
                                        tmux</a></li>
                                </ol>
                            </p>

                            <p>
                                I personally use {co}screen{cc}, and haven't found the need to mess around with any others. And I've put together a super brief
                                guide to {co}screen{cc} <a href="https://goodest-goodlab.github.io/griz/start.html#screen" target="_blank">here</a>.
                            </p>

                        </div>
                        <div class="col-2-24" id="inner-margin"></div>
                    </div>
                </div>
            </div>

            <!-- -------- END SECTION -------- -->

            <!-- ------- BEGIN SECTION ------- -->

            <a class="internal-link" name="conda"></a>
            <div class="row" id="section-header-cont">
                <div class="col-24-24" id="section-header-row">
                    <div id="section-header">Installing software with conda & conda environments</div>
                </div>
            </div>

            <div class="row" id="section-cont">
                <div class="col-24-24" id="section-col">
                    <div class="row" id="section-row">
                        <div class="col-2-24" id="inner-margin"></div>
                        <div class="col-20-24" id="section-content">
                        
                        <p>
                            If you have any prior experience with data science in the command line you know that installing new software is often the most
                            painful part of a project. The dreaded <b>command not found</b> and <b>library path not found</b> errors can stop you in your tracks.
                            Some clusters have {co}module systems{cc} that can make life a lot easier, but they often have only the most popular software, and
                            you would have to wait for an administrator to install what you need.
                        </p>

                        <p>
                            Luckily, a program called <a href="https://en.wikipedia.org/wiki/Anaconda_(Python_distribution)" target="_blank">Anaconda</a>, along
                            with it's software manager, <a href="https://en.wikipedia.org/wiki/Conda_(package_manager)" target="_blank">conda</a>.
                            {co}Anaconda{cc} is a distribution of the Python programming language that has grown into a useful tool for data science. Importantly,
                            it allows users to install software on their local account with {co}conda{cc}.
                        </p>

                        <p>
                            {co}conda{cc} also has the capability to run software in different <b>environments</b>. An environment is simply an emulated fresh
                            installation of the operating system. Since the software you want to use often depends on other software, {co}conda{cc} handles the
                            installation of these dependencies, and using separate environments for separate projects or software can often reduce these issues
                            further.
                        </p>

                        <p>
                            <a href="https://anaconda.org/bioconda" target="_blank">bioconda</a> is a <b>channel</b> of conda specifically tailored to bioinformatics
                            software.
                        </p>

                        <p>
                            I have another brief guide to installing and using conda <a href="https://goodest-goodlab.github.io/griz/install.html" target="_blank">here</a>.
                        </p>

                        </div>
                        <div class="col-2-24" id="inner-margin"></div>
                    </div>
                </div>
            </div>

            <!-- -------- END SECTION -------- -->

            <!-- ------- BEGIN SECTION ------- -->

            <a class="internal-link" name="clusters"></a>
            <div class="row" id="section-header-cont">
                <div class="col-24-24" id="section-header-row">
                    <div id="section-header">Job scheduling with high performance computing (HPC) clusters</div>
                </div>
            </div>

            <div class="row" id="section-cont">
                <div class="col-24-24" id="section-col">
                    <div class="row" id="section-row">
                        <div class="col-2-24" id="inner-margin"></div>
                        <div class="col-20-24" id="section-content">
                        
                            <p>
                                As you scale up your workflows, you may find that the resources on the server you login to may no longer be sufficient to run
                                the programs you want. This is where scheduling jobs on HPC clusters comes in handy.
                            </p>

                            <p>
                                Basically, when you login to an HPC cluster, you login to one particular node (or computer) of that cluster. This node is designed
                                to handle user interactions and other low-resource activities. On this node, or another node that this node talks to (the head node) a
                                job scheduling software is usually installed. This software coordinates the resources of all users who are requesting to run jobs on 
                                the cluster and passes the jobs to other, high resource computer nodes on which the jobs are actually run. There is also often another
                                node or set of nodes dedicated to big data storage.
                            </p>

                            <div class="row" id="img-row">
                                <div class="col-4-24" id="margin"></div>
                                <div class="col-16-24" id="img-col">
                                    <img id="res-img" src="img/hpc.svg">
                                    <center><span class="fig-caption">Figure 6.1: A simple diagram of an HPC cluster 
                                        (<a href="https://docs.hpc.qmul.ac.uk/intro/" target="_blank">Source</a>).</span></center>
                                </div>
                                <div class="col-4-24" id="margin"></div>
                            </div>

                            <p>
                                HPC clusters differ between institutions, so be sure to check how yours is setup. Hopefully the administrators provide some
                                helpful documents to get started. But generally, you work out your workflow on some test data, then put the commands you want to
                                run into a script, along with the resources needed to run, and then submit this script through the <b>job scheduler</b>.
                            </p>

                            <p>
                                There are many job schedulers out there, but a popular one is <a href="https://slurm.schedmd.com/documentation.html" target="_blank">SLURM</a>.
                                I have a brief guide to the {co}SLURM{cc} job scheduler implemented on the University of Montana's cluster, Griz, 
                                <a href="https://goodest-goodlab.github.io/griz/jobs.html" target="_blank">here</a>.
                            </p>

                        </div>
                        <div class="col-2-24" id="inner-margin"></div>
                    </div>
                </div>
            </div>

            <!-- -------- END SECTION -------- -->

            <!-- ------- BEGIN SECTION ------- -->

            <a class="internal-link" name="parallel"></a>
            <div class="row" id="section-header-cont">
                <div class="col-24-24" id="section-header-row">
                    <div id="section-header">Scaling up with {co}GNU parallel{cc}</div>
                </div>
            </div>

            <div class="row" id="section-cont">
                <div class="col-24-24" id="section-col">
                    <div class="row" id="section-row">
                        <div class="col-2-24" id="inner-margin"></div>
                        <div class="col-20-24" id="section-content">
                        
                            <p>
                                Again, as you increase your throughput you're going to start to wonder how you can run commands in parallel. A really versatile
                                and powerful way to do this directly in the command line is with 
                                <a href="https://www.gnu.org/software/parallel/" target="_blank">GNU parallel</a>.
                            </p>

                            <p>
                                {co}parallel{cc} can easily take a list of commands and a number of jobs and run that many jobs in parallel:
                            </p>

                            <center><pre class="cmd-ne"><code>parallel -j 20 &lt; list-of-cmds.txt{cc}</pre></center>

                            <div class="table-cont">
                                <table class="cmd-table">
                                    <thead><th class="tcol-1">Command line parameter</th><th class="tcol-2">Description</th></thead>
                                    <tr>
                                        <td class="tcol-1">parallel</td><td class="tcol-2">The GNU parallel program that allows users to run
                                            commands in parallel across multiple cores</td>
                                    </tr>
                                    <tr>
                                        <td class="tcol-1">-j 20</td><td class="tcol-2">This tells {co}parallel{cc} to try and run 20 commands (jobs)
                                            at once</td>
                                    </tr>
                                    <tr>
                                        <td class="tcol-1">&lt;</td><td class="tcol-2">Similar to the redirect shortcut (&gt;) that saves output
                                            from a command to a file, this symbol (&lt;) tells the command to read input from a file</td>
                                    </tr>
                                    <tr>
                                        <td class="tcol-1">list-of-cmds.txt</td><td class="tcol-2">A file with multiple commands in it to pass to {co}parallel{cc}, with
                                            one command per line</td>
                                    </tr>
                                </table>
                            </div> 

                            <p>
                                This can really speed up your work. {co}parallel{cc} may or may not be installed on your cluster, 
                                but is available as a {co}conda{cc} package. I have a brief guide to {co}parallel{cc} and how to use Python scripts to generate
                                commands for it <a href="https://goodest-goodlab.github.io/griz/start.html#parallel" target="_blank">here</a>.
                            </p>

                        </div>
                        <div class="col-2-24" id="inner-margin"></div>
                    </div>
                </div>
            </div>

            <!-- -------- END SECTION -------- -->

            <!-- ------- BEGIN SECTION ------- -->

            <a class="internal-link" name="snakemake"></a>
            <div class="row" id="section-header-cont">
                <div class="col-24-24" id="section-header-row">
                    <div id="section-header">Complex workflows with Snakemake</div>
                </div>
            </div>

            <div class="row" id="section-cont">
                <div class="col-24-24" id="section-col">
                    <div class="row" id="section-row">
                        <div class="col-2-24" id="inner-margin"></div>
                        <div class="col-20-24" id="section-content">
                        
                            <p>
                                <a href="https://snakemake.github.io/" target="_blank">Snakemake</a> is a Python-based scripting language specifically designed
                                to help scale up and make bioinformatics workflows reproducible. The basic idea behind {co}snakemake{cc} is that we often run
                                the same commands over many different but similar files (e.g., VCF files from different samples, alignments from different genes, etc.)
                                A {co}snakemake{cc} file then consists of rules that depend on each other based on the specified output files of previous rules. Rules can be 
                                run over a range of files (e.g., samples) allowing one to compactly represent and run an entire workflow. {co}Snakemake{cc} also integrates
                                well with HPC clusters to run these rules in parallel.
                            </p>

                            <p>
                                While I've found {co}snakemake{cc} to be extremely powerful, it is also somewhat difficult to learn. Importantly, it is based off of
                                Python syntax, which allows for great integration with Python code, also means familiarity with Python is a must. I have also found
                                the <a href="https://snakemake.readthedocs.io/en/stable/tutorial/tutorial.html" target="_blank">documentation for {co}snakemake{cc}</a>
                                to be complex, though there may be some great tutorials out there that I haven't found yet.
                            </p>

                            <p>
                                All of this means that {co}snakemake{cc} could take up a whole workshop, but I'm happy to answer any questions I can about it!
                            </p> 

                        </div>
                        <div class="col-2-24" id="inner-margin"></div>
                    </div>
                </div>
            </div>

            <!-- -------- END SECTION -------- -->

            <!-- ------- BEGIN SECTION ------- -->

            <a class="internal-link" name="search"></a>
            <div class="row" id="section-header-cont">
                <div class="col-24-24" id="section-header-row">
                    <div id="section-header">Searching for answers</div>
                </div>
            </div>

            <div class="row" id="section-cont">
                <div class="col-24-24" id="section-col">
                    <div class="row" id="section-row">
                        <div class="col-2-24" id="inner-margin"></div>
                        <div class="col-20-24" id="section-content">
                        
                            <p>
                                I think I've saved the most important skill for last: how to search for answers on the internet. Many times you'll come across
                                an error or want to figure out a solution to an analysis and not know where to start. Luckily, we have the vast collective knowledge
                                of the internet to help us out!
                            </p>

                            <p>
                                Oftentimes simply searching for the error message you receive is enough to bring up some discussion about it, but that may not answer
                                your question exactly. So I say that simply "knowing how to search" for something, or knowing what to type in to get you the answers 
                                you want, is one of the greatest skills of a data scientist. In that vain, it really helps to know more about the underlying 
                                program/command/data structure that the error is about to get you the answers you need.
                            </p>

                            <p>
                                That being said, there are some great resources out there besides search engines where people post their questions and others
                                respond:

                                <ol>
                                    <li><a href="https://stackoverflow.com/" target="_blank">Stack overflow</a></li>
                                    <li><a href="https://bioinformatics.stackexchange.com/" target="_blank">Stack exchange for bioinformatics</a></li>
                                    <li><a href="http://seqanswers.com/" target="_blank">SeqAnswers</a></li>
                                    <li><a href="https://www.biostars.org/" target="_blank">BioStars</a></li>
                                </ol>
                             
                        </div>
                        <div class="col-2-24" id="inner-margin"></div>
                    </div>
                </div>
            </div>

            <!-- -------- END SECTION -------- -->

            <!-- ------- BEGIN SECTION ------- -->

            <a class="internal-link" name="other"></a>
            <div class="row" id="section-header-cont">
                <div class="col-24-24" id="section-header-row">
                    <div id="section-header">The other stuff</div>
                </div>
            </div>

            <div class="row" id="section-cont">
                <div class="col-24-24" id="section-col">
                    <div class="row" id="section-row">
                        <div class="col-2-24" id="inner-margin"></div>
                        <div class="col-20-24" id="section-content">
                        
                            <p>
                                Of course this workshop focuses on text-based data science from the command line. But there is another side to data science and 
                                bioinformatics that we haven't touched on. I recently read <a href="https://plain-text.co/" target="_blank">a take</a> about this
                                that I agree with: data science can be broken down into two parts: (1) The Engineering Model (or the text model), where most work
                                is done with text files in the command line and version control, and that we've covered here today, and (2) The Office Model 
                                where work is done on more centralized files that can be saved and passed between collaborators (think a Word Document for a
                                manuscript).                                
                            </p>

                            <p>
                                This I think is a good distinction, but I would expand the Office Model to include data visualization as well, which can be 
                                done with things like <a href="https://jupyter.org/" target="_blank">Jupyter notebooks</a> or
                                <a href="https://rmarkdown.rstudio.com/" target="_blank">R Markdown</a> scripts.
                            </p>

                            <p>
                                All of this is to say that there is much more out there that we haven't covered.
                            </p>

                        </div>
                        <div class="col-2-24" id="inner-margin"></div>
                    </div>
                </div>
            </div>

            <!-- -------- END SECTION -------- -->

            <a class="internal-link" name="fin"></a>
            <div class="row" id="section-header-cont">
                <div class="col-24-24" id="section-header-row">
                    <div id="section-header">Fin</div>
                </div>
            </div>    

            <div class="row" id="section-cont">
                <div class="col-24-24" id="section-col">
                    <div class="row" id="section-row">
                        <div class="col-2-24" id="inner-margin"></div>
                        <div class="col-20-24" id="section-content">

                            <h2>
                                This brings us to <a href="end.html">the end</a> of our Introduction to Bioinformatics workshop. We'll be available to answer
                                questions throughout the rest of the symposium. Thanks for attending!
                            </h2>
                        
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
                <a href="wolf-snps.html">&lt;&nbsp;Previous</a>    
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
"""

######################
# Main block
######################
pagefile = "advanced.html";
print("Generating " + pagefile + "...");
title = "ConGen2021 - Intro to Bioinformatics"


head = RC.readHead(title);
nav = RC.readNav(pagefile);
footer = RC.readFooter();

outfilename = "../../" + pagefile;

with open(outfilename, "w") as outfile:
    outfile.write(html_template.format(head=head, nav=nav, footer=footer, co="<code class='inline'>", cc="</code>"));
