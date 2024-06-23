"""
Many of life's failures are people who did not realize
how close they were to success when they gave up.
-Thomas A. Edison
"""

exclude = ["dist",
           "__pycache__",
           "build",
           "lib",
           "algorithms"
]


def _get_dirs(exclude):
    from os import listdir
    from os.path import isfile
    dirs = {"hero24/algorithms" : "."}
    for d in listdir("."):
        if d in exclude or isfile(d):
            continue
        dirs["hero24/algorithms/"+d] = d
    print(dirs)
    return dirs

from distutils.core import setup, Extension
from sys import argv
ext_modules = []
args = {
    "name":"algorithms",
    "version":"0.2",
    "description":"Python implementations of various algorithms",
    "author":"hero24"
}
if "capi" in argv:
    args["ext_modules"] = [
        Extension("hero24/algorithms/capi/rabin_karp", ["capi/rk.c"]),
        Extension("hero24/algorithms/capi/boyer_moore", ["capi/bm.c"]),
        Extension("hero24/algorithms/capi/knuth_morris_pratt", ["capi/kmp.c"]),
        Extension("hero24/algorithms/capi/hashing", ["capi/hashing.c"])
    ]
    argv.remove("capi")
else:
    exclude += ["capi"]
argv += ['install']
args["package_dir"] = _get_dirs(exclude)
args["packages"] = [k for k in args["package_dir"]]

setup(**args)
