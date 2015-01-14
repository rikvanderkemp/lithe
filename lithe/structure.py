import os
import re
from lithe.config import *


def get_files_from_path(path, depth=0):
    f = []

    """
        Do not allow structures deeper then
        two directories deep.

        Directory structure is matched on the way
        templates are managed. Everything under the
        'path' folder is considered a hidden or dynamic
        template, so in order to avoid any incorrect
        requests we limit the depth in which we are allowed
        to travel. In the future this will change so you can
        have subfolders in the template structure. This limit
        will then have to be removed.
    """
    if depth >= 2:
        return f

    for (item) in os.listdir(path):
        if (os.path.isfile(os.path.join(path, item))):
            """
                Anything else deeper then the root will need
                to contain the folder structure they are in.
                We will assume this happens when files are
                accessed or read from the CONTENT_FILE_DIR we
                will need to strip this reference of the base
                path so we will end up with just the regular path.
            """
            file_name = (
                '%s/%s' % (path.replace(CONTENT_FILE_DIR, ''), item)
            ).lstrip('/')

            """
                Simply replace yml extension files with
                .html so it is more web friendly :-)
            """
            if re.search('.*\.yml', file_name):
                file_name = ('%s.html' % file_name[:-4])

            f.append(file_name)

        elif (os.path.isdir(os.path.join(path, item))):
            f.extend(
                get_files_from_path(os.path.join(path, item), depth + 1)
            )

    return f


def get_static_html_files(file_listing, directory):
    """
        Go through all files in our given directory
        and add these to our files list. We will only be scanning
        through our root directory and won't descend
        into any subdirectories.

        Static files in lithe are considered without the usage
        of a _ (underscore) at the beginning of the file name.
    """
    for (item) in os.listdir(directory):
        if (os.path.isfile(os.path.join(directory, item))):
            """
                Exclude files beginning with a _ (underscore)
                these files will be used to populate from yaml files
            """
            if re.search('^(?!\_)', item):
                file_listing.append(item)
