from __future__ import annotations

import importlib.metadata

project = "pyauthorizer"
copyright = "2023-2024, msclock"
author = "msclock"
version = release = importlib.metadata.version("pyauthorizer")

extensions = [
    "myst_parser",
    "sphinx.ext.autodoc",
    "sphinx.ext.intersphinx",
    "sphinx.ext.mathjax",
    "sphinx.ext.viewcode",
    "sphinx.ext.napoleon",
    "sphinx_autodoc_typehints",
    "sphinx_copybutton",
    "sphinx_inline_tabs",
]

source_suffix = [".rst", ".md"]
exclude_patterns = [
    "_build",
    "**.ipynb_checkpoints",
    "Thumbs.db",
    ".DS_Store",
    ".env",
    ".venv",
]

html_theme = "furo"

myst_enable_extensions = [
    "colon_fence",
]

intersphinx_mapping = {
    "python": ("https://docs.python.org/3", None),
    "entrypoints": ("https://entrypoints.readthedocs.io/en/latest/", None),
    "cryptography": ("https://cryptography.io/en/latest/", None),
    "typing": ("https://typing.readthedocs.io/en/latest/", None),
}

nitpick_ignore = [
    ("py:class", "_io.StringIO"),
    ("py:class", "_io.BytesIO"),
]

always_document_param_types = True
