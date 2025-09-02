# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'Lizenzen'
copyright = '2025, Hochschulbibliothekszentrum des Landes Nordrhein-Westfalen (hbz)'
author = 'Peter Reimer'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration



extensions = [
  "sphinx_rtd_theme",
]

templates_path = ['_templates']
exclude_patterns = ['_venv', '_build', 'Thumbs.db', '.DS_Store']

language = 'de'

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_title = "Lizenzen"
html_theme = 'furo'
html_static_path = ['_static']
html_logo = "hbz-Logo-rgb-ohne-Claim.svg"
html_css_files = [
  'css/custom.css',
  'https://fonts.pubsys.hbz-nrw.de/hbz-cd-2024/hbz-cd-2024.css'
]
