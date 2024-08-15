############################################################
# For ConGen2021 site, 08.21
# This generates the file "commands.html"
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

    <a class="internal-link" name="macaque-data"></a>
   	<div class="row" id="header">Structural variation in macaques</div>

    <div class="row" id="body-row">
        <div class="col-3-24" id="side-nav-cont">
            <div id="side-nav">
                <span id="side-header">Page contents</span>
                <ul>
                    <li><a href="macaque-svs.html#macaque-data">Macaque dataset</a></li>
                    <li><a href="macaque-svs.html#bed">Bed files</a></li>
                    <li><a href="macaque-svs.html#summarizing-svs">Summarizing SVs</a></li>
                    <li><a href="macaque-svs.html#grep">Introduction to grep</a></li>
                    <li><a href="macaque-svs.html#awk">Introduction to awk</a></li>
                    <li><a href="macaque-svs.html#grep-awk">Combining grep and awk</a></li>
                    <li><a href="macaque-svs.html#gtf">Annotation files</a></li>
                    <li><a href="macaque-svs.html#gtf-to-bed">Converting GTF to bed</a></li>
                    <li><a href="macaque-svs.html#bedtools">Bedtools intersect</a></li>
                </ul>
            </div>
        </div>

        <div class="col-21-24" id="main-cont">

            <div class="row" id="top-row-cont">
                <div class="col-24-24" id="top-row"></div>
            </div>
            <div class="row" id="section-header-cont">
                <div class="col-24-24" id="section-header-row">
                    <div id="section-header">Rhesus macaque dataset</div>
                </div>
            </div>

            <div class="row" id="section-cont">
                <div class="col-24-24" id="section-col">
                    <div class="row" id="section-row">
                        <div class="col-2-24" id="inner-margin"></div>
                        <div class="col-20-24" id="section-content">
                            <p>
                                Today, we're going to use what we've learned about the command line to perform some basic bioinformatics tasks on a sample
                                of 32 rhesus macaque whole genomes. Rhesus macaques are an Old World monkey, found throughout southern Asia, and are a common model organism for
                                the study of human disease and primate evolution. We sequenced these genomes to study the evolution structural variation over different 
                                timescales (<a href="https://doi.org/10.1093/molbev/msaa303" target="_blank">Thomas et al. 2020</a>).
                            </p>

                            <div class="row" id="img-row">
                                <div class="col-4-24" id="margin"></div>
                                <div class="col-16-24" id="img-col">
                                    <img id="res-img" src="img/macaque.png">
                                    <center><span class="fig-caption">Figure 4.1: A Rhesus macaque <a href="https://commons.wikimedia.org/wiki/File:Macaque_India_3.jpg/" target="_blank">(left)</a>
                                        and Old World monkeys' placement in the primate phylogeny
                                        <a href="https://flexbooks.ck12.org/cbook/ck-12-college-human-biology-flexbook-2.0/section/7.2/primary/lesson/primate-classification-and-evolution-chumbio/" target="_blank">(right)</a>
                                        .</span></center>
                                </div>
                                <div class="col-4-24" id="margin"></div>
                            </div>

                            <p>
                                As a very brief overview, we sequenced genomes from 32 macaque individuals from several pedigrees and mapped the reads to the
                                <a href="https://uswest.ensembl.org/Macaca_mulatta/Info/Index" target="_blank">macaque reference genome</a>. Then, using programs that look at the orientation
                                of the mapped reads as well as the read depth, we identified regions in each sample with may have been deleted or duplicated. Today, we'll look at these structural
                                variant calls.
                            </p>

                        </div>
                        <div class="col-2-24" id="inner-margin"></div>
                    </div>
                </div>
            </div>
                                
            <a class="internal-link" name="bed"></a>
            <div class="row" id="section-header-cont">
                <div class="col-24-24" id="section-header-row">
                    <div id="section-header">Bed files</div>
                </div>
            </div>

            <div class="row" id="section-cont">
                <div class="col-24-24" id="section-col">
                    <div class="row" id="section-row">
                        <div class="col-2-24" id="inner-margin"></div>
                        <div class="col-20-24" id="section-content">

                            <p>
                                You'll find in your project repo (folder) a file at the following path: <code class="inline">data/macaque-svs/macaque-svs-filtered.bed</code>
                            </p>


                            <p>
                                Note that this file has the extension <code class="inline">.bed</code>. This tells us something about how the text within the file is formatted.
                                If you remember our central dogma for Unix commands (<b>formatted text -> command -> processed text</b>), you'll know that being familiar
                                with how our files are formatted is really important.
                            </p>

                            <p>
                                So what is a <code class="inline">.bed</code> file? <code class="inline">Bed</code> files are used to indicate regions within a genome. It
                                is an extremely flexible format -- these regions can represent anything. 
                            </p>

                            <p>
                                In it's most basic form, a <code class="inline">.bed</code> file consists of three columns of text, separated by a tab character. The first
                                column represents the chromosome or assembly scaffold of the region, while the second indicates the starting coordinate, and the third indicates
                                the ending coordinate of the region.
                            </p>

                            <p>Each row represents a separate region</p>

                            <p>
                                Additional columns can be defined, particularly of interest is a fourth column, which indicates a name or ID for the current region.
                                See these links for more information about <code class="inline">.bed</code> files:

                                <ul>
                                    <li><a href="https://bedtools.readthedocs.io/en/latest/content/general-usage.html" target="_blank">bedtools description of BED format</a></li>
                                    <li><a href="http://genome.ucsc.edu/FAQ/FAQformat#format1" target="_blank">UCSC description of BED format</a></li>
                                </ul>
                            </p>
                                
                            <p>
                                Let's take a look at our <code class="inline">.bed</code> file:
                            </p>

                            <center><pre class="cmd"><code>less -S data/macaque-svs/macaque-svs-filtered.bed</code></pre></center>

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
                                        <td class="tcol-1">data/macaque-svs/macaque-svs-filtered.bed</td><td class="tcol-2">The path to the file you want to view</td>
                                    </tr>
                                </table>
                            </div>

                            <p>You should see something like this:</p>

                            <pre class="text"><code>chr1    89943   90471   chr1:89943:&lt;DUP&gt;:528:1907.19
chr1    130740  131675  chr1:130740:&lt;DEL&gt;:935:285.63
chr1    218574  219534  chr1:218574:&lt;DUP&gt;:960:5699.01
chr1    219608  220078  chr1:219608:&lt;DUP&gt;:470:2074.69
chr1    519434  541582  chr1:519434:&lt;DUP&gt;:22148:1673.64
chr1    519473  542033  chr1:519473:&lt;DUP&gt;:22560:2560.16
chr1    520173  541800  chr1:520173:&lt;DEL&gt;:21627:2955.11
chr1    525401  525806  chr1:525401:&lt;DEL&gt;:405:2986.21
chr1    541132  590572  chr1:541132:&lt;DEL&gt;:49440:316.41
chr1    552968  582234  chr1:552968:&lt;DUP&gt;:29266:189.32
chr1    766381  766933  chr1:766381:&lt;DEL&gt;:552:5099.0</code></pre> 

                            <p>
                                As defined above, this bed file has text in columns, separated by tabs. The first column being the chromosome of the region, second
                                being the start coordinate, and third being the end coordinate. This <code class="inline">.bed</code> file also has the optional
                                fourth column giving us a name or ID for each region. In this case, the name indicates whether the structural variant call is a
                                deletion (&lt;DEL&gt;) or a duplication (&lt;DUP&gt;).
                            </p>

                        </div>
                        <div class="col-2-24" id="inner-margin"></div>
                    </div>
                </div>
            </div>

            <a class="internal-link" name="summarizing-svs"></a>
            <div class="row" id="section-header-cont">
                <div class="col-24-24" id="section-header-row">
                    <div id="section-header">Summarizing SVs from the command line</div>
                </div>
            </div>

            <div class="row" id="section-cont">
                <div class="col-24-24" id="section-col">
                    <div class="row" id="section-row">
                        <div class="col-2-24" id="inner-margin"></div>
                        <div class="col-20-24" id="section-content">
                            <p>
                                So our collaborator hands us this BED file, and we want to get a general idea about the called variants. What can we do from
                                the command line?
                            </p>

                            <h3>TASK 1: How many structural variants are there?</h3>

                                <p>
                                    The most basic thing we'll want to know is how many structural variants have been called. Recalling that each line in a
                                    <code class="inline">bed</code> file represents one region, which in this case means one structural variant, we can simply count the number of lines
                                    in the file with the <code class="inline">wc</code> command:
                                </p>

                                <center><pre class="cmd"><code>wc -l data/macaque-svs/macaque-svs-filtered.bed</code></pre></center>

                                <div class="table-cont">
                                    <table class="cmd-table">
                                        <thead><th class="tcol-1">Command line parameter</th><th class="tcol-2">Description</th></thead>
                                        <tr>
                                            <td class="tcol-1">wc</td><td class="tcol-2">The Linux word count command. Counts the number of lines, words, and
                                                characters in an input file.</td>
                                        </tr>
                                        <tr>
                                            <td class="tcol-1">-l</td><td class="tcol-2">Tells <code class="inline">wc</code> to only count number of lines</td>
                                        </tr>
                                        <tr>
                                            <td class="tcol-1">data/macaque-svs/macaque-svs-filtered.bed</td><td class="tcol-2">The path to the file you want to count</td>
                                        </tr>
                                    </table>
                                </div>

                                <p>
                                    When I do this, I see
                                </p>

                                <pre class="text"><code>3646</code></pre>

                                <p>
                                    Which means there are a total of 3,646 structural variants called in our sample of 32 macaques.
                                </p>

                        </div>
                        <div class="col-2-24" id="inner-margin"></div>
                    </div>
                </div>
            </div>

            <a class="internal-link" name="grep"></a>
            <div class="row" id="section-header-cont">
                <div class="col-24-24" id="section-header-row">
                    <div id="section-header">Introduction to grep</div>
                </div>
            </div>

            <div class="row" id="section-cont">
                <div class="col-24-24" id="section-col">
                    <div class="row" id="section-row">
                        <div class="col-2-24" id="inner-margin"></div>
                        <div class="col-20-24" id="section-content">

                            <h3>TASK 2: How many DELETIONS are there?</h3>

                                <p>
                                    In order to answer this question, we must first separate out the deletions from the duplications. Then we can take the resulting text
                                    and use <code class="inline">wc -l</code> again.
                                </p>

                                <p>
                                    As with many problems in data science and scripting, there are many possible solutions. What we'll use is the Unix pattern matching
                                    command, <code class="inline">grep</code> along with the piping function we learned about before.
                                </p>

                                <p>

                                    <a href="https://www.gnu.org/software/grep/" target="_blank">grep</a> stands for "<b>g</b>lobally search for a <b>r</b>egular
                                    <b>e</b>xpression and <b>p</b>rint matching lines," which is a pretty descriptive way of saying it is a command for string and
                                    pattern matching. You supply grep with a file you want to search, and a string within that file you want to search for, and it 
                                    will print out each line in the file that contains that string:
                                </p>

                                <center><pre class="cmd-ne"><code>grep "&lt;string or pattern&gt;" &lt;input file&gt;</code></pre></center>

                                <div class="table-cont">
                                    <table class="cmd-table">
                                        <thead><th class="tcol-1">Command line parameter</th><th class="tcol-2">Description</th></thead>
                                        <tr>
                                            <td class="tcol-1">grep</td><td class="tcol-2">A Unix string and pattern searching command</td>
                                        </tr>
                                        <tr>
                                            <td class="tcol-1">'&lt;string or pattern&gt;'</td><td class="tcol-2">The string or pattern you want to search for</td>
                                        </tr>
                                        <tr>
                                            <td class="tcol-1">&lt;input file&gt;</td><td class="tcol-2">The path to the file you want to search</td>
                                        </tr>
                                    </table>
                                </div>     

                                <p>
                                    Searching an input file may seem like a simple task, but can be enormously helpful, and is made even more powerful by the use
                                    of <b><a href="https://en.wikipedia.org/wiki/Regular_expression" target="_blank">regular expressions</a></b>. Regular expressions
                                    are a syntax for string matching using wildcards to indicate patterns. The <code class="inline">*</code> wild card is a regular
                                    expression that you've learned about previously which means "match ANY string."
                                </p>

                                <p>
                                    Using regular expressions, you can both expand and narrow the types of strings you're searching for. For instance, let's say I have
                                    a file, <code class="inline">sample-ids.txt</code> that lists sample IDs, one per line, all of the pattern. Some samples are 
                                    from batch "A" and follow the pattern A-<sample number>. Some are from batch "B" and similarly follow the pattern B-<sample number>. 
                                    Maybe I want to perform an operation only on the samples in batch A. I could use grep to get all of them:
                                </p>

                                <center><pre class="cmd-ne"><code>grep "A-*" sample-ids.txt</code></pre></center>

                                <div class="table-cont">
                                    <table class="cmd-table">
                                        <thead><th class="tcol-1">Command line parameter</th><th class="tcol-2">Description</th></thead>
                                        <tr>
                                            <td class="tcol-1">grep</td><td class="tcol-2">A Unix string and pattern searching command</td>
                                        </tr>
                                        <tr>
                                            <td class="tcol-1">A-*</td><td class="tcol-2">The string or pattern you want to search for. In this case, grep
                                                will print any lines that contain the string "A-" followed by any other characters using the <code class="inline">*</code>
                                                wildcard.</td>
                                        </tr>
                                        <tr>
                                            <td class="tcol-1">sample-ids.txt</td><td class="tcol-2">The path to the file you want to search</td>
                                        </tr>
                                    </table>
                                </div>                                   

                                <p>
                                    Regular expressions can get much more complex to search for more complex patterns, but for now, let's focus on the basics of
                                    <code class="inline">grep</code> and how it can help us answer how many deletions are in our <code class="inline">bed</code> file.
                                </p>

                                <p>
                                    As mentioned above, will use a combination of <code class="inline">grep</code>, piping with <code class="inline">|</code>, and
                                    our line counting command, <code class="inline">wc</code>.  Let's first just run the pattern matching command to print out
                                    lines in our input file that represent deletions:
                                </p>

                                <center><pre class="cmd"><code>grep "&lt;DEL&gt;" data/macaque-svs/macaque-svs-filtered.bed</code></pre></center>

                                <div class="table-cont">
                                    <table class="cmd-table">
                                        <thead><th class="tcol-1">Command line parameter</th><th class="tcol-2">Description</th></thead>
                                        <tr>
                                            <td class="tcol-1">grep</td><td class="tcol-2">A Linux string search and pattern matching command that takes
                                                as input a file or stream from a pipe and searches for a given string.</td>
                                        </tr>
                                        <tr>
                                            <td class="tcol-1">"&lt;DEL&gt;"</td><td class="tcol-2">The pattern or specific string we want to search for</td>
                                        </tr>
                                        <tr>
                                            <td class="tcol-1">data/macaque-svs/macaque-svs-filtered.bed</td><td class="tcol-2">The path to the file you want to search</td>
                                        </tr>
                                    </table>
                                </div>

                                <p>
                                    This should print out a whole lot of lines from our input file to the screen, as is the default behavior for most Unix commands.
                                    On my screen, the end of this output looks like this:
                                </p>

                                <pre class="text"><code>chrX    135682628       135718741       chrX:135682628:&lt;DEL&gt;:36113:4892.62
chrX    137821409       137821980       chrX:137821409:&lt;DEL&gt;:571:17208.79
chrX    146387029       146422365       chrX:146387029:&lt;DEL&gt;:35336:4990.42
chrY    4875713 4904730 chrY:4875713:&lt;DEL&gt;:29017:9217.23
chrY    4902981 4904657 chrY:4902981:&lt;DEL&gt;:1676:1876.99
chrY    6907076 6907624 chrY:6907076:&lt;DEL&gt;:548:578.79
chrY    7143528 7144240 chrY:7143528:&lt;DEL&gt;:712:915.06
chrY    7424851 7429392 chrY:7424851:&lt;DEL&gt;:4541:1978.63
chrY    10903282        10911159        chrY:10903282:&lt;DEL&gt;:7877:2856.38</code></pre> 

                                <p>
                                    This is similar to what we saw when we just looked at the raw file with <code class="inline">less</code>, but if you scrolled
                                    through this you'll notice that all the lines printed are deletions, with the &lt;DEL&gt; string. This is because <code class="inline">grep</code>
                                    took out search string and only returned lines that had that string in it
                                </p>

                                <p>
                                    Now then, how does this help us know how MANY deletions there are. Well, we have two options:
                                    <ol>
                                        <li>   
                                            We could save the output from grep to a file with a redirect (<code class="inline">&gt;</code>) and then use 
                                            <code class="inline">wc -l</code> on that file.
                                        </li>
                                        <li>
                                            We could directly pipe (<code class="inline">|</code>) the output from <code class="inline">grep</code>
                                            to <code class="inline">wc -l</code>.
                                        </li>
                                </p>

                                <p>
                                    Let's try option number two, with piping:
                                </p>

                                <center><pre class="cmd"><code>grep "&lt;DEL&gt;" data/macaque-svs/macaque-svs-filtered.bed | wc -l</code></pre></center>

                                <div class="table-cont">
                                    <table class="cmd-table">
                                        <thead><th class="tcol-1">Command line parameter</th><th class="tcol-2">Description</th></thead>
                                        <tr>
                                            <td class="tcol-1">grep</td><td class="tcol-2">A Linux string search and pattern matching command that takes
                                                as input a file or stream from a pipe and searches for a given string.</td>
                                        </tr>
                                        <tr>
                                            <td class="tcol-1">"&lt;DEL&gt;"</td><td class="tcol-2">The pattern or specific string we want to search for</td>
                                        </tr>
                                        <tr>
                                            <td class="tcol-1">data/macaque-svs/macaque-svs-filtered.bed</td><td class="tcol-2">The path to the file you want to search</td>
                                        </tr>
                                        <tr>
                                            <td class="tcol-1">|</td><td class="tcol-2">The pipe character means the output from the command specified before it
                                                will be used as the input tot he command specified after it</td>
                                        </tr>
                                    </table>
                                </div>                            

                                <p>
                                    When I do this, I see
                                </p>

                                <pre class="text"><code>3214</code></pre>

                                <p>
                                    This means that out of our total 3,646 structural variants, 3,214, or 88%, are deletions.
                                </p>                            

                        </div>
                        <div class="col-2-24" id="inner-margin"></div>
                    </div>
                </div>
            </div>

            <a class="internal-link" name="awk"></a>
            <div class="row" id="section-header-cont">
                <div class="col-24-24" id="section-header-row">
                    <div id="section-header">Introduction to awk</div>
                </div>
            </div>

            <div class="row" id="section-cont">
                <div class="col-24-24" id="section-col">
                    <div class="row" id="section-row">
                        <div class="col-2-24" id="inner-margin"></div>
                        <div class="col-20-24" id="section-content">

                            <h3>TASK 3: What is the length of each variant?</h3>

                                <p>
                                    To answer this question from the command line, we'll first introduce a new command: <code class="inline">awk</code>
                                </p>

                                <p>
                                    <a href="https://www.gnu.org/software/gawk/manual/gawk.html#Getting-Started" target="_blank">awk</a> is slightly different from the other
                                    commands we've learned about in that it is a fully defined scripting language meant to be used in conjunction with other Unix commands.
                                    Given that, it has a much more elaborate <em>syntax</em> than the rest of the commands: it doesn't just have input parameters, but also 
                                    accepts user defined rules and functions.
                                </p>

                                <p>
                                    This makes <code class="inline">awk</code> extremely powerful, and is our first step into scripting, since we will use the <code class="inline">awk</code>
                                    syntax to define our own commands.
                                </p>

                                <p>
                                    <code class="inline">awk</code> can be run in two ways:

                                    <ol>
                                        <li>The traditional scripting/programming way, where you write your rules in a file.</li>
                                        <li>The Unix way, where you write your rules directly in the command line. These are generally referred to as <b>one-liners</b>.</li>
                                    </ol>

                                    For one-liners, the general command typed would be:
                                </p>

                                <center><pre class="cmd-ne"><code>awk '&lt;user-defined rules&gt;' &lt;input file&gt;</code></pre></center>

                                <div class="table-cont">
                                    <table class="cmd-table">
                                        <thead><th class="tcol-1">Command line parameter</th><th class="tcol-2">Description</th></thead>
                                        <tr>
                                            <td class="tcol-1">awk</td><td class="tcol-2">A Linux text processing language</td>
                                        </tr>
                                        <tr>
                                            <td class="tcol-1">'&lt;user-defined rules&gt;'</td><td class="tcol-2">The user-coded program to run</td>
                                        </tr>
                                        <tr>
                                            <td class="tcol-1">&lt;input file&gt;</td><td class="tcol-2">The path to the file on which to run the program</td>
                                        </tr>
                                    </table>
                                </div>     

                                <p>
                                    Like many other Unix commands, <code class="inline">awk</code> processes the input text in the file line-by-line, and generally for each line (or <b>record</b>)
                                    it processes one column (or <b>field</b>) at a time. By default, <code class="inline">awk</code> assumes that fields are separated
                                    by tab characers, but this can be changed with an input option.
                                </p>

                                <p>
                                    <b>Fields</b> (columns) in the file are represented by variables specified by a dollar sign (<code class="inline">$</code>) and then the
                                    number of the column. For instance, the first column in a file is represented by <code class="inline">$1</code>, the fourth column by
                                    <code class="inline">$4</code>, and so on.
                                </p>

                                <p>
                                    As a brief example, let's say we wanted to extract only the column in our input bed file that represents the end of each region. We know
                                    from our <code class="inline">.bed</code> format specifications that this is the third column. So we would type:
                                </p>

                                <center><pre class="cmd"><code>awk '{{print $3}}' data/macaque-svs/macaque-svs-filtered.bed</code></pre></center>

                                <div class="table-cont">
                                    <table class="cmd-table">
                                        <thead><th class="tcol-1">Command line parameter</th><th class="tcol-2">Description</th></thead>
                                        <tr>
                                            <td class="tcol-1">awk</td><td class="tcol-2">A Linux text processing language</td>
                                        </tr>
                                        <tr>
                                            <td class="tcol-1">'{{print $3}}'</td><td class="tcol-2">The user-coded program to run. In this case, we only want to print
                                                the third column of the file to the screen.</td>
                                        </tr>
                                        <tr>
                                            <td class="tcol-1">data/macaque-svs/macaque-svs-filtered.bed</td><td class="tcol-2">The path to the file on which to run 
                                                the program</td>
                                        </tr>
                                    </table>
                                </div>                                     


                                <p>
                                    The last few lines of this output should be:
                                </p>

                                <pre class="text"><code>135715923
135718741
137821980
145552312
146422365
4904730
4904657
6907624
7144240
7429392
10911159</code></pre> 

                                <p>
                                    We can do this with any other column we want, and we can <b>perform operations</b> on the values in those columns as well, which
                                    brings us to how we find out the length of each region in the <code class="inline">.bed</code> file.
                                </p>

                                <p>
                                    Since <code class="inline">awk</code> is a fully realized scripting language, it supports basic mathematical operations. Since we have
                                    the start and end coordinates of each region, we can just tell <code class="inline">awk</code> to subtract the end from the start,
                                    giving us the length of each region:
                                </p>

                                <center><pre class="cmd"><code>awk '{{print $3 - $2}}' data/macaque-svs/macaque-svs-filtered.bed</code></pre></center>

                                <div class="table-cont">
                                    <table class="cmd-table">
                                        <thead><th class="tcol-1">Command line parameter</th><th class="tcol-2">Description</th></thead>
                                        <tr>
                                            <td class="tcol-1">awk</td><td class="tcol-2">A Linux text processing language</td>
                                        </tr>
                                        <tr>
                                            <td class="tcol-1">'{{print $3 - $2}}'</td><td class="tcol-2">The user-coded program to run. In this case, we are telling awk
                                                to take the value in the third column and subtract the value in the second column of each row in the file.</td>
                                        </tr>
                                        <tr>
                                            <td class="tcol-1">data/macaque-svs/macaque-svs-filtered.bed</td><td class="tcol-2">The path to the file on which to run 
                                                the program</td>
                                        </tr>
                                    </table>
                                </div>   

                                <p>
                                    The last few lines of this output should be:
                                </p>

                                <pre class="text"><code>36311
36113
571
1156
35336
29017
1676
548
712
4541
7877</code></pre>

                            <div id="task-sep"></div>

                            <h3>TASK 4: What is the average length of all variants?</h3>

                                <p>
                                    <code class="inline">awk</code> can let us do more complex operations as well (it is a full scripting language!). To calculate
                                    an average across lines in a file, we also need to keep track of a sum over all lines in the file and make a calculation at the end:
                                </p>

                                <center><pre class="cmd"><code>awk '{{sum += $3 - $2}} END {{if (NR > 0) print sum / NR }}' data/macaque-svs/macaque-svs-filtered.bed</code></pre></center>

                                <div class="table-cont">
                                    <table class="cmd-table">
                                        <thead><th class="tcol-1">Command line parameter</th><th class="tcol-2">Description</th></thead>
                                        <tr>
                                            <td class="tcol-1">awk</td><td class="tcol-2">A Linux text processing language</td>
                                        </tr>
                                        <tr>
                                            <td class="tcol-1">'{{sum += $3 - $2}} END {{if (NR > 0) print sum / NR }}'</td><td class="tcol-2">The user-coded program to run. 
                                                In this case, we are telling awk to keep track of the sum of all lengths and average them at the end.</td>
                                        </tr>
                                        <tr>
                                            <td class="tcol-1">data/macaque-svs/macaque-svs-filtered.bed</td><td class="tcol-2">The path to the file on which to run 
                                                the program</td>
                                        </tr>
                                    </table>
                                </div>                                  

                                <p>
                                    For me this prints:
                                </p>

                                <pre class="text"><code>3615.02</code></pre>

                                <p>
                                    Meaning our structural variants are, on average, 3,615 bases long.
                                </p>

                                <p>
                                    But this awk program we've written is slightly more complex. Let's break it down even more:
                                </p>

                                <div class="table-cont">
                                    <table class="norm-table">
                                        <thead><th class="tcol-1">Code</th><th class="tcol-2">Purpose</th></thead>
                                        <tr>
                                            <td class="tcol-1"><code class="inline">awk</code></td>
                                            <td class="tcol-2">The main call to the <code class="inline">awk</code> program. This tells the terminal to use 
                                                <code class="inline">awk</code> to process the rest of the command.
                                            </td>
                                        </tr>
                                        <tr>
                                            <td class="tcol-1"><code class="inline">'</code></td>
                                            <td class="tcol-2"><code class="inline">awk</code> programs defined as one-liners in the command line must be surrounded
                                                by quotes to be read as a single chunk of code.
                                            </td>
                                        </tr>
                                        <tr>
                                            <td class="tcol-1"><code class="inline">{{sum += $3 - $2}}</code></td>
                                            <td class="tcol-2">This tells <code class="inline">awk</code> to subtract the value in the second column of the current line
                                                from the value in the third column and to add that difference to a variable called <code class="inline">sum</code>.
                                                <code class="inline">sum</code> is then a cumuluative sum of the lengths of all SVs over all lines in the file.
                                            </td>
                                        </tr>
                                        <tr>
                                            <td class="tcol-1"><code class="inline">END</code></td>
                                            <td class="tcol-2">This indicates that this is the end of the code to be executed on a per-line basis. All following
                                                code will only be executed after all lines in the file have been processed.
                                            </td>
                                        </tr>
                                        <tr>
                                            <td class="tcol-1"><code class="inline">{{if (NR > 0)</code></td>
                                            <td class="tcol-2">A conditional. <code class="inline">NR</code> is an internal <code class="inline">awk</code>
                                                variable that stores the number of rows/lines in the input file. So this conditional states that the code
                                                after should only be executed <code class="inline">if</code> there are more than 0 rows in the input file.
                                                This prevents any divide by zero errors in the next expression.
                                            </td>
                                        </tr>
                                        <tr>
                                            <td class="tcol-1"><code class="inline">print sum / NR}}</code></td>
                                            <td class="tcol-2">This tells <code class="inline">awk</code> to take the cumulative sum of all SV lengths, saved in 
                                                the variable <code class="inline">sum</code> and divide it by the total number of rows in the input file, 
                                                <code class="inline">NR</code> and <code class="inline">print</code> the resulting value to the screen. Since 
                                                <code class="inline">NR</code> represents the number of SVs, this gives us the average length of all SVs.
                                            </td>
                                        </tr>
                                        <tr>
                                            <td class="tcol-1"><code class="inline">'</code></td>
                                            <td class="tcol-2"><code class="inline">awk</code> programs defined as one-liners in the command line must be surrounded
                                                by quotes to be read as a single chunk of code. This is the second quote, meaning the <code class="inline">awk</code>
                                                program is complete.
                                            </td>
                                        </tr>  
                                        <tr>
                                            <td class="tcol-1"><code class="inline">data/macaque-svs/macaque-svs-filtered.bed</code></td>
                                            <td class="tcol-2">This is the name of the input file on which to run the <code class="inline">awk</code> program 
                                                we've written between the single quotes.
                                            </td>
                                        </tr>                                      
                                    </table>
                                </div>

                        </div>
                        <div class="col-2-24" id="inner-margin"></div>
                    </div>
                </div>
            </div>


            <a class="internal-link" name="grep-awk"></a>
            <div class="row" id="section-header-cont">
                <div class="col-24-24" id="section-header-row">
                    <div id="section-header">Combining grep and awk with piping</div>
                </div>
            </div>

            <div class="row" id="section-cont">
                <div class="col-24-24" id="section-col">
                    <div class="row" id="section-row">
                        <div class="col-2-24" id="inner-margin"></div>
                        <div class="col-20-24" id="section-content">

                            <h3>TASK 5: What is the average length of deletions only?</h3>

                                <p>
                                    Much like we piped the output from <code class="inline">grep</code> into <code class="inline">wc</code> to count the
                                    total number of deletions, we can pipe output from <code class="inline">grep</code> to <code class="inline">awk</code> to
                                    perform more complex operations on a subset of input data:
                                </p>

                                <center><pre class="cmd"><code>grep "&lt;DEL&gt;" data/macaque-svs/macaque-svs-filtered.bed | awk '{{sum += $3 - $2}} END {{if (NR > 0) print sum / NR }}'</code></pre></center>

                                <div class="table-cont">
                                    <table class="cmd-table">
                                        <thead><th class="tcol-1">Command line parameter</th><th class="tcol-2">Description</th></thead>
                                        <tr>
                                            <td class="tcol-1">grep</td><td class="tcol-2">A Linux string search and pattern matching command that takes
                                                as input a file or stream from a pipe and searches for a given string.</td>
                                        </tr>
                                        <tr>
                                            <td class="tcol-1">"&lt;DEL&gt;"</td><td class="tcol-2">The pattern or specific string we want to search for</td>
                                        </tr>
                                        <tr>
                                            <td class="tcol-1">data/macaque-svs/macaque-svs-filtered.bed</td><td class="tcol-2">The path to the file you want to search</td>
                                        </tr>
                                        <tr>
                                            <td class="tcol-1">|</td><td class="tcol-2">The pipe character means the output from the command specified before it
                                                will be used as the input to the command specified after it</td>
                                        </tr>
                                        <tr>
                                            <td class="tcol-1">awk</td><td class="tcol-2">A Linux text processing language</td>
                                        </tr>
                                        <tr>
                                            <td class="tcol-1">'{{sum += $3 - $2}} END {{if (NR > 0) print sum / NR }}'</td><td class="tcol-2">The user-coded program to run. 
                                                In this case, we are telling awk to keep track of the sum of all lengths and average them at the end.</td>
                                        </tr>
                                        <tr>
                                            <td class="tcol-1">data/macaque-svs/macaque-svs-filtered.bed</td><td class="tcol-2">The path to the file on which to run 
                                                the program</td>
                                        </tr>
                                    </table>
                                </div>                                     

                                <p>
                                    So now <code class="inline">awk</code>, rather than having an input file specified, takes input from the output of 
                                    <code class="inline">grep</code>. For me, this prints the average length of deletions as:
                                </p>

                                <pre class="text"><code>3161.33</code></pre>

                                <p>
                                    This is pretty close to the overall average of 3,615bp, but a little shorter. What about the average length of duplications?
                                </p>

                                <center><pre class="cmd"><code>grep "&lt;DUP&gt;" data/macaque-svs/macaque-svs-filtered.bed | awk '{{sum += $3 - $2}} END {{if (NR > 0) print sum / NR }}'</code></pre></center>

                                <div class="table-cont">
                                    <table class="cmd-table">
                                        <thead><th class="tcol-1">Command line parameter</th><th class="tcol-2">Description</th></thead>
                                        <tr>
                                            <td class="tcol-1">grep</td><td class="tcol-2">A Linux string search and pattern matching command that takes
                                                as input a file or stream from a pipe and searches for a given string.</td>
                                        </tr>
                                        <tr>
                                            <td class="tcol-1">"&lt;DUP&gt;"</td><td class="tcol-2">The pattern or specific string we want to search for</td>
                                        </tr>
                                        <tr>
                                            <td class="tcol-1">data/macaque-svs/macaque-svs-filtered.bed</td><td class="tcol-2">The path to the file you want to search</td>
                                        </tr>
                                        <tr>
                                            <td class="tcol-1">|</td><td class="tcol-2">The pipe character means the output from the command specified before it
                                                will be used as the input to the command specified after it</td>
                                        </tr>
                                        <tr>
                                            <td class="tcol-1">awk</td><td class="tcol-2">A Linux text processing language</td>
                                        </tr>
                                        <tr>
                                            <td class="tcol-1">'{{sum += $3 - $2}} END {{if (NR > 0) print sum / NR }}'</td><td class="tcol-2">The user-coded program to run. 
                                                In this case, we are telling awk to keep track of the sum of all lengths and average them at the end.</td>
                                        </tr>
                                        <tr>
                                            <td class="tcol-1">data/macaque-svs/macaque-svs-filtered.bed</td><td class="tcol-2">The path to the file on which to run 
                                                the program</td>
                                        </tr>
                                    </table>
                                </div>     

                                <pre class="text"><code>6990.42</code></pre>

                                <p>
                                    Wow! So deletions make up almost 90% of all SVs, but duplications are, on average, more than twice as long.
                                </p>

                        </div>
                        <div class="col-2-24" id="inner-margin"></div>
                    </div>
                </div>
            </div>

            <a class="internal-link" name="gtf"></a>
            <div class="row" id="section-header-cont">
                <div class="col-24-24" id="section-header-row">
                    <div id="section-header">Annotation files</div>
                </div>
            </div>

            <div class="row" id="section-cont">
                <div class="col-24-24" id="section-col">
                    <div class="row" id="section-row">
                        <div class="col-2-24" id="inner-margin"></div>
                        <div class="col-20-24" id="section-content">

                            <h3>TASK 6: How many SVs overlap with genes?</h3>

                                <p>
                                    For many types of genomic variation the question of how they affect annotated functional regions, like genes, will inevitably be asked.
                                    In order to answer this question, we'll need to familiarize ourselves with another file format, that of <b>GTF</b> and <b>GFF</b> files.
                                </p>

                                <p>
                                    <code class="inline">GTF</code> stands for General Transfer Format and <code class="inline">GFF</code> stands for General Feature Format.
                                </p>

                                <p>
                                    <code class="inline">GTF</code> and <code class="inline">GFF</code> files are both tab delimited formats that indicate regions in a 
                                    genome, much like a <code class="inline">bed</code> file. However, these files are limited to annotated functional regions and contain
                                    extra information about those regions, such as functional class (e.g., gene, transcript, UTR), and orientation.
                                </p>

                                <p>
                                    Read more about <code class="inline">GTF</code> and <code class="inline">GFF</code> file formats here:

                                    <ul>                                        
                                        <li><a href="https://genome.ucsc.edu/FAQ/FAQformat.html#format3" target="_blank">UCSC description</a></li>
                                        <li><a href="http://www.ensembl.org/info/website/upload/gff.html?redirect=no" target="_blank">Ensembl description</a></li>
                                        <li><a href="https://www.ncbi.nlm.nih.gov/datasets/docs/reference-docs/file-formats/about-ncbi-gff3/" target="_blank">NCBI description</a></li>
                                    </ul>
                                </p>
                                    
                                <p>
                                    We've pre-downloaded a <code class="inline">GTF</code> file for the rhesus macaque from Ensembl. Let's take a look at it:
                                </p>

                                <center><pre class="cmd"><code>zless -S data/macaque-svs/annotation-files/Macaca_mulatta.Mmul_8.0.1.97.chromes.gtf.gz</code></pre></center>

                                <div class="table-cont">
                                    <table class="cmd-table">
                                        <thead><th class="tcol-1">Command line parameter</th><th class="tcol-2">Description</th></thead>
                                        <tr>
                                            <td class="tcol-1">zless</td><td class="tcol-2">A Linux <b>compressed</b> text file viewer (use space to scroll down, 
                                                b to scroll up, and q to exit)</td>
                                        </tr>
                                        <tr>
                                            <td class="tcol-1">-S</td><td class="tcol-2">Turn off line-wrapping within zless (use the left and right arrow keys to scroll left and right).</td>
                                        </tr>
                                        <tr>
                                            <td class="tcol-1">data/macaque-svs/annotation-files/Macaca_mulatta.Mmul_8.0.1.97.chromes.gtf.gz</td><td class="tcol-2">The path to the file you want to view</td>
                                        </tr>
                                    </table>
                                </div>

                                <p>You should see something like this:</p>

                                <pre class="text"><code>1	ensembl	gene	25432	42232	.	+	.	gene_id "ENSMMUG00000005947"; gene_version "3"; gene_name "SAMD11"; gene_source "ensembl"; gene_biotype "protein_coding";
1	ensembl	transcript	25432	42232	.	+	.	gene_id "ENSMMUG00000005947"; gene_version "3"; transcript_id "ENSMMUT00000063154"; transcript_version "1"; gene_name "SAMD11"; gene_source "ensembl"; gene_biotype "protein_coding"; transcript_name "SAMD11-201"; transcript_source "ensembl"; transcript_biotype "protein_coding";
1	ensembl	exon	25432	25503	.	+	.	gene_id "ENSMMUG00000005947"; gene_version "3"; transcript_id "ENSMMUT00000063154"; transcript_version "1"; exon_number "1"; gene_name "SAMD11"; gene_source "ensembl"; gene_biotype "protein_coding"; transcript_name "SAMD11-201"; transcript_source "ensembl"; transcript_biotype "protein_coding"; exon_id "ENSMMUE00000311984"; exon_version "2";
1	ensembl	CDS	25432	25503	.	+	0	gene_id "ENSMMUG00000005947"; gene_version "3"; transcript_id "ENSMMUT00000063154"; transcript_version "1"; exon_number "1"; gene_name "SAMD11"; gene_source "ensembl"; gene_biotype "protein_coding"; transcript_name "SAMD11-201"; transcript_source "ensembl"; transcript_biotype "protein_coding"; protein_id "ENSMMUP00000049946"; protein_version "1";
1	ensembl	start_codon	25432	25434	.	+	0	gene_id "ENSMMUG00000005947"; gene_version "3"; transcript_id "ENSMMUT00000063154"; transcript_version "1"; exon_number "1"; gene_name "SAMD11"; gene_source "ensembl"; gene_biotype "protein_coding"; transcript_name "SAMD11-201"; transcript_source "ensembl"; transcript_biotype "protein_coding";
1	ensembl	exon	29573	29754	.	+	.	gene_id "ENSMMUG00000005947"; gene_version "3"; transcript_id "ENSMMUT00000063154"; transcript_version "1"; exon_number "2"; gene_name "SAMD11"; gene_source "ensembl"; gene_biotype "protein_coding"; transcript_name "SAMD11-201"; transcript_source "ensembl"; transcript_biotype "protein_coding"; exon_id "ENSMMUE00000311983"; exon_version "1";
1	ensembl	CDS	29573	29754	.	+	0	gene_id "ENSMMUG00000005947"; gene_version "3"; transcript_id "ENSMMUT00000063154"; transcript_version "1"; exon_number "2"; gene_name "SAMD11"; gene_source "ensembl"; gene_biotype "protein_coding"; transcript_name "SAMD11-201"; transcript_source "ensembl"; transcript_biotype "protein_coding"; protein_id "ENSMMUP00000049946"; protein_version "1";</code></pre> 

                                <p>
                                    So this should have all the columns required of a <code class="inline">GTF</code> file as outlined in the links above. Notably, the first,
                                    third, and fourth columns define the location within the genome, being the chromosome, start coordinate, and end coordinate respectively.
                                    Columns 2 defines the regions annotation source while column 3 defines the type of region. You can notice here the nesting structure
                                    associated with genes and their sub-elements.
                                </p>

                                <p>
                                    Column 6 shows the regions orientation. This is an often overlooked but important thing to consider when extracting sequences in a genome:
                                    if the region indicated is on the opposite strand (indicated with a - sign), then you must take the reverse complement of that sequence,
                                    and for genes the sub-elements (exons, CDS, etc.) must be taken in reverse order. Today, since we're not actually extracting sequence and 
                                    only looking at coordinates, we shouldn't need to worry about this.
                                </p>

                                <p>
                                    The last column in the <code class="inline">GTF</code> files serves as a sort of catch-all. This column is named 'attributes', but programs
                                    and users are free to put any information in this column that they like, separated by semi-colons. Unfortunately, this leads to variations
                                    between <code class="inline">GTF</code> files, which can cause trouble for down-stream users. Again, today we don't need to worry about this.
                                </p>

                        </div>
                        <div class="col-2-24" id="inner-margin"></div>
                    </div>
                </div>
            </div>

            <a class="internal-link" name="gtf-to-bed"></a>
            <div class="row" id="section-header-cont">
                <div class="col-24-24" id="section-header-row">
                    <div id="section-header">Converting GTF to BED</div>
                </div>
            </div>

            <div class="row" id="section-cont">
                <div class="col-24-24" id="section-col">
                    <div class="row" id="section-row">
                        <div class="col-2-24" id="inner-margin"></div>
                        <div class="col-20-24" id="section-content">

                                <p>
                                    In order to address our question, <b>"How many SVs overalp with genes?"</b>, we'll be using a program called 
                                    <a href="https://bedtools.readthedocs.io/en/latest/index.html" target="_blank">bedtools</a>. <code class="inline">bedtools</code>
                                    is a staple bioinformatic program used for working with genomic regions in <code class="inline">bed</code> format. It is actually
                                    a suite of tools designed with the Unix philosophy: each sub-program does one thing really well, and the sub-programs can work 
                                    together by taking input from each other.
                                </p>

                                <p>
                                    Since <code class="inline">bedtools</code> works with <code class="inline">bed</code> files, we'll need to convert our 
                                    <code class="inline">GTF</code> regions of interest to <code class="inline">bed</code> format.
                                </p>

                                <p>
                                    First, let's use <code class="inline">awk</code> to extract only lines that are defined as "gene" in the third column:
                                </p>

                                <center><pre class="cmd"><code>zcat data/macaque-svs/annotation-files/Macaca_mulatta.Mmul_8.0.1.97.chromes.gtf.gz | awk '{{if($3 == "gene"){{print}}}}'</code></pre></center>

                                <div class="table-cont">
                                    <table class="cmd-table">
                                        <thead><th class="tcol-1">Command line parameter</th><th class="tcol-2">Description</th></thead>
                                        <tr>
                                            <td class="tcol-1">zcat</td><td class="tcol-2">This prints lines from a compressed text file to the screen.
                                                Since this file is compressed (.gz) we first need to decompress the text for awk to read.</td>
                                        </tr>
                                        <tr>
                                            <td class="tcol-1">data/macaque-svs/annotation-files/Macaca_mulatta.Mmul_8.0.1.97.chromes.gtf.gz</td><td class="tcol-2">The path to the input
                                                file to read</td>
                                        </tr>                                        
                                        <tr>
                                            <td class="tcol-1">|</td><td class="tcol-2">The pipe character means the output from the command specified before it
                                                will be used as the input to the command specified after it</td>
                                        </tr>
                                        <tr>
                                            <td class="tcol-1">awk</td><td class="tcol-2">A Linux text processing language</td>
                                        </tr>
                                        <tr>
                                            <td class="tcol-1">'{{if($3 == "gene"){{print}}}}'</td><td class="tcol-2">The user-coded program to run. 
                                                In this case, we want to print the line to the screen if the third column matches the string "gene".</td>
                                        </tr>
                                    </table>
                                </div>

                                <p>
                                    This should print all the lines that are genes to the screen. But now we want to convert these lines into <code class="inline">bed</code>
                                    format. This should be easy since all the information we need is in the first, fourth, and fifth columns:
                                </p>

                                <center><pre class="cmd"><code>zcat data/macaque-svs/annotation-files/Macaca_mulatta.Mmul_8.0.1.97.chromes.gtf.gz | awk '{{if($3 == "gene"){{print}}}}' | awk 'BEGIN{{OFS="\\t"}}{{print "chr"$1, $4, $5}}'</code></pre></center>

                                <div class="table-cont">
                                    <table class="cmd-table">
                                        <thead><th class="tcol-1">Command line parameter</th><th class="tcol-2">Description</th></thead>
                                        <tr>
                                            <td class="tcol-1">zcat</td><td class="tcol-2">This prints lines from a compressed text file to the screen.
                                                Since this file is compressed (.gz) we first need to decompress the text for awk to read.</td>
                                        </tr>
                                        <tr>
                                            <td class="tcol-1">data/macaque-svs/annotation-files/Macaca_mulatta.Mmul_8.0.1.97.chromes.gtf.gz</td><td class="tcol-2">The path to the input
                                                file to read</td>
                                        </tr>                                        
                                        <tr>
                                            <td class="tcol-1">|</td><td class="tcol-2">The pipe character means the output from the command specified before it
                                                will be used as the input to the command specified after it</td>
                                        </tr>
                                        <tr>
                                            <td class="tcol-1">awk</td><td class="tcol-2">A Linux text processing language</td>
                                        </tr>
                                        <tr>
                                            <td class="tcol-1">'{{if($3 == "gene"){{print}}}}'</td><td class="tcol-2">The user-coded program to run. 
                                                In this case, we want to print the line to the screen if the third column matches the string "gene".</td>
                                        </tr>
                                        <tr>
                                            <td class="tcol-1">|</td><td class="tcol-2">The pipe character means the output from the command specified before it
                                                will be used as the input to the command specified after it</td>
                                        </tr>
                                        <tr>
                                            <td class="tcol-1">awk</td><td class="tcol-2">A Linux text processing language</td>
                                        </tr>
                                        <tr>
                                            <td class="tcol-1">'BEGIN{{OFS="\\t"}}{{print "chr"$1, $4, $5}}'</td><td class="tcol-2">The user-coded program to run. 
                                                In this case, we want to print the first, fourth, and fifth columns of the input file.</td>
                                        </tr>    
                                    </table>
                                </div>

                                <p>
                                    This should print the specified columns of all lines that have "gene" in the third column to the screen. One new thing here is that
                                    we've re-set the internal <code class="inline">awk</code> variable <code class="inline">OFS</code> (output field separator) to a tab
                                    character. This means output columns will print with this character between them. Using a tab character matches <code class="inline">bed</code>
                                    format specifications. Note that also columns must be listed with commas in the <code class="inline">awk</code> program.
                                </p>

                                <p>
                                    You'll also notice that we've added a string to the first column: "chr". This is because the <code class="inline">bed</code> file with our SV
                                    calls names chromosomes as chr1, chr2, etc., while this <code class="inline">GTF</code> file simply names them 1, 2, etc. This mis-match would
                                    prevent <code class="inline">bedtools</code> from finding overlaps so we need to add the "chr" string here.
                                </p>

                                <p>
                                    Finally, since we want to use this text later, we'll need to save it by <b>redirecting it</b> to a file with <code class="inline">&gt;</code>:
                                </p>

                                <center><pre class="cmd"><code>zcat data/macaque-svs/annotation-files/Macaca_mulatta.Mmul_8.0.1.97.chromes.gtf.gz | awk '{{if($3 == "gene"){{print}}}}' | awk 'BEGIN{{OFS="\\t"}}{{print "chr"$1, $4, $5}}' > data/macaque-svs/annotation-files/macaque-genes.bed</code></pre></center>

                                <div class="table-cont">
                                    <table class="cmd-table">
                                        <thead><th class="tcol-1">Command line parameter</th><th class="tcol-2">Description</th></thead>
                                        <tr>
                                            <td class="tcol-1">zcat</td><td class="tcol-2">This prints lines from a compressed text file to the screen.
                                                Since this file is compressed (.gz) we first need to decompress the text for awk to read.</td>
                                        </tr>
                                        <tr>
                                            <td class="tcol-1">data/macaque-svs/annotation-files/Macaca_mulatta.Mmul_8.0.1.97.chromes.gtf.gz</td><td class="tcol-2">The path to the input
                                                file to read</td>
                                        </tr>
                                        <tr>
                                            <td class="tcol-1">|</td><td class="tcol-2">The pipe character means the output from the command specified before it
                                                will be used as the input to the command specified after it</td>
                                        </tr>
                                        <tr>
                                            <td class="tcol-1">awk</td><td class="tcol-2">A Linux text processing language</td>
                                        </tr>
                                        <tr>
                                            <td class="tcol-1">'{{if($3 == "gene"){{print}}}}'</td><td class="tcol-2">The user-coded program to run. 
                                                In this case, we want to print the line to the screen if the third column matches the string "gene".</td>
                                        </tr>
                                        <tr>
                                            <td class="tcol-1">|</td><td class="tcol-2">The pipe character means the output from the command specified before it
                                                will be used as the input to the command specified after it</td>
                                        </tr>
                                        <tr>
                                            <td class="tcol-1">awk</td><td class="tcol-2">A Linux text processing language</td>
                                        </tr>
                                        <tr>
                                            <td class="tcol-1">'BEGIN{{OFS="\\t"}}{{print "chr"$1, $4, $5}}'</td><td class="tcol-2">The user-coded program to run. 
                                                In this case, we want to print the first, fourth, and fifth columns of the input file.</td>
                                        </tr>
                                        <tr>
                                            <td class="tcol-1">></td><td class="tcol-2">The redirect character means the output from the command specified before it
                                                will be saved to the file specified after it</td>
                                        </tr> 
                                        <tr>
                                            <td class="tcol-1">data/macaque-svs/annotation-files/macaque-genes.bed</td><td class="tcol-2">The path to the desired output file. This will be created if
                                                it doesn't exist and WILL OVERWRITE files that do exist</td>
                                        </tr>
                                    </table>
                                </div>

                                <p>
                                    Now, instead of printing the output of our command to the screen, it will be saved in the file
                                    <code class="inline">macaque-genes.bed</code>, and we can use it as we wish later.
                                </p>

                        </div>
                        <div class="col-2-24" id="inner-margin"></div>
                    </div>
                </div>
            </div>

            <a class="internal-link" name="bedtools"></a>
            <div class="row" id="section-header-cont">
                <div class="col-24-24" id="section-header-row">
                    <div id="section-header">Using bedtools to get overlapping regions</div>
                </div>
            </div>

            <div class="row" id="section-cont">
                <div class="col-24-24" id="section-col">
                    <div class="row" id="section-row">
                        <div class="col-2-24" id="inner-margin"></div>
                        <div class="col-20-24" id="section-content">

                                <p>
                                    As we mentioned above, <a href="https://bedtools.readthedocs.io/en/latest/index.html" target="_blank">bedtools</a>, is an extremely
                                    versatile program for working with genomic regions in <code class="inline">bed</code> format. <code class="inline">bedtools</code>
                                    is a suite of programs that are generally run as follows:
                                <p>

                                <center><pre class="cmd-ne"><code>bedtools &lt;sub-program&gt; &lt;options&gt; &lt;input file&gt;</code></pre></center>

                                <div class="table-cont">
                                    <table class="cmd-table">
                                        <thead><th class="tcol-1">Command line parameter</th><th class="tcol-2">Description</th></thead>
                                        <tr>
                                            <td class="tcol-1">bedtools</td><td class="tcol-2">A program for working with genomic regions in bed format</td>
                                        </tr>
                                        <tr>
                                            <td class="tcol-1">&lt;sub-program&gt;</td><td class="tcol-2">The desired sub-program within bedtools to run</td>
                                        </tr>
                                        <tr>
                                            <td class="tcol-1">&lt;options&gt;</td><td class="tcol-2">Sub-program specific run options</td>
                                        </tr>
                                        <tr>
                                            <td class="tcol-1">&lt;input file&gt;</td><td class="tcol-2">The path to the file you want to run on</td>
                                        </tr>
                                    </table>
                                </div>

                                <p>
                                    A lot more info can be found on the <a href="https://bedtools.readthedocs.io/en/latest/index.html" target="_blank">bedtools website</a>.
                                </p>

                                <p>
                                    Now we're going to use <a href="https://bedtools.readthedocs.io/en/latest/content/tools/intersect.html" target="_blank">bedtools intersect</a>
                                    to see how many of our structural variants overlap with genes. <code class="inline">bedtools intersect</code> takes as input 2 bed 
                                    files and prints output based on their overlaps. This output can be customized to include the number or percent of bases overlapped, 
                                    among other things.
                                </p>

                                <center><pre class="cmd"><code>bedtools intersect -u -a data/macaque-svs/macaque-svs-filtered.bed -b data/macaque-svs/annotation-files/macaque-genes.bed</code></pre></center>

                                <div class="table-cont">
                                    <table class="cmd-table">
                                        <thead><th class="tcol-1">Command line parameter</th><th class="tcol-2">Description</th></thead>
                                        <tr>
                                            <td class="tcol-1">bedtools</td><td class="tcol-2">A program for working with genomic regions in bed format</td>
                                        </tr>
                                        <tr>
                                            <td class="tcol-1">intersect</td><td class="tcol-2">A sub-program for bedtools that compares 2 bed files and reports overlaps</td>
                                        </tr>
                                        <tr>
                                            <td class="tcol-1">-u</td><td class="tcol-2">This option says to print the region in file a if it has any overlaps in file b</td>
                                        </tr>
                                        <tr>
                                            <td class="tcol-1">-a</td><td class="tcol-2">The option to specify the first bed file</td>
                                        </tr>
                                        <tr>
                                            <td class="tcol-1">data/macaque-svs/macaque-svs-filtered.bed</td><td class="tcol-2">The path to the first bed file</td>
                                        </tr>
                                        <tr>
                                            <td class="tcol-1">-b</td><td class="tcol-2">The option to specify the second bed file</td>
                                        </tr>
                                        <tr>
                                            <td class="tcol-1">data/macaque-svs/annotation-files/macaque-genes.bed</td><td class="tcol-2">The path to the second bed file</td>
                                        </tr>
                                    </table>
                                </div>                                                               

                                <p>
                                    This prints out all lines in file a that overlap with a region in file b. The end of my output looks something like this:
                                </p>

                                <pre class="text"><code>chrX    86600287        86600725        chrX:86600287:&lt;DEL&gt;:438:6027.45
chrX    86613955        86615407        chrX:86613955:&lt;DEL&gt;:1452:1737.19
chrX    91174961        91176888        chrX:91174961:&lt;DEL&gt;:1927:4205.93
chrX    92753089        92753972        chrX:92753089:&lt;DEL&gt;:883:3724.23
chrX    98845605        98847132        chrX:98845605:&lt;DEL&gt;:1527:1678.29
chrX    123944663       123946419       chrX:123944663:&lt;DEL&gt;:1756:2666.16
chrX    129328746       129330969       chrX:129328746:&lt;DEL&gt;:2223:5690.06
chrX    135679612       135715923       chrX:135679612:&lt;DEL&gt;:36311:1521.72
chrX    135682628       135718741       chrX:135682628:&lt;DEL&gt;:36113:4892.62
chrX    146387029       146422365       chrX:146387029:&lt;DEL&gt;:35336:4990.42</code></pre>                                 

                                <p>
                                    These are the SVs in our sample that overlap genes in the macaque genome! How many of these are there? Let's pipe this output 
                                    into <code class="inline">wc</code>:
                                </p>

                                <center><pre class="cmd"><code>bedtools intersect -u -a data/macaque-svs/macaque-svs-filtered.bed -b data/macaque-svs/annotation-files/macaque-genes.bed | wc -l</code></pre></center>

                                <div class="table-cont">
                                    <table class="cmd-table">
                                        <thead><th class="tcol-1">Command line parameter</th><th class="tcol-2">Description</th></thead>
                                        <tr>
                                            <td class="tcol-1">bedtools</td><td class="tcol-2">A program for working with genomic regions in bed format</td>
                                        </tr>
                                        <tr>
                                            <td class="tcol-1">intersect</td><td class="tcol-2">A sub-program for bedtools that compares 2 bed files and reports overlaps</td>
                                        </tr>
                                        <tr>
                                            <td class="tcol-1">-u</td><td class="tcol-2">This option says to print the region in file a if it has any overlaps in file b</td>
                                        </tr>
                                        <tr>
                                            <td class="tcol-1">-a</td><td class="tcol-2">The option to specify the first bed file</td>
                                        </tr>
                                        <tr>
                                            <td class="tcol-1">data/macaque-svs/macaque-svs-filtered.bed</td><td class="tcol-2">The path to the first bed file</td>
                                        </tr>
                                        <tr>
                                            <td class="tcol-1">-b</td><td class="tcol-2">The option to specify the second bed file</td>
                                        </tr>
                                        <tr>
                                            <td class="tcol-1">data/macaque-svs/annotation-files/macaque-genes.bed</td><td class="tcol-2">The path to the second bed file</td>
                                        </tr>
                                        <tr>
                                            <td class="tcol-1">|</td><td class="tcol-2">The pipe character means the output from the command specified before it
                                                will be used as the input to the command specified after it</td>
                                        </tr>
                                        <tr>
                                            <td class="tcol-1">wc</td><td class="tcol-2">The Linux word count command. Counts the number of lines, words, and
                                                characters in an input file.</td>
                                        </tr>
                                        <tr>
                                            <td class="tcol-1">-l</td><td class="tcol-2">Tells <code class="inline">wc</code> to only count number of lines</td>
                                        </tr>                                                                              
                                    </table>
                                </div>                                    

                                <p>
                                    When I do this, I see
                                </p>

                                <pre class="text"><code>1609</code></pre>

                                <p>
                                    Meaning 1,609 structural variants overlap a gene. This is roughly 44%.
                                </p>

                                <p>
                                    Next, we'll build on these bioinformatic skills by looking at a set of SNPs from a sample of wolves!
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
                <a href="commands.html">&lt;&nbsp;Previous</a>    
            </div>
        </div>
        <div class="col-6-24" id="nav-margin"></div>
        <div class="col-6-24" id="nav-btn-cont">
            <div class="nav-btn">
                <a href="wolf-snps.html">Next&nbsp;&gt;</a>
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
pagefile = "macaque-svs.html";
print("Generating " + pagefile + "...");
year = RC.getYear();
title = "ConGen" + year + " - Intro to Bioinformatics"

head = RC.readHead(title);
nav = RC.readNav(pagefile);
banner = "";
#banner = RC.readPrevBanner(year, "bioinformatics");
footer = RC.readFooter();

outfilename = "../../" + pagefile;

with open(outfilename, "w") as outfile:
    outfile.write(html_template.format(head=head, nav=nav, banner=banner, footer=footer));