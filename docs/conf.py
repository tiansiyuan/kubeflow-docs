# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'Kubeflow'
copyright = '2023, Elements of AI'
author = 'Elements of AI'
release = '0.1'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = ["sphinx_immaterial"]

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']


# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_favicon = "./_static/favicon.ico"
# html_logo = "./_static/sphinx-needs-logo-white.png"
html_title = "Kubeflow Enterprise Docs"

# material theme options (see theme.conf for more information)
html_theme_options = {
#    "site_url": "https://useblocks.com/sphinx-needs-enterprise/",
    "repo_url": "https://github.com/elements-of-ai/kubeflow-docs",
    "repo_name": "Kubeflow Docs",
    "repo_type": "github",
    "edit_uri": "blob/master/docs",
    "globaltoc_collapse": True,
    "features": [
        "navigation.expand",
        "navigation.sections",
        "navigation.top",
        "search.share",
    ],
    "palette": [
        {
            "media": "(prefers-color-scheme: light)",
            "scheme": "default",
            "primary": "blue",
            "accent": "light-blue",
            "toggle": {
                "icon": "material/weather-night",
                "name": "Switch to dark mode",
            },
        },
        {
            "media": "(prefers-color-scheme: dark)",
            "scheme": "slate",
            "primary": "blue",
            "accent": "yellow",
            "toggle": {
                "icon": "material/weather-sunny",
                "name": "Switch to light mode",
            },
        },
    ],
    "toc_title_is_page_title": True,
}


html_theme = 'sphinx_immaterial'
html_static_path = ['_static']
