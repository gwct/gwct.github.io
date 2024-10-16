############################################################
# For murine web development, 11.17
# Functions to read static html chunks
############################################################

def readHead(title):
    headfile = "lib/html-chunks/head.html";
    return open(headfile, "r").read().replace("TMPTITLE", title);

def readNav(active_url):
    repl_url = active_url;
    if active_url in ['start.html', 'organization.html', 'commands.html', 'macaque-svs.html', 'wolf-snps.html', 'end.html']:
        active_url = 'start.html';
    navfile = "lib/html-chunks/nav.html";
    navlines = open(navfile, "r").readlines();
    for x in range(len(navlines)):
        if active_url == "start.html":
            if repl_url in navlines[x]:
                if repl_url == 'mapping.html' and 'iterative-mapping.html' in navlines[x]:
                    pass;
                else:
                    navlines[x] = navlines[x].replace(repl_url, "#");
            if 'class="nav_link">Workshop</a>' in navlines[x]:
                navlines[x] = navlines[x].replace('class="nav_link"', 'class="nav_link" id="active"')
            if '<div class="col-4-24 dropdown" id="nav_link_cell">' in navlines[x]:
                navlines[x] = navlines[x].replace('id="nav_link_cell"', 'id="nav_link_cell_active"');
        # For the Workshop dropdown menu

        elif active_url in navlines[x]:
            navlines[x] = navlines[x].replace(active_url, "#");
            if 'id="nav_link_cell"' in navlines[x]:
                navlines[x] = navlines[x].replace('class="nav_link"', 'class="nav_link" id="active"');
                navlines[x] = navlines[x].replace('id="nav_link_cell"', 'id="nav_link_cell_active"');

        if "mobile_nav" in navlines[x]:
            break;

    return "".join(navlines);

def readFooter():
    import time, subprocess
    from datetime import datetime
    footerfile = "lib/html-chunks/footer.html";
    now = datetime.now().strftime("%m/%d/%Y %H:%M:%S");
    zone = subprocess.check_output("date +%Z").decode().strip();
    return open(footerfile, "r").read().replace("DATETIME", now + " " + zone);