from __future__ import print_function
import fnmatch
import os
import subprocess

src_dir = "/tmp/clang-build/src"
os.chdir("/tmp/patches")
patches = []
for dirpath, dirnames, filenames in os.walk("."):
    for filename in fnmatch.filter(filenames, "*.patch"):
        patch = os.path.join(dirpath, filename)
        patches.append(patch)

for patch in sorted(patches):
    cmd = ["patch", "-d", os.path.dirname(patch), "-p1", "-i", os.path.abspath(patch)]
    print(cmd)
    subprocess.call(cmd, cwd=src_dir)
