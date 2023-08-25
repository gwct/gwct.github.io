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

    <a class="internal-link" name="concepts"></a>
   	<div class="row" id="header">Command concepts</div>

    <div class="row" id="body-row">
        <div class="col-3-24" id="side-nav-cont">
            <div id="side-nav">
                <span id="side-header">Page contents</span>
                <ul>
                    <li><a href="commands.html#concepts">Commands as concepts</a></li>
                    <li><a href="commands.html#text-proc">Commands as text</a></li>
                    <li><a href="commands.html#text-editors">Text editors</a></li>
                    <li><a href="commands.html#philosophy">The Unix philosophy</a></li>
                    <li><a href="commands.html#pipe-redirect">Piping and redirecting</a></li>
                </ul>
            </div>
        </div>

        <div class="col-21-24" id="main-cont">

            <div class="row" id="top-row-cont">
                <div class="col-24-24" id="top-row"></div>
            </div>
            <div class="row" id="section-header-cont">
                <div class="col-24-24" id="section-header-row">
                    <div id="section-header">What is a command?</div>
                </div>
            </div>

            <div class="row" id="section-cont">
                <div class="col-24-24" id="section-col">
                    <div class="row" id="section-row">
                        <div class="col-2-24" id="inner-margin"></div>
                        <div class="col-20-24" id="section-content">
                            <p>
                                I think it is important to ground ourselves in some of the computational concepts that are common among data scientists and
                                bioinformaticians. This can again help to remove the black box of the computer and the terminal, and can improve our 
                                productivity as scientists. With that, I want to step back and just sort of reintroduce the concept of commands from the 
                                command line from a conceptual standpoint.
                            </p>

                            <p>
                                What is a command? A command is basically just a program or an app. It is a chunk of code that someone has written that takes
                                input, processes that input, and produces output. The really common and useful chunks of code (e.g. <code class="inline">ls</code>
                                or <code class="inline">cd</code>) have become mainstays in modern operating systems to the extent that we don't even need to 
                                think about the underlying code, but it is there.
                            </p>

                            <p>
                                The other main difference between commands and modern programs or apps is that they are invoked almost entirely in a text-based
                                terminal program. This provides versatility, as commands can be scripted to run in sequence, as well as the power to convey complex
                                instructions to the computer.
                            </p>

                            <p>
                                Imagine being in a country where you don't know the language. Maybe you go into a coffee shop and want to order something, but
                                without knowledge of the language, you basically have to resort to pointing at what you want on the menu. This is really effective! 
                                It can convey a lot of meaning and be really quick to get across some ideas. But there may be details that you can't convey because
                                they aren't on the menu, like that you wanted extra sugar in your coffee.
                            </p>

                            <p>
                                But if you knew the language you could easily get this information and much more complex and nuanced information across in
                                your order. This is the difference between using the mouse to convey instructions to the computer, and using text-based commands, 
                                and opens up a wide-range of possibilities for the user of the computer... though just like learning a new spoken language, 
                                it can be difficult to grasp at first.
                            </p>
 
                            <div class="row" id="img-row">
                                <div class="col-4-24" id="margin"></div>
                                <div class="col-16-24" id="img-col">
                                    <img id="res-img" src="img/coffee.png">
                                    <center><span class="fig-caption">Figure 3.1: Coffee ordered by pointing at the menu 
                                        <a href="https://pixabay.com/vectors/drink-coffee-tea-beverage-156144/" target="_blank">(left)</a> vs. coffee ordered 
                                        with language <a href="https://www.buzzfeednews.com/article/stephaniemcneal/venti-diabetes" target="_blank">(right)</a>.</span></center>
                                </div>
                                <div class="col-4-24" id="margin"></div>
                            </div>

                        </div>
                        <div class="col-2-24" id="inner-margin"></div>
                    </div>
                </div>
            </div>
                                
            <a class="internal-link" name="text-proc"></a>
            <div class="row" id="section-header-cont">
                <div class="col-24-24" id="section-header-row">
                    <div id="section-header">Commands as text processing</div>
                </div>
            </div>

            <div class="row" id="section-cont">
                <div class="col-24-24" id="section-col">
                    <div class="row" id="section-row">
                        <div class="col-2-24" id="inner-margin"></div>
                        <div class="col-20-24" id="section-content">

                            <p>
                                Most commands, and most data science in general, relies on plain-text formatted documents and input. When it comes
                                down to it, a command is really just:
                            </p>


                                <center><b>formatted text -> command -> processed text</b></center>

                            <p>
                                I refer to this as the central dogma of data science.
                            </p>

                            <p>
                                This means 2 things:

                                <ol>
                                    <li>Text formatting is very important. Knowing the expected input format for a command means you can format your
                                            data correctly</li>
                                    <li>Being able to easily view and manipulate text files becomes crucial for a productive data scientist</li>
                                </ol>
                            </p>

                            <p>
                                We'll learn some common bioinformatics data formats in this workshop and throughout ConGen, but for now let's
                                focus on point 2: viewing and manipulating text with text editors
                            </p>

                        </div>
                        <div class="col-2-24" id="inner-margin"></div>
                    </div>
                </div>
            </div>

            <a class="internal-link" name="text-editors"></a>
            <div class="row" id="section-header-cont">
                <div class="col-24-24" id="section-header-row">
                    <div id="section-header">Text editors</div>
                </div>
            </div>

            <div class="row" id="section-cont">
                <div class="col-24-24" id="section-col">
                    <div class="row" id="section-row">
                        <div class="col-2-24" id="inner-margin"></div>
                        <div class="col-20-24" id="section-content">
                            <p>
                                There are many programs you could use as a text editor, ranging from the most basic text editing capabilities, to full blown
                                integrated development environments (IDEs) with syntax highlighting for different languages, remote syncing, git integration
                                and so on.
                            </p>

                            <p>
                                The RStudio interface we're using right now is an example of an IDE, centered around the R programming language, and contains
                                it's own text editor.
                            </p>

                            <div class="row" id="img-row">
                                <!-- <div class="col-4-24" id="margin"></div> -->
                                <div class="col-24-24" id="img-col">
                                    <img id="res-img" src="img/rstudio-editor.png">
                                    <center><span class="fig-caption">Figure 3.2: The text editor in your Rstudio interface is highlighted in the orange box.</span></center>
                                </div>
                                <!-- <div class="col-4-24" id="margin"></div> -->
                            </div>

                            <p>
                                Text editors are also available within Linux terminals themselves, in the form of programs such as <code class="inline">nano</code>,
                                <code class="inline">Emacs</code>, or <code class="inline">vim</code>. See <a href="programs.html">this table</a> for a list of some 
                                text editors. You should find one that suits your style to make you a more productive bioinformatician.
                            </p>

                            <p>
                                After years of trying many of the options listed in the table, I have settled on VScode as my text editor. It provides many of the 
                                capabilities of an IDE, but keeps true to it's basic function: editing text. The remote addon has also been a gamechanger for editing
                                files on remote servers.
                            </p>

                        </div>
                        <div class="col-2-24" id="inner-margin"></div>
                    </div>
                </div>
            </div>

            <a class="internal-link" name="philosophy"></a>
            <div class="row" id="section-header-cont">
                <div class="col-24-24" id="section-header-row">
                    <div id="section-header">The Unix philosophy</div>
                </div>
            </div>

            <div class="row" id="section-cont">
                <div class="col-24-24" id="section-col">
                    <div class="row" id="section-row">
                        <div class="col-2-24" id="inner-margin"></div>
                        <div class="col-20-24" id="section-content">
                            <p>
                                The last conceptual topic I want to discuss is the philosophy for command development, which leads nicely into
                                our activities.
                            </p>

                            <p>
                                In the late 1970's as the Unix operating system was being developed, the software engineers settled on a set of norms for the programs
                                they wrote. Their philosophy basically boiled down to two things, for our purposes:

                                <ol>
                                    <li>Write a program that does one thing and does that thing really well</li>
                                    <li>Write programs that can work with each other -- the output of one program should become the input of another.</li>
                                </ol>
                            </p>

                            <p>
                                This is opposed to other software design philosophies, for instance Microsoft, which designs software to do one thing well,
                                but also gives that software to ability to do numerous other things, maybe not optimally. For example, the primary purpose
                                of Microsoft Word is word processing -- writing and formatting text. But within work you can also make tables, edit images,
                                and a plethora of other things that have little to do directly with word processing.
                            </p>

                            <div class="row" id="img-row">
                                <!-- <div class="col-4-24" id="margin"></div> -->
                                <div class="col-24-24" id="img-col">
                                    <img id="res-img" src="img/philosophies.png">
                                    <center><span class="fig-caption">Figure 3.3. Screenshots of a Unix-based program (<code class="inline">ls</code>; top) and
                                        a Microsoft program (Word).</span></center>
                                </div>
                                <!-- <div class="col-4-24" id="margin"></div> -->
                            </div>

                            <p>
                                This does not mean that Unix commands lack versatility. They often have input options that you can read about using the
                                <code class="inline">man</code> (manual) command. For instance, by typing <code class="inline">man ls</code>, you will bring up
                                a screen that shows all of ls's options. The main thing to notice is that these options all work towards the main goal of the 
                                <code class="inline">ls</code> program: listing directory contents to the screen.
                            </p>

                            <p>
                                You can read more about the Unix philosophy <a href="https://en.wikipedia.org/wiki/Unix_philosophy" target="_blank">here</a>.
                            </p>

                        </div>
                        <div class="col-2-24" id="inner-margin"></div>
                    </div>
                </div>
            </div>

            <a class="internal-link" name="pipe-redirect"></a>
            <div class="row" id="section-header-cont">
                <div class="col-24-24" id="section-header-row">
                    <div id="section-header">Piping and redirecting command output</div>
                </div>
            </div>

            <div class="row" id="section-cont">
                <div class="col-24-24" id="section-col">
                    <div class="row" id="section-row">
                        <div class="col-2-24" id="inner-margin"></div>
                        <div class="col-20-24" id="section-content">
                            <p>
                                The second point of the Unix philosophy leads us to a couple of powerful ways for manipulating text from the command line:
                                <b>piping</b> and <b>redirecting</b> text output from a command.
                            </p>

                            <p>
                                Piping output from one command to another is done with the vertical bar character (<code class="inline">|</code>). By default,
                                most Unix commands print their output directly to the screen. What the pipe says is that, instead of printing the output to the screen,
                                use that output as the input of another command. For instance, we know that <code class="inline">ls</code> lists the contents of a
                                directory by printing them to the screen. But what if we're searching for a specific file? Well we could <b>pipe</b> the output from
                                <code class="inline">ls</code> to our string search program, <code class="inline">grep</code>:
                            </p>

                            <center><pre class="cmd-ne"><code>ls | grep "interesting-filename"</code></pre></center>

                            <div class="table-cont">
                                <table class="cmd-table">
                                    <thead><th class="tcol-1">Command line parameter</th><th class="tcol-2">Description</th></thead>
                                    <tr>
                                        <td class="tcol-1"</td>ls<td class="tcol-2">The Linux list directory contents command. With no path specified,
                                            this lists the contents of the current directory.</td>
                                    </tr>
                                    <tr>
                                        <td class="tcol-1">|</td><td class="tcol-2">The pipe character, telling the shell to use the output from the 
                                            previous command as the input to the next command.</td>
                                    </tr>
                                    <tr>
                                        <td class="tcol-1">grep</td><td class="tcol-2">A Linux string search and pattern matching command that takes
                                            as input a file or stream from a pipe and searches for a given string.</td>
                                    </tr>
                                    <tr>
                                        <td class="tcol-1">"interesting-filename"</td><td class="tcol-2">The string we want grep to search for in the given input.</td>
                                    </tr>
                                </table>
                            </div>

                            <p>
                                Now we would expect only files with the string "interesting-filename" in them to be printed to the screen, because we've piped our
                                <code class="inline">ls</code> output to <code class="inline">grep</code>.
                            </p>

                            <p><b>Redirecting</b> command output is another essential command line function, and is accomplished with the greater than
                                character (<code class="inline">></code>). Redirecting takes the output that would have been printed to the screen and instead
                                writes it to a specified file. For instance, if we want to save contents of our current directory to a file, we could run:
                            </p>

                            <center><pre class="cmd-ne"><code>ls > dir-contents.txt</code></pre></center>

                            <div class="table-cont">
                                <table class="cmd-table">
                                    <thead><th class="tcol-1">Command line parameter</th><th class="tcol-2">Description</th></thead>
                                    <tr>
                                        <td class="tcol-1"</td>ls<td class="tcol-2">The Linux list directory contents command. With no path specified,
                                            this lists the contents of the current directory.</td>
                                    </tr>
                                    <tr>
                                        <td class="tcol-1">></td><td class="tcol-2">The redirect character, telling the shell to save the output from the 
                                            previous command to the specified file.</td>
                                    </tr>
                                    <tr>
                                        <td class="tcol-1">dir-contents.txt</td><td class="tcol-2">The file we want to save the output to.</td>
                                    </tr>
                                </table>
                            </div>                           

                            <p>
                                Now, if we were to open the file <code class="inline">dir-contents.txt</code> in our favorite text editor, we would see
                                the list of files saved there.
                            </p>

                            <p>
                                <b>Piping</b> and <b>redirecting</b> can be used in conjunction with each other:
                            </p>

                            <center><pre class="cmd-ne"><code>ls | grep "interesting-filename" > interesting-dir-contents.txt</code></pre></center>

                            <div class="table-cont">
                                <table class="cmd-table">
                                    <thead><th class="tcol-1">Command line parameter</th><th class="tcol-2">Description</th></thead>
                                    <tr>
                                        <td class="tcol-1"</td>ls<td class="tcol-2">The Linux list directory contents command. With no path specified,
                                            this lists the contents of the current directory.</td>
                                    </tr>
                                    <tr>
                                        <td class="tcol-1">|</td><td class="tcol-2">The pipe character, telling the shell to use the output from the 
                                            previous command as the input to the next command.</td>
                                    </tr>
                                    <tr>
                                        <td class="tcol-1">grep</td><td class="tcol-2">A Linux string search and pattern matching command that takes
                                            as input a file or stream from a pipe and searches for a given string.</td>
                                    </tr>
                                    <tr>
                                        <td class="tcol-1">"interesting-filename"</td><td class="tcol-2">The string we want grep to search for in the given input.</td>
                                    </tr>
                                    <tr>
                                        <td class="tcol-1">></td><td class="tcol-2">The redirect character, telling the shell to save the output from the 
                                            previous command to the specified file.</td>
                                    </tr>
                                    <tr>
                                        <td class="tcol-1">interesting-dir-contents.txt</td><td class="tcol-2">The file we want to save the output to.</td>
                                    </tr>
                                </table>
                            </div>                            

                            <p>
                                Now we've taken the output from <code class="inline">ls</code>, piped it to <code class="inline">grep</code> to search for filenames
                                containing a string, and redirected that output to a file called <code class="inline">interesting-dir-contents.txt</code>. If we were
                                to open this file we'd see only the files in the current directory that have the string "interesting-file" in their name.
                            </p>

                            <p>
                                Also of note, you are not limited in the number of pipes you can do. This means that you could start with text input in a file
                                and process it with several commands via piping to drastically change the information that is output. It is an extremely powerful
                                method of <b>scripting</b>!
                            </p>

                            <div id="msg_cont">
                                <div id="msg">
                                    <div id="warn_banner">Warning! Redirecting to a file overwrites that file!</div>
                                    <div id="warn_text">
                                        <p>
                                            You should be aware that if you redirect with <code class="inline">></code> to an existing file that the contents of that
                                            file will be overwritten <b>without warning!</b> 
                                        </p>

                                        <p>
                                            If you have a file you want to redirect output to without overwriting, use two redirect characters in order to <b>append</b> to 
                                            the file:
                                        </p>

                                        <center><code class="inline">ls &gt;&gt; dir-contents.txt</code></center>
                                        <p></p>
                                    </div>
                                </div>
                            </div>

                            <p>
                                Now that we have the conceptual basics of commands reviewed, we'll put these in practice by analyzing some biological 
                                data from the command line!
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
                <a href="organization.html">&lt;&nbsp;Previous</a>    
            </div>
        </div>
        <div class="col-6-24" id="nav-margin"></div>
        <div class="col-6-24" id="nav-btn-cont">
            <div class="nav-btn">
                <a href="macaque-svs.html">Next&nbsp;&gt;</a>
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
pagefile = "commands.html";
print("Generating " + pagefile + "...");
title = "ConGen2021 - Intro to Bioinformatics"

head = RC.readHead(title);
nav = RC.readNav(pagefile);
banner = RC.readPrevBanner("2021", "bioinformatics");
footer = RC.readFooter();

outfilename = "../../" + pagefile;

with open(outfilename, "w") as outfile:
    outfile.write(html_template.format(head=head, nav=nav, banner=banner, footer=footer));