############################################################
# For ConGen2020 site, 08.20
# This generates the file "terms.html"
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

    <a class="internal-link" name="terms"></a>
    <div class="row" id="header">Terminology & File Formats</div>

    <div class="row" id="body-row">
        <div class="col-3-24" id="side-nav-cont">
            <div id="side-nav">
                <span id="side-header">Page contents</span>
                <ul>
                    <li><a href="terms.html#terms">Term definitions</a></li>
                    <li><a href="terms.html#formats">Common file formats</a></li>
                </ul>
            </div>
        </div>

        <div class="col-21-24" id="main-cont">
            <div class="row" id="top-row-cont">
                <div class="col-24-24" id="top-row"></div>
            </div>
            <div class="row" id="section-header-cont">
                <div class="col-24-24" id="section-header-row">
                    <div id="section-header">Definitions of frequently used terms</div>
                </div>
            </div>
            <div class="row" id="section-cont">
                <div class="col-24-24" id="section-col">
                    <div class="row" id="section-row">
                        <div class="col-2-24" id="inner-margin"></div>
                        <div class="col-20-24" id="section-content">

                            {terms_table}
                            <div id="sep_div"></div>

                        </div>
                        <div class="col-2-24" id="inner-margin"></div>
                    </div>
                </div>
            </div>

            <a class="internal-links" name="formats"></a>
            <div class="row" id="section-header-cont">
                <div class="col-24-24" id="section-header-row">
                    <div id="section-header">File formats</div>
                </div>
            </div>
            <div class="row" id="section-cont">
                <div class="col-24-24" id="section-col">
                    <div class="row" id="section-row">
                        <div class="col-2-24" id="inner-margin"></div>
                        <div class="col-20-24" id="section-content">

                            {formats_table}
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
pagefile = "terms.html";
print("Generating " + pagefile + "...");
title = "ConGen2020 - Assembly Workshop"

head = RC.readHead(title);
nav = RC.readNav(pagefile);
footer = RC.readFooter();

tables = {'terms' : "../../data/terms.csv", 'formats' : "../../data/formats.csv" };

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
                    if cur_col == "NA":
                        cur_rows += "<td>NA</td>"
                    else:
                        cur_rows += "<td><a href='" + cur_col + "' target='_blank'>Wikipedia</a></td>";
                elif cur_header == "Specs":
                    if cur_col == "NA":
                        cur_rows += "<td>NA</td>"
                    else:
                        cur_rows += "<td><a href='" + cur_col + "' target='_blank'>Link</a></td>";
                else:
                    if c == 0:
                        cur_rows += "<td><b>" + cur_col + "</b></td>";
                    else:
                        cur_rows += "<td>" + cur_col + "</td>";
            cur_rows += "</tr>";
            # Go through columns in rows to add <td> tags.

        if table == "terms":
            terms_table = table_template.format(table_rows=cur_rows);
        elif table == "formats":
            formats_table = table_template.format(table_rows=cur_rows);


outfilename = "../../" + pagefile;

with open(outfilename, "w") as outfile:
    outfile.write(html_template.format(head=head, nav=nav, terms_table=terms_table, formats_table=formats_table, footer=footer));