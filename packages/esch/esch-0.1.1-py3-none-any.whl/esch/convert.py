# convert.py
#   convert function for esch
# by: Noah Syrkis


# imports
from pathlib import Path
import subprocess
import frontmatter


# contants
kinds = "slide book resume letter paper invoice proposal portfolio".split()
zotero = Path("~/Zotero").expanduser()
library = Path("~/code/esch/library.bib").expanduser()  # temporary hard coded
templates = Path("~/code/esch/templates").expanduser()  # temporary hard coded
filters = Path("~/code/esch/filters").expanduser()  # temporary hard coded


# functions
def config_fn(path, doc_type):
    with open(path) as f:
        fm = frontmatter.load(f)
    return {
        **fm.metadata,
        "doc_type": doc_type,
        "zotero": str(zotero),
        "library": str(library),
        "template": str(templates / f"{doc_type}.tex"),
        "filters": str(filters),
        "bibfile": str(library),
    }


def convert_fn(f, doc_type):
    path = Path(f)
    script = f"scripts/{doc_type}.sh"

    filebase = str(path.with_suffix(""))
    config = str(config_fn(path, doc_type)).replace("'", '"')

    command = [script, filebase, config]
    subprocess.run(command, check=True)

    return filebase + ".pdf"
