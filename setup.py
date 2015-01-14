import os.path
import subprocess
import sys

SETUP_DIR = 'web'


def cleanup():
    print("Cleaning up (removing) old setup")
    subprocess.call(["rm", "-Rf", "./web/"])
    subprocess.call(["rm", "lithe.sh"])
    subprocess.call(["rm", "build.py"])


def sanity_checks():
    """
        Sanity check, this needs to be run outside of
        the lithe folder
    """
    if os.path.isfile('main.py'):
        print(
            """You are in the root folder of lithe,
            please change directory to one level up"""
        )
        sys.exit(0)

    if os.path.isdir(SETUP_DIR):
        print("""
Previous installation detected. Would you like to
remove old files and do a fresh installation?

Type REMOVE to confirm

WARNING: This will remove ALL files part of the
         original installation of lithe this includes
         the web/ folder.
""")
        removal_confirmation = input(": ")

        if (removal_confirmation == "REMOVE"):
            cleanup()
        else:
            print("Setup canceled")
            sys.exit(1)


def copy_web_folder():
    print("-> Copying example web folder")
    subprocess.call(["cp", "-Rf", "./lithe/example/web", "."])

    print("-> Web copied and available under web/")


def symlink_binaries():
    print("-> Symlinking useful scripts")
    subprocess.call(["ln", "-s", "./lithe/bin/lithe.sh", "lithe.sh"])
    print("--> Symlinked lithe.sh control script. Used to start, stop lithe")


def final_words():
    print("""
If all is well, lithe is ready to fly.

    -> To start/stop/restart lithe use ./lithe.sh start|stop|restart
    -> To build a html output for upload to your server use python/build.py

Thanks for using lithe!

""")


def setup():
    sanity_checks()
    copy_web_folder()
    symlink_binaries()
    final_words()


print(
    """
  | _)  |    |
  |  |   _|    \    -_)
 _| _| \__| _| _| \___|
"""
)

print("""
This setup script will copy the web folder folder from the examples
directory and will make sure you can run lithe asap.

Would you like to continue? Type yes
""")
confirmation = input(": ")

if confirmation == "yes":
    setup()
