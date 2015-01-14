import lithe.structure
import lithe.config
import os.path
import os
import urllib.request
import subprocess
import sys
import re
from optparse import OptionParser

BUILD_FOLDER = './build'
BUILD_FOLDER_STRUCTURE = True


def clean():
    """
        Cleanup build directory
    """
    print("Removing possible build directory....")
    subprocess.call(["rm", "-Rf", BUILD_FOLDER])


def ping():
    try:
        urllib.request.urlopen('http://localhost:8000')
    except:
        print("Did you start lithe?")
        sys.exit()


def generate_file_list():
    file_list = []

    lithe.structure.get_static_html_files(
        file_list, lithe.config.TEMPLATE_FILE_DIR)

    if os.path.isdir(lithe.config.CONTENT_FILE_DIR):
        file_list.extend(
            lithe.structure.get_files_from_path(lithe.config.CONTENT_FILE_DIR))

    return file_list


def read_write_response():
    file_list = generate_file_list()

    for url in file_list:
        try:
            if lithe.config.USE_HTML_EXTENSION is False:
                get_url = re.sub('\.html', '', url)
            else:
                get_url = url

            full_url = 'http://localhost:8000/%s' % get_url
            print("Processing %s" % full_url)
            response = urllib.request.urlopen(full_url)

            html = response.read().decode('utf-8')
        except UnicodeDecodeError:
            html = response.read()
        except:
            print("Weirdness has happened trying to process %s" % full_url)
            sys.exit()

        if BUILD_FOLDER_STRUCTURE is False:
            path_chunks = re.split('\/', url)
            target_path = '%s/%s' % (BUILD_FOLDER, path_chunks[-1])
        else:
            target_path = '%s/%s' % (BUILD_FOLDER, url)

        print("Saving HTML output to %s" % target_path)

        target_file = open(target_path, 'w')
        target_file.write(str(html))
        target_file.close()
        response.close()


def generate_folder_structure():
    """ Create build folder """
    subprocess.call(["mkdir", BUILD_FOLDER])

    if BUILD_FOLDER_STRUCTURE:
        file_list = generate_file_list()

        for url in file_list:
            """
                We are being quite ignorant and only building
                one level deep structures, this is the way lithe
                behaves and so we not need recursiveness
            """
            path_chunks = re.split('\/', url)
            if len(path_chunks) > 1:
                """
                    We are only concerned about non-root level elements
                """
                subprocess.call(
                    ["mkdir", "%s/%s" % (BUILD_FOLDER, path_chunks[0])]
                )


def collect_static():
    print("Copying static folder to build folder")
    subprocess.call(
        [
            "cp", "-Rf",
            "%s/web/static" % os.path.abspath(os.getcwd()),
            BUILD_FOLDER
        ]
    )


print(
    """
  | _)  |    |
  |  |   _|    \    -_)
 _| _| \__| _| _| \___|
"""
)


parser = OptionParser()
parser.add_option(
    "-i",
    "--ignore-folder-structure",
    dest="ignore_folder_structure",
    action="store_true"
)

(options, args) = parser.parse_args()

if options.ignore_folder_structure:
    BUILD_FOLDER_STRUCTURE = False


clean()
ping()
generate_folder_structure()
read_write_response()
collect_static()
