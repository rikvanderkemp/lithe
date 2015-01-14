import os
import re
import mimetypes
from wsgiref.simple_server import make_server

import lithe.config
import lithe.structure
import lithe.template


def run_server():
    """ Lets run a simple wsgi server on port 8000
    we route everything through our 'server' app """

    httpd = make_server('', 8000, server)
    httpd.serve_forever()


def server(environ, start_response):
    # only serve the file if it is within STATIC_FILE_DIR and
    # if it exists
    if environ['PATH_INFO'].startswith(lithe.config.STATIC_URL_PREFIX):
        return static(environ, start_response)
    else:
        status = '200 OK'
        headers = [('Content-type', 'text/html; charset=utf-8')]
        start_response(status, headers)

        path = environ['PATH_INFO']
        path = os.path.normpath(path)

        if path == '/':
            """
                The root of our website will contain a very simple
                file listing containing links to both static
                and dynamic (=yaml fueled) files
            """
            file_listing = []

            lithe.structure.get_static_html_files(
                file_listing, lithe.config.TEMPLATE_FILE_DIR)

            if os.path.isdir(lithe.config.CONTENT_FILE_DIR):
                file_listing.extend(
                    lithe.structure.get_files_from_path(
                        lithe.config.CONTENT_FILE_DIR
                    )
                )

            return [('<a href="%s">%s</a><br>' %
                    (format_file_name_for_listing(filename),
                        format_file_name_for_listing(filename))).encode('UTF-8')
                    for filename in file_listing]
        else:
            if path == '/favicon.ico':
                content = read_file(
                    '%s/favicon.ico' % lithe.config.TEMPLATE_FILE_DIR
                )
                return [content]

            template_data = False

            if lithe.config.USE_HTML_EXTENSION is False:
                """
                    Add html extension else we won't
                    find the required or optional file.
                """
                path = '%s.html' % path

            template_data = lithe.template.get_yaml_data(path)
            if template_data:
                path = lithe.template.determine_template_by_path(path)

            # Serve regular existing html templates
            template = lithe.config.TEMPLATE_ENVIRONMENT_LOADER \
                .get_template(path)
            render = template.render(data=template_data)

            return [render.encode('UTF-8')]


def format_file_name_for_listing(filename):
    if lithe.config.USE_HTML_EXTENSION:
        return filename
    else:
        return re.sub('\.html', '', filename)


def static(environ, start_response):
    """Serve static files from the directory named
    in STATIC_FILE_DIR"""

    path = environ['PATH_INFO']
    # we want to remove '/static' from the start
    path = path.replace(
        lithe.config.STATIC_URL_PREFIX,
        lithe.config.STATIC_FILE_DIR
    )

    path = os.path.normpath(path)

    if path.startswith(lithe.config.STATIC_FILE_DIR) and os.path.exists(path):
        content = read_file(path)

        headers = [('content-type', content_type(path))]
        start_response('200 OK', headers)
        return [content]
    else:
        start_response('404 NOT FOUND')
        return []


def read_file(path):
    h = open(path, 'rb')
    content = h.read()
    h.close()
    return content


def content_type(path):
    """Return a guess at the mime type for this path
    based on the file extension"""

    name, ext = os.path.splitext(path)
    guessed_mimetypes = mimetypes.guess_type(path)

    if guessed_mimetypes[0] is not None:
        return guessed_mimetypes[0]
    else:
        return "application/octet-stream"
