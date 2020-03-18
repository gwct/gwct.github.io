############################################################
# For Good lab Griz docs, 03.2020
# Generates "start.html"
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
	<div class="pure-u-24-24" id="header">Good lab Griz cluster docs &mdash; Getting Started</div>

	{nav}

	<div class="pure-u-24-24" id="server_sep_div"></div>
	<div class="pure-g" id="griz_head_row">
		<div class="pure-u-4-24" id="margin"></div>
		<div class="pure-u-4-24" id="griz_img_cont">
			<img class="pure-img" id="griz_img" src="../img/logo/griz.png">
		</div>

		<div class="pure-u-12-24" id="griz_title">
			<h1>Logging in to Griz</h1>
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

					<p>
						Griz has two nodes to which we can login and interact with the cluster, either by ssh or FTP:
					</p>
<pre>
	Head node:	griz.gscc.umt.edu (on campus access only)
	Login node:	login.gscc.umt.edu (on campus access with off campus access available soon)
</pre>

					<p>
						Both of these nodes can be used to navigate the file system and submit jobs. Until the login node is setup for 
						off-campus access you will need to login to UM's VPN before attempting to log on to one of the log in nodes when 
						not on campus:
					</p>

					<div id="imp_link_cont">
						<a id="imp_link" href="https://www.umt.edu/it/support/vpn/default.php" target="_blank">UM VPN Docs</a>
					</div>

					<h2>SSH logins</h2>

					<div id="section_sep_top"></div>
					<div id="section_line"></div>
					<div id="section_sep_btm"></div>

					<p>
						To log in to Griz with a command line interface to navigate the file system and submit jobs, you will need an SSH client.
						On MacOS, Linux, and newer Windows installs an SSH client is pre-installed. Simply open your terminal and type:
					</p>

					<code>ssh [NetID as username]@[server name]</code>

					<p>Accept any fingerprint prompts and enter your password when prompted and you should be good to go!</p>

					<p>Explicitly, if I wanted to log in to the head node, I would type:</p>

					<code>ssh gt156213e@griz.gscc.umt.edu</code>

					<p></p>

					<div id="msg_cont">
						<div id="msg">
							<div id="rec_banner">Recommendation</div>
							<div id="rec_text">
								<p>
									Though newer versions of Windows 10 have an SSH client pre-installed, I still prefer the PuTTY SSH client:
								</p>
								<div id="imp_link_cont">
									<a id="imp_link" href="https://www.chiark.greenend.org.uk/~sgtatham/putty/latest.html" target="_blank">PuTTY Download</a>
								</div>
								<p></p>

							</div>
						</div>
					</div>

					<div id="section_sep_top"></div>
					<div id="section_line"></div>
					<div id="section_sep_btm"></div>

					<h2>FTP logins</h2>

					<p>
						For drag-and-drop file transfers, and FTP client may be preferred. I recommend 
						<a href="https://filezilla-project.org/" target="_blank">FileZilla</a> for MacOS and Linux and
						<a href="https://winscp.net/eng/index.php" target="_blank">WinSCP</a> for Windows.
					</p>

					<p>
						Usage is similar regardless of FTP client chosen. Simply find in the GUI where you can enter the username and 
						server address for the server you want to login to and connect. Enter your password when prompted. Then you should
						be able to drag and drop files between your local computer and the remote server via the FTP GUI.
					</p>

					<div id="msg_cont">
						<div id="msg">
							<div id="rec_banner">Recommendation</div>
							<div id="rec_text">
								<p>
									For both SSH and FTP logins, consider setting up public-key authentication to login. 
									This can provide enhanced security and ease of access compared to logging in with a password.
									See the following for in depth instructions:
								</p>
								<div id="imp_link_cont">
									<a id="imp_link" href="https://kb.iu.edu/d/aews" target="_blank">Set up SSH public-key authentication</a>
								</div>
								<p></p>
							</div>
						</div>
					</div>

					<div id="section_sep_top"></div>
					<div id="section_line"></div>
					<div id="section_sep_btm"></div>

					<h2>TightVNC Remote Desktop logins</h2>

					<p>
						We also have available to us remote desktop software called TightVNC:
					</p>
					
					<div id="imp_link_cont">
						<a id="imp_link" href="https://www.tightvnc.com/download.html" target="_blank">TightVNC Download</a>
					</div>

					<p>
						Using TightVNC, you will be able to login to one of the nodes and be able to interact with the filesystem with 
						your mouse and keyboard as if you were sitting at the remote node with a monitor. You can even interact 
						with the <a href="jobs.html">SLURM job management software</a> from the remote desktop and open a terminal
						from within the remote desktop.
					</p>

					<p>
						This remote desktop software will prove useful in many situations. However, while some of you may be more 
						comfortable interacting with the cluster in this fashion, I highly recommend logging
						in through a command line interface with SSH!
					</p>

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
pagefile = "start.html";
print("Generating " + pagefile + "...");
title = "Griz logins"

head = RC.readHead(title, pagefile);
nav = RC.readNav(pagefile);
footer = RC.readFooter();

outfilename = "../../" + pagefile;

with open(outfilename, "w") as outfile:
    outfile.write(html_template.format(head=head, nav=nav, footer=footer));