from jinja2 import Environment, FileSystemLoader

import lithe.filters

STATIC_URL_PREFIX = '/static/'
STATIC_FILE_DIR = 'web/static/'
TEMPLATE_FILE_DIR = 'web/templates/'
CONTENT_FILE_DIR = 'web/content/'
USE_HTML_EXTENSION = True

# Setting up Jinja2 do not alter unless you know what you are doing
fileSystemLoader = FileSystemLoader(TEMPLATE_FILE_DIR)
TEMPLATE_ENVIRONMENT_LOADER = Environment(loader=fileSystemLoader,
                                          trim_blocks=True,
                                          lstrip_blocks=True)

TEMPLATE_ENVIRONMENT_LOADER.filters['markdown'] = lithe.filters.markdown_filter
