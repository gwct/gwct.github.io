import sys, os, argparse

print()
print("###### Build site pages ######");
print("PYTHON VERSION: " + ".".join(map(str, sys.version_info[:3])))
print("# Script call: " + " ".join(sys.argv) + "\n----------");

parser = argparse.ArgumentParser(description="Gets stats from a bunch of abyss assemblies.");
parser.add_argument("--all", dest="all", help="Build all pages", action="store_true", default=False);
parser.add_argument("--index", dest="index", help="Without --all: build index.html. With --all: exlude index.html", action="store_true", default=False);
parser.add_argument("--start", dest="start", help="Without --all: build start.html. With --all: exlude start.html", action="store_true", default=False);
parser.add_argument("--organization", dest="organization", help="Without --all: build organization.html. With --all: exlude organization.html", action="store_true", default=False);
parser.add_argument("--commands", dest="commands", help="Without --all: build commands.html. With --all: exlude commands.html", action="store_true", default=False);
parser.add_argument("--macaque", dest="macaque", help="Without --all: build macaque-svs.html. With --all: exlude macaque-svs.html", action="store_true", default=False);
parser.add_argument("--wolf", dest="wolf", help="Without --all: build wolf-snps.html. With --all: exlude wolf-snps.html", action="store_true", default=False);
parser.add_argument("--advanced", dest="advanced", help="Without --all: build advanced.html. With --all: exlude advanced.html", action="store_true", default=False);
parser.add_argument("--end", dest="end", help="Without --all: build end.html. With --all: exlude end.html", action="store_true", default=False);
#parser.add_argument("--programs", dest="programs", help="Without --all: build programs.html. With --all: exlude programs.html", action="store_true", default=False);
parser.add_argument("--links", dest="links", help="Without --all: build links.html. With --all: exlude links.html", action="store_true", default=False);
args = parser.parse_args();
# Input options.

#cwd = os.getcwd();
os.chdir("generators");

pages = {
    'index' : args.index,
    'start' : args.start,
    'organization' : args.organization,
    'commands' : args.commands,
    'macaque' : args.macaque,
    'wolf' : args.wolf,
    'advanced' : args.advanced,
    'end' : args.end,
    #'programs' : args.programs,
    'links' : args.links
}

if args.all:
    pages = { page : False if pages[page] == True else True for page in pages };

if pages['index']:
    os.system("python index_generator.py");

if pages['start']:
    os.system("python start_generator.py");

if pages['organization']:
    os.system("python organization_generator.py");

if pages['commands']:
    os.system("python commands_generator.py");

if pages['macaque']:
    os.system("python macaque_generator.py");

if pages['wolf']:
    os.system("python wolf_generator.py");

if pages['advanced']:
    os.system("python advanced_generator.py");

if pages['end']:
    os.system("python end_generator.py");

# if pages['programs']:
#     os.system("python programs_generator.py");

if pages['links']:
    os.system("python links_generator.py");

print("----------\nDone!");


