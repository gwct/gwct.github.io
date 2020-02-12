############################################################
# For personal site, 11.19
# This generates the file "archive.html"
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


    <div class="pure-g" id="main_div_links">
	<div class="pure-u-24-24" id="header">Good lab computational resources</div>
		<div class="pure-u-24-24" id="sep_div"></div>
		<div class="pure-u-2-24" id="margin"></div>
		<div class="pure-u-20-24" id="link_text">
			<!-- <div class="pure-g" id="line_cont"><div class="pure-u-24-24" id="line"></div></div> -->
			<!-- <div class="section_header_cont"><div class="section_header">My Software</div></div> -->
				<div class="pure-g">
					<div class="pure-u-2-24" id="margin"></div>
					<div class="pure-u-20-24" id="server_row">
						<div id="server_img_cont">
							<img class="pure-img" id="server_img" src="img/logo/musculus.png">
						</div>
						<div id="server_desc">
							<h3>Musculus (musculus.dbs.umt.edu:22)</h3>

							<table id="sum-tab">
								<tr><td class="td-label">Access: </td class="td-label"><td>Good lab</td></tr>
								<tr><td class="td-label">Operating System: </td class="td-label"><td>Linux version 4.4.0-135-generic</td></tr>
								<tr><td class="td-label">Processor: </td class="td-label"><td>Intel Xeon Processor E5-2650 @ 2GHz (8 cores, 16 threads)</td></tr>
								<tr><td class="td-label">Memory: </td class="td-label"><td>200GB</td></tr>
								<tr><td class="td-label">Storage:</td class="td-label"><td>One 40TB HDD containing one partition and several logical volumes</td></tr>
							</table>

							<center>
							<table id="vol-tab">
								<thead><th>Volume name</th><th>Path</th><th>Capactity</th></thead>
								<tr><td><em>home</em></td><td>/home</td><td>3TB</td></tr>
								<tr><td><em>data</em></td><td>/data</td><td>15TB</td></tr>
								<tr><td><em>scratch</em></td><td>/scratch/1</td><td>10TB</td></tr>
								<tr><td><em>morescratch</em></td><td>/scratch/2</td><td>2TB</td></tr>
							</table>
							</center>
						</div>
					</div>
					<div class="pure-u-2-24" id="margin"></div>
				</div>

				<div class="pure-u-24-24" id="sep_div"></div>

				<div class="pure-g">
					<div class="pure-u-2-24" id="margin"></div>
					<div class="pure-u-20-24" id="server_row">
						<div id="server_img_cont">
							<img class="pure-img" id="server_img" src="img/logo/lepus.png">
						</div>
						<div id="server_desc">
							<h3>Lepus (lepus.dbs.umt.edu:22)</h3>

							<table id="sum-tab">
								<tr><td class="td-label">Access: </td class="td-label"><td>Good lab</td></tr>
								<tr><td class="td-label">Operating System: </td class="td-label"><td>Linux version 4.4.0-109-generic</td></tr>
								<tr><td class="td-label">Processor: </td class="td-label"><td>Intel Xeon Processor E5-2650 @ 2GHz (8 cores, 16 threads)</td></tr>
								<tr><td class="td-label">Memory: </td class="td-label"><td>200GB</td></tr>
								<tr><td class="td-label">Storage:</td class="td-label">
									<td>
										One 12TB HDD containing several partitions, including the OS</br>
										One 12TB HDD containing one partition</br>
										One 4TB HDD containing one partition</br>
										One 4TB HDD containing one partition</br>
									</td>
								</tr>
							</table>

							<center>
							<table id="vol-tab">
								<thead><th>Partition name</th><th>Path</th><th>Capactity</th></thead>
								<tr><td><em>home</em></td><td>/home</td><td>3.3TB</td></tr>
								<tr><td><em>data</em></td><td>/data</td><td>7.5TB</td></tr>
								<tr><td><em>scratch</em></td><td>/scratch/1</td><td>11TB</td></tr>
								<tr><td><em>scratch2</em></td><td>/scratch/2</td><td>3.7TB</td></tr>
								<tr><td><em>scratch3</em></td><td>/scratch/3</td><td>3.7TB</td></tr>
							</table>
							</center>
						</div>
					</div>
					<div class="pure-u-2-24" id="margin"></div>
				</div>

				<div class="pure-u-24-24" id="sep_div"></div>

				<div class="pure-g">
					<div class="pure-u-2-24" id="margin"></div>
					<div class="pure-u-20-24" id="server_row">
						<div id="server_img_cont">
							<img class="pure-img" id="server_img" src="img/logo/rat.png">
						</div>
						<div id="server_desc">
							<h3>Rat (?? -- Coming soon!)</h3>

							<table id="sum-tab">
								<tr><td class="td-label">Access: </td class="td-label"><td>Good lab</td></tr>
								<tr><td class="td-label">Operating System: </td class="td-label"><td></td></tr>
								<tr><td class="td-label">Processor: </td class="td-label"><td></td></tr>
								<tr><td class="td-label">Memory: </td class="td-label"><td></td></tr>
								<tr><td class="td-label">Storage:</td class="td-label"><td>12 HDD x 16TB (192TB) Network attached storage</td>
								</tr>
							</table>

							<!-- <center>
							<table id="vol-tab">
								<thead><th>Partition name</th><th>Path</th><th>Capactity</th></thead>
							</table>
							</center> -->
						</div>
					</div>
					<div class="pure-u-2-24" id="margin"></div>
				</div>

				<div class="pure-u-24-24" id="sep_div"></div>

				<div class="pure-g">
					<div class="pure-u-2-24" id="margin"></div>
					<div class="pure-u-20-24" id="server_row">
						<div id="server_img_cont">
							<img class="pure-img" id="server_img" src="img/logo/carnation.png">
						</div>
						<div id="server_desc">
							<h3><a href="http://hs.umt.edu/dbs/labs/genomics/bioinformatics/servers.php" target="_blank">Carnation</a> (carnation.dbs.umt.edu:2225)</h3>

							<table id="sum-tab">
								<tr><td class="td-label">Access: </td><td><a href="http://hs.umt.edu/dbs/labs/genomics/default.php" target="_blank">Genomics Core Laboratory</a></td></tr>
								<tr><td class="td-label">Operating System: </td class="td-label"><td>Linux version 4.4.0-104-generic</td></tr>
								<tr><td class="td-label">Processor: </td class="td-label"><td>4 x Intel Xeon CPU E7-8860 v3 @ 2.20GHz (64 cores, 128 threads total)</td></tr>
								<tr><td class="td-label">Memory: </td class="td-label"><td>2TB</td></tr>
								<tr><td class="td-label">Storage:</td class="td-label"><td>200TB</td></tr>
								<tr><td class="td-label">Summary:</td class="td-label"><td><a href="http://hs.umt.edu/dbs/labs/genomics/bioinformatics/servers.php" target="_blank">http://hs.umt.edu/dbs/labs/genomics/bioinformatics/servers.php</a></td></tr>
							</table>

						</div>
					</div>
					<div class="pure-u-2-24" id="margin"></div>
				</div>

				<div class="pure-u-24-24" id="sep_div"></div>

				<div class="pure-g">
					<div class="pure-u-2-24" id="margin"></div>
					<div class="pure-u-20-24" id="server_row">
						<div id="server_img_cont">
							<img class="pure-img" id="server_img" src="img/logo/reincarnation.png">
						</div>
						<div id="server_desc">
							<h3>Reincarnation (?? -- Coming soon!)</h3>

							<table id="sum-tab">
								<tr><td class="td-label">Access: </td><td><a href="http://hs.umt.edu/dbs/labs/genomics/default.php" target="_blank">Genomics Core Laboratory</a></td></tr>
								<tr><td class="td-label">Operating System: </td class="td-label"><td></td></tr>
								<tr><td class="td-label">Processor: </td class="td-label"><td></td></tr>
								<tr><td class="td-label">Memory: </td class="td-label"><td></td></tr>
								<tr><td class="td-label">Storage:</td class="td-label"><td></td></tr>
								<tr><td class="td-label">Summary:</td class="td-label"></td></tr>
							</table>

						</div>
					</div>
					<div class="pure-u-2-24" id="margin"></div>
				</div>


				<div class="pure-u-24-24" id="sep_div"></div>

				<div class="pure-g">
					<div class="pure-u-2-24" id="margin"></div>
					<div class="pure-u-20-24" id="server_row">
						<div id="server_img_cont">
							<img class="pure-img" id="server_img" src="img/logo/griz.png">
						</div>
						<div id="server_desc">
							<h3>Griz (?? -- Coming soon!)</h3>

							<table id="sum-tab">
								<tr><td class="td-label">Access: </td><td>University-wide</td></tr>
								<tr><td class="td-label">Operating System: </td class="td-label"><td></td></tr>
								<tr><td class="td-label">Processor: </td class="td-label"><td></td></tr>
								<tr><td class="td-label">Memory: </td class="td-label"><td></td></tr>
								<tr><td class="td-label">Storage:</td class="td-label"><td></td></tr>
								<tr><td class="td-label">Summary:</td class="td-label"></td></tr>
							</table>

						</div>
					</div>
					<div class="pure-u-2-24" id="margin"></div>
				</div>

			</div>
		</div>

		<div class="pure-u-24-24" id="sep_div"></div>

    {footer}
</body>
"""

######################
# Main block
######################
pagefile = "servers.html";
print("Generating " + pagefile + "...");
title = "Good lab - Servers"

head = RC.readHead(title, pagefile);
footer = RC.readFooter();

outfilename = "../../" + pagefile;

with open(outfilename, "w") as outfile:
    outfile.write(html_template.format(head=head, footer=footer));