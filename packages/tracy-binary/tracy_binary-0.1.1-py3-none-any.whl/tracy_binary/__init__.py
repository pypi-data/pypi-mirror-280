import os, sys, subprocess


def main():
    sys.exit(subprocess.call([
        os.path.join(os.path.dirname(__file__), "tracy_v0.7.5_linux_x86_64bit"),
        *sys.argv[1:]
    ]))