############################################################
# For ConGen2020 site, 08.20
# This generates the file "programs.html"
############################################################

import sys, os, csv
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

    <a class="internal-link" name="top"></a>
    <div class="row" id="header">Genomics programs</div>

    <div class="row" id="body-row">
        <div class="col-3-24" id="side-nav-cont">
            <div id="side-nav">
                <span id="side-header">Page contents</span>
                <ul>
                    <li><a href="programs.html#top">Intro</a></li>
                    <li><a href="programs.html#asm-table">Genome assembly programs</a></li>
                    <li><a href="programs.html#map-table">Read mapping programs</a></li>
                    <li><a href="programs.html#var-table">Single-nucleotide variant callers</a></li>
                    <li><a href="programs.html#other-table">Other helpful programs</a></li>
                </ul>
            </div>
        </div>

        <div class="col-21-24" id="main-cont">
            <div class="row" id="section-cont">
                <div class="col-24-24" id="section-col">
                    <div class="row" id="section-row">
                        <div class="col-2-24" id="inner-margin"></div>
                        <div class="col-20-24" id="section-content">

                            <p>Here is a list of programs used in the genome assembly and variant calling process. Very basic information is provided about each program. 
                                Check the paper and program documentation links for more extensive information. If you feel any information is inaccurate or out of date,
                                or if you want to recommend a program to add to the lists, please contact <a href="https://gwct.github.io/" target="_blank">me</a>.
                            </p>

                            <p>Programs listed with a <span id="used-prog">GREEN BACKGROUND</span> are ones used in this class.</p>
                    
                        </div>
                        <div class="col-2-24" id="inner-margin"></div>
                    </div>
                </div>
            </div>

            <a class="internal-link" name="asm-table"></a>
            <div class="row" id="section-header-cont">
                <div class="col-24-24" id="section-header-row">
                    <div id="section-header">Genome assembly programs</div>
                </div>
            </div>
            <div class="row" id="section-cont">
                <div class="col-24-24" id="section-col">
                    <div class="row" id="section-row">
                        <div class="col-2-24" id="inner-margin"></div>
                        <div class="col-20-24" id="section-content">

                            {asm_table}
                            <div id="sep_div"></div>

                        </div>
                        <div class="col-2-24" id="inner-margin"></div>
                    </div>
                </div>
            </div>

            <a class="internal-link" name="map-table"></a>
            <div class="row" id="section-header-cont">
                <div class="col-24-24" id="section-header-row">
                    <div id="section-header">Read mapping programs</div>
                </div>
            </div>
            <div class="row" id="section-cont">
                <div class="col-24-24" id="section-col">
                    <div class="row" id="section-row">
                        <div class="col-2-24" id="inner-margin"></div>
                        <div class="col-20-24" id="section-content">

                            {map_table}
                            <div id="sep_div"></div>

                        </div>
                        <div class="col-2-24" id="inner-margin"></div>
                    </div>
                </div>
            </div>

            <a class="internal-link" name="var-table"></a>
            <div class="row" id="section-header-cont">
                <div class="col-24-24" id="section-header-row">
                    <div id="section-header">Single-nucleotide variant calling programs</div>
                </div>
            </div>
            <div class="row" id="section-cont">
                <div class="col-24-24" id="section-col">
                    <div class="row" id="section-row">
                        <div class="col-2-24" id="inner-margin"></div>
                        <div class="col-20-24" id="section-content">

                            {var_table}
                            <div id="sep_div"></div>

                        </div>
                        <div class="col-2-24" id="inner-margin"></div>
                    </div>
                </div>
            </div>

            <a class="internal-link" name="other-table"></a>
            <div class="row" id="section-header-cont">
                <div class="col-24-24" id="section-header-row">
                    <div id="section-header">Other helpful programs</div>
                </div>
            </div>
            <div class="row" id="section-cont">
                <div class="col-24-24" id="section-col">
                    <div class="row" id="section-row">
                        <div class="col-2-24" id="inner-margin"></div>
                        <div class="col-20-24" id="section-content">

                            {other_table}
                            <div id="sep_div"></div>

                        </div>
                        <div class="col-2-24" id="inner-margin"></div>
                    </div>
                </div>
            </div>
        
        </div>
    </div>

    {footer}
</body>
"""

table_template = """
<div class="table-cont">
    <table class="prog-table">
        {table_rows}
    </table>
</div>
"""

######################
# Main block
######################
pagefile = "programs.html";
print("Generating " + pagefile + "...");
title = "UVU Genomics - Programs"

head = RC.readHead(title);
nav = RC.readNav(pagefile);
footer = RC.readFooter();

tables = {'asm' : "../../data/assemblers.csv", 'map' : "../../data/mappers.csv", 'var' : "../../data/varcallers.csv", 'other' : "../../data/other.csv" };

#asm_file, map_file, var_file, other_file = "../../data/assemblers.csv", "../../data/mappers.csv", "../../data/varcallers.csv", "../../data/other.csv"
for table in tables:
    #print(table);
    cur_rows, headers = "",  [];
    first = True;
    with open(tables[table]) as csvfile:
        table_reader = csv.reader(csvfile);
        for line in table_reader:
            if first:
                cur_rows += "<thead>";
                for col in line:
                    headers.append(col);
                    if col == "Used":
                        continue;
                    cur_rows += "<th>" + col + "</th>";
                cur_rows += "</thead>";
                first = False
                #print(headers);
                continue;
            # Get the header lines and add the <th> tags.

            #print(line);
            if line[-1] == "Y":
                cur_rows += "<tr id='used-prog'>";
            else:
                cur_rows += "<tr>";
            for c in range(len(line)):
                cur_header = headers[c];
                cur_col = line[c];
                cur_col = cur_col.replace('"', '');

                if cur_header == "Used":
                    continue;

                if cur_header == "Link":
                    cur_rows += "<td><a href='" + cur_col + "' target='_blank'>Website</a></td>";
                elif cur_header == "Paper":
                    cur_rows += "<td><a href='" + cur_col + "' target='_blank'>Paper</a></td>";
                else:
                    cur_rows += "<td>" + cur_col + "</td>";
            cur_rows += "</tr>";
            # Go through columns in rows to add <td> tags.

        if table == "asm":
            asm_table = table_template.format(table_rows=cur_rows);
        elif table == "map":
            map_table = table_template.format(table_rows=cur_rows);
        elif table == "var":
            var_table = table_template.format(table_rows=cur_rows);
        elif table == "other":
            other_table = table_template.format(table_rows=cur_rows);

outfilename = "../../" + pagefile;

with open(outfilename, "w") as outfile:
    outfile.write(html_template.format(head=head, nav=nav, asm_table=asm_table, map_table=map_table, var_table=var_table, other_table=other_table, footer=footer));