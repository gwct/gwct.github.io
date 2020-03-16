############################################################
# For Good lab Griz docs, 03.2020
# Generates "nodes.html"
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
	<div class="pure-u-24-24" id="header">Good lab Griz cluster docs &mdash; Node info</div>

	{nav}

	<div class="pure-u-24-24" id="server_sep_div"></div>
		<div class="pure-g" id="griz_head_row">
			<div class="pure-u-4-24" id="margin"></div>
			<div class="pure-u-4-24" id="griz_img_cont">
				<img class="pure-img" id="griz_img" src="../img/logo/griz.png">
			</div>

		<div class="pure-u-12-24" id="griz_title">
			<h1>Compute node info</h1>
		</div>
		<div class="pure-u-4-24" id="margin"></div>
	</div>

	<div class="pure-g" id="griz_main_div">
		<div class="pure-u-24-24" id="server_sep_div"></div>
		<div class="pure-u-2-24" id="margin"></div>
		<div class="pure-u-20-24" id="griz_main_row">

		<div class="pure-g">
			<div class="pure-u-2-24" id="margin"></div>
			<div class="pure-u-20-24" id="server_row">
				<div id="griz_node_desc">

					<h3>We have several classes of compute nodes currently available to us. Use the <code>sinfo</code> command to monitor usage and availability.</h3>

					<table id="sum-tab">
						<tr><td class="td-label">Partition: </td><td>good_lab_cpu</td></tr>
						<tr><td class="td-label"># nodes</td><td>8</td></tr>
						<tr><td class="td-label">Name: </td><td>compute-0-[1-8]</td></tr>
						<tr><td class="td-label">Operating System: </td><td>CentOS Linux release 7.4.1708</td></tr>
						<tr><td class="td-label">Processors: </td>
							<td>
								<b>72 threads: </b>
								<a href="https://ark.intel.com/content/www/us/en/ark/products/120490/intel-xeon-gold-6150-processor-24-75m-cache-2-70-ghz.html" target="_blank">
									Intel(R) Xeon(R) Gold 6150 CPU @ 2.70 GHz</a> (2 CPU x 18 cores per CPU x 2 threads per core)
							</td>
						</tr>
						<tr><td class="td-label">Memory: </td><td>790GB</td></tr>
						<!-- <tr><td class="td-label">Storage:</td><td>200GB</td></tr> -->
					</table>			
					<!-- good_lab_cpu -->

					<table id="sum-tab">
						<tr><td class="td-label">Partition: </td><td>good_lab_large_cpu</td></tr>
						<tr><td class="td-label"># nodes</td><td>??</td></tr>
						<tr><td class="td-label">Name: </td><td>??</td></tr>
						<tr><td class="td-label">Operating System: </td><td>CentOS Linux release 7.4.1708</td></tr>
						<tr><td class="td-label">Processors: </td>
							<td>
								<b>36 threads: </b>
								<a href="https://ark.intel.com/content/www/us/en/ark/products/192443/intel-xeon-gold-6240-processor-24-75m-cache-2-60-ghz.html" target="_blank">
									Intel(R) Xeon(R) Gold 6240 CPU @ 2.60GHz</a> (1 CPU x 8 cores per CPU x 2 threads per core)
							</td>
						</tr>
						<tr><td class="td-label">Memory: </td><td>512GB</td></tr>
						<!-- <tr><td class="td-label">Storage:</td><td>200GB</td></tr> -->
					</table>
					<!-- good_lab_large_cpu -->

					<table id="sum-tab">
						<tr><td class="td-label">Partition: </td><td>good_lab_small_cpu</td></tr>
						<tr><td class="td-label"># nodes</td><td>4</td></tr>
						<tr><td class="td-label">Name: </td><td>compute-0-[9-12]</td></tr>
						<tr><td class="td-label">Operating System: </td><td>CentOS Linux release 7.4.1708</td></tr>
						<tr><td class="td-label">Processors: </td>
							<td>
								<b>32 threads: </b>
								<a href="https://ark.intel.com/content/www/us/en/ark/products/92986/intel-xeon-processor-e5-2620-v4-20m-cache-2-10-ghz.html" target="_blank">
									Intel(R) Xeon(R) CPU E5-2620 v4 @ 2.10GHz</a> (1 CPU x 18 cores per CPU x 2 threads per core)
							</td>
						</tr>
						<tr><td class="td-label">Memory: </td><td>264GB</td></tr>
						<!-- <tr><td class="td-label">Storage:</td><td>200GB</td></tr> -->
					</table>
					<!-- good_lab_small_cpu -->

					<table id="sum-tab">
						<tr><td class="td-label">Partition: </td><td>good_lab_gpu</td></tr>
						<tr><td class="td-label"># nodes</td><td>8</td></tr>
						<tr><td class="td-label">Name: </td><td>compute-1-[5-12]</td></tr>
						<tr><td class="td-label">Operating System: </td><td>CentOS Linux release 7.4.1708</td></tr>
						<tr><td class="td-label">Processors: </td>
							<td>
								<b>36 threads: </b>
								<a href="https://ark.intel.com/content/www/us/en/ark/products/192443/intel-xeon-gold-6240-processor-24-75m-cache-2-60-ghz.html" target="_blank">
									Intel(R) Xeon(R) Gold 6240 CPU @ 2.60GHz</a> (1 CPU x 8 cores per CPU x 2 threads per core)
							</td>
						</tr>
						<tr><td class="td-label">GPU: </td>
							<td>
								<b>4 GPU per node: </b>
								<a href="https://www.techpowerup.com/gpu-specs/geforce-rtx-2080-ti.c3305" target="_blank">
									NVIDIA RTX 2080Ti</a>
							</td>
						</tr>
						<tr><td class="td-label">Memory: </td><td>512GB</td></tr>
						<!-- <tr><td class="td-label">Storage:</td><td>200GB</td></tr> -->
					</table>
					<!-- good_lab_gpu -->

					<table id="sum-tab">
						<tr><td class="td-label">Partition: </td><td>good_lab_reincarnation</td></tr>
						<tr><td class="td-label"># nodes</td><td>1</td></tr>
						<tr><td class="td-label">Name: </td><td>compute-2-1</td></tr>
						<tr><td class="td-label">Operating System: </td><td>??</td></tr>
						<tr><td class="td-label">Processors: </td>
							<td>
								<b>32 threads: </b>
								<a href="" target="_blank">
									</a> (1 CPU x 18 cores per CPU x 2 threads per core)
							</td>
						</tr>
						<tr><td class="td-label">Memory: </td><td>2TB</td></tr>
						<!-- <tr><td class="td-label">Storage:</td><td>200GB</td></tr> -->
					</table>
					<!-- good_lab_reincarnation -->

				</div>
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
pagefile = "nodes.html";
print("Generating " + pagefile + "...");
title = "Griz node info"

head = RC.readHead(title, pagefile);
nav = RC.readNav(pagefile);
footer = RC.readFooter();

outfilename = "../../" + pagefile;

with open(outfilename, "w") as outfile:
    outfile.write(html_template.format(head=head, nav=nav, footer=footer));