import os
import platform
import subprocess
import sys


SYSTEM_MACHINE_BINARY_MAP = {
    ("Linux", "x86_64"): "tracy_v0.7.5_linux_x86_64bit",
}


def main():
    platform_system = platform.system()
    platform_machine = platform.machine()
    binary = SYSTEM_MACHINE_BINARY_MAP.get((platform_system, platform_machine))
    if not binary:
        print("No binary is available for " + platform_system + " " + platform_machine)
        sys.exit(1)
    sys.exit(subprocess.call([
        os.path.join(os.path.dirname(__file__), binary),
        *sys.argv[1:]
    ]))
