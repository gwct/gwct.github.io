############################################################
# For ConGen2021 site, 08.21
# This generates the file "wolf-snps.html"
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

    <a class="internal-link" name="wolf-data"></a>
   	<div class="row" id="header">Single nucleotide polymorphisms in gray wolves</div>

    <div class="row" id="body-row">
        <div class="col-3-24" id="side-nav-cont">
            <div id="side-nav">
                <span id="side-header">Page contents</span>
                <ul>
                    <li><a href="wolf-snps.html#wolf-data">Wolf dataset</a></li>
                    <li><a href="wolf-snps.html#vcf">VCF files and vcftools</a></li>
                    <li><a href="wolf-snps.html#het">Calculating heterozygosity</a></li>
                    <li><a href="wolf-snps.html#variables">Introduction to variables</a></li>
                    <li><a href="wolf-snps.html#scripts">Introduction to scripting</a></li>
                    <li><a href="wolf-snps.html#loops">Introduction to loops</a></li>
                </ul>
            </div>
        </div>

        <div class="col-21-24" id="main-cont">

            <div class="row" id="top-row-cont">
                <div class="col-24-24" id="top-row"></div>
            </div>
            <div class="row" id="section-header-cont">
                <div class="col-24-24" id="section-header-row">
                    <div id="section-header">Gray wolf dataset</div>
                </div>
            </div>

            <div class="row" id="section-cont">
                <div class="col-24-24" id="section-col">
                    <div class="row" id="section-row">
                        <div class="col-2-24" id="inner-margin"></div>
                        <div class="col-20-24" id="section-content">
                            <p>
                                This section will focus on analyzing SNP data from North American gray wolves (<em>Canis lupus</em>). The original data consist of
                                a few hundred wolf samples that were enriched for a custom capture array consisting of several thousands of reagions across the wolf
                                genome.
                            </p>

                            <p>
                                Our data consist of genic SNPs genotyped for three wolf ecotypes: (1) the British Columbia coastal, (2) the High Arctic, and (3)
                                the Boreal Forest. These wolves have pretty striking ecological and behavioral differences that are in part driven by differences
                                amongst their environments. We used these data to look at population genetic variation and signals of local adaptation amongst these
                                ecotypes ((<a href="https://doi.org/10.1111/mec.13364" target="_blank">Schweizer et al. 2015, <em>Molecular Ecology</em></a>).).
                            </p>

                            <div class="row" id="img-row">
                                <div class="col-4-24" id="margin"></div>
                                <div class="col-16-24" id="img-col">
                                    <img id="res-img" src="img/gray-wolf-ranges.png">
                                    <center><span class="fig-caption">Figure 5.1: Ranges and ecotypes of gray sampled gray wolf populations.</span></center>
                                </div>
                                <div class="col-4-24" id="margin"></div>
                            </div>

                            <p>
                                This data is also included in the project repo you previously cloned. Let's navigate to the {co}wolf-snps{cc}
                                folder now to minimize the paths we have to type when using the data. You should already be in the root project directory
                                ({co}~/congen-2021-bioinformatics/{cc}), so you should just have to type the command:
                            </p>

                            <center><pre class="cmd"><code>cd data/wolf-data/{cc}</pre></center>

                            <div class="table-cont">
                                <table class="cmd-table">
                                    <thead><th class="tcol-1">Command line parameter</th><th class="tcol-2">Description</th></thead>
                                    <tr>
                                        <td class="tcol-1">cd</td><td class="tcol-2">The Linux change directory command</td>
                                    </tr>
                                    <tr>
                                        <td class="tcol-1">data/wolf-data</td><td class="tcol-2">The path to the directory you want to change to. In this case,
                                            this is a <b>relative path</b>. If you are not in the {co}~/congen-2021-bioinformatics/{cc} directory,
                                            you will likely get an error saying this path does not exist.</td>
                                    </tr>
                                </table>
                            </div>     

                            <p>
                                If you are somewhere else other than the root project directory, first navigate back to that folder and then change to the
                                {co}wolf-data{cc} folder. Or, if you're familiar enough with the file tree, navigate straight to the
                                data folder!
                            </p>

                            <div id="msg_cont">
                                <div id="msg">
                                    <div id="msg_banner">Tip - Remember the {co}pwd{cc} command!</div>
                                    <div id="msg_text">
                                        <p>
                                            Lost somewhere in the file system? Not sure exactly where you are? Remember the <b>print working directory</b> command:
                                            {co}pwd{cc}. This simply prints your current location in the file system and can help you get your
                                            bearings if you've been moving around a lot. This and {co}ls{cc} are essential for navigating your
                                            file system.
                                        </p>

                                        <p></p>
                                    </div>
                                </div>
                            </div>                       

                        </div>
                        <div class="col-2-24" id="inner-margin"></div>
                    </div>
                </div>
            </div>
                                
            <a class="internal-link" name="vcf"></a>
            <div class="row" id="section-header-cont">
                <div class="col-24-24" id="section-header-row">
                    <div id="section-header">VCF files and vcftools</div>
                </div>
            </div>

            <div class="row" id="section-cont">
                <div class="col-24-24" id="section-col">
                    <div class="row" id="section-row">
                        <div class="col-2-24" id="inner-margin"></div>
                        <div class="col-20-24" id="section-content">

                            <p>
                                I've downsampled the full data set to consist of 35 individuals and a set of genic SNPs. We will be working with these SNP data in a VCF file.
                                VCF stands for variant call format and is just another plain text file that shows genotype data for each individual with associated quality scores,
                                depth of coverage, etc. for each variant and sample in tab-delimited format.
                            </p>

                            <p>
                                The full VCF file format specifications can be found here: 
                                <a href="https://samtools.github.io/hts-specs/VCFv4.2.pdf" target="_blank">samtools VCF specs</a>
                            </p>

                            <p>
                                VCF files alos contain a <b>header</b>, denoted with the {co}#{cc} character at the beginning of the line.
                                The header can be a single line or thousands of lines and provides information on how the VCF file was generated, to which reference genome
                                the sequence data was aligned, and definitions nof the various fields in each column of the data mean. Given all this information, VCF files
                                can potentially be enormous in size and cumbersome to work with.
                            </p>

                            <p>
                                Luckily, there is software out there to help! <a href="https://vcftools.github.io/index.html" target="_blank">vcftools</a> is a suite of useful programs designed for 
                                use on VCF formatted files. {co}vcftools{cc} can be used to parse out SNPs and individuals, assess quality metrics of variants,
                                and output a variety of statistics like Fst, linkage, and heterozygosity
                            </p>

                            <p>
                                Much like {co}bedtools{cc}, {co}vcftools{cc} is desiged to follow the
                                <a href="commands.html#philosophy">Unix philosophy</a>: commands work on properly formatted text input and and output the processed
                                data to the terminal, which can easily be <b>piped</b> ({co}|{cc}) or <b>redirected</b> ({co}&gt;{cc}).
                                {co}vcftools{cc} contains many options allowing users to perform different analyses. In general, the program is called
                                as follows:
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

                            <p>
                                Here are some more explicit examples of {co}vcftools{cc} commands:
                            </p>

                            <div class="row" id="img-row">
                                <div class="col-4-24" id="margin"></div>
                                <div class="col-16-24" id="img-col">
                                    <img id="res-img" src="img/vcftools-examples.png">
                                    <center><span class="fig-caption">Figure 5.2: Example vcftools commands</a></span></center>
                                </div>
                                <div class="col-4-24" id="margin"></div>
                            </div>
                                
                        </div>
                        <div class="col-2-24" id="inner-margin"></div>
                    </div>
                </div>
            </div>

            <a class="internal-link" name="het"></a>
            <div class="row" id="section-header-cont">
                <div class="col-24-24" id="section-header-row">
                    <div id="section-header">Calculating heterozygosity from a VCF file</div>
                </div>
            </div>

            <div class="row" id="section-cont">
                <div class="col-24-24" id="section-col">
                    <div class="row" id="section-row">
                        <div class="col-2-24" id="inner-margin"></div>
                        <div class="col-20-24" id="section-content">

                            <p>
                                For this section of the workshop, we're going to start with a simple task, calculating heterozygosity, for a single wolf ecotype. 
                                Then we're going to learn how to automate it over multiple populations through using loops and writing a script.
                            </p>

                            <p>
                                Before we do that, let's get some basic info about out called variants in the VCF file.
                            </p>

                            <h3>TASK 1: How many SNPs are there?</h3>

                                <p>
                                    We know that our VCF file has a number of header lines (which don't count towards the actual number of SNPs) and then a separate 
                                    line for each SNP. Because of this, ff we just use {co}wc -l{cc} we will count all lines of the file, which doesn't 
                                    tell us the number of SNPs.
                                </p>

                                <p> 
                                    But by using {co}grep{cc} with the {co}-v{cc} flag, we can find all the lines of text that don't 
                                    contain a character, string, or pattern. Then we can use our handy {co}|{cc} to get our answer:
                                </p>

                                <center><pre class="cmd"><code>grep -v "#" Filtered_NAwolf_n35_variableSites_GenicRegions.recode.vcf | wc -l{cc}</pre></center>

                                <div class="table-cont">
                                    <table class="cmd-table">
                                        <thead><th class="tcol-1">Command line parameter</th><th class="tcol-2">Description</th></thead>
                                        <tr>
                                            <td class="tcol-1">grep</td><td class="tcol-2">A Unix string and pattern searching command</td>
                                        </tr>
                                        <tr>
                                            <td class="tcol-1">-v</td><td class="tcol-2">By default, {co}grep{cc} prints all lines that contain 
                                                the specified string/pattern. The {co}-v{cc} option tells {co}grep{cc} to print 
                                                all the lines that DO NOT contain the specified string/pattern instead.</td>
                                        </tr>
                                        <tr>
                                            <td class="tcol-1">"#"</td><td class="tcol-2">The string or pattern you want to search for</td>
                                        </tr>
                                        <tr>
                                            <td class="tcol-1">Filtered_NAwolf_n35_variableSites_GenicRegions.recode.vcf</td><td class="tcol-2">The path to the file you want to search</td>
                                        </tr>
                                        <tr>
                                            <td class="tcol-1">|</td><td class="tcol-2">The pipe character means the output from the command specified before it
                                                will be used as the input tot he command specified after it</td>
                                        </tr>
                                        <tr>
                                            <td class="tcol-1">wc</td><td class="tcol-2">The Linux word count command. Counts the number of lines, words, and
                                                characters in an input file.</td>
                                        </tr>
                                        <tr>
                                            <td class="tcol-1">-l</td><td class="tcol-2">Tells {co}wc{cc} to only count number of lines</td>
                                        </tr>
                                    </table>
                                </div>

                                <p>
                                    This should output the number of lines in the VCF file that don't contain the "#" character:
                                </p>
                                    
                                <pre class="text"><code>19620{cc}</pre>

                                <p>
                                    Since the only lines with "#" should be the informational header lines and all other lines represent one SNP, this means there
                                    are 19,620 SNPs represented in this VCF file.
                                </p>

                            <h3>TASK 2: Calculate heterozygosity for the coastal wolf samples.</h3>

                                <p>
                                    We're going to use one of the functions of {co}vcftools{cc} to calculate the heterozygosity 
                                    ({co}--het{cc}) within only the coastal wolf population. {co}vcftools{cc}
                                    lets us specify which individuals to include in an analysis through the {co}--keep{cc} flag with 
                                    a file of sample IDs.
                                </p>

                                <center><pre class="cmd"><code>vcftools --vcf Filtered_NAwolf_n35_variableSites_GenicRegions.recode.vcf --out Filtered_NAwolf_n35_variableSites_GenicRegions_coastal --het --keep pop_coastal.txt{cc}</pre></center>

                                <div class="table-cont">
                                    <table class="cmd-table">
                                        <thead><th class="tcol-1">Command line parameter</th><th class="tcol-2">Description</th></thead>
                                        <tr>
                                            <td class="tcol-1">vcftools</td><td class="tcol-2">A program for working with variant calls in VCF format</td>
                                        </tr>
                                        <tr>
                                            <td class="tcol-1">-vcf</td><td class="tcol-2">The option to specify the input file</td>
                                        </tr>
                                        <tr>
                                            <td class="tcol-1">Filtered_NAwolf_n35_variableSites_GenicRegions.recode.vcf</td><td class="tcol-2">
                                                The path to the input file</td>
                                        </tr>
                                        <tr>
                                            <td class="tcol-1">--out</td><td class="tcol-2">The option to specify the <b>prefix</b> for all output
                                                files. The file extension will be determined by the analysis.</td>
                                        </tr>
                                        <tr>
                                            <td class="tcol-1">Filtered_NAwolf_n35_variableSites_GenicRegions_coastal</td><td class="tcol-2">
                                                The desired name of the output file. If it exists it will be overwritten.</td>
                                        </tr>
                                        <tr>
                                            <td class="tcol-1">--het</td><td class="tcol-2">This option tells {co}vcftools{cc} to calculate
                                                heterozygosity of the samples in the input file.</td>
                                        </tr>
                                        <tr>
                                            <td class="tcol-1">--keep</td><td class="tcol-2">This option is used with a file that lists sample IDs. Only samples
                                                in that file will be used by the program for this run.</td>
                                        </tr>
                                        <tr>
                                            <td class="tcol-1">pop_coastal.txt</td><td class="tcol-2">The path to the file with the sample IDs to keep</td>
                                        </tr>     
                                    </table>
                                </div>                                

                                <p>
                                    If we use {co}ls{cc} to look at the output files, we can see that {co}vcftools{cc} has provided a .log file, which contains
                                    our command history, as well as a .het file that provides the per-individual heterozygosity.
                                </p>

                                <p>
                                    But does this file actually give us the heterozygosity?
                                </p>

                                <center><pre class="cmd"><code>head Filtered_NAwolf_n35_variableSites_GenicRegions_coastal{cc}</pre></center>

                                <div class="table-cont">
                                    <table class="cmd-table">
                                        <thead><th class="tcol-1">Command line parameter</th><th class="tcol-2">Description</th></thead>
                                        <tr>
                                            <td class="tcol-1">head</td><td class="tcol-2">A Unix command that prints the first few lines of a file</td>
                                        </tr>
                                        <tr>
                                            <td class="tcol-1">Filtered_NAwolf_n35_variableSites_GenicRegions_coastal</td><td class="tcol-2">
                                                The path to the input file</td>
                                        </tr>  
                                    </table>
                                </div>    

                                <p>
                                    No, the output provides the number of homozygous sites and the total number of sites. But we can use this information
                                    with a handy one-liner in {co}awk{cc} to calculate heterozygosity:
                                </p>

                                <center><pre class="cmd"><code>awk '/RKW/ {{print $1,$2,$3,$4,$5,(($4-$2)/$4)}}' Filtered_NAwolf_n35_variableSites_GenicRegions_coastal.het &gt; Filtered_NAwolf_n35_variableSites_GenicRegions_coastal.het.calc{cc}</pre></center>

                                <div class="table-cont">
                                    <table class="cmd-table">
                                        <thead><th class="tcol-1">Command line parameter</th><th class="tcol-2">Description</th></thead>
                                        <tr>
                                            <td class="tcol-1">awk</td><td class="tcol-2">A Linux text processing language</td>
                                        </tr>
                                        <tr>
                                            <td class="tcol-1">'/RKW/ {{print $1,$2,$3,$4,$5,(($4-$2)/$4)}}'</td><td class="tcol-2">
                                                The user-coded program to run</td>
                                        </tr>  
                                            <td class="tcol-1">Filtered_NAwolf_n35_variableSites_GenicRegions_coastal.het</td><td class="tcol-2">
                                                The path to the file on which to run the program</td>
                                        </tr>    
                                        </tr>  
                                            <td class="tcol-1">&gt;</td><td class="tcol-2">The redirect character means the output from the command specified before it
                                                will be saved to the file specified after it</td>
                                        </tr>      
                                        </tr>  
                                            <td class="tcol-1">Filtered_NAwolf_n35_variableSites_GenicRegions_coastal.het.calc</td><td class="tcol-2">
                                                The path to the desired output file. This will be created if it doesn't exist and WILL OVERWRITE files that do exist</td>
                                        </tr>                                            
                                    </table>
                                </div>  

                                <p>
                                    Using this, we can also calculate the mean population heterozygosity using {co}awk{cc}:
                                </p>

                                <center><pre class="cmd"><code>awk '{{sum += $6}} END {{if (NR > 0) print sum / NR }}' Filtered_NAwolf_n35_variableSites_GenicRegions_coastal.het.calc{cc}</pre></center>

                                <div class="table-cont">
                                    <table class="cmd-table">
                                        <thead><th class="tcol-1">Command line parameter</th><th class="tcol-2">Description</th></thead>
                                        <tr>
                                            <td class="tcol-1">awk</td><td class="tcol-2">A Linux text processing language</td>
                                        </tr>
                                        <tr>
                                            <td class="tcol-1">'{{sum += $6}} END {{if (NR > 0) print sum / NR }}'</td><td class="tcol-2">
                                                The user-coded program to run</td>
                                        </tr>  
                                            <td class="tcol-1">Filtered_NAwolf_n35_variableSites_GenicRegions_coastal.het.calc</td><td class="tcol-2">
                                                The path to the file on which to run the program</td>
                                        </tr>                                       
                                    </table>
                                </div>                                 

                                <p>
                                    Great! So now we have calculated the per-individual heterozygosity and the population heterozygosity for the coastal populations.
                                    Let's figure out how to repeat this set of commands for any number of additional populations.
                                </p>

                        </div>
                        <div class="col-2-24" id="inner-margin"></div>
                    </div>
                </div>
            </div>

            <a class="internal-link" name="variables"></a>
            <div class="row" id="section-header-cont">
                <div class="col-24-24" id="section-header-row">
                    <div id="section-header">Introduction to variables in Unix</div>
                </div>
            </div>

            <div class="row" id="section-cont">
                <div class="col-24-24" id="section-col">
                    <div class="row" id="section-row">
                        <div class="col-2-24" id="inner-margin"></div>
                        <div class="col-20-24" id="section-content">

                            <p>
                                Instead of hard-coding our command to be specific to the coastal wolves, we can use shell variables. We indicate a shell variable like so:
                            </p>

                            <center><pre class="cmd"><code>wolf_pop=coastal{cc}</pre></center>

                            <div class="table-cont">
                                <table class="cmd-table">
                                    <thead><th class="tcol-1">Command line parameter</th><th class="tcol-2">Description</th></thead>
                                    <tr>
                                        <td class="tcol-1">wolf_pop</td><td class="tcol-2">The desired variable name appears to the left of the equals sign</td>
                                    </tr>
                                    <tr>
                                        <td class="tcol-1">=</td><td class="tcol-2">The equals sign indicates variable assignment in programming languages</td>
                                    </tr>  
                                        <td class="tcol-1">coastal</td><td class="tcol-2">The value you wish to assign to the variable name</td>
                                    </tr>                                       
                                </table>
                            </div>                              

                            <p>
                                We can check that variable assignment was successful by printing the value with the {co}echo{cc} command:
                            </p>

                            <center><pre class="cmd"><code>echo ${{wolf_pop}}{cc}</pre></center>

                            <div class="table-cont">
                                <table class="cmd-table">
                                    <thead><th class="tcol-1">Command line parameter</th><th class="tcol-2">Description</th></thead>
                                    <tr>
                                        <td class="tcol-1">echo</td><td class="tcol-2">The Unix print command. Values given as input will be printed to the screen.</td>
                                    </tr>
                                    <tr>
                                        <td class="tcol-1">$wolf_pop</td><td class="tcol-2">The item to print to the screen. In this case, because {co}wolf_pop{cc} is a
                                            defined variable, we must use the {co}${{}}{cc} symbols to let {co}echo{cc} know to print it's assigned value to the screen, rather
                                            than just the text "wolf_pop".</td>                                       
                                </table>
                            </div>

                            <p>
                                We can use variables in any command in the terminal. For instance, we can run the same command as before to calculate heterozygosity, but
                                instead of typing "coastal" in the command, we can use our variable:
                            </p>

                            <center><pre class="cmd"><code>vcftools --vcf Filtered_NAwolf_n35_variableSites_GenicRegions.recode.vcf --out Filtered_NAwolf_n35_variableSites_GenicRegions_${{wolf_pop}} --het --keep pop_${{wolf_pop}}.txt{cc}</pre></center>

                            <div class="table-cont">
                                <table class="cmd-table">
                                    <thead><th class="tcol-1">Command line parameter</th><th class="tcol-2">Description</th></thead>
                                    <tr>
                                        <td class="tcol-1">vcftools</td><td class="tcol-2">A program for working with variant calls in VCF format</td>
                                    </tr>
                                    <tr>
                                        <td class="tcol-1">-vcf</td><td class="tcol-2">The option to specify the input file</td>
                                    </tr>
                                    <tr>
                                        <td class="tcol-1">Filtered_NAwolf_n35_variableSites_GenicRegions.recode.vcf</td><td class="tcol-2">
                                            The path to the input file</td>
                                    </tr>
                                    <tr>
                                        <td class="tcol-1">--out</td><td class="tcol-2">The option to specify the <b>prefix</b> for all output
                                            files. The file extension will be determined by the analysis.</td>
                                    </tr>
                                    <tr>
                                        <td class="tcol-1">Filtered_NAwolf_n35_variableSites_GenicRegions_${{wolf_pop}}</td><td class="tcol-2">
                                            The desired name of the output file. If it exists it will be overwritten. In this case, we use the {co}wolf_pop{cc}
                                            variable to create a file with the name of the current population.</td>
                                    </tr>
                                    <tr>
                                        <td class="tcol-1">--het</td><td class="tcol-2">This option tells {co}vcftools{cc} to calculate
                                            heterozygosity of the samples in the input file.</td>
                                    </tr>
                                    <tr>
                                        <td class="tcol-1">--keep</td><td class="tcol-2">This option is used with a file that lists sample IDs. Only samples
                                            in that file will be used by the program for this run.</td>
                                    </tr>
                                    <tr>
                                        <td class="tcol-1">pop_{{wolf_pop}}.txt</td><td class="tcol-2">The path to the file with the sample IDs to keep. In 
                                            this case, we're using our variable, {co}wolf_pop{cc} to indicate which existing file to use.</td>
                                    </tr>     
                                </table>
                            </div> 

                            <p>
                                This provides the same output as the command we ran earlier. So, we could assign a new value to the {co}wolf_pop{cc}
                                variable. Notice also how I have been consistent in how I named all of my pop files so that I can substitute an ecotype
                                name but otherwise still have that same general file name.
                            </p>

                            <center><pre class="cmd"><code>wolf_pop=highArctic{cc}</pre></center>

                            <div class="table-cont">
                                <table class="cmd-table">
                                    <thead><th class="tcol-1">Command line parameter</th><th class="tcol-2">Description</th></thead>
                                    <tr>
                                        <td class="tcol-1">wolf_pop</td><td class="tcol-2">The desired variable name appears to the left of the equals sign</td>
                                    </tr>
                                    <tr>
                                        <td class="tcol-1">=</td><td class="tcol-2">The equals sign indicates variable assignment in programming languages</td>
                                    </tr>  
                                        <td class="tcol-1">highArctic</td><td class="tcol-2">The value you wish to assign to the variable name</td>
                                    </tr>                                       
                                </table>
                            </div>                              

                            <p>
                                We can check that variable assignment was successful by printing the value with the {co}echo{cc} command:
                            </p>

                            <center><pre class="cmd"><code>echo ${{wolf_pop}}{cc}</pre></center>

                            <div class="table-cont">
                                <table class="cmd-table">
                                    <thead><th class="tcol-1">Command line parameter</th><th class="tcol-2">Description</th></thead>
                                    <tr>
                                        <td class="tcol-1">echo</td><td class="tcol-2">The Unix print command. Values given as input will be printed to the screen.</td>
                                    </tr>
                                    <tr>
                                        <td class="tcol-1">$wolf_pop</td><td class="tcol-2">The item to print to the screen. In this case, because {co}wolf_pop{cc} is a
                                            defined variable, we must use the {co}${{}}{cc} symbols to let {co}echo{cc} know to print it's assigned value to the screen, rather
                                            than just the text "wolf_pop".</td>                                       
                                </table>
                            </div>                            

                            <p>
                                Now that we've reassigned the {co}wolf_pop{cc} variable to the highArctic population, we can run the same series of commands as above,
                                but {co}vcftools{cc} will use the samples and provide output for this population.
                            </p>

                            <p>
                                First, run {co}vcftools{cc} to count the number of sites:
                            </p>

                            <center><pre class="cmd"><code>vcftools --vcf Filtered_NAwolf_n35_variableSites_GenicRegions.recode.vcf --out Filtered_NAwolf_n35_variableSites_GenicRegions_${{wolf_pop}} --het --keep pop_${{wolf_pop}}.txt{cc}</pre></center>

                            <div class="table-cont">
                                <table class="cmd-table">
                                    <thead><th class="tcol-1">Command line parameter</th><th class="tcol-2">Description</th></thead>
                                    <tr>
                                        <td class="tcol-1">vcftools</td><td class="tcol-2">A program for working with variant calls in VCF format</td>
                                    </tr>
                                    <tr>
                                        <td class="tcol-1">-vcf</td><td class="tcol-2">The option to specify the input file</td>
                                    </tr>
                                    <tr>
                                        <td class="tcol-1">Filtered_NAwolf_n35_variableSites_GenicRegions.recode.vcf</td><td class="tcol-2">
                                            The path to the input file</td>
                                    </tr>
                                    <tr>
                                        <td class="tcol-1">--out</td><td class="tcol-2">The option to specify the <b>prefix</b> for all output
                                            files. The file extension will be determined by the analysis.</td>
                                    </tr>
                                    <tr>
                                        <td class="tcol-1">Filtered_NAwolf_n35_variableSites_GenicRegions_${{wolf_pop}}</td><td class="tcol-2">
                                            The desired name of the output file. If it exists it will be overwritten. In this case, we use the {co}wolf_pop{cc}
                                            variable to create a file with the name of the current population.</td>
                                    </tr>
                                    <tr>
                                        <td class="tcol-1">--het</td><td class="tcol-2">This option tells {co}vcftools{cc} to calculate
                                            heterozygosity of the samples in the input file.</td>
                                    </tr>
                                    <tr>
                                        <td class="tcol-1">--keep</td><td class="tcol-2">This option is used with a file that lists sample IDs. Only samples
                                            in that file will be used by the program for this run.</td>
                                    </tr>
                                    <tr>
                                        <td class="tcol-1">pop_{{wolf_pop}}.txt</td><td class="tcol-2">The path to the file with the sample IDs to keep. In 
                                            this case, we're using our variable, {co}wolf_pop{cc} to indicate which existing population file to use.</td>
                                    </tr>     
                                </table>
                            </div>

                            <p>
                                Then run {co}awk{cc} to calculate heterozygosity for each individual in the highArctic sample. Again note that we use the 
                                {co}wolf_pop{cc} variable in our input and output file names:
                            </p>

                            <center><pre class="cmd"><code>awk '/RKW/ {{print $1,$2,$3,$4,$5,(($4-$2)/$4)}}' Filtered_NAwolf_n35_variableSites_GenicRegions_${{wolf_pop}}.het &gt; Filtered_NAwolf_n35_variableSites_GenicRegions_${{wolf_pop}}.het.calc{cc}</pre></center>

                            <div class="table-cont">
                                <table class="cmd-table">
                                    <thead><th class="tcol-1">Command line parameter</th><th class="tcol-2">Description</th></thead>
                                    <tr>
                                        <td class="tcol-1">awk</td><td class="tcol-2">A Linux text processing language</td>
                                    </tr>
                                    <tr>
                                        <td class="tcol-1">'/RKW/ {{print $1,$2,$3,$4,$5,(($4-$2)/$4)}}'</td><td class="tcol-2">
                                            The user-coded program to run</td>
                                    </tr>  
                                        <td class="tcol-1">Filtered_NAwolf_n35_variableSites_GenicRegions_${{wolf_pop}}.het</td><td class="tcol-2">
                                            The path to the file on which to run the program. Note that we use the {co}wolf_pop{cc}variable to indicate
                                            the population file to run.</td>
                                    </tr>    
                                    </tr>  
                                        <td class="tcol-1">&gt;</td><td class="tcol-2">The redirect character means the output from the command specified before it
                                            will be saved to the file specified after it</td>
                                    </tr>      
                                    </tr>  
                                        <td class="tcol-1">Filtered_NAwolf_n35_variableSites_GenicRegions_${{wolf_pop}}.het.calc</td><td class="tcol-2">
                                            The path to the desired output file. This will be created if it doesn't exist and WILL OVERWRITE files that do exist.
                                            Note that we use the {co}wolf_pop{cc}variable to save to a file name labeled with the correct population.</td>
                                    </tr>                                            
                                </table>
                            </div>                              

                            <p>
                                And then {co}awk{cc} again with the {co}wolf_pop{cc} variable to get mean population heterozygosity:
                            </p>

                            <center><pre class="cmd"><code>awk '{{sum += $6}} END {{if (NR > 0) print sum / NR }}' Filtered_NAwolf_n35_variableSites_GenicRegions_${{wolf_pop}}.het.calc{cc}</pre></center>

                            <div class="table-cont">
                                <table class="cmd-table">
                                    <thead><th class="tcol-1">Command line parameter</th><th class="tcol-2">Description</th></thead>
                                    <tr>
                                        <td class="tcol-1">awk</td><td class="tcol-2">A Linux text processing language</td>
                                    </tr>
                                    <tr>
                                        <td class="tcol-1">'{{sum += $6}} END {{if (NR > 0) print sum / NR }}'</td><td class="tcol-2">
                                            The user-coded program to run</td>
                                    </tr>  
                                        <td class="tcol-1">Filtered_NAwolf_n35_variableSites_GenicRegions_${{wolf_pop}}.het.calc</td><td class="tcol-2">
                                            The path to the file on which to run the program. Note that we use the {co}wolf_pop{cc} variable to indicate
                                            the population file to run.</td>
                                    </tr>                                       
                                </table>
                            </div> 

                        </div>
                        <div class="col-2-24" id="inner-margin"></div>
                    </div>
                </div>
            </div>


            <a class="internal-link" name="scripts"></a>
            <div class="row" id="section-header-cont">
                <div class="col-24-24" id="section-header-row">
                    <div id="section-header">Introduction to scripting</div>
                </div>
            </div>

            <div class="row" id="section-cont">
                <div class="col-24-24" id="section-col">
                    <div class="row" id="section-row">
                        <div class="col-2-24" id="inner-margin"></div>
                        <div class="col-20-24" id="section-content">

                            <p>
                                Now, we're going to add some of these commands with variables to a <b>script</b> so that we can automate the series of commands
                                to generate per-individual and per-population heterozygosity. 
                            </p>
                            
                            <p>
                                A <b>script</b> is simply a text file where we can write and save the code and commands we want to run. Scripts give use the
                                flexibility to perform complex operations based on conditions and ranges of values. Since a script is a text file, we're going 
                                to create a new text file and copy some commands into it. We're going to use an in-terminal text editor, <a href="https://www.vim.org/">vim</a>
                                to do this, although there are several other <a href="#">options</a>.
                            </p>

                            <center><pre class="cmd"><code>vim het_analysis.sh{cc}</pre></center>

                            <div class="table-cont">
                                <table class="cmd-table">
                                    <thead><th class="tcol-1">Command line parameter</th><th class="tcol-2">Description</th></thead>
                                    <tr>
                                        <td class="tcol-1">vim</td><td class="tcol-2">An in-terminal text editor available on Linux.</td>
                                    </tr>
                                    <tr>
                                        <td class="tcol-1">het_analysis.sh</td><td class="tcol-2">The name of the text file to create or view (if it exists).
                                            The .sh extension indicates this is a <b>shell script</b></td>                                      
                                </table>
                            </div>    

                            <p>
                                You should now be in the {co}vim{cc} text editor. Your screen should be cleared of commands and cursor should be blinking on top, with
                                tilde characteres ({co}~{cc}) on every other line. Importantly, {co}vim{cc} has both a <b>viewing</b> mode and an <b>editing</b> mode.
                                When you create a new file with {co}vim{cc}, as we have here, you start out in <b>viewing</b> mode. We can switch to <b>editing</b> mode
                                by pressing the {co}a{cc} key. Once you do this, you'll see the text {co}-- INSERT --{cc} at the bottom of the screen, indicating we have
                                switched to <b>editing</b> mode.
                            </p>

                            <p>
                                Now, we can copy and paste our commands for calculating heterozygosity into this file. Of course, there are other ways we could get the 
                                commands into the file (such as using {co}echo{cc} and redirecting), but we'll stay simple today.
                            </p>

                            <p>
                                Copy the following commands:
                            </p>

                                <pre class="script"><code>wolf_pop=$1
vcftools --vcf Filtered_NAwolf_n35_variableSites_GenicRegions.recode.vcf --out Filtered_NAwolf_n35_variableSites_GenicRegions_${{wolf_pop}} --het --keep pop_${{wolf_pop}}.txt
awk '/RKW/ {{print $1,$2,$3,$4,$5,(($4-$2)/$4)}}' Filtered_NAwolf_n35_variableSites_GenicRegions_${{wolf_pop}}.het > Filtered_NAwolf_n35_variableSites_GenicRegions_${{wolf_pop}}.het.calc
awk '{{sum += $6}} END {{if (NR > 0) print sum / NR }}' Filtered_NAwolf_n35_variableSites_GenicRegions_${{wolf_pop}}.het.calc</code></pre>                            

                            <p>
                                The last three commands should be familiar to you already. They are the same commands we used above for the coastal population, but
                                we've substituted the string "coastal" for the variable {co}wolf_pop{cc}.
                            </p>

                            <p>
                                The first line, {co}wolf_pop=$1{cc} is our variable assignment. It tells the script to assign the variable {cc}wolf_pop{cc} the value 
                                of {co}$1{cc}. Well what is {co}$1{cc}? It has a dollar sign ({co}${cc}) preceding it, so we know it is a variable. But we haven't
                                assigned anything to it yet.
                            </p>

                            <p>
                                Like other commands, your own scripts can take input options from the command line. By default, a shell script (like the one we are
                                writing) will assign these options to internal variables: {co}$1{cc} for the first option, {co}$2{cc} for the second one, and so on.
                                So, {co}wolf_pop{cc} will be assigned whatever we type into the terminal when we run the script.
                            </p>

                            <p>
                                Let's exit out of {co}vim{cc} to try and run our script. First, switch back to <b>viewing</b> mode by pressing the {co}ESC{cc} key.
                                You should no longer see the text {co}-- INSERT --{cc} at the bottom of the screen. When in <b>viewing</b> mode, any input we type
                                is interpreted as internal {co}vim{cc} commands, such as saving, exiting, etc. Let's tell {co}vim{cc} to save the changes we've made to
                                the file with the write command ({co}w{cc}) and then quit ({co}q{cc}) the text editor by typing:

                            <center><pre class="cmd"><code>:wq{cc}</pre></center>

                            <div class="table-cont">
                                <table class="cmd-table">
                                    <thead><th class="tcol-1">Command line parameter</th><th class="tcol-2">Description</th></thead>
                                    <tr>
                                        <td class="tcol-1">:</td><td class="tcol-2">Tells {co}vim{cc} to interpret the following text as commands</td>
                                    </tr>
                                    <tr>
                                        <td class="tcol-1">w</td><td class="tcol-2">The {co}vim{cc} write command that saves changes made to the file</td>
                                    </tr>
                                    <tr>
                                        <td class="tcol-1">q</td><td class="tcol-2">The {co}vim{cc} quit command to exit the text editor and return to the
                                            terminal</td>
                                    </tr>
                                </table>
                            </div>                                 

                            <h3>TASK 3: Make the script executable and try it</h3>

                                <p>
                                    We will use the {co}chmod{cc} command to change the permissions on the script to the shell knows that it's contents
                                    should be interpreted as commands. This is known as making the file <b>executable</b>:
                                </p>

                                <center><pre class="cmd"><code>chmod a+x het_analysis.sh{cc}</pre></center>

                                <div class="table-cont">
                                    <table class="cmd-table">
                                        <thead><th class="tcol-1">Command line parameter</th><th class="tcol-2">Description</th></thead>
                                        <tr>
                                            <td class="tcol-1">chmod</td><td class="tcol-2">The Unix change mode command used to change permissions on files</td>
                                        </tr>
                                        <tr>
                                            <td class="tcol-1">a+x</td><td class="tcol-2">This tells {co}chmod{cc} to modify ({co}a{cc} the file's permissions
                                             to make it executable ({co}+x{cc})</td>
                                        </tr>
                                        <tr>
                                            <td class="tcol-1">het_analysis.sh</td><td class="tcol-2">The name of the file to change permissions</td>
                                        </tr>
                                    </table>
                                </div>  

                                <p>
                                    Now let's try to execute our file on the <b>coastal</b> population:
                                </p>

                                <center><pre class="cmd"><code>./het_analysis.sh coastal{cc}</pre></center>

                                <div class="table-cont">
                                    <table class="cmd-table">
                                        <thead><th class="tcol-1">Command line parameter</th><th class="tcol-2">Description</th></thead>
                                        <tr>
                                            <td class="tcol-1">./het_analysis.sh</td><td class="tcol-2">The name of the file to run. Since we have changed its 
                                                permissions to be executable, its contents will be interpreted as shell commands. {co}./{cc} also indicates to
                                                run this file as a shell script</td>
                                        </tr>
                                        <tr>
                                            <td class="tcol-1">coastal</td><td class="tcol-2">Remember, the script we wrote expects input from the command
                                                line to assign to the {co}$1{cc} variable. This will be that value</td>
                                        </tr>
                                    </table>
                                </div>

                                <p>
                                    If we use our handy {co}ls -lht{cc} command, we can see that the three newest files are of the coastal wolf samples, and that
                                    the script we wrote printed the mean population heterozygosity to the screen.
                                </p>

                            <h3>TASK 4: Which population has the highest mean heterozygosity?</h3>

                                <p>
                                    To find this out now, all we have to do is run our script on all three populations:
                                </p>

                                <pre class="cmd"><code>./het_analysis.sh coastal
./het_analysis.sh highArctic
./het_analysis.sh borealForest{cc}</pre>

                                <p>
                                    This shows that the High Arctic populations has the highest mean heterozygosity at 0.36179.
                                </p>

                        </div>
                        <div class="col-2-24" id="inner-margin"></div>
                    </div>
                </div>
            </div>

            <a class="internal-link" name="loops"></a>
            <div class="row" id="section-header-cont">
                <div class="col-24-24" id="section-header-row">
                    <div id="section-header">Introduction to {co}for{cc} loops</div>
                </div>
            </div>

            <div class="row" id="section-cont">
                <div class="col-24-24" id="section-col">
                    <div class="row" id="section-row">
                        <div class="col-2-24" id="inner-margin"></div>
                        <div class="col-20-24" id="section-content">

                            <p>
                                If only there was a way to automate the analysis even further... Aha! We can use {co}for loops{cc} to call the script
                                multiple times with different input values, in this case our 3 population strings, for the {co}wolf_pop{cc} variable.
                                {co}for{cc} loops in a shell script are generated in a similar way as in other programming languages:
                            </p>

                            <center><pre class="cmd-ne"><code>for &lt;variable&gt; in &lt;iterable&gt;; do &lt;code&gt;; done{cc}</pre></center>

                            <div class="table-cont">
                                <table class="cmd-table">
                                    <thead><th class="tcol-1">Command line parameter</th><th class="tcol-2">Description</th></thead>
                                    <tr>
                                        <td class="tcol-1">for</td><td class="tcol-2">The start of the {co}for{cc} loop</td>
                                    </tr>
                                    <tr>
                                        <td class="tcol-1">&lt;variable&gt;</td><td class="tcol-2">{co}for{cc} loops iterate over a set of values. Whatever
                                            is named here as <variable> will be the variable name of the current value in the set.</td>
                                    </tr>
                                    <tr>
                                        <td class="tcol-1">in</td><td class="tcol-2">Indicates that the following will be the set of values to iterate over</td>
                                    </tr>
                                    <tr>
                                        <td class="tcol-1">&lt;iterable&gt;;</td><td class="tcol-2">A data type that contains multiple values</td>
                                    </tr>
                                    <tr>
                                        <td class="tcol-1">do</td><td class="tcol-2">A keyword that indicates a block of code within a {co}for{cc} loop
                                            has started</td>
                                    </tr>
                                    <tr>
                                        <td class="tcol-1">&lt;code&gt;;</td><td class="tcol-2">The code to execute on each value in the set of values</td>
                                    </tr>
                                    <tr>
                                        <td class="tcol-1">done</td><td class="tcol-2">A keyword that indicates the end of the {co}for{cc} loop</td>
                                    </tr>
                                </table>
                            </div> 

                            <p>
                                For instance, we could do the following to loop over letters in the alphabet from A to F and print them out:
                            </p>

                            <center><pre class="cmd-ne"><code>for letter in {{A..F}}; do echo $letter; done{cc}</pre></center>

                            <p>
                                Or the following to subtract 1 from each integer from 1 to 4 and print the resulting value to the screen:
                            </p>

                            <center><pre class="cmd-ne"><code>for num in 1 2 3 4; do echo "The value of $num - 1 is " `expr $num - 1`; done{cc}</pre></center>

                            <h3>TASK 5: Use a {co}for{cc} loop to calculate heterozygosity for the three wolf ecotypes</h3>

                            <center><pre class="cmd"><code>for pop in coastal highArctic borealForest; do ./het_analysis.sh $pop; done{cc}</pre></center>

                            <div class="table-cont">
                                <table class="cmd-table">
                                    <thead><th class="tcol-1">Command line parameter</th><th class="tcol-2">Description</th></thead>
                                    <tr>
                                        <td class="tcol-1">for</td><td class="tcol-2">The start of the {co}for{cc} loop</td>
                                    </tr>
                                    <tr>
                                        <td class="tcol-1">pop</td><td class="tcol-2">This tells the {co}for{cc} loop to assign the current value
                                            being executed to the {co}$pop{cc} variable</td>
                                    </tr>
                                    <tr>
                                        <td class="tcol-1">in</td><td class="tcol-2">Indicates that the following will be the set of values to iterate over</td>
                                    </tr>
                                    <tr>
                                        <td class="tcol-1">coastal highArctic borealForest</td><td class="tcol-2">The values over which to iterate</td>
                                    </tr>
                                    <tr>
                                        <td class="tcol-1">do</td><td class="tcol-2">A keyword that indicates a block of code within a {co}for{cc} loop
                                            has started</td>
                                    </tr>
                                    <tr>
                                        <td class="tcol-1">./het_analysis.sh $pop;</td><td class="tcol-2">Run the het_analysis script on the current value
                                            stored in {co}$pop{cc}</td>
                                    </tr>
                                    <tr>
                                        <td class="tcol-1">done</td><td class="tcol-2">A keyword that indicates the end of the {co}for{cc} loop</td>
                                    </tr>
                                </table>
                            </div>

                            <p>
                                This should produce the same output as when we ran the three commands manually above!
                            </p>

                            <p>
                                Hopefully you've become more familiar with how to use variables in the command-line and in scripts, how to write a script and edit it 
                                using {co}vim{cc}, and how to use {co}for{cc} loops to make your life easier!                
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
                <a href="advanced.html">Next&nbsp;&gt;</a>
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
pagefile = "wolf-snps.html";
print("Generating " + pagefile + "...");
title = "ConGen2021 - Intro to Bioinformatics"


head = RC.readHead(title);
nav = RC.readNav(pagefile);
footer = RC.readFooter();

outfilename = "../../" + pagefile;

with open(outfilename, "w") as outfile:
    outfile.write(html_template.format(head=head, nav=nav, footer=footer, co="<code class='inline'>", cc="</code>"));