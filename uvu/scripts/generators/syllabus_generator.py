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

    <a class="internal-link" name="schedule"></a>
   	<div class="row" id="header">Genomics Syllabus</div>

    <div class="row" id="body-row">
        <div class="col-3-24" id="side-nav-cont">
            <div id="side-nav">
                <span id="side-header">Page contents</span>
                <ul>
                    <li><a href="syllabus.html#schedule">Topics & Schedule</a></li>
                    <li><a href="syllabus.html#materials">Course Materials</a></li>
                    <li><a href="syllabus.html#assess">Assessments & Evaluation</a></li>
                    <li><a href="syllabus.html#policies">Course Policies</a></li>
                    <li><a href="syllabus.html#attendance">Attendance</a></li>
                    <li><a href="syllabus.html#acad-integrity">Academic Honesty & Integrity</a></li>
                    <li><a href="syllabus.html#accomodations">Accomodations for Disabilities</a></li>
                    <li><a href="syllabus.html#inclusivity">Inclusivity in the Classroom</a></li>
                    <li><a href="syllabus.html#office-hours">Office Hours</a></li>
                </ul>
            </div>
        </div>

        <div class="col-21-24" id="main-cont">

            <div class="row" id="top-row-cont">
                <div class="col-24-24" id="top-row"></div>
            </div>
            <div class="row" id="section-header-cont">
                <div class="col-24-24" id="section-header-row">
                    <div id="section-header">Course Topics & Schedule</div>
                </div>
            </div>

            <div class="row" id="section-cont">
                <div class="col-24-24" id="section-col">
                    <div class="row" id="section-row">
                        <div class="col-2-24" id="inner-margin"></div>
                        <div class="col-20-24" id="section-content">
                            <div class="table-cont">
                                <table class="main-table">
                                    <thead><th class="tcol-1">Week</th><th class="tcol-2">Topic</th><th class="tcol-2">Assignment</th></thead>
                                    <tr>
                                        <td class="tcol-1">1</td>
                                        <td class="tcol-2">Introduction and review</td>
                                        <td class="tcol-2">Resource check and syllabus scavenger hunt</td>
                                    </tr>

                                    <tr>
                                        <td class="tcol-1">2</td>
                                        <td class="tcol-2">Review of Python and R</td>
                                        <td class="tcol-2">Python coding assignment</td>
                                    </tr>

                                    <tr>
                                        <td class="tcol-1">3</td>
                                        <td class="tcol-2">Sequencing</td>
                                        <td class="tcol-2">Review of R</td>
                                    </tr>

                                    <tr>
                                        <td class="tcol-1">4</td>
                                        <td class="tcol-2">Sequencing</td>
                                        <td class="tcol-2">FASTQ format and assessing read quality</td>
                                    </tr>

                                    <tr>
                                        <td class="tcol-1">5</td>
                                        <td class="tcol-2">Assembly</td>
                                        <td class="tcol-2">Genome assembly and assessment</td>
                                    </tr>

                                    <tr>
                                        <td class="tcol-1">6</td>
                                        <td class="tcol-2">Assembly</td>
                                        <td class="tcol-2">Transcriptome and Exome assembly</td>
                                    </tr>

                                    <tr>
                                        <td class="tcol-1">7</td>
                                        <td class="tcol-2">Alignment and read mapping</td>
                                        <td class="tcol-2">Smith-Waterman algorithm and dynamic programming</td>
                                    </tr>

                                    <tr>
                                        <td class="tcol-1">8</td>
                                        <td class="tcol-2">Alignment and read mapping</td>
                                        <td class="tcol-2">Burrows-wheeler transform</td>
                                    </tr>

                                    <tr>
                                        <td class="tcol-1">9</td>
                                        <td class="tcol-2">Annotation and gene prediction</td>
                                        <td class="tcol-2">Parsing GFF/GTF files</td>
                                    </tr>

                                    <tr>
                                        <td class="tcol-1">10</td>
                                        <td class="tcol-2">Orthology prediction/clustering</td>
                                        <td class="tcol-2">Using public databases (OrthoDB, Ensembl)</td>
                                    </tr>

                                    <tr>
                                        <td class="tcol-1">11</td>
                                        <td class="tcol-2">Multiple sequence alignment</td>
                                        <td class="tcol-2">Running MSA and assessing alignments</td>
                                    </tr>

                                    <tr>
                                        <td class="tcol-1">12</td>
                                        <td class="tcol-2">Phylogenetics</td>
                                        <td class="tcol-2">Building neighbor-joining, maximum likelihood trees</td>
                                    </tr>

                                    <tr>
                                        <td class="tcol-1">13</td>
                                        <td class="tcol-2">Phylogenetics</td>
                                        <td class="tcol-2">Bayesian phylogenetics</td>
                                    </tr>

                                    <tr>
                                        <td class="tcol-1">14</td>
                                        <td class="tcol-2">Variant calling</td>
                                        <td class="tcol-2">Calculating genotype likelihoods</td>
                                    </tr>

                                    <tr>
                                        <td class="tcol-1">15</td>
                                        <td class="tcol-2">Scans for selection</td>
                                        <td class="tcol-2">Running HyPhy or PAML</td>
                                    </tr>

                                </table>
                            </div>

                        </div>
                        <div class="col-2-24" id="inner-margin"></div>
                    </div>
                </div>
            </div>

            <a class="internal-link" name="materials"></a>
            <div class="row" id="section-header-cont">
                <div class="col-24-24" id="section-header-row">
                    <div id="section-header">Course Materials</div>
                </div>
            </div>
            <div class="row" id="section-cont">
                <div class="col-24-24" id="section-col">
                    <div class="row" id="section-row">
                        <div class="col-2-24" id="inner-margin"></div>
                        <div class="col-20-24" id="section-content">

                            <ul>
                                <li>
                                    Access to computer labs with necessarys specifications and software to complete lab assignments will be provided.
                                </li>

                                <li>
                                    Required readings will be posted online.
                                </li>
                                
                                <li>
                                    Lecture and lab materials (including slides, worksheets, and lab activities) will be posted on this website.
                                </li>
                            </ul>

                        </div>
                        <div class="col-2-24" id="inner-margin"></div>
                    </div>
                </div>
            </div>

            <a class="internal-link" name="assess"></a>
            <div class="row" id="section-header-cont">
                <div class="col-24-24" id="section-header-row">
                    <div id="section-header">Assessments & Evaluation</div>
                </div>
            </div>
            <div class="row" id="section-cont">
                <div class="col-24-24" id="section-col">
                    <div class="row" id="section-row">
                        <div class="col-2-24" id="inner-margin"></div>
                        <div class="col-20-24" id="section-content">

                            <p>
                                Assignments will be in-lab activities, such as running a program or coding assignments. Assignments are due 
                                at the end of the week, and you may finish assignments outside of class. Some coding assignments will be completed 
                                in groups, and some coding assignment will be completed individually; each type will be clearly indicated at the 
                                top of the assignment sheet.
                            </p>

                            <div class="table-cont">
                                <table class="main-table">
                                    <thead><th class="tcol-1">Activity</th><th class="tcol-2">Description</th><th class="tcol-2">% of Final Grade</th></thead>
                                    <tr>
                                        <td class="tcol-1">Attendance and in-class participation</td>
                                        <td class="tcol-2-just">
                                            <p>
                                                Many of the methods and software we will use is presented to the scientific community in the form of 
                                                peer-reviewed publications. To gain a full understanding of these pieces of software, we will read 
                                                and discuss papers in class. Students are responsible for completing assigned readings for the week's 
                                                topic before the first session of the week.
                                            </p>
                                        </td>
                                        <td class="tcol-3">10%</td>
                                    </tr>

                                    <tr>
                                        <td class="tcol-1">Computational Assignments</td>
                                        <td class="tcol-2-just">
                                            <p>
                                                <em>Group assignments</em>: Some algorithms will be easy to implement ourselves as we develop an in-depth 
                                                understanding of the underlying methods. As coding is typically collaborative, these assignments 
                                                will be done in groups. Group members will decide among themselves how they will divide the assignment 
                                                into discrete coding tasks, where one member of each group codes a separate function. These functions 
                                                will then be combined to perform an entire operation. Examples of group coding may include the 
                                                Smith-Waterman algorithm for sequence alignment or calculating genotype likelihoods from mapped 
                                                sequence reads using Bayes theorem.
                                            </p>                                    

                                            <p>
                                                <em>Individual assignments</em>: Some methods will be too complicated to code ourselves, so we will 
                                                rely on existing software to gain experience. In these cases, students will work individually to run 
                                                the software analyze the outputs. These analyses may require students to write some pieces of code to 
                                                visualize and interpret the data, but working effectively with existing software (a valuable skill in itself) 
                                                is the primary focus.
                                            </p>

                                        </td>
                                        <td class="tcol-3">80%</td>
                                    </tr>

                                    <tr>
                                        <td class="tcol-1">Final</td>
                                        <td class="tcol-2-just">
                                            <p>
                                                The final will be a "choose your own adventure" with possible activities including (1) writing an in-depth 
                                                review paper over a topic(s) covered in class, (2) a traditional written exam covering the methods discussed 
                                                in class, (3) giving a presentation about a topic discussed in class, or (4) a custom coding or data analysis
                                                project using the methods covered in class. The goal of this strategy is to provide an accessible way for you 
                                                to demonstrate what you've learned in the class, so if you can think of other activities that accomplish that 
                                                please feel free to discuss it with me. I'd like you to have something you're really interested in for your final!
                                            </p>
                                        </td>
                                        <td class="tcol-3">10%</td>
                                    </tr>

                                </table>
                            </div>

                        </div>
                        <div class="col-2-24" id="inner-margin"></div>
                    </div>
                </div>
            </div>

            <a class="internal-link" name="policies"></a>
            <div class="row" id="section-header-cont">
                <div class="col-24-24" id="section-header-row">
                    <div id="section-header">Course Policies</div>
                </div>
            </div>
            <div class="row" id="section-cont">
                <div class="col-24-24" id="section-col">
                    <div class="row" id="section-row">
                        <div class="col-2-24" id="inner-margin"></div>
                        <div class="col-20-24" id="section-content">

                            <a class="internal-link" name="attendance"></a>
                            <h3>Attendance</h3>
                            <p>
                                Attendance at all lab sessions is required. Students will be permitted up to 2 unexcused absences without penalty (besides missing the in-class 
                                activities for the day). Students are responsible for checking the syllabus, reviewing posted course materials, and contacting classmates to determine 
                                what they missed during these absences.  Students have the opportunity to complete lab-based assignments outside of class. Keep in mind that it can be 
                                challenging to join a group assignment late, so please contact me or your classmates as soon as you know you'll be absent in order to join a group.
                            </p>

                            <p>
                                In the event of illness or emergency, students will be permitted to make-up any missed work and these absences do not count towards total absences 
                                or attendance grade. Please contact me directly if such an occasion arises to make arrangements for making up missed work.
                            </p>

                            <a class="internal-link" name="acad-integrity"></a>
                            <h3>Academic Honesty & Integrity</h3>
                            <p>
                                This course will adhere to the University's policies regarding academic honesty and integrity: [link to institution policies]
                            </p>

                            <p>
                                Additionally, we offer the following policies specific to this course:
                            </p>

                            <a class="internal-link" name="sharing-code"></a>
                            <p>
                                <b>Sharing Code:</b>
                                One of the benefits of implementing a method is developing a far more in-depth understanding than from just using or reading about it. 
                                Coding often has multiple logical paths to achieve the same goal and coming up with your own solution can further benefit your understanding 
                                of the problem. At the same time, coding is often a collaborative activity, and I encourage programmers to use all available resources including
                                classmates to solve a problem. Please feel free to discuss approaches with each other, but please do not exactly copy code outside group assignments. 
                                As such:
                            </p>

                            <ul>
                                <li>
                                    Students will not be penalized for sharing code <b>within their assigned group</b> during group work.
                                </li>

                                <li>
                                    Students <b>will</b> be penalized for copying code during individual assignments. Penalties include a grade of 0 for the 
                                    assignment that was plagiarized, and possible dismissal from the course for repeated instances of plagiarism.
                                </li>

                                <li>
                                    I find online resources such as stackoverflow or biostars extremely useful when solving both basic and advanced programming problems, and these
                                    resources are a good way to learn new techniques. Likewise, simply knowing the correct terms to search for online is a useful skill to learn. 
                                    As such, students will not be penalized for using or adapting small blocks of code found online, as long as they <b>attribute the source via a 
                                    commented link within the code</b>. However, do not copy entire assignments that you may have found online.
                                </li>
                            </ul>

                            <a class="internal-link" name="accomodations"></a>
                            <h3>Accomodations for Disabilities</h3>
                            <p>
                                As an instructor I strive to make my teaching materials as open and accessible as possible. If you are struggling in class or note any 
                                way I could improve in this area, please do not hesitate to contact me. All course materials will be posted online and any note-taking 
                                method is acceptable in class. The final project is designed to be accommodating to different learning styles
                            </p>

                            <p>
                                [link to institutional resources]
                            </p>

                            <a class="internal-link" name="inclusivity"></a>
                            <h3>Inclusivity in the Classroom</h3>
                            <p>
                                My classroom is a space of inclusion, where we welcome people from diverse backgrounds and identities. We do not tolerate discrimination 
                                based on race, nationality, ethnicity, culture, gender, sexual orientation, disability, or socio-economic status.
                            </p>

                            <p>
                                [link to institutional resources]
                            </p>

                            <a class="internal-link" name="office-hours"></a>
                            <h3>Office Hours</h3>
                            <p>
                                I will be available for office hours and am also available via email.
                            </p>

                            <div id="sep_div"></div>

                        </div>
                        <div class="col-2-24" id="inner-margin"></div>
                    </div>
                </div>
            </div>

        </div>
    </div>

    <!-- 
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
    -->

    {footer}
</body>
</html>
"""

######################
# Main block
######################
pagefile = "syllabus.html";
print("Generating " + pagefile + "...");
title = "UVU Genomics - Syllabus"

head = RC.readHead(title);
nav = RC.readNav(pagefile);
footer = RC.readFooter();

outfilename = "../../" + pagefile;

with open(outfilename, "w") as outfile:
    outfile.write(html_template.format(head=head, nav=nav, footer=footer));