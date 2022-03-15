# -*- coding: utf-8 -*-
#
# Configuration file for the Sphinx documentation builder.
#
# This file does only contain a selection of the most common options. For a
# full list see the documentation:
# http://www.sphinx-doc.org/en/master/config

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))


# -- Project information -----------------------------------------------------

project = 'GiselleBot'
copyright = '2022, cycloptux'
author = 'cycloptux'

# The short X.Y version
version = '1.14'
# The full version, including alpha/beta/rc tags
release = '1.14.0-dev'

# Substitutions
rst_prolog = '''
.. |bot_name| replace:: GiselleBot
.. |bot_email| replace:: gisellebot@cycloptux.com
.. |bot_invite| replace:: https://gisl.eu/invite
.. |bot_support| replace:: https://discord.gg/vY5zdmzukb
.. |bot_prefix| replace:: !
.. |bot_prefix_name| replace:: an exclamation point
'''

# -- General configuration ---------------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
#
# needs_sphinx = '1.0'

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
import sphinx_rtd_theme

extensions = [
    'sphinx_rtd_theme',
    'sphinx_sitemap'
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# The suffix(es) of source filenames.
# You can specify multiple suffix as a list of string:
#
# source_suffix = ['.rst', '.md']
source_suffix = '.rst'

# The master toctree document.
master_doc = 'index'

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = None

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = []

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = None


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'sphinx_rtd_theme'

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
#
# html_theme_options = {}

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

# Custom sidebar templates, must be a dictionary that maps document names
# to template names.
#
# The default sidebars (for documents that don't match any pattern) are
# defined by theme itself.  Builtin themes are using these templates by
# default: ``['localtoc.html', 'relations.html', 'sourcelink.html',
# 'searchbox.html']``.
#
# html_sidebars = {}

# https://github.com/readthedocs/sphinx_rtd_theme/issues/1240
html_css_files = [
    "_static/theme_overrides.css" # override wide tables in RTD theme
]

# The URL which points to the root of the HTML documentation. It is used to indicate the location of document like canonical_url.
html_baseurl = 'https://docs.gisellebot.com/'

# A list of paths that contain extra files not directly related to the documentation, such as robots.txt or .htaccess. Relative paths are taken as relative to the configuration directory. They are copied to the output directory. They will overwrite any existing file of the same name.
# As these files are not meant to be built, they are automatically excluded from source files.
html_extra_path = ['robots.txt']

# Logo of the docs, or URL that points an image file for the logo. It is placed at the top of the sidebar
html_logo = 'images/gisellebot-logo.png'

# Website Favicon
html_favicon = 'favicon.ico'


# -- Options for HTMLHelp output ---------------------------------------------

# Output file base name for HTML help builder.
htmlhelp_basename = 'GiselleBotdoc'

# -- Options for LaTeX output ------------------------------------------------

latex_elements = {
    # The paper size ('letterpaper' or 'a4paper').
    #
    # 'papersize': 'letterpaper',

    # The font size ('10pt', '11pt' or '12pt').
    #
    # 'pointsize': '10pt',

    # Additional stuff for the LaTeX preamble.
    #
    # 'preamble': '',

    # Latex figure (float) alignment
    #
    # 'figure_align': 'htbp',
}

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title,
#  author, documentclass [howto, manual, or own class]).
latex_documents = [
    (master_doc, 'GiselleBot.tex', 'GiselleBot Documentation',
     'cycloptux', 'manual'),
]


# -- Options for manual page output ------------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [
    (master_doc, 'gisellebot', 'GiselleBot Documentation',
     [author], 1)
]


# -- Options for Texinfo output ----------------------------------------------

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [
    (master_doc, 'GiselleBot', 'GiselleBot Documentation',
     author, 'GiselleBot', 'One line description of project.',
     'Miscellaneous'),
]


# -- Options for Epub output -------------------------------------------------

# Bibliographic Dublin Core info.
epub_title = project

# The unique identifier of the text. This can be a ISBN number
# or the project homepage.
#
# epub_identifier = ''

# A unique identification for the text.
#
# epub_uid = ''

# A list of files that should not be packed into the epub file.
epub_exclude_files = ['search.html']

# -- Options for sphinx-sitemap ----------------------------------------------
# https://pypi.org/project/sphinx-sitemap/

# Customizing the URL scheme
# sitemap_url_scheme = "{lang}{version}{link}"
sitemap_url_scheme = "{lang}{link}"

# for MarkdownParser
from sphinx_markdown_parser.parser import MarkdownParser

def setup(app):
    app.add_source_suffix('.md', 'markdown')
    app.add_source_parser(MarkdownParser)
    app.add_config_value('markdown_parser_config', {
        'auto_toc_tree_section': 'Content',
        'enable_auto_doc_ref': True,
        'enable_auto_toc_tree': True,
        'enable_eval_rst': True,
        'extensions': [
            'extra',
            'nl2br',
            'sane_lists',
            'smarty',
            'toc',
            'wikilinks',
            'pymdownx.arithmatex',
        ],
    }, True)

# for CommonMarkParser
# from recommonmark.parser import CommonMarkParser
# 
# def setup(app):
#     app.add_source_suffix('.md', 'markdown')
#     app.add_source_parser(CommonMarkParser)
#     app.add_config_value('markdown_parser_config', {
#         'auto_toc_tree_section': 'Content',
#         'enable_auto_doc_ref': True,
#         'enable_auto_toc_tree': True,
#         'enable_eval_rst': True,
#         'enable_inline_math': True,
#         'enable_math': True,
#     }, True)