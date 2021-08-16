############################################################
# For ConGen2021 site, 08.21
# This generates the file "organization.html"
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

    <a class="internal-link" name="file-systems"></a>
   	<div class="row" id="header">Project organization</div>

    <div class="row" id="body-row">
        <div class="col-3-24" id="side-nav-cont">
            <div id="side-nav">
                <span id="side-header">Page contents</span>
                <ul>
                    <li><a href="organization.html#file-systems">File systems</a></li>
                    <li><a href="organization.html#proj-folder">Project folders</a></li>
                </ul>
            </div>
        </div>

        <div class="col-21-24" id="main-cont">

            <div class="row" id="top-row-cont">
                <div class="col-24-24" id="top-row"></div>
            </div>
            <div class="row" id="section-header-cont">
                <div class="col-24-24" id="section-header-row">
                    <div id="section-header">File system refresher</div>
                </div>
            </div>

            <div class="row" id="section-cont">
                <div class="col-24-24" id="section-col">
                    <div class="row" id="section-row">
                        <div class="col-2-24" id="inner-margin"></div>
                        <div class="col-20-24" id="section-content">
                            <p>
                                One of the most important and under-taught aspects of data science is project organization. But part of the reason it isn't mentioned that
                                often is because there are so many good ways to do it. What follows is an explanation of how we setup this project, with justifications
                                for why we think this is a good setup. Hopefully, you can use this as the basis to figure out a file organization system that works for 
                                you!
                            </p>

                            <p>
                                Any project organization will ultimately come back to understanding how file systems work. Whether you're on Linux, Mac, Windows, or
                                something else, they generally have a lot in common:
                            </p>

                            <ol>
                                <li>Files are organized inside folders. Folders can contain other folders, which leads to a nesting, tree-like structure.</li>
                                <li>Files are referred to by paths, which are simply all folders and nested sub-folders in which the file lives. Folders and files
                                        in paths are separated by a slash (/) character*. In graphical file explorers, these paths are often hidden as they 
                                        are not needed to access files, but in text-based interactions with the file system, it is important to know your paths.</li>
                                <li>Command lines often recognize both absolute and relative paths. An absolute path is one that specifies all folders starting
                                        from the root of the file system, while a relative path is one that specifies all folders starting from the current
                                        working directory.

                                        <p>
                                            For example, if I am in folder A, which contains folder B, and want to list the contents of folder B, I could type:
                                        </p>

                                        <center><pre class="cmd-ne"><code>ls /root/users/username/A/B/</code></pre></center>

                                        <center><em>OR</em></center>

                                        <center><pre class="cmd-ne"><code>ls B</code></pre></center>

                                        <p>
                                            These are equivalent commands, with the first providing the absolute path, and the second providing only the relative:
                                            Since I'm already in folder A, the path to folder B is just B.
                                        </p>
                                </li>
                                <li>Usually, it isn't necessary to know the whole file system to the root -- paths relative to one's Home or User (or data/scratch) 
                                        folder are sufficient. In terminals of Unix-based systems (Mac and Linux) and modern Windows versions, the path to a 
                                        user's home directory is stored as the tilde character (<code class="inline">~</code>).</li>
                                <li>Other paths are stored as shortcuts: (<code class="inline">.</code>) means "the current directory" and (<code class="inline">..</code>)
                                        means "the directory directly above the current directory."

                                        <p>
                                            So, given the example earlier, if I'm now in folder B and want to list the contents of folder A, I can just type:
                                        </p>

                                        <center><pre class="cmd-ne"><code>ls ..</code></pre></center>
                                </li>                                     
                            </ol>
 
                        </div>
                        <div class="col-2-24" id="inner-margin"></div>
                    </div>
                </div>
            </div>
                                
            <a class="internal-link" name="proj-folder"></a>
            <div class="row" id="section-header-cont">
                <div class="col-24-24" id="section-header-row">
                    <div id="section-header">Organizing a project</div>
                </div>
            </div>

            <div class="row" id="section-cont">
                <div class="col-24-24" id="section-col">
                    <div class="row" id="section-row">
                        <div class="col-2-24" id="inner-margin"></div>
                        <div class="col-20-24" id="section-content">

                            <p>
                                So what does all of that have to do with starting a bioinformatics project? Well, the first thing I usually do to get started is to
                                create a <b>project folder</b> and populate it with other folders I think I'll need for the project. Folders like
                                <code class="inline">data</code>, <code class="inline">scripts</code>, <code class="inline">results</code>, <code class="inline">etc</code>,
                                and things like that. Then, knowing how the underlying file system works, I can easily add files, install softare, and run commands on
                                relative paths within the project folder.
                            </p>

                            <p>
                                Let's see how the current project folder's contents look using the <code class="inline">tree</code> command:
                            </p>

                            <center><pre class="cmd"><code>tree</code></pre></center>

                            <p>Following each command will be a table that goes through and explains each part of the command explicitly:</p>

                            <div class="table-cont">
                                <table class="cmd-table">
                                    <thead><th class="tcol-1">Command line parameter</th><th class="tcol-2">Description</th></thead>
                                    <tr>
                                        <td class="tcol-1">tree</td><td class="tcol-2">A command that lists the contents of the current directory
                                            and all sub-directories and displays them in a tree-like format.</td>
                                    </tr>
                                </table>
                            </div>
                            
                            <p>
                                This should show the full file tree descending from our current working directory:
                            </p>

                            <pre class="text"><code>{treestr}
                            </code></pre>

                            <p>
                                So, like I said, I like to start off with some basic folders for each project:
                            </p>

                            <div class="table-cont">
                                <table class="norm-table">
                                    <thead><th class="tcol-1">Folder</th><th class="tcol-2">Purpose</th></thead>
                                    <tr>
                                        <td class="tcol-1"><code class="inline">data</code></td>
                                        <td class="tcol-2">Holds all initial and processed data files for the project. This can include raw data (if not too large),
                                            data for reference genomes, and sample information (all in descriptive sub-folders). This can also include sub-folders
                                            for each step of analysis. For example, I might create numbered sub-folders along the way for each step like 
                                            <code class="inline">01-Read-trimming</code>, <code class="inline">02-Read-mapping</code>, 
                                            <code class="inline">03-Variant-calling</code>, etc.
                                        </td>
                                    </tr>
                                    <tr>
                                        <td class="tcol-1"><code class="inline">results</code></td>
                                        <td class="tcol-2">After data has been processed, the end goal should be something easily analyzable, e.g. summary statistics
                                            in comma separated (.csv) or tab delimited (.tab, .tsv) format whenever possible. I like to keep these main results files here
                                            for easy access.
                                        </td>
                                    </tr>
                                    <tr>
                                        <td class="tcol-1"><code class="inline">Scripts</code></td>
                                        <td class="tcol-2">Any code that I write for a project goes here.</td>
                                    </tr>
                                    <tr>
                                        <td class="tcol-1"><code class="inline">etc</code></td>
                                        <td class="tcol-2">Oftentimes project files accumulate that don't fit into one of these categories, such as an important figure
                                            from a paper I saved or notes I make. I usually lump all of those into the etc folder.
                                        </td>
                                    </tr>
                                </table>
                            </div>

                            <p>
                                Other folders might be important as a project progresses. For instance, a folder called <code class="inline">manuscript</code> as I
                                start writing, which itself contains sub-folders for <code class="inline">figs</code>, <code class="inline">tables</code>, and
                                <code class="inline">scripts</code>.
                            </p>

                            <p>
                                Next, lets talk a bit about processing textual data with <a href="commands.html">commands</a> and the more conceptual advantages
                                of manipulating data in this fashion.
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
                <a href="start.html">&lt;&nbsp;Previous</a>    
            </div>
        </div>
        <div class="col-6-24" id="nav-margin"></div>
        <div class="col-6-24" id="nav-btn-cont">
            <div class="nav-btn">
                <a href="commands.html">Next&nbsp;&gt;</a>
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
pagefile = "organization.html";
print("Generating " + pagefile + "...");
title = "ConGen2021 - Intro to Bioinformatics"

treestr = open("tree-output.txt", "r").read();
#print(treestr.encode());

head = RC.readHead(title);
nav = RC.readNav(pagefile);
footer = RC.readFooter();

outfilename = "../../" + pagefile;

with open(outfilename, "w") as outfile:
    outfile.write(html_template.format(head=head, nav=nav, treestr=treestr, footer=footer));