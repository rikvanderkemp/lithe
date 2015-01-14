import os
import yaml
import re
from lithe.config import *


def get_yaml_data(path):
    """
        Retrieve yaml data from a given path
        if file not exist, return False
    """
    yaml_path = "%s%s.yml" % (CONTENT_FILE_DIR, path[:-5])
    if os.path.isfile(yaml_path):
        f = open(yaml_path, 'r')
        template_data = yaml.load(f)
        return template_data
    else:
        return False


def determine_template_by_path(path):
    """
        Try and determine the correct _ (underscore)
        template matching the files directory structure
    """
    path = path.lstrip('/')

    path_chunks = re.split('\/', path)
    if len(path_chunks) <= 1:
        return path
    else:
        """
            For now be ignorant and just return the
            first entry of the list as the possible template
            name, so in fact we only have a 1 level deep structure
        """
        return '_%s.html' % path_chunks[0]
