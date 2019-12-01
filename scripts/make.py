import sys, os, argparse

print()
print("###### Build site pages ######");
print("PYTHON VERSION: " + ".".join(map(str, sys.version_info[:3])))
print("# Script call: " + " ".join(sys.argv) + "\n----------");

parser = argparse.ArgumentParser(description="Gets stats from a bunch of abyss assemblies.");
parser.add_argument("--all", dest="all", help="Build all pages", action="store_true", default=False);
parser.add_argument("--index", dest="index", help="Without --all: build index.html. With --all: exlude index.html", action="store_true", default=False);
parser.add_argument("--research", dest="research", help="Without --all: build research.html. With --all: exlude research.html", action="store_true", default=False);
parser.add_argument("--pubs", dest="pubs", help="Without --all: build pubs.html. With --all: exlude pubs.html", action="store_true", default=False);
parser.add_argument("--links", dest="links", help="Without --all: build links.html. With --all: exlude links.html", action="store_true", default=False);
parser.add_argument("--archive", dest="archive", help="Without --all: build archive.html. With --all: exlude archive.html", action="store_true", default=False);
args = parser.parse_args();
# Input options.

#cwd = os.getcwd();
os.chdir("generators");

pages = {
    'index' : args.index,
    'research' : args.research,
    'pubs' : args.pubs,
    'links' : args.links,
    'archive' : args.archive,
}

if args.all:
    pages = { page : False if pages[page] == True else True for page in pages };

if pages['index']:
    os.system("python index_generator.py");

if pages['research']:
    os.system("python research_generator.py");

if pages['pubs']:
    os.system("python pubs_generator.py");

if pages['links']:
    os.system("python links_generator.py");

if pages['archive']:
    os.system("python archive_generator.py");
    
print("----------\nDone!");


