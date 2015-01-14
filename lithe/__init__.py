import mimetypes
import os.path
import os

"""
    Lets load our custom mimetypes,
    these are necessary for webfonts etc.
"""
mime_type_file_path = ['%s/config/mime.types' % os.path.abspath(os.getcwd())]
mimetypes.knownfiles += mime_type_file_path
