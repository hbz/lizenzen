from datetime import datetime
# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'Lizenzen'
#copyright = '2026, Hochschulbibliothekszentrum des Landes Nordrhein-Westfalen (hbz)'
author = 'Peter Reimer'
copyright = f"{datetime.now().year}, Hochschulbibliothekszentrum des Landes Nordrhein-Westfalen (hbz)"

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration



extensions = []

templates_path = ['_templates']
exclude_patterns = ['venv', '_build', 'Thumbs.db', '.DS_Store', 'README.rst']

language = 'de'

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_title = "Lizenzen"
html_theme = 'furo'
html_static_path = ['_static']
#html_extra_path = ['_extra']
html_logo = "hbz-Logo-rgb-ohne-Claim.svg"
html_css_files = [
  'css/custom.css',
  'https://fonts.pubsys.hbz-nrw.de/wix-madefor-text/v16/css/wix-madefor-text.css'
]
# Matomo Webstatistics
# wichtig: schließendes "/" bei der url

html_context = {
    "analytics_url": "https://analytics.hbz-nrw.de/",
    "analytics_siteid": "42"
}
html_theme_options = {
    "source_repository": "https://github.com/hbz/lizenzen",
    "source_branch": "main",
    "source_directory": "/",
    "light_css_variables": {
        "color-brand-primary": "#0000C0",
        "color-brand-content": "#0000C0",
        "color-admonition-background": "orange",
    },
}
html_show_sourcelink = True