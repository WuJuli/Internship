__version__ = None
exec(open("../../cotracker/version.py", "r").read())

project = "CoTracker"
copyright = "2023-24, Meta Platforms, Inc. and affiliates"
author = "Meta Platforms"
release = __version__

extensions = [
    "sphinx.ext.napoleon",
    "sphinx.ext.duration",
    "sphinx.ext.doctest",
    "sphinx.ext.autodoc",
    "sphinx.ext.autosummary",
    "sphinx.ext.intersphinx",
    "sphinxcontrib.bibtex",
]

intersphinx_mapping = {
    "python": ("https://docs.python.org/3/", None),
    "sphinx": ("https://www.sphinx-doc.org/en/master/", None),
}
intersphinx_disabled_domains = ["std"]

# templates_path = ["_templates"]
html_theme = "alabaster"

# Ignore >>> when copying code
copybutton_prompt_text = r">>> |\.\.\. "
copybutton_prompt_is_regexp = True

# -- Options for EPUB output
epub_show_urls = "footnote"

# typehints
autodoc_typehints = "description"

# citations
bibtex_bibfiles = ["references.bib"]
