# Stubs for posixpath (Python 2)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from genericpath import *
from typing import Any

curdir: str
pardir: str
extsep: str
sep: str
pathsep: str
defpath: str
altsep: Any
devnull: str

def normcase(s): ...
def isabs(s: str) -> bool: ...
def join(a: str, *p: str) -> str: ...
def split(p): ...
def splitext(p): ...
def splitdrive(p): ...
def basename(p: str) -> str: ...
def dirname(p): ...
def islink(path): ...
def lexists(path): ...
def samefile(f1, f2): ...
def sameopenfile(fp1, fp2): ...
def samestat(s1, s2): ...
def ismount(path): ...
def walk(top, func, arg): ...
def expanduser(path): ...
def expandvars(path): ...
def normpath(path): ...
def abspath(path): ...
def realpath(filename): ...

supports_unicode_filenames: Any

def relpath(path, start: Any = ...): ...

# Names in __all__ with no definition:
#   commonprefix
#   exists
#   getatime
#   getctime
#   getmtime
#   getsize
#   isdir
#   isfile