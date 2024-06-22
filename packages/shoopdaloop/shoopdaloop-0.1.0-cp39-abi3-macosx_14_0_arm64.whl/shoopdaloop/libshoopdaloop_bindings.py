r"""Wrapper for libshoopdaloop.h

Generated with:
/private/var/folders/b3/2xm02wpd21qgrpkck5q1c6k40000gn/T/build-env-xjf15ul9/bin/ctypesgen --no-macro-warnings -lshoopdaloop /Users/runner/work/shoopdaloop/shoopdaloop/src/libshoopdaloop/libshoopdaloop.h /Users/runner/work/shoopdaloop/shoopdaloop/src/libshoopdaloop/types.h -o /Users/runner/work/shoopdaloop/shoopdaloop/build/cp39-cp39-macosx_14_arm64/libshoopdaloop/libshoopdaloop_bindings.py

Do not modify this file.
"""

__docformat__ = "restructuredtext"

# Begin preamble for Python

import ctypes
import sys
from ctypes import *  # noqa: F401, F403

_int_types = (ctypes.c_int16, ctypes.c_int32)
if hasattr(ctypes, "c_int64"):
    # Some builds of ctypes apparently do not have ctypes.c_int64
    # defined; it's a pretty good bet that these builds do not
    # have 64-bit pointers.
    _int_types += (ctypes.c_int64,)
for t in _int_types:
    if ctypes.sizeof(t) == ctypes.sizeof(ctypes.c_size_t):
        c_ptrdiff_t = t
del t
del _int_types



class UserString:
    def __init__(self, seq):
        if isinstance(seq, bytes):
            self.data = seq
        elif isinstance(seq, UserString):
            self.data = seq.data[:]
        else:
            self.data = str(seq).encode()

    def __bytes__(self):
        return self.data

    def __str__(self):
        return self.data.decode()

    def __repr__(self):
        return repr(self.data)

    def __int__(self):
        return int(self.data.decode())

    def __long__(self):
        return int(self.data.decode())

    def __float__(self):
        return float(self.data.decode())

    def __complex__(self):
        return complex(self.data.decode())

    def __hash__(self):
        return hash(self.data)

    def __le__(self, string):
        if isinstance(string, UserString):
            return self.data <= string.data
        else:
            return self.data <= string

    def __lt__(self, string):
        if isinstance(string, UserString):
            return self.data < string.data
        else:
            return self.data < string

    def __ge__(self, string):
        if isinstance(string, UserString):
            return self.data >= string.data
        else:
            return self.data >= string

    def __gt__(self, string):
        if isinstance(string, UserString):
            return self.data > string.data
        else:
            return self.data > string

    def __eq__(self, string):
        if isinstance(string, UserString):
            return self.data == string.data
        else:
            return self.data == string

    def __ne__(self, string):
        if isinstance(string, UserString):
            return self.data != string.data
        else:
            return self.data != string

    def __contains__(self, char):
        return char in self.data

    def __len__(self):
        return len(self.data)

    def __getitem__(self, index):
        return self.__class__(self.data[index])

    def __getslice__(self, start, end):
        start = max(start, 0)
        end = max(end, 0)
        return self.__class__(self.data[start:end])

    def __add__(self, other):
        if isinstance(other, UserString):
            return self.__class__(self.data + other.data)
        elif isinstance(other, bytes):
            return self.__class__(self.data + other)
        else:
            return self.__class__(self.data + str(other).encode())

    def __radd__(self, other):
        if isinstance(other, bytes):
            return self.__class__(other + self.data)
        else:
            return self.__class__(str(other).encode() + self.data)

    def __mul__(self, n):
        return self.__class__(self.data * n)

    __rmul__ = __mul__

    def __mod__(self, args):
        return self.__class__(self.data % args)

    # the following methods are defined in alphabetical order:
    def capitalize(self):
        return self.__class__(self.data.capitalize())

    def center(self, width, *args):
        return self.__class__(self.data.center(width, *args))

    def count(self, sub, start=0, end=sys.maxsize):
        return self.data.count(sub, start, end)

    def decode(self, encoding=None, errors=None):  # XXX improve this?
        if encoding:
            if errors:
                return self.__class__(self.data.decode(encoding, errors))
            else:
                return self.__class__(self.data.decode(encoding))
        else:
            return self.__class__(self.data.decode())

    def encode(self, encoding=None, errors=None):  # XXX improve this?
        if encoding:
            if errors:
                return self.__class__(self.data.encode(encoding, errors))
            else:
                return self.__class__(self.data.encode(encoding))
        else:
            return self.__class__(self.data.encode())

    def endswith(self, suffix, start=0, end=sys.maxsize):
        return self.data.endswith(suffix, start, end)

    def expandtabs(self, tabsize=8):
        return self.__class__(self.data.expandtabs(tabsize))

    def find(self, sub, start=0, end=sys.maxsize):
        return self.data.find(sub, start, end)

    def index(self, sub, start=0, end=sys.maxsize):
        return self.data.index(sub, start, end)

    def isalpha(self):
        return self.data.isalpha()

    def isalnum(self):
        return self.data.isalnum()

    def isdecimal(self):
        return self.data.isdecimal()

    def isdigit(self):
        return self.data.isdigit()

    def islower(self):
        return self.data.islower()

    def isnumeric(self):
        return self.data.isnumeric()

    def isspace(self):
        return self.data.isspace()

    def istitle(self):
        return self.data.istitle()

    def isupper(self):
        return self.data.isupper()

    def join(self, seq):
        return self.data.join(seq)

    def ljust(self, width, *args):
        return self.__class__(self.data.ljust(width, *args))

    def lower(self):
        return self.__class__(self.data.lower())

    def lstrip(self, chars=None):
        return self.__class__(self.data.lstrip(chars))

    def partition(self, sep):
        return self.data.partition(sep)

    def replace(self, old, new, maxsplit=-1):
        return self.__class__(self.data.replace(old, new, maxsplit))

    def rfind(self, sub, start=0, end=sys.maxsize):
        return self.data.rfind(sub, start, end)

    def rindex(self, sub, start=0, end=sys.maxsize):
        return self.data.rindex(sub, start, end)

    def rjust(self, width, *args):
        return self.__class__(self.data.rjust(width, *args))

    def rpartition(self, sep):
        return self.data.rpartition(sep)

    def rstrip(self, chars=None):
        return self.__class__(self.data.rstrip(chars))

    def split(self, sep=None, maxsplit=-1):
        return self.data.split(sep, maxsplit)

    def rsplit(self, sep=None, maxsplit=-1):
        return self.data.rsplit(sep, maxsplit)

    def splitlines(self, keepends=0):
        return self.data.splitlines(keepends)

    def startswith(self, prefix, start=0, end=sys.maxsize):
        return self.data.startswith(prefix, start, end)

    def strip(self, chars=None):
        return self.__class__(self.data.strip(chars))

    def swapcase(self):
        return self.__class__(self.data.swapcase())

    def title(self):
        return self.__class__(self.data.title())

    def translate(self, *args):
        return self.__class__(self.data.translate(*args))

    def upper(self):
        return self.__class__(self.data.upper())

    def zfill(self, width):
        return self.__class__(self.data.zfill(width))


class MutableString(UserString):
    """mutable string objects

    Python strings are immutable objects.  This has the advantage, that
    strings may be used as dictionary keys.  If this property isn't needed
    and you insist on changing string values in place instead, you may cheat
    and use MutableString.

    But the purpose of this class is an educational one: to prevent
    people from inventing their own mutable string class derived
    from UserString and than forget thereby to remove (override) the
    __hash__ method inherited from UserString.  This would lead to
    errors that would be very hard to track down.

    A faster and better solution is to rewrite your program using lists."""

    def __init__(self, string=""):
        self.data = string

    def __hash__(self):
        raise TypeError("unhashable type (it is mutable)")

    def __setitem__(self, index, sub):
        if index < 0:
            index += len(self.data)
        if index < 0 or index >= len(self.data):
            raise IndexError
        self.data = self.data[:index] + sub + self.data[index + 1 :]

    def __delitem__(self, index):
        if index < 0:
            index += len(self.data)
        if index < 0 or index >= len(self.data):
            raise IndexError
        self.data = self.data[:index] + self.data[index + 1 :]

    def __setslice__(self, start, end, sub):
        start = max(start, 0)
        end = max(end, 0)
        if isinstance(sub, UserString):
            self.data = self.data[:start] + sub.data + self.data[end:]
        elif isinstance(sub, bytes):
            self.data = self.data[:start] + sub + self.data[end:]
        else:
            self.data = self.data[:start] + str(sub).encode() + self.data[end:]

    def __delslice__(self, start, end):
        start = max(start, 0)
        end = max(end, 0)
        self.data = self.data[:start] + self.data[end:]

    def immutable(self):
        return UserString(self.data)

    def __iadd__(self, other):
        if isinstance(other, UserString):
            self.data += other.data
        elif isinstance(other, bytes):
            self.data += other
        else:
            self.data += str(other).encode()
        return self

    def __imul__(self, n):
        self.data *= n
        return self


class String(MutableString, ctypes.Union):
    _fields_ = [("raw", ctypes.POINTER(ctypes.c_char)), ("data", ctypes.c_char_p)]

    def __init__(self, obj=b""):
        if isinstance(obj, (bytes, UserString)):
            self.data = bytes(obj)
        else:
            self.raw = obj

    def __len__(self):
        return self.data and len(self.data) or 0

    def from_param(cls, obj):
        # Convert None or 0
        if obj is None or obj == 0:
            return cls(ctypes.POINTER(ctypes.c_char)())

        # Convert from String
        elif isinstance(obj, String):
            return obj

        # Convert from bytes
        elif isinstance(obj, bytes):
            return cls(obj)

        # Convert from str
        elif isinstance(obj, str):
            return cls(obj.encode())

        # Convert from c_char_p
        elif isinstance(obj, ctypes.c_char_p):
            return obj

        # Convert from POINTER(ctypes.c_char)
        elif isinstance(obj, ctypes.POINTER(ctypes.c_char)):
            return obj

        # Convert from raw pointer
        elif isinstance(obj, int):
            return cls(ctypes.cast(obj, ctypes.POINTER(ctypes.c_char)))

        # Convert from ctypes.c_char array
        elif isinstance(obj, ctypes.c_char * len(obj)):
            return obj

        # Convert from object
        else:
            return String.from_param(obj._as_parameter_)

    from_param = classmethod(from_param)


def ReturnString(obj, func=None, arguments=None):
    return String.from_param(obj)


# As of ctypes 1.0, ctypes does not support custom error-checking
# functions on callbacks, nor does it support custom datatypes on
# callbacks, so we must ensure that all callbacks return
# primitive datatypes.
#
# Non-primitive return values wrapped with UNCHECKED won't be
# typechecked, and will be converted to ctypes.c_void_p.
def UNCHECKED(type):
    if hasattr(type, "_type_") and isinstance(type._type_, str) and type._type_ != "P":
        return type
    else:
        return ctypes.c_void_p


# ctypes doesn't have direct support for variadic functions, so we have to write
# our own wrapper class
class _variadic_function(object):
    def __init__(self, func, restype, argtypes, errcheck):
        self.func = func
        self.func.restype = restype
        self.argtypes = argtypes
        if errcheck:
            self.func.errcheck = errcheck

    def _as_parameter_(self):
        # So we can pass this variadic function as a function pointer
        return self.func

    def __call__(self, *args):
        fixed_args = []
        i = 0
        for argtype in self.argtypes:
            # Typecheck what we can
            fixed_args.append(argtype.from_param(args[i]))
            i += 1
        return self.func(*fixed_args + list(args[i:]))


def ord_if_char(value):
    """
    Simple helper used for casts to simple builtin types:  if the argument is a
    string type, it will be converted to it's ordinal value.

    This function will raise an exception if the argument is string with more
    than one characters.
    """
    return ord(value) if (isinstance(value, bytes) or isinstance(value, str)) else value

# End preamble

_libs = {}
_libdirs = []

# Begin loader

"""
Load libraries - appropriately for all our supported platforms
"""
# ----------------------------------------------------------------------------
# Copyright (c) 2008 David James
# Copyright (c) 2006-2008 Alex Holkner
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions
# are met:
#
#  * Redistributions of source code must retain the above copyright
#    notice, this list of conditions and the following disclaimer.
#  * Redistributions in binary form must reproduce the above copyright
#    notice, this list of conditions and the following disclaimer in
#    the documentation and/or other materials provided with the
#    distribution.
#  * Neither the name of pyglet nor the names of its
#    contributors may be used to endorse or promote products
#    derived from this software without specific prior written
#    permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
# "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
# LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS
# FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE
# COPYRIGHT OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT,
# INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING,
# BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
# LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
# CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT
# LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN
# ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
# POSSIBILITY OF SUCH DAMAGE.
# ----------------------------------------------------------------------------

import ctypes
import ctypes.util
import glob
import os.path
import platform
import re
import sys


def _environ_path(name):
    """Split an environment variable into a path-like list elements"""
    if name in os.environ:
        return os.environ[name].split(":")
    return []


class LibraryLoader:
    """
    A base class For loading of libraries ;-)
    Subclasses load libraries for specific platforms.
    """

    # library names formatted specifically for platforms
    name_formats = ["%s"]

    class Lookup:
        """Looking up calling conventions for a platform"""

        mode = ctypes.DEFAULT_MODE

        def __init__(self, path):
            super(LibraryLoader.Lookup, self).__init__()
            self.access = dict(cdecl=ctypes.CDLL(path, self.mode, winmode=0))

        def get(self, name, calling_convention="cdecl"):
            """Return the given name according to the selected calling convention"""
            if calling_convention not in self.access:
                raise LookupError(
                    "Unknown calling convention '{}' for function '{}'".format(
                        calling_convention, name
                    )
                )
            return getattr(self.access[calling_convention], name)

        def has(self, name, calling_convention="cdecl"):
            """Return True if this given calling convention finds the given 'name'"""
            if calling_convention not in self.access:
                return False
            return hasattr(self.access[calling_convention], name)

        def __getattr__(self, name):
            return getattr(self.access["cdecl"], name)

    def __init__(self):
        self.other_dirs = []

    def __call__(self, libname):
        """Given the name of a library, load it."""
        paths = self.getpaths(libname)

        errors = dict()
        for path in paths:
            # noinspection PyBroadException
            try:
                return self.Lookup(path)
            except Exception as e:  # pylint: disable=broad-except
                errors[path] = str(e)
                pass

        formatted_errors = '\n'.join(['-  {}: {}'.format(k, v) for k,v in errors.items()])
        raise ImportError("Could not load {}. Errors per tried path:\n{}".format(libname, formatted_errors))

    def getpaths(self, libname):
        """Return a list of paths where the library might be found."""
        if os.path.isabs(libname):
            yield libname
        else:
            # search through a prioritized series of locations for the library

            # we first search any specific directories identified by user
            for dir_i in self.other_dirs:
                for fmt in self.name_formats:
                    # dir_i should be absolute already
                    yield os.path.join(dir_i, fmt % libname)

            # check if this code is even stored in a physical file
            try:
                this_file = __file__
            except NameError:
                this_file = None

            # then we search the directory where the generated python interface is stored
            if this_file is not None:
                for fmt in self.name_formats:
                    yield os.path.abspath(os.path.join(os.path.dirname(__file__), fmt % libname))

            # now, use the ctypes tools to try to find the library
            for fmt in self.name_formats:
                path = ctypes.util.find_library(fmt % libname)
                if path:
                    yield path

            # then we search all paths identified as platform-specific lib paths
            for path in self.getplatformpaths(libname):
                yield path

            # Finally, we'll try the users current working directory
            for fmt in self.name_formats:
                yield os.path.abspath(os.path.join(os.path.curdir, fmt % libname))

    def getplatformpaths(self, _libname):  # pylint: disable=no-self-use
        """Return all the library paths available in this platform"""
        return []


# Darwin (Mac OS X)


class DarwinLibraryLoader(LibraryLoader):
    """Library loader for MacOS"""

    name_formats = [
        "lib%s.dylib",
        "lib%s.so",
        "lib%s.bundle",
        "%s.dylib",
        "%s.so",
        "%s.bundle",
        "%s",
    ]

    class Lookup(LibraryLoader.Lookup):
        """
        Looking up library files for this platform (Darwin aka MacOS)
        """

        # Darwin requires dlopen to be called with mode RTLD_GLOBAL instead
        # of the default RTLD_LOCAL.  Without this, you end up with
        # libraries not being loadable, resulting in "Symbol not found"
        # errors
        mode = ctypes.RTLD_GLOBAL

    def getplatformpaths(self, libname):
        if os.path.pathsep in libname:
            names = [libname]
        else:
            names = [fmt % libname for fmt in self.name_formats]

        for directory in self.getdirs(libname):
            for name in names:
                yield os.path.join(directory, name)

    @staticmethod
    def getdirs(libname):
        """Implements the dylib search as specified in Apple documentation:

        http://developer.apple.com/documentation/DeveloperTools/Conceptual/
            DynamicLibraries/Articles/DynamicLibraryUsageGuidelines.html

        Before commencing the standard search, the method first checks
        the bundle's ``Frameworks`` directory if the application is running
        within a bundle (OS X .app).
        """

        dyld_fallback_library_path = _environ_path("DYLD_FALLBACK_LIBRARY_PATH")
        if not dyld_fallback_library_path:
            dyld_fallback_library_path = [
                os.path.expanduser("~/lib"),
                "/usr/local/lib",
                "/usr/lib",
            ]

        dirs = []

        if "/" in libname:
            dirs.extend(_environ_path("DYLD_LIBRARY_PATH"))
        else:
            dirs.extend(_environ_path("LD_LIBRARY_PATH"))
            dirs.extend(_environ_path("DYLD_LIBRARY_PATH"))
            dirs.extend(_environ_path("LD_RUN_PATH"))

        if hasattr(sys, "frozen") and getattr(sys, "frozen") == "macosx_app":
            dirs.append(os.path.join(os.environ["RESOURCEPATH"], "..", "Frameworks"))

        dirs.extend(dyld_fallback_library_path)

        return dirs


# Posix


class PosixLibraryLoader(LibraryLoader):
    """Library loader for POSIX-like systems (including Linux)"""

    _ld_so_cache = None

    _include = re.compile(r"^\s*include\s+(?P<pattern>.*)")

    name_formats = ["lib%s.so", "%s.so", "%s"]

    class _Directories(dict):
        """Deal with directories"""

        def __init__(self):
            dict.__init__(self)
            self.order = 0

        def add(self, directory):
            """Add a directory to our current set of directories"""
            if len(directory) > 1:
                directory = directory.rstrip(os.path.sep)
            # only adds and updates order if exists and not already in set
            if not os.path.exists(directory):
                return
            order = self.setdefault(directory, self.order)
            if order == self.order:
                self.order += 1

        def extend(self, directories):
            """Add a list of directories to our set"""
            for a_dir in directories:
                self.add(a_dir)

        def ordered(self):
            """Sort the list of directories"""
            return (i[0] for i in sorted(self.items(), key=lambda d: d[1]))

    def _get_ld_so_conf_dirs(self, conf, dirs):
        """
        Recursive function to help parse all ld.so.conf files, including proper
        handling of the `include` directive.
        """

        try:
            with open(conf) as fileobj:
                for dirname in fileobj:
                    dirname = dirname.strip()
                    if not dirname:
                        continue

                    match = self._include.match(dirname)
                    if not match:
                        dirs.add(dirname)
                    else:
                        for dir2 in glob.glob(match.group("pattern")):
                            self._get_ld_so_conf_dirs(dir2, dirs)
        except IOError:
            pass

    def _create_ld_so_cache(self):
        # Recreate search path followed by ld.so.  This is going to be
        # slow to build, and incorrect (ld.so uses ld.so.cache, which may
        # not be up-to-date).  Used only as fallback for distros without
        # /sbin/ldconfig.
        #
        # We assume the DT_RPATH and DT_RUNPATH binary sections are omitted.

        directories = self._Directories()
        for name in (
            "LD_LIBRARY_PATH",
            "SHLIB_PATH",  # HP-UX
            "LIBPATH",  # OS/2, AIX
            "LIBRARY_PATH",  # BE/OS
        ):
            if name in os.environ:
                directories.extend(os.environ[name].split(os.pathsep))

        self._get_ld_so_conf_dirs("/etc/ld.so.conf", directories)

        bitage = platform.architecture()[0]

        unix_lib_dirs_list = []
        if bitage.startswith("64"):
            # prefer 64 bit if that is our arch
            unix_lib_dirs_list += ["/lib64", "/usr/lib64"]

        # must include standard libs, since those paths are also used by 64 bit
        # installs
        unix_lib_dirs_list += ["/lib", "/usr/lib"]
        if sys.platform.startswith("linux"):
            # Try and support multiarch work in Ubuntu
            # https://wiki.ubuntu.com/MultiarchSpec
            if bitage.startswith("32"):
                # Assume Intel/AMD x86 compat
                unix_lib_dirs_list += ["/lib/i386-linux-gnu", "/usr/lib/i386-linux-gnu"]
            elif bitage.startswith("64"):
                # Assume Intel/AMD x86 compatible
                unix_lib_dirs_list += [
                    "/lib/x86_64-linux-gnu",
                    "/usr/lib/x86_64-linux-gnu",
                ]
            else:
                # guess...
                unix_lib_dirs_list += glob.glob("/lib/*linux-gnu")
        directories.extend(unix_lib_dirs_list)

        cache = {}
        lib_re = re.compile(r"lib(.*)\.s[ol]")
        # ext_re = re.compile(r"\.s[ol]$")
        for our_dir in directories.ordered():
            try:
                for path in glob.glob("%s/*.s[ol]*" % our_dir):
                    file = os.path.basename(path)

                    # Index by filename
                    cache_i = cache.setdefault(file, set())
                    cache_i.add(path)

                    # Index by library name
                    match = lib_re.match(file)
                    if match:
                        library = match.group(1)
                        cache_i = cache.setdefault(library, set())
                        cache_i.add(path)
            except OSError:
                pass

        self._ld_so_cache = cache

    def getplatformpaths(self, libname):
        if self._ld_so_cache is None:
            self._create_ld_so_cache()

        result = self._ld_so_cache.get(libname, set())
        for i in result:
            # we iterate through all found paths for library, since we may have
            # actually found multiple architectures or other library types that
            # may not load
            yield i


# Windows


class WindowsLibraryLoader(LibraryLoader):
    """Library loader for Microsoft Windows"""

    name_formats = ["%s.dll", "lib%s.dll", "%slib.dll", "%s"]

    class Lookup(LibraryLoader.Lookup):
        """Lookup class for Windows libraries..."""

        def __init__(self, path):
            super(WindowsLibraryLoader.Lookup, self).__init__(path)
            self.access["stdcall"] = ctypes.windll.LoadLibrary(path)


# Platform switching

# If your value of sys.platform does not appear in this dict, please contact
# the Ctypesgen maintainers.

loaderclass = {
    "darwin": DarwinLibraryLoader,
    "cygwin": WindowsLibraryLoader,
    "win32": WindowsLibraryLoader,
    "msys": WindowsLibraryLoader,
}

load_library = loaderclass.get(sys.platform, PosixLibraryLoader)()


def add_library_search_dirs(other_dirs):
    """
    Add libraries to search paths.
    If library paths are relative, convert them to absolute with respect to this
    file's directory
    """
    for path in other_dirs:
        if not os.path.isabs(path):
            path = os.path.abspath(path)
        load_library.other_dirs.append(path)


del loaderclass

# End loader

add_library_search_dirs([])

# Begin libraries
_libs["shoopdaloop"] = load_library("shoopdaloop")

# 1 libraries
# End libraries

# No modules

audio_sample_t = c_float# /Users/runner/work/shoopdaloop/shoopdaloop/src/libshoopdaloop/types.h: 6

enum_anon_1 = c_int# /Users/runner/work/shoopdaloop/shoopdaloop/src/libshoopdaloop/types.h: 13

Jack = 0# /Users/runner/work/shoopdaloop/shoopdaloop/src/libshoopdaloop/types.h: 13

JackTest = (Jack + 1)# /Users/runner/work/shoopdaloop/shoopdaloop/src/libshoopdaloop/types.h: 13

Dummy = (JackTest + 1)# /Users/runner/work/shoopdaloop/shoopdaloop/src/libshoopdaloop/types.h: 13

shoop_audio_driver_type_t = enum_anon_1# /Users/runner/work/shoopdaloop/shoopdaloop/src/libshoopdaloop/types.h: 13

enum_anon_2 = c_int# /Users/runner/work/shoopdaloop/shoopdaloop/src/libshoopdaloop/types.h: 19

ShoopPortDataType_Audio = 0# /Users/runner/work/shoopdaloop/shoopdaloop/src/libshoopdaloop/types.h: 19

ShoopPortDataType_Midi = (ShoopPortDataType_Audio + 1)# /Users/runner/work/shoopdaloop/shoopdaloop/src/libshoopdaloop/types.h: 19

ShoopPortDataType_Any = (ShoopPortDataType_Midi + 1)# /Users/runner/work/shoopdaloop/shoopdaloop/src/libshoopdaloop/types.h: 19

shoop_port_data_type_t = enum_anon_2# /Users/runner/work/shoopdaloop/shoopdaloop/src/libshoopdaloop/types.h: 19

enum_anon_3 = c_int# /Users/runner/work/shoopdaloop/shoopdaloop/src/libshoopdaloop/types.h: 31

LoopMode_Unknown = 0# /Users/runner/work/shoopdaloop/shoopdaloop/src/libshoopdaloop/types.h: 31

LoopMode_Stopped = (LoopMode_Unknown + 1)# /Users/runner/work/shoopdaloop/shoopdaloop/src/libshoopdaloop/types.h: 31

LoopMode_Playing = (LoopMode_Stopped + 1)# /Users/runner/work/shoopdaloop/shoopdaloop/src/libshoopdaloop/types.h: 31

LoopMode_Recording = (LoopMode_Playing + 1)# /Users/runner/work/shoopdaloop/shoopdaloop/src/libshoopdaloop/types.h: 31

LoopMode_Replacing = (LoopMode_Recording + 1)# /Users/runner/work/shoopdaloop/shoopdaloop/src/libshoopdaloop/types.h: 31

LoopMode_PlayingDryThroughWet = (LoopMode_Replacing + 1)# /Users/runner/work/shoopdaloop/shoopdaloop/src/libshoopdaloop/types.h: 31

LoopMode_RecordingDryIntoWet = (LoopMode_PlayingDryThroughWet + 1)# /Users/runner/work/shoopdaloop/shoopdaloop/src/libshoopdaloop/types.h: 31

LOOP_MODE_INVALID = (LoopMode_RecordingDryIntoWet + 1)# /Users/runner/work/shoopdaloop/shoopdaloop/src/libshoopdaloop/types.h: 31

shoop_loop_mode_t = enum_anon_3# /Users/runner/work/shoopdaloop/shoopdaloop/src/libshoopdaloop/types.h: 31

enum_anon_4 = c_int# /Users/runner/work/shoopdaloop/shoopdaloop/src/libshoopdaloop/types.h: 40

log_level_debug_trace = 0# /Users/runner/work/shoopdaloop/shoopdaloop/src/libshoopdaloop/types.h: 40

log_level_always_trace = (log_level_debug_trace + 1)# /Users/runner/work/shoopdaloop/shoopdaloop/src/libshoopdaloop/types.h: 40

log_level_debug = (log_level_always_trace + 1)# /Users/runner/work/shoopdaloop/shoopdaloop/src/libshoopdaloop/types.h: 40

log_level_info = (log_level_debug + 1)# /Users/runner/work/shoopdaloop/shoopdaloop/src/libshoopdaloop/types.h: 40

log_level_warning = (log_level_info + 1)# /Users/runner/work/shoopdaloop/shoopdaloop/src/libshoopdaloop/types.h: 40

log_level_error = (log_level_warning + 1)# /Users/runner/work/shoopdaloop/shoopdaloop/src/libshoopdaloop/types.h: 40

shoop_log_level_t = enum_anon_4# /Users/runner/work/shoopdaloop/shoopdaloop/src/libshoopdaloop/types.h: 40

enum_anon_5 = c_int# /Users/runner/work/shoopdaloop/shoopdaloop/src/libshoopdaloop/types.h: 45

Success = 0# /Users/runner/work/shoopdaloop/shoopdaloop/src/libshoopdaloop/types.h: 45

Failure = (Success + 1)# /Users/runner/work/shoopdaloop/shoopdaloop/src/libshoopdaloop/types.h: 45

shoop_result_t = enum_anon_5# /Users/runner/work/shoopdaloop/shoopdaloop/src/libshoopdaloop/types.h: 45

enum_anon_6 = c_int# /Users/runner/work/shoopdaloop/shoopdaloop/src/libshoopdaloop/types.h: 83

ChannelMode_Disabled = 0# /Users/runner/work/shoopdaloop/shoopdaloop/src/libshoopdaloop/types.h: 83

ChannelMode_Direct = (ChannelMode_Disabled + 1)# /Users/runner/work/shoopdaloop/shoopdaloop/src/libshoopdaloop/types.h: 83

ChannelMode_Dry = (ChannelMode_Direct + 1)# /Users/runner/work/shoopdaloop/shoopdaloop/src/libshoopdaloop/types.h: 83

ChannelMode_Wet = (ChannelMode_Dry + 1)# /Users/runner/work/shoopdaloop/shoopdaloop/src/libshoopdaloop/types.h: 83

CHANNEL_MODE_INVALID = (ChannelMode_Wet + 1)# /Users/runner/work/shoopdaloop/shoopdaloop/src/libshoopdaloop/types.h: 83

shoop_channel_mode_t = enum_anon_6# /Users/runner/work/shoopdaloop/shoopdaloop/src/libshoopdaloop/types.h: 83

enum_anon_7 = c_int# /Users/runner/work/shoopdaloop/shoopdaloop/src/libshoopdaloop/types.h: 90

Carla_Rack = 0# /Users/runner/work/shoopdaloop/shoopdaloop/src/libshoopdaloop/types.h: 90

Carla_Patchbay = (Carla_Rack + 1)# /Users/runner/work/shoopdaloop/shoopdaloop/src/libshoopdaloop/types.h: 90

Carla_Patchbay_16x = (Carla_Patchbay + 1)# /Users/runner/work/shoopdaloop/shoopdaloop/src/libshoopdaloop/types.h: 90

Test2x2x1 = (Carla_Patchbay_16x + 1)# /Users/runner/work/shoopdaloop/shoopdaloop/src/libshoopdaloop/types.h: 90

shoop_fx_chain_type_t = enum_anon_7# /Users/runner/work/shoopdaloop/shoopdaloop/src/libshoopdaloop/types.h: 90

enum_anon_8 = c_int# /Users/runner/work/shoopdaloop/shoopdaloop/src/libshoopdaloop/types.h: 96

ShoopPortConnectability_Internal = 1# /Users/runner/work/shoopdaloop/shoopdaloop/src/libshoopdaloop/types.h: 96

ShoopPortConnectability_External = 2# /Users/runner/work/shoopdaloop/shoopdaloop/src/libshoopdaloop/types.h: 96

shoop_port_connectability_t = enum_anon_8# /Users/runner/work/shoopdaloop/shoopdaloop/src/libshoopdaloop/types.h: 96

# /Users/runner/work/shoopdaloop/shoopdaloop/src/libshoopdaloop/types.h: 98
class struct__shoopdaloop_loop(Structure):
    pass

shoopdaloop_loop_t = struct__shoopdaloop_loop# /Users/runner/work/shoopdaloop/shoopdaloop/src/libshoopdaloop/types.h: 98

# /Users/runner/work/shoopdaloop/shoopdaloop/src/libshoopdaloop/types.h: 99
class struct__shoopdaloop_loop_audio_channel(Structure):
    pass

shoopdaloop_loop_audio_channel_t = struct__shoopdaloop_loop_audio_channel# /Users/runner/work/shoopdaloop/shoopdaloop/src/libshoopdaloop/types.h: 99

# /Users/runner/work/shoopdaloop/shoopdaloop/src/libshoopdaloop/types.h: 100
class struct__shoopdaloop_loop_midi_channel(Structure):
    pass

shoopdaloop_loop_midi_channel_t = struct__shoopdaloop_loop_midi_channel# /Users/runner/work/shoopdaloop/shoopdaloop/src/libshoopdaloop/types.h: 100

# /Users/runner/work/shoopdaloop/shoopdaloop/src/libshoopdaloop/types.h: 101
class struct__shoopdaloop_audio_port(Structure):
    pass

shoopdaloop_audio_port_t = struct__shoopdaloop_audio_port# /Users/runner/work/shoopdaloop/shoopdaloop/src/libshoopdaloop/types.h: 101

# /Users/runner/work/shoopdaloop/shoopdaloop/src/libshoopdaloop/types.h: 102
class struct__shoopdaloop_midi_port(Structure):
    pass

shoopdaloop_midi_port_t = struct__shoopdaloop_midi_port# /Users/runner/work/shoopdaloop/shoopdaloop/src/libshoopdaloop/types.h: 102

# /Users/runner/work/shoopdaloop/shoopdaloop/src/libshoopdaloop/types.h: 103
class struct__shoopdaloop_decoupled_midi_port(Structure):
    pass

shoopdaloop_decoupled_midi_port_t = struct__shoopdaloop_decoupled_midi_port# /Users/runner/work/shoopdaloop/shoopdaloop/src/libshoopdaloop/types.h: 103

# /Users/runner/work/shoopdaloop/shoopdaloop/src/libshoopdaloop/types.h: 104
class struct__shoopdaloop_backend_session(Structure):
    pass

shoop_backend_session_t = struct__shoopdaloop_backend_session# /Users/runner/work/shoopdaloop/shoopdaloop/src/libshoopdaloop/types.h: 104

# /Users/runner/work/shoopdaloop/shoopdaloop/src/libshoopdaloop/types.h: 105
class struct__shoopdaloop_fx_chain(Structure):
    pass

shoopdaloop_fx_chain_t = struct__shoopdaloop_fx_chain# /Users/runner/work/shoopdaloop/shoopdaloop/src/libshoopdaloop/types.h: 105

# /Users/runner/work/shoopdaloop/shoopdaloop/src/libshoopdaloop/types.h: 106
class struct__shoopdaloop_logger(Structure):
    pass

shoopdaloop_logger_t = struct__shoopdaloop_logger# /Users/runner/work/shoopdaloop/shoopdaloop/src/libshoopdaloop/types.h: 106

# /Users/runner/work/shoopdaloop/shoopdaloop/src/libshoopdaloop/types.h: 107
class struct__shoopdaloop_audio_driver(Structure):
    pass

shoop_audio_driver_t = struct__shoopdaloop_audio_driver# /Users/runner/work/shoopdaloop/shoopdaloop/src/libshoopdaloop/types.h: 107

# /Users/runner/work/shoopdaloop/shoopdaloop/src/libshoopdaloop/types.h: 115
class struct_anon_9(Structure):
    pass

struct_anon_9.__slots__ = [
    'mode',
    'length',
    'position',
    'maybe_next_mode',
    'maybe_next_mode_delay',
]
struct_anon_9._fields_ = [
    ('mode', shoop_loop_mode_t),
    ('length', c_uint),
    ('position', c_uint),
    ('maybe_next_mode', shoop_loop_mode_t),
    ('maybe_next_mode_delay', c_uint),
]

shoop_loop_state_info_t = struct_anon_9# /Users/runner/work/shoopdaloop/shoopdaloop/src/libshoopdaloop/types.h: 115

# /Users/runner/work/shoopdaloop/shoopdaloop/src/libshoopdaloop/types.h: 125
class struct_anon_10(Structure):
    pass

struct_anon_10.__slots__ = [
    'input_peak',
    'output_peak',
    'gain',
    'muted',
    'passthrough_muted',
    'ringbuffer_n_samples',
    'name',
]
struct_anon_10._fields_ = [
    ('input_peak', c_float),
    ('output_peak', c_float),
    ('gain', c_float),
    ('muted', c_uint),
    ('passthrough_muted', c_uint),
    ('ringbuffer_n_samples', c_uint),
    ('name', String),
]

shoop_audio_port_state_info_t = struct_anon_10# /Users/runner/work/shoopdaloop/shoopdaloop/src/libshoopdaloop/types.h: 125

# /Users/runner/work/shoopdaloop/shoopdaloop/src/libshoopdaloop/types.h: 136
class struct_anon_11(Structure):
    pass

struct_anon_11.__slots__ = [
    'n_input_events',
    'n_input_notes_active',
    'n_output_events',
    'n_output_notes_active',
    'muted',
    'passthrough_muted',
    'ringbuffer_n_samples',
    'name',
]
struct_anon_11._fields_ = [
    ('n_input_events', c_uint),
    ('n_input_notes_active', c_uint),
    ('n_output_events', c_uint),
    ('n_output_notes_active', c_uint),
    ('muted', c_uint),
    ('passthrough_muted', c_uint),
    ('ringbuffer_n_samples', c_uint),
    ('name', String),
]

shoop_midi_port_state_info_t = struct_anon_11# /Users/runner/work/shoopdaloop/shoopdaloop/src/libshoopdaloop/types.h: 136

# /Users/runner/work/shoopdaloop/shoopdaloop/src/libshoopdaloop/types.h: 140
class struct_anon_12(Structure):
    pass

struct_anon_12.__slots__ = [
    'audio_driver',
]
struct_anon_12._fields_ = [
    ('audio_driver', POINTER(shoop_audio_driver_t)),
]

shoop_backend_session_state_info_t = struct_anon_12# /Users/runner/work/shoopdaloop/shoopdaloop/src/libshoopdaloop/types.h: 140

# /Users/runner/work/shoopdaloop/shoopdaloop/src/libshoopdaloop/types.h: 151
class struct_anon_13(Structure):
    pass

struct_anon_13.__slots__ = [
    'dsp_load_percent',
    'xruns_since_last',
    'maybe_driver_handle',
    'maybe_instance_name',
    'sample_rate',
    'buffer_size',
    'active',
    'last_processed',
]
struct_anon_13._fields_ = [
    ('dsp_load_percent', c_float),
    ('xruns_since_last', c_uint),
    ('maybe_driver_handle', POINTER(None)),
    ('maybe_instance_name', String),
    ('sample_rate', c_uint),
    ('buffer_size', c_uint),
    ('active', c_uint),
    ('last_processed', c_uint),
]

shoop_audio_driver_state_t = struct_anon_13# /Users/runner/work/shoopdaloop/shoopdaloop/src/libshoopdaloop/types.h: 151

# /Users/runner/work/shoopdaloop/shoopdaloop/src/libshoopdaloop/types.h: 157
class struct_anon_14(Structure):
    pass

struct_anon_14.__slots__ = [
    'ready',
    'active',
    'visible',
]
struct_anon_14._fields_ = [
    ('ready', c_uint),
    ('active', c_uint),
    ('visible', c_uint),
]

shoop_fx_chain_state_info_t = struct_anon_14# /Users/runner/work/shoopdaloop/shoopdaloop/src/libshoopdaloop/types.h: 157

# /Users/runner/work/shoopdaloop/shoopdaloop/src/libshoopdaloop/types.h: 162
class struct_anon_15(Structure):
    pass

struct_anon_15.__slots__ = [
    'client_name_hint',
    'maybe_server_name',
]
struct_anon_15._fields_ = [
    ('client_name_hint', String),
    ('maybe_server_name', String),
]

shoop_jack_audio_driver_settings_t = struct_anon_15# /Users/runner/work/shoopdaloop/shoopdaloop/src/libshoopdaloop/types.h: 162

# /Users/runner/work/shoopdaloop/shoopdaloop/src/libshoopdaloop/types.h: 168
class struct_anon_16(Structure):
    pass

struct_anon_16.__slots__ = [
    'client_name',
    'sample_rate',
    'buffer_size',
]
struct_anon_16._fields_ = [
    ('client_name', String),
    ('sample_rate', c_uint),
    ('buffer_size', c_uint),
]

shoop_dummy_audio_driver_settings_t = struct_anon_16# /Users/runner/work/shoopdaloop/shoopdaloop/src/libshoopdaloop/types.h: 168

enum_anon_17 = c_int# /Users/runner/work/shoopdaloop/shoopdaloop/src/libshoopdaloop/types.h: 174

ShoopPortDirection_Input = 0# /Users/runner/work/shoopdaloop/shoopdaloop/src/libshoopdaloop/types.h: 174

ShoopPortDirection_Output = (ShoopPortDirection_Input + 1)# /Users/runner/work/shoopdaloop/shoopdaloop/src/libshoopdaloop/types.h: 174

ShoopPortDirection_Any = (ShoopPortDirection_Output + 1)# /Users/runner/work/shoopdaloop/shoopdaloop/src/libshoopdaloop/types.h: 174

shoop_port_direction_t = enum_anon_17# /Users/runner/work/shoopdaloop/shoopdaloop/src/libshoopdaloop/types.h: 174

# /Users/runner/work/shoopdaloop/shoopdaloop/src/libshoopdaloop/types.h: 185
class struct_anon_18(Structure):
    pass

struct_anon_18.__slots__ = [
    'mode',
    'gain',
    'output_peak',
    'length',
    'start_offset',
    'played_back_sample',
    'n_preplay_samples',
    'data_dirty',
]
struct_anon_18._fields_ = [
    ('mode', shoop_channel_mode_t),
    ('gain', c_float),
    ('output_peak', c_float),
    ('length', c_uint),
    ('start_offset', c_int),
    ('played_back_sample', c_int),
    ('n_preplay_samples', c_uint),
    ('data_dirty', c_uint),
]

shoop_audio_channel_state_info_t = struct_anon_18# /Users/runner/work/shoopdaloop/shoopdaloop/src/libshoopdaloop/types.h: 185

# /Users/runner/work/shoopdaloop/shoopdaloop/src/libshoopdaloop/types.h: 196
class struct_anon_19(Structure):
    pass

struct_anon_19.__slots__ = [
    'mode',
    'n_events_triggered',
    'n_notes_active',
    'length',
    'start_offset',
    'played_back_sample',
    'n_preplay_samples',
    'data_dirty',
]
struct_anon_19._fields_ = [
    ('mode', shoop_channel_mode_t),
    ('n_events_triggered', c_uint),
    ('n_notes_active', c_uint),
    ('length', c_uint),
    ('start_offset', c_int),
    ('played_back_sample', c_int),
    ('n_preplay_samples', c_uint),
    ('data_dirty', c_uint),
]

shoop_midi_channel_state_info_t = struct_anon_19# /Users/runner/work/shoopdaloop/shoopdaloop/src/libshoopdaloop/types.h: 196

# /Users/runner/work/shoopdaloop/shoopdaloop/src/libshoopdaloop/types.h: 201
class struct_anon_20(Structure):
    pass

struct_anon_20.__slots__ = [
    'n_samples',
    'data',
]
struct_anon_20._fields_ = [
    ('n_samples', c_uint),
    ('data', POINTER(audio_sample_t)),
]

shoop_audio_channel_data_t = struct_anon_20# /Users/runner/work/shoopdaloop/shoopdaloop/src/libshoopdaloop/types.h: 201

# /Users/runner/work/shoopdaloop/shoopdaloop/src/libshoopdaloop/types.h: 210
class struct_anon_21(Structure):
    pass

struct_anon_21.__slots__ = [
    'time',
    'size',
    'data',
]
struct_anon_21._fields_ = [
    ('time', c_int),
    ('size', c_uint),
    ('data', POINTER(c_ubyte)),
]

shoop_midi_event_t = struct_anon_21# /Users/runner/work/shoopdaloop/shoopdaloop/src/libshoopdaloop/types.h: 210

# /Users/runner/work/shoopdaloop/shoopdaloop/src/libshoopdaloop/types.h: 216
class struct_anon_22(Structure):
    pass

struct_anon_22.__slots__ = [
    'n_events',
    'events',
    'length_samples',
]
struct_anon_22._fields_ = [
    ('n_events', c_uint),
    ('events', POINTER(POINTER(shoop_midi_event_t))),
    ('length_samples', c_uint),
]

shoop_midi_sequence_t = struct_anon_22# /Users/runner/work/shoopdaloop/shoopdaloop/src/libshoopdaloop/types.h: 216

# /Users/runner/work/shoopdaloop/shoopdaloop/src/libshoopdaloop/types.h: 224
class struct_anon_23(Structure):
    pass

struct_anon_23.__slots__ = [
    'key',
    'n_samples',
    'average',
    'worst',
    'most_recent',
]
struct_anon_23._fields_ = [
    ('key', String),
    ('n_samples', c_float),
    ('average', c_float),
    ('worst', c_float),
    ('most_recent', c_float),
]

shoop_profiling_report_item_t = struct_anon_23# /Users/runner/work/shoopdaloop/shoopdaloop/src/libshoopdaloop/types.h: 224

# /Users/runner/work/shoopdaloop/shoopdaloop/src/libshoopdaloop/types.h: 229
class struct_anon_24(Structure):
    pass

struct_anon_24.__slots__ = [
    'n_items',
    'items',
]
struct_anon_24._fields_ = [
    ('n_items', c_uint),
    ('items', POINTER(shoop_profiling_report_item_t)),
]

shoop_profiling_report_t = struct_anon_24# /Users/runner/work/shoopdaloop/shoopdaloop/src/libshoopdaloop/types.h: 229

# /Users/runner/work/shoopdaloop/shoopdaloop/src/libshoopdaloop/types.h: 234
class struct_anon_25(Structure):
    pass

struct_anon_25.__slots__ = [
    'name',
    'connected',
]
struct_anon_25._fields_ = [
    ('name', String),
    ('connected', c_uint),
]

shoop_port_maybe_connection_t = struct_anon_25# /Users/runner/work/shoopdaloop/shoopdaloop/src/libshoopdaloop/types.h: 234

# /Users/runner/work/shoopdaloop/shoopdaloop/src/libshoopdaloop/types.h: 239
class struct_anon_26(Structure):
    pass

struct_anon_26.__slots__ = [
    'n_ports',
    'ports',
]
struct_anon_26._fields_ = [
    ('n_ports', c_uint),
    ('ports', POINTER(shoop_port_maybe_connection_t)),
]

shoop_port_connections_state_t = struct_anon_26# /Users/runner/work/shoopdaloop/shoopdaloop/src/libshoopdaloop/types.h: 239

# /Users/runner/work/shoopdaloop/shoopdaloop/src/libshoopdaloop/types.h: 245
class struct_anon_27(Structure):
    pass

struct_anon_27.__slots__ = [
    'n_channels',
    'n_frames',
    'data',
]
struct_anon_27._fields_ = [
    ('n_channels', c_uint),
    ('n_frames', c_uint),
    ('data', POINTER(audio_sample_t)),
]

shoop_multichannel_audio_t = struct_anon_27# /Users/runner/work/shoopdaloop/shoopdaloop/src/libshoopdaloop/types.h: 245

# /Users/runner/work/shoopdaloop/shoopdaloop/src/libshoopdaloop/types.h: 251
class struct_anon_28(Structure):
    pass

struct_anon_28.__slots__ = [
    'data_type',
    'direction',
    'name',
]
struct_anon_28._fields_ = [
    ('data_type', shoop_port_data_type_t),
    ('direction', shoop_port_direction_t),
    ('name', String),
]

shoop_external_port_descriptor_t = struct_anon_28# /Users/runner/work/shoopdaloop/shoopdaloop/src/libshoopdaloop/types.h: 251

# /Users/runner/work/shoopdaloop/shoopdaloop/src/libshoopdaloop/types.h: 256
class struct_anon_29(Structure):
    pass

struct_anon_29.__slots__ = [
    'n_ports',
    'ports',
]
struct_anon_29._fields_ = [
    ('n_ports', c_uint),
    ('ports', POINTER(shoop_external_port_descriptor_t)),
]

shoop_external_port_descriptors_t = struct_anon_29# /Users/runner/work/shoopdaloop/shoopdaloop/src/libshoopdaloop/types.h: 256

# /Users/runner/work/shoopdaloop/shoopdaloop/src/libshoopdaloop/libshoopdaloop.h: 14
if _libs["shoopdaloop"].has("create_audio_driver", "cdecl"):
    create_audio_driver = _libs["shoopdaloop"].get("create_audio_driver", "cdecl")
    create_audio_driver.argtypes = [shoop_audio_driver_type_t]
    create_audio_driver.restype = POINTER(shoop_audio_driver_t)

# /Users/runner/work/shoopdaloop/shoopdaloop/src/libshoopdaloop/libshoopdaloop.h: 15
if _libs["shoopdaloop"].has("get_audio_driver_state", "cdecl"):
    get_audio_driver_state = _libs["shoopdaloop"].get("get_audio_driver_state", "cdecl")
    get_audio_driver_state.argtypes = [POINTER(shoop_audio_driver_t)]
    get_audio_driver_state.restype = POINTER(shoop_audio_driver_state_t)

# /Users/runner/work/shoopdaloop/shoopdaloop/src/libshoopdaloop/libshoopdaloop.h: 16
if _libs["shoopdaloop"].has("driver_type_supported", "cdecl"):
    driver_type_supported = _libs["shoopdaloop"].get("driver_type_supported", "cdecl")
    driver_type_supported.argtypes = [shoop_audio_driver_type_t]
    driver_type_supported.restype = c_uint

# /Users/runner/work/shoopdaloop/shoopdaloop/src/libshoopdaloop/libshoopdaloop.h: 17
if _libs["shoopdaloop"].has("destroy_audio_driver", "cdecl"):
    destroy_audio_driver = _libs["shoopdaloop"].get("destroy_audio_driver", "cdecl")
    destroy_audio_driver.argtypes = [POINTER(shoop_audio_driver_t)]
    destroy_audio_driver.restype = None

# /Users/runner/work/shoopdaloop/shoopdaloop/src/libshoopdaloop/libshoopdaloop.h: 18
if _libs["shoopdaloop"].has("maybe_driver_handle", "cdecl"):
    maybe_driver_handle = _libs["shoopdaloop"].get("maybe_driver_handle", "cdecl")
    maybe_driver_handle.argtypes = [POINTER(shoop_audio_driver_t)]
    maybe_driver_handle.restype = POINTER(c_ubyte)
    maybe_driver_handle.errcheck = lambda v,*a : cast(v, c_void_p)

# /Users/runner/work/shoopdaloop/shoopdaloop/src/libshoopdaloop/libshoopdaloop.h: 19
if _libs["shoopdaloop"].has("maybe_driver_instance_name", "cdecl"):
    maybe_driver_instance_name = _libs["shoopdaloop"].get("maybe_driver_instance_name", "cdecl")
    maybe_driver_instance_name.argtypes = [POINTER(shoop_audio_driver_t)]
    maybe_driver_instance_name.restype = c_char_p

# /Users/runner/work/shoopdaloop/shoopdaloop/src/libshoopdaloop/libshoopdaloop.h: 20
if _libs["shoopdaloop"].has("get_sample_rate", "cdecl"):
    get_sample_rate = _libs["shoopdaloop"].get("get_sample_rate", "cdecl")
    get_sample_rate.argtypes = [POINTER(shoop_audio_driver_t)]
    get_sample_rate.restype = c_uint

# /Users/runner/work/shoopdaloop/shoopdaloop/src/libshoopdaloop/libshoopdaloop.h: 21
if _libs["shoopdaloop"].has("get_buffer_size", "cdecl"):
    get_buffer_size = _libs["shoopdaloop"].get("get_buffer_size", "cdecl")
    get_buffer_size.argtypes = [POINTER(shoop_audio_driver_t)]
    get_buffer_size.restype = c_uint

# /Users/runner/work/shoopdaloop/shoopdaloop/src/libshoopdaloop/libshoopdaloop.h: 22
if _libs["shoopdaloop"].has("get_driver_active", "cdecl"):
    get_driver_active = _libs["shoopdaloop"].get("get_driver_active", "cdecl")
    get_driver_active.argtypes = [POINTER(shoop_audio_driver_t)]
    get_driver_active.restype = c_uint

# /Users/runner/work/shoopdaloop/shoopdaloop/src/libshoopdaloop/libshoopdaloop.h: 23
if _libs["shoopdaloop"].has("start_dummy_driver", "cdecl"):
    start_dummy_driver = _libs["shoopdaloop"].get("start_dummy_driver", "cdecl")
    start_dummy_driver.argtypes = [POINTER(shoop_audio_driver_t), shoop_dummy_audio_driver_settings_t]
    start_dummy_driver.restype = None

# /Users/runner/work/shoopdaloop/shoopdaloop/src/libshoopdaloop/libshoopdaloop.h: 24
if _libs["shoopdaloop"].has("start_jack_driver", "cdecl"):
    start_jack_driver = _libs["shoopdaloop"].get("start_jack_driver", "cdecl")
    start_jack_driver.argtypes = [POINTER(shoop_audio_driver_t), shoop_jack_audio_driver_settings_t]
    start_jack_driver.restype = None

# /Users/runner/work/shoopdaloop/shoopdaloop/src/libshoopdaloop/libshoopdaloop.h: 25
if _libs["shoopdaloop"].has("wait_process", "cdecl"):
    wait_process = _libs["shoopdaloop"].get("wait_process", "cdecl")
    wait_process.argtypes = [POINTER(shoop_audio_driver_t)]
    wait_process.restype = None

# /Users/runner/work/shoopdaloop/shoopdaloop/src/libshoopdaloop/libshoopdaloop.h: 26
if _libs["shoopdaloop"].has("find_external_ports", "cdecl"):
    find_external_ports = _libs["shoopdaloop"].get("find_external_ports", "cdecl")
    find_external_ports.argtypes = [POINTER(shoop_audio_driver_t), String, shoop_port_direction_t, shoop_port_data_type_t]
    find_external_ports.restype = POINTER(shoop_external_port_descriptors_t)

# /Users/runner/work/shoopdaloop/shoopdaloop/src/libshoopdaloop/libshoopdaloop.h: 29
if _libs["shoopdaloop"].has("do_segfault_on_process_thread", "cdecl"):
    do_segfault_on_process_thread = _libs["shoopdaloop"].get("do_segfault_on_process_thread", "cdecl")
    do_segfault_on_process_thread.argtypes = [POINTER(shoop_backend_session_t)]
    do_segfault_on_process_thread.restype = None

# /Users/runner/work/shoopdaloop/shoopdaloop/src/libshoopdaloop/libshoopdaloop.h: 30
if _libs["shoopdaloop"].has("do_abort_on_process_thread", "cdecl"):
    do_abort_on_process_thread = _libs["shoopdaloop"].get("do_abort_on_process_thread", "cdecl")
    do_abort_on_process_thread.argtypes = [POINTER(shoop_backend_session_t)]
    do_abort_on_process_thread.restype = None

# /Users/runner/work/shoopdaloop/shoopdaloop/src/libshoopdaloop/libshoopdaloop.h: 33
if _libs["shoopdaloop"].has("create_backend_session", "cdecl"):
    create_backend_session = _libs["shoopdaloop"].get("create_backend_session", "cdecl")
    create_backend_session.argtypes = []
    create_backend_session.restype = POINTER(shoop_backend_session_t)

# /Users/runner/work/shoopdaloop/shoopdaloop/src/libshoopdaloop/libshoopdaloop.h: 34
if _libs["shoopdaloop"].has("destroy_backend_session", "cdecl"):
    destroy_backend_session = _libs["shoopdaloop"].get("destroy_backend_session", "cdecl")
    destroy_backend_session.argtypes = [POINTER(shoop_backend_session_t)]
    destroy_backend_session.restype = None

# /Users/runner/work/shoopdaloop/shoopdaloop/src/libshoopdaloop/libshoopdaloop.h: 35
if _libs["shoopdaloop"].has("get_backend_session_state", "cdecl"):
    get_backend_session_state = _libs["shoopdaloop"].get("get_backend_session_state", "cdecl")
    get_backend_session_state.argtypes = [POINTER(shoop_backend_session_t)]
    get_backend_session_state.restype = POINTER(shoop_backend_session_state_info_t)

# /Users/runner/work/shoopdaloop/shoopdaloop/src/libshoopdaloop/libshoopdaloop.h: 36
if _libs["shoopdaloop"].has("get_profiling_report", "cdecl"):
    get_profiling_report = _libs["shoopdaloop"].get("get_profiling_report", "cdecl")
    get_profiling_report.argtypes = [POINTER(shoop_backend_session_t)]
    get_profiling_report.restype = POINTER(shoop_profiling_report_t)

# /Users/runner/work/shoopdaloop/shoopdaloop/src/libshoopdaloop/libshoopdaloop.h: 37
if _libs["shoopdaloop"].has("set_audio_driver", "cdecl"):
    set_audio_driver = _libs["shoopdaloop"].get("set_audio_driver", "cdecl")
    set_audio_driver.argtypes = [POINTER(shoop_backend_session_t), POINTER(shoop_audio_driver_t)]
    set_audio_driver.restype = shoop_result_t

# /Users/runner/work/shoopdaloop/shoopdaloop/src/libshoopdaloop/libshoopdaloop.h: 40
if _libs["shoopdaloop"].has("create_loop", "cdecl"):
    create_loop = _libs["shoopdaloop"].get("create_loop", "cdecl")
    create_loop.argtypes = [POINTER(shoop_backend_session_t)]
    create_loop.restype = POINTER(shoopdaloop_loop_t)

# /Users/runner/work/shoopdaloop/shoopdaloop/src/libshoopdaloop/libshoopdaloop.h: 41
if _libs["shoopdaloop"].has("add_audio_channel", "cdecl"):
    add_audio_channel = _libs["shoopdaloop"].get("add_audio_channel", "cdecl")
    add_audio_channel.argtypes = [POINTER(shoopdaloop_loop_t), shoop_channel_mode_t]
    add_audio_channel.restype = POINTER(shoopdaloop_loop_audio_channel_t)

# /Users/runner/work/shoopdaloop/shoopdaloop/src/libshoopdaloop/libshoopdaloop.h: 42
if _libs["shoopdaloop"].has("add_midi_channel", "cdecl"):
    add_midi_channel = _libs["shoopdaloop"].get("add_midi_channel", "cdecl")
    add_midi_channel.argtypes = [POINTER(shoopdaloop_loop_t), shoop_channel_mode_t]
    add_midi_channel.restype = POINTER(shoopdaloop_loop_midi_channel_t)

# /Users/runner/work/shoopdaloop/shoopdaloop/src/libshoopdaloop/libshoopdaloop.h: 43
if _libs["shoopdaloop"].has("get_n_audio_channels", "cdecl"):
    get_n_audio_channels = _libs["shoopdaloop"].get("get_n_audio_channels", "cdecl")
    get_n_audio_channels.argtypes = [POINTER(shoopdaloop_loop_t)]
    get_n_audio_channels.restype = c_uint

# /Users/runner/work/shoopdaloop/shoopdaloop/src/libshoopdaloop/libshoopdaloop.h: 44
if _libs["shoopdaloop"].has("get_n_midi_channels", "cdecl"):
    get_n_midi_channels = _libs["shoopdaloop"].get("get_n_midi_channels", "cdecl")
    get_n_midi_channels.argtypes = [POINTER(shoopdaloop_loop_t)]
    get_n_midi_channels.restype = c_uint

# /Users/runner/work/shoopdaloop/shoopdaloop/src/libshoopdaloop/libshoopdaloop.h: 45
if _libs["shoopdaloop"].has("clear_loop", "cdecl"):
    clear_loop = _libs["shoopdaloop"].get("clear_loop", "cdecl")
    clear_loop.argtypes = [POINTER(shoopdaloop_loop_t), c_uint]
    clear_loop.restype = None

# /Users/runner/work/shoopdaloop/shoopdaloop/src/libshoopdaloop/libshoopdaloop.h: 46
if _libs["shoopdaloop"].has("get_loop_state", "cdecl"):
    get_loop_state = _libs["shoopdaloop"].get("get_loop_state", "cdecl")
    get_loop_state.argtypes = [POINTER(shoopdaloop_loop_t)]
    get_loop_state.restype = POINTER(shoop_loop_state_info_t)

# /Users/runner/work/shoopdaloop/shoopdaloop/src/libshoopdaloop/libshoopdaloop.h: 47
if _libs["shoopdaloop"].has("set_loop_length", "cdecl"):
    set_loop_length = _libs["shoopdaloop"].get("set_loop_length", "cdecl")
    set_loop_length.argtypes = [POINTER(shoopdaloop_loop_t), c_uint]
    set_loop_length.restype = None

# /Users/runner/work/shoopdaloop/shoopdaloop/src/libshoopdaloop/libshoopdaloop.h: 48
if _libs["shoopdaloop"].has("set_loop_position", "cdecl"):
    set_loop_position = _libs["shoopdaloop"].get("set_loop_position", "cdecl")
    set_loop_position.argtypes = [POINTER(shoopdaloop_loop_t), c_uint]
    set_loop_position.restype = None

# /Users/runner/work/shoopdaloop/shoopdaloop/src/libshoopdaloop/libshoopdaloop.h: 49
if _libs["shoopdaloop"].has("set_loop_sync_source", "cdecl"):
    set_loop_sync_source = _libs["shoopdaloop"].get("set_loop_sync_source", "cdecl")
    set_loop_sync_source.argtypes = [POINTER(shoopdaloop_loop_t), POINTER(shoopdaloop_loop_t)]
    set_loop_sync_source.restype = None

# /Users/runner/work/shoopdaloop/shoopdaloop/src/libshoopdaloop/libshoopdaloop.h: 50
if _libs["shoopdaloop"].has("adopt_ringbuffer_contents", "cdecl"):
    adopt_ringbuffer_contents = _libs["shoopdaloop"].get("adopt_ringbuffer_contents", "cdecl")
    adopt_ringbuffer_contents.argtypes = [POINTER(shoopdaloop_loop_t), c_int, c_int, c_int, shoop_loop_mode_t]
    adopt_ringbuffer_contents.restype = None

# /Users/runner/work/shoopdaloop/shoopdaloop/src/libshoopdaloop/libshoopdaloop.h: 57
if _libs["shoopdaloop"].has("loop_transition", "cdecl"):
    loop_transition = _libs["shoopdaloop"].get("loop_transition", "cdecl")
    loop_transition.argtypes = [POINTER(shoopdaloop_loop_t), shoop_loop_mode_t, c_int, c_int]
    loop_transition.restype = None

# /Users/runner/work/shoopdaloop/shoopdaloop/src/libshoopdaloop/libshoopdaloop.h: 61
if _libs["shoopdaloop"].has("loops_transition", "cdecl"):
    loops_transition = _libs["shoopdaloop"].get("loops_transition", "cdecl")
    loops_transition.argtypes = [c_uint, POINTER(POINTER(shoopdaloop_loop_t)), shoop_loop_mode_t, c_int, c_int]
    loops_transition.restype = None

# /Users/runner/work/shoopdaloop/shoopdaloop/src/libshoopdaloop/libshoopdaloop.h: 68
if _libs["shoopdaloop"].has("clear_audio_channel", "cdecl"):
    clear_audio_channel = _libs["shoopdaloop"].get("clear_audio_channel", "cdecl")
    clear_audio_channel.argtypes = [POINTER(shoopdaloop_loop_audio_channel_t), c_uint]
    clear_audio_channel.restype = None

# /Users/runner/work/shoopdaloop/shoopdaloop/src/libshoopdaloop/libshoopdaloop.h: 69
if _libs["shoopdaloop"].has("clear_midi_channel", "cdecl"):
    clear_midi_channel = _libs["shoopdaloop"].get("clear_midi_channel", "cdecl")
    clear_midi_channel.argtypes = [POINTER(shoopdaloop_loop_midi_channel_t)]
    clear_midi_channel.restype = None

# /Users/runner/work/shoopdaloop/shoopdaloop/src/libshoopdaloop/libshoopdaloop.h: 70
if _libs["shoopdaloop"].has("connect_audio_output", "cdecl"):
    connect_audio_output = _libs["shoopdaloop"].get("connect_audio_output", "cdecl")
    connect_audio_output.argtypes = [POINTER(shoopdaloop_loop_audio_channel_t), POINTER(shoopdaloop_audio_port_t)]
    connect_audio_output.restype = None

# /Users/runner/work/shoopdaloop/shoopdaloop/src/libshoopdaloop/libshoopdaloop.h: 71
if _libs["shoopdaloop"].has("connect_midi_output", "cdecl"):
    connect_midi_output = _libs["shoopdaloop"].get("connect_midi_output", "cdecl")
    connect_midi_output.argtypes = [POINTER(shoopdaloop_loop_midi_channel_t), POINTER(shoopdaloop_midi_port_t)]
    connect_midi_output.restype = None

# /Users/runner/work/shoopdaloop/shoopdaloop/src/libshoopdaloop/libshoopdaloop.h: 72
if _libs["shoopdaloop"].has("connect_audio_input", "cdecl"):
    connect_audio_input = _libs["shoopdaloop"].get("connect_audio_input", "cdecl")
    connect_audio_input.argtypes = [POINTER(shoopdaloop_loop_audio_channel_t), POINTER(shoopdaloop_audio_port_t)]
    connect_audio_input.restype = None

# /Users/runner/work/shoopdaloop/shoopdaloop/src/libshoopdaloop/libshoopdaloop.h: 73
if _libs["shoopdaloop"].has("connect_midi_input", "cdecl"):
    connect_midi_input = _libs["shoopdaloop"].get("connect_midi_input", "cdecl")
    connect_midi_input.argtypes = [POINTER(shoopdaloop_loop_midi_channel_t), POINTER(shoopdaloop_midi_port_t)]
    connect_midi_input.restype = None

# /Users/runner/work/shoopdaloop/shoopdaloop/src/libshoopdaloop/libshoopdaloop.h: 74
if _libs["shoopdaloop"].has("disconnect_audio_outputs", "cdecl"):
    disconnect_audio_outputs = _libs["shoopdaloop"].get("disconnect_audio_outputs", "cdecl")
    disconnect_audio_outputs.argtypes = [POINTER(shoopdaloop_loop_audio_channel_t)]
    disconnect_audio_outputs.restype = None

# /Users/runner/work/shoopdaloop/shoopdaloop/src/libshoopdaloop/libshoopdaloop.h: 75
if _libs["shoopdaloop"].has("disconnect_midi_outputs", "cdecl"):
    disconnect_midi_outputs = _libs["shoopdaloop"].get("disconnect_midi_outputs", "cdecl")
    disconnect_midi_outputs.argtypes = [POINTER(shoopdaloop_loop_midi_channel_t)]
    disconnect_midi_outputs.restype = None

# /Users/runner/work/shoopdaloop/shoopdaloop/src/libshoopdaloop/libshoopdaloop.h: 76
if _libs["shoopdaloop"].has("disconnect_audio_output", "cdecl"):
    disconnect_audio_output = _libs["shoopdaloop"].get("disconnect_audio_output", "cdecl")
    disconnect_audio_output.argtypes = [POINTER(shoopdaloop_loop_audio_channel_t), POINTER(shoopdaloop_audio_port_t)]
    disconnect_audio_output.restype = None

# /Users/runner/work/shoopdaloop/shoopdaloop/src/libshoopdaloop/libshoopdaloop.h: 77
if _libs["shoopdaloop"].has("disconnect_midi_output", "cdecl"):
    disconnect_midi_output = _libs["shoopdaloop"].get("disconnect_midi_output", "cdecl")
    disconnect_midi_output.argtypes = [POINTER(shoopdaloop_loop_midi_channel_t), POINTER(shoopdaloop_midi_port_t)]
    disconnect_midi_output.restype = None

# /Users/runner/work/shoopdaloop/shoopdaloop/src/libshoopdaloop/libshoopdaloop.h: 78
if _libs["shoopdaloop"].has("disconnect_audio_inputs", "cdecl"):
    disconnect_audio_inputs = _libs["shoopdaloop"].get("disconnect_audio_inputs", "cdecl")
    disconnect_audio_inputs.argtypes = [POINTER(shoopdaloop_loop_audio_channel_t)]
    disconnect_audio_inputs.restype = None

# /Users/runner/work/shoopdaloop/shoopdaloop/src/libshoopdaloop/libshoopdaloop.h: 79
if _libs["shoopdaloop"].has("disconnect_midi_inputs", "cdecl"):
    disconnect_midi_inputs = _libs["shoopdaloop"].get("disconnect_midi_inputs", "cdecl")
    disconnect_midi_inputs.argtypes = [POINTER(shoopdaloop_loop_midi_channel_t)]
    disconnect_midi_inputs.restype = None

# /Users/runner/work/shoopdaloop/shoopdaloop/src/libshoopdaloop/libshoopdaloop.h: 80
if _libs["shoopdaloop"].has("disconnect_audio_input", "cdecl"):
    disconnect_audio_input = _libs["shoopdaloop"].get("disconnect_audio_input", "cdecl")
    disconnect_audio_input.argtypes = [POINTER(shoopdaloop_loop_audio_channel_t), POINTER(shoopdaloop_audio_port_t)]
    disconnect_audio_input.restype = None

# /Users/runner/work/shoopdaloop/shoopdaloop/src/libshoopdaloop/libshoopdaloop.h: 81
if _libs["shoopdaloop"].has("disconnect_midi_input", "cdecl"):
    disconnect_midi_input = _libs["shoopdaloop"].get("disconnect_midi_input", "cdecl")
    disconnect_midi_input.argtypes = [POINTER(shoopdaloop_loop_midi_channel_t), POINTER(shoopdaloop_midi_port_t)]
    disconnect_midi_input.restype = None

# /Users/runner/work/shoopdaloop/shoopdaloop/src/libshoopdaloop/libshoopdaloop.h: 82
if _libs["shoopdaloop"].has("get_audio_channel_data", "cdecl"):
    get_audio_channel_data = _libs["shoopdaloop"].get("get_audio_channel_data", "cdecl")
    get_audio_channel_data.argtypes = [POINTER(shoopdaloop_loop_audio_channel_t)]
    get_audio_channel_data.restype = POINTER(shoop_audio_channel_data_t)

# /Users/runner/work/shoopdaloop/shoopdaloop/src/libshoopdaloop/libshoopdaloop.h: 83
if _libs["shoopdaloop"].has("get_midi_channel_data", "cdecl"):
    get_midi_channel_data = _libs["shoopdaloop"].get("get_midi_channel_data", "cdecl")
    get_midi_channel_data.argtypes = [POINTER(shoopdaloop_loop_midi_channel_t)]
    get_midi_channel_data.restype = POINTER(shoop_midi_sequence_t)

# /Users/runner/work/shoopdaloop/shoopdaloop/src/libshoopdaloop/libshoopdaloop.h: 84
if _libs["shoopdaloop"].has("load_audio_channel_data", "cdecl"):
    load_audio_channel_data = _libs["shoopdaloop"].get("load_audio_channel_data", "cdecl")
    load_audio_channel_data.argtypes = [POINTER(shoopdaloop_loop_audio_channel_t), POINTER(shoop_audio_channel_data_t)]
    load_audio_channel_data.restype = None

# /Users/runner/work/shoopdaloop/shoopdaloop/src/libshoopdaloop/libshoopdaloop.h: 85
if _libs["shoopdaloop"].has("load_midi_channel_data", "cdecl"):
    load_midi_channel_data = _libs["shoopdaloop"].get("load_midi_channel_data", "cdecl")
    load_midi_channel_data.argtypes = [POINTER(shoopdaloop_loop_midi_channel_t), POINTER(shoop_midi_sequence_t)]
    load_midi_channel_data.restype = None

# /Users/runner/work/shoopdaloop/shoopdaloop/src/libshoopdaloop/libshoopdaloop.h: 86
if _libs["shoopdaloop"].has("get_audio_channel_state", "cdecl"):
    get_audio_channel_state = _libs["shoopdaloop"].get("get_audio_channel_state", "cdecl")
    get_audio_channel_state.argtypes = [POINTER(shoopdaloop_loop_audio_channel_t)]
    get_audio_channel_state.restype = POINTER(shoop_audio_channel_state_info_t)

# /Users/runner/work/shoopdaloop/shoopdaloop/src/libshoopdaloop/libshoopdaloop.h: 87
if _libs["shoopdaloop"].has("set_audio_channel_gain", "cdecl"):
    set_audio_channel_gain = _libs["shoopdaloop"].get("set_audio_channel_gain", "cdecl")
    set_audio_channel_gain.argtypes = [POINTER(shoopdaloop_loop_audio_channel_t), c_float]
    set_audio_channel_gain.restype = None

# /Users/runner/work/shoopdaloop/shoopdaloop/src/libshoopdaloop/libshoopdaloop.h: 88
if _libs["shoopdaloop"].has("get_midi_channel_state", "cdecl"):
    get_midi_channel_state = _libs["shoopdaloop"].get("get_midi_channel_state", "cdecl")
    get_midi_channel_state.argtypes = [POINTER(shoopdaloop_loop_midi_channel_t)]
    get_midi_channel_state.restype = POINTER(shoop_midi_channel_state_info_t)

# /Users/runner/work/shoopdaloop/shoopdaloop/src/libshoopdaloop/libshoopdaloop.h: 89
if _libs["shoopdaloop"].has("set_audio_channel_mode", "cdecl"):
    set_audio_channel_mode = _libs["shoopdaloop"].get("set_audio_channel_mode", "cdecl")
    set_audio_channel_mode.argtypes = [POINTER(shoopdaloop_loop_audio_channel_t), shoop_channel_mode_t]
    set_audio_channel_mode.restype = None

# /Users/runner/work/shoopdaloop/shoopdaloop/src/libshoopdaloop/libshoopdaloop.h: 90
if _libs["shoopdaloop"].has("set_midi_channel_mode", "cdecl"):
    set_midi_channel_mode = _libs["shoopdaloop"].get("set_midi_channel_mode", "cdecl")
    set_midi_channel_mode.argtypes = [POINTER(shoopdaloop_loop_midi_channel_t), shoop_channel_mode_t]
    set_midi_channel_mode.restype = None

# /Users/runner/work/shoopdaloop/shoopdaloop/src/libshoopdaloop/libshoopdaloop.h: 91
if _libs["shoopdaloop"].has("set_audio_channel_start_offset", "cdecl"):
    set_audio_channel_start_offset = _libs["shoopdaloop"].get("set_audio_channel_start_offset", "cdecl")
    set_audio_channel_start_offset.argtypes = [POINTER(shoopdaloop_loop_audio_channel_t), c_int]
    set_audio_channel_start_offset.restype = None

# /Users/runner/work/shoopdaloop/shoopdaloop/src/libshoopdaloop/libshoopdaloop.h: 92
if _libs["shoopdaloop"].has("set_midi_channel_start_offset", "cdecl"):
    set_midi_channel_start_offset = _libs["shoopdaloop"].get("set_midi_channel_start_offset", "cdecl")
    set_midi_channel_start_offset.argtypes = [POINTER(shoopdaloop_loop_midi_channel_t), c_int]
    set_midi_channel_start_offset.restype = None

# /Users/runner/work/shoopdaloop/shoopdaloop/src/libshoopdaloop/libshoopdaloop.h: 93
if _libs["shoopdaloop"].has("set_audio_channel_n_preplay_samples", "cdecl"):
    set_audio_channel_n_preplay_samples = _libs["shoopdaloop"].get("set_audio_channel_n_preplay_samples", "cdecl")
    set_audio_channel_n_preplay_samples.argtypes = [POINTER(shoopdaloop_loop_audio_channel_t), c_uint]
    set_audio_channel_n_preplay_samples.restype = None

# /Users/runner/work/shoopdaloop/shoopdaloop/src/libshoopdaloop/libshoopdaloop.h: 94
if _libs["shoopdaloop"].has("set_midi_channel_n_preplay_samples", "cdecl"):
    set_midi_channel_n_preplay_samples = _libs["shoopdaloop"].get("set_midi_channel_n_preplay_samples", "cdecl")
    set_midi_channel_n_preplay_samples.argtypes = [POINTER(shoopdaloop_loop_midi_channel_t), c_uint]
    set_midi_channel_n_preplay_samples.restype = None

# /Users/runner/work/shoopdaloop/shoopdaloop/src/libshoopdaloop/libshoopdaloop.h: 95
if _libs["shoopdaloop"].has("clear_audio_channel_data_dirty", "cdecl"):
    clear_audio_channel_data_dirty = _libs["shoopdaloop"].get("clear_audio_channel_data_dirty", "cdecl")
    clear_audio_channel_data_dirty.argtypes = [POINTER(shoopdaloop_loop_audio_channel_t)]
    clear_audio_channel_data_dirty.restype = None

# /Users/runner/work/shoopdaloop/shoopdaloop/src/libshoopdaloop/libshoopdaloop.h: 96
if _libs["shoopdaloop"].has("clear_midi_channel_data_dirty", "cdecl"):
    clear_midi_channel_data_dirty = _libs["shoopdaloop"].get("clear_midi_channel_data_dirty", "cdecl")
    clear_midi_channel_data_dirty.argtypes = [POINTER(shoopdaloop_loop_midi_channel_t)]
    clear_midi_channel_data_dirty.restype = None

# /Users/runner/work/shoopdaloop/shoopdaloop/src/libshoopdaloop/libshoopdaloop.h: 97
if _libs["shoopdaloop"].has("reset_midi_channel_state_tracking", "cdecl"):
    reset_midi_channel_state_tracking = _libs["shoopdaloop"].get("reset_midi_channel_state_tracking", "cdecl")
    reset_midi_channel_state_tracking.argtypes = [POINTER(shoopdaloop_loop_midi_channel_t)]
    reset_midi_channel_state_tracking.restype = None

# /Users/runner/work/shoopdaloop/shoopdaloop/src/libshoopdaloop/libshoopdaloop.h: 100
if _libs["shoopdaloop"].has("create_fx_chain", "cdecl"):
    create_fx_chain = _libs["shoopdaloop"].get("create_fx_chain", "cdecl")
    create_fx_chain.argtypes = [POINTER(shoop_backend_session_t), shoop_fx_chain_type_t, String]
    create_fx_chain.restype = POINTER(shoopdaloop_fx_chain_t)

# /Users/runner/work/shoopdaloop/shoopdaloop/src/libshoopdaloop/libshoopdaloop.h: 101
if _libs["shoopdaloop"].has("fx_chain_set_ui_visible", "cdecl"):
    fx_chain_set_ui_visible = _libs["shoopdaloop"].get("fx_chain_set_ui_visible", "cdecl")
    fx_chain_set_ui_visible.argtypes = [POINTER(shoopdaloop_fx_chain_t), c_uint]
    fx_chain_set_ui_visible.restype = None

# /Users/runner/work/shoopdaloop/shoopdaloop/src/libshoopdaloop/libshoopdaloop.h: 102
if _libs["shoopdaloop"].has("get_fx_chain_state", "cdecl"):
    get_fx_chain_state = _libs["shoopdaloop"].get("get_fx_chain_state", "cdecl")
    get_fx_chain_state.argtypes = [POINTER(shoopdaloop_fx_chain_t)]
    get_fx_chain_state.restype = POINTER(shoop_fx_chain_state_info_t)

# /Users/runner/work/shoopdaloop/shoopdaloop/src/libshoopdaloop/libshoopdaloop.h: 103
if _libs["shoopdaloop"].has("set_fx_chain_active", "cdecl"):
    set_fx_chain_active = _libs["shoopdaloop"].get("set_fx_chain_active", "cdecl")
    set_fx_chain_active.argtypes = [POINTER(shoopdaloop_fx_chain_t), c_uint]
    set_fx_chain_active.restype = None

# /Users/runner/work/shoopdaloop/shoopdaloop/src/libshoopdaloop/libshoopdaloop.h: 104
if _libs["shoopdaloop"].has("get_fx_chain_internal_state", "cdecl"):
    get_fx_chain_internal_state = _libs["shoopdaloop"].get("get_fx_chain_internal_state", "cdecl")
    get_fx_chain_internal_state.argtypes = [POINTER(shoopdaloop_fx_chain_t)]
    get_fx_chain_internal_state.restype = c_char_p

# /Users/runner/work/shoopdaloop/shoopdaloop/src/libshoopdaloop/libshoopdaloop.h: 105
if _libs["shoopdaloop"].has("restore_fx_chain_internal_state", "cdecl"):
    restore_fx_chain_internal_state = _libs["shoopdaloop"].get("restore_fx_chain_internal_state", "cdecl")
    restore_fx_chain_internal_state.argtypes = [POINTER(shoopdaloop_fx_chain_t), String]
    restore_fx_chain_internal_state.restype = None

# /Users/runner/work/shoopdaloop/shoopdaloop/src/libshoopdaloop/libshoopdaloop.h: 106
if _libs["shoopdaloop"].has("n_fx_chain_audio_input_ports", "cdecl"):
    n_fx_chain_audio_input_ports = _libs["shoopdaloop"].get("n_fx_chain_audio_input_ports", "cdecl")
    n_fx_chain_audio_input_ports.argtypes = [POINTER(shoopdaloop_fx_chain_t)]
    n_fx_chain_audio_input_ports.restype = c_uint

# /Users/runner/work/shoopdaloop/shoopdaloop/src/libshoopdaloop/libshoopdaloop.h: 107
if _libs["shoopdaloop"].has("n_fx_chain_audio_output_ports", "cdecl"):
    n_fx_chain_audio_output_ports = _libs["shoopdaloop"].get("n_fx_chain_audio_output_ports", "cdecl")
    n_fx_chain_audio_output_ports.argtypes = [POINTER(shoopdaloop_fx_chain_t)]
    n_fx_chain_audio_output_ports.restype = c_uint

# /Users/runner/work/shoopdaloop/shoopdaloop/src/libshoopdaloop/libshoopdaloop.h: 108
if _libs["shoopdaloop"].has("n_fx_chain_midi_input_ports", "cdecl"):
    n_fx_chain_midi_input_ports = _libs["shoopdaloop"].get("n_fx_chain_midi_input_ports", "cdecl")
    n_fx_chain_midi_input_ports.argtypes = [POINTER(shoopdaloop_fx_chain_t)]
    n_fx_chain_midi_input_ports.restype = c_uint

# /Users/runner/work/shoopdaloop/shoopdaloop/src/libshoopdaloop/libshoopdaloop.h: 109
if _libs["shoopdaloop"].has("fx_chain_audio_input_port", "cdecl"):
    fx_chain_audio_input_port = _libs["shoopdaloop"].get("fx_chain_audio_input_port", "cdecl")
    fx_chain_audio_input_port.argtypes = [POINTER(shoopdaloop_fx_chain_t), c_uint]
    fx_chain_audio_input_port.restype = POINTER(shoopdaloop_audio_port_t)

# /Users/runner/work/shoopdaloop/shoopdaloop/src/libshoopdaloop/libshoopdaloop.h: 110
if _libs["shoopdaloop"].has("fx_chain_audio_output_port", "cdecl"):
    fx_chain_audio_output_port = _libs["shoopdaloop"].get("fx_chain_audio_output_port", "cdecl")
    fx_chain_audio_output_port.argtypes = [POINTER(shoopdaloop_fx_chain_t), c_uint]
    fx_chain_audio_output_port.restype = POINTER(shoopdaloop_audio_port_t)

# /Users/runner/work/shoopdaloop/shoopdaloop/src/libshoopdaloop/libshoopdaloop.h: 111
if _libs["shoopdaloop"].has("fx_chain_midi_input_port", "cdecl"):
    fx_chain_midi_input_port = _libs["shoopdaloop"].get("fx_chain_midi_input_port", "cdecl")
    fx_chain_midi_input_port.argtypes = [POINTER(shoopdaloop_fx_chain_t), c_uint]
    fx_chain_midi_input_port.restype = POINTER(shoopdaloop_midi_port_t)

# /Users/runner/work/shoopdaloop/shoopdaloop/src/libshoopdaloop/libshoopdaloop.h: 114
if _libs["shoopdaloop"].has("connect_audio_port_internal", "cdecl"):
    connect_audio_port_internal = _libs["shoopdaloop"].get("connect_audio_port_internal", "cdecl")
    connect_audio_port_internal.argtypes = [POINTER(shoopdaloop_audio_port_t), POINTER(shoopdaloop_audio_port_t)]
    connect_audio_port_internal.restype = None

# /Users/runner/work/shoopdaloop/shoopdaloop/src/libshoopdaloop/libshoopdaloop.h: 115
if _libs["shoopdaloop"].has("connect_audio_port_external", "cdecl"):
    connect_audio_port_external = _libs["shoopdaloop"].get("connect_audio_port_external", "cdecl")
    connect_audio_port_external.argtypes = [POINTER(shoopdaloop_audio_port_t), String]
    connect_audio_port_external.restype = None

# /Users/runner/work/shoopdaloop/shoopdaloop/src/libshoopdaloop/libshoopdaloop.h: 116
if _libs["shoopdaloop"].has("disconnect_audio_port_external", "cdecl"):
    disconnect_audio_port_external = _libs["shoopdaloop"].get("disconnect_audio_port_external", "cdecl")
    disconnect_audio_port_external.argtypes = [POINTER(shoopdaloop_audio_port_t), String]
    disconnect_audio_port_external.restype = None

# /Users/runner/work/shoopdaloop/shoopdaloop/src/libshoopdaloop/libshoopdaloop.h: 117
if _libs["shoopdaloop"].has("disconnect_audio_port_internal", "cdecl"):
    disconnect_audio_port_internal = _libs["shoopdaloop"].get("disconnect_audio_port_internal", "cdecl")
    disconnect_audio_port_internal.argtypes = [POINTER(shoopdaloop_audio_port_t), POINTER(shoopdaloop_audio_port_t)]
    disconnect_audio_port_internal.restype = None

# /Users/runner/work/shoopdaloop/shoopdaloop/src/libshoopdaloop/libshoopdaloop.h: 118
if _libs["shoopdaloop"].has("set_audio_port_gain", "cdecl"):
    set_audio_port_gain = _libs["shoopdaloop"].get("set_audio_port_gain", "cdecl")
    set_audio_port_gain.argtypes = [POINTER(shoopdaloop_audio_port_t), c_float]
    set_audio_port_gain.restype = None

# /Users/runner/work/shoopdaloop/shoopdaloop/src/libshoopdaloop/libshoopdaloop.h: 119
if _libs["shoopdaloop"].has("set_audio_port_muted", "cdecl"):
    set_audio_port_muted = _libs["shoopdaloop"].get("set_audio_port_muted", "cdecl")
    set_audio_port_muted.argtypes = [POINTER(shoopdaloop_audio_port_t), c_uint]
    set_audio_port_muted.restype = None

# /Users/runner/work/shoopdaloop/shoopdaloop/src/libshoopdaloop/libshoopdaloop.h: 120
if _libs["shoopdaloop"].has("set_audio_port_passthroughMuted", "cdecl"):
    set_audio_port_passthroughMuted = _libs["shoopdaloop"].get("set_audio_port_passthroughMuted", "cdecl")
    set_audio_port_passthroughMuted.argtypes = [POINTER(shoopdaloop_audio_port_t), c_uint]
    set_audio_port_passthroughMuted.restype = None

# /Users/runner/work/shoopdaloop/shoopdaloop/src/libshoopdaloop/libshoopdaloop.h: 121
if _libs["shoopdaloop"].has("get_audio_port_state", "cdecl"):
    get_audio_port_state = _libs["shoopdaloop"].get("get_audio_port_state", "cdecl")
    get_audio_port_state.argtypes = [POINTER(shoopdaloop_audio_port_t)]
    get_audio_port_state.restype = POINTER(shoop_audio_port_state_info_t)

# /Users/runner/work/shoopdaloop/shoopdaloop/src/libshoopdaloop/libshoopdaloop.h: 122
if _libs["shoopdaloop"].has("get_audio_port_connections_state", "cdecl"):
    get_audio_port_connections_state = _libs["shoopdaloop"].get("get_audio_port_connections_state", "cdecl")
    get_audio_port_connections_state.argtypes = [POINTER(shoopdaloop_audio_port_t)]
    get_audio_port_connections_state.restype = POINTER(shoop_port_connections_state_t)

# /Users/runner/work/shoopdaloop/shoopdaloop/src/libshoopdaloop/libshoopdaloop.h: 123
if _libs["shoopdaloop"].has("get_audio_port_driver_handle", "cdecl"):
    get_audio_port_driver_handle = _libs["shoopdaloop"].get("get_audio_port_driver_handle", "cdecl")
    get_audio_port_driver_handle.argtypes = [POINTER(shoopdaloop_audio_port_t)]
    get_audio_port_driver_handle.restype = POINTER(c_ubyte)
    get_audio_port_driver_handle.errcheck = lambda v,*a : cast(v, c_void_p)

# /Users/runner/work/shoopdaloop/shoopdaloop/src/libshoopdaloop/libshoopdaloop.h: 124
if _libs["shoopdaloop"].has("open_driver_audio_port", "cdecl"):
    open_driver_audio_port = _libs["shoopdaloop"].get("open_driver_audio_port", "cdecl")
    open_driver_audio_port.argtypes = [POINTER(shoop_backend_session_t), POINTER(shoop_audio_driver_t), String, shoop_port_direction_t, c_uint]
    open_driver_audio_port.restype = POINTER(shoopdaloop_audio_port_t)

# /Users/runner/work/shoopdaloop/shoopdaloop/src/libshoopdaloop/libshoopdaloop.h: 131
if _libs["shoopdaloop"].has("open_internal_audio_port", "cdecl"):
    open_internal_audio_port = _libs["shoopdaloop"].get("open_internal_audio_port", "cdecl")
    open_internal_audio_port.argtypes = [POINTER(shoop_backend_session_t), String, c_uint]
    open_internal_audio_port.restype = POINTER(shoopdaloop_audio_port_t)

# /Users/runner/work/shoopdaloop/shoopdaloop/src/libshoopdaloop/libshoopdaloop.h: 136
if _libs["shoopdaloop"].has("get_audio_port_input_connectability", "cdecl"):
    get_audio_port_input_connectability = _libs["shoopdaloop"].get("get_audio_port_input_connectability", "cdecl")
    get_audio_port_input_connectability.argtypes = [POINTER(shoopdaloop_audio_port_t)]
    get_audio_port_input_connectability.restype = c_uint

# /Users/runner/work/shoopdaloop/shoopdaloop/src/libshoopdaloop/libshoopdaloop.h: 137
if _libs["shoopdaloop"].has("get_audio_port_output_connectability", "cdecl"):
    get_audio_port_output_connectability = _libs["shoopdaloop"].get("get_audio_port_output_connectability", "cdecl")
    get_audio_port_output_connectability.argtypes = [POINTER(shoopdaloop_audio_port_t)]
    get_audio_port_output_connectability.restype = c_uint

# /Users/runner/work/shoopdaloop/shoopdaloop/src/libshoopdaloop/libshoopdaloop.h: 138
if _libs["shoopdaloop"].has("set_audio_port_ringbuffer_n_samples", "cdecl"):
    set_audio_port_ringbuffer_n_samples = _libs["shoopdaloop"].get("set_audio_port_ringbuffer_n_samples", "cdecl")
    set_audio_port_ringbuffer_n_samples.argtypes = [POINTER(shoopdaloop_audio_port_t), c_uint]
    set_audio_port_ringbuffer_n_samples.restype = None

# /Users/runner/work/shoopdaloop/shoopdaloop/src/libshoopdaloop/libshoopdaloop.h: 141
if _libs["shoopdaloop"].has("connect_midi_port_internal", "cdecl"):
    connect_midi_port_internal = _libs["shoopdaloop"].get("connect_midi_port_internal", "cdecl")
    connect_midi_port_internal.argtypes = [POINTER(shoopdaloop_midi_port_t), POINTER(shoopdaloop_midi_port_t)]
    connect_midi_port_internal.restype = None

# /Users/runner/work/shoopdaloop/shoopdaloop/src/libshoopdaloop/libshoopdaloop.h: 142
if _libs["shoopdaloop"].has("connect_midi_port_external", "cdecl"):
    connect_midi_port_external = _libs["shoopdaloop"].get("connect_midi_port_external", "cdecl")
    connect_midi_port_external.argtypes = [POINTER(shoopdaloop_midi_port_t), String]
    connect_midi_port_external.restype = None

# /Users/runner/work/shoopdaloop/shoopdaloop/src/libshoopdaloop/libshoopdaloop.h: 143
if _libs["shoopdaloop"].has("disconnect_midi_port_external", "cdecl"):
    disconnect_midi_port_external = _libs["shoopdaloop"].get("disconnect_midi_port_external", "cdecl")
    disconnect_midi_port_external.argtypes = [POINTER(shoopdaloop_midi_port_t), String]
    disconnect_midi_port_external.restype = None

# /Users/runner/work/shoopdaloop/shoopdaloop/src/libshoopdaloop/libshoopdaloop.h: 144
if _libs["shoopdaloop"].has("disconnect_midi_port_internal", "cdecl"):
    disconnect_midi_port_internal = _libs["shoopdaloop"].get("disconnect_midi_port_internal", "cdecl")
    disconnect_midi_port_internal.argtypes = [POINTER(shoopdaloop_midi_port_t), POINTER(shoopdaloop_midi_port_t)]
    disconnect_midi_port_internal.restype = None

# /Users/runner/work/shoopdaloop/shoopdaloop/src/libshoopdaloop/libshoopdaloop.h: 145
if _libs["shoopdaloop"].has("get_midi_port_state", "cdecl"):
    get_midi_port_state = _libs["shoopdaloop"].get("get_midi_port_state", "cdecl")
    get_midi_port_state.argtypes = [POINTER(shoopdaloop_midi_port_t)]
    get_midi_port_state.restype = POINTER(shoop_midi_port_state_info_t)

# /Users/runner/work/shoopdaloop/shoopdaloop/src/libshoopdaloop/libshoopdaloop.h: 146
if _libs["shoopdaloop"].has("set_midi_port_muted", "cdecl"):
    set_midi_port_muted = _libs["shoopdaloop"].get("set_midi_port_muted", "cdecl")
    set_midi_port_muted.argtypes = [POINTER(shoopdaloop_midi_port_t), c_uint]
    set_midi_port_muted.restype = None

# /Users/runner/work/shoopdaloop/shoopdaloop/src/libshoopdaloop/libshoopdaloop.h: 147
if _libs["shoopdaloop"].has("set_midi_port_passthroughMuted", "cdecl"):
    set_midi_port_passthroughMuted = _libs["shoopdaloop"].get("set_midi_port_passthroughMuted", "cdecl")
    set_midi_port_passthroughMuted.argtypes = [POINTER(shoopdaloop_midi_port_t), c_uint]
    set_midi_port_passthroughMuted.restype = None

# /Users/runner/work/shoopdaloop/shoopdaloop/src/libshoopdaloop/libshoopdaloop.h: 148
if _libs["shoopdaloop"].has("get_midi_port_connections_state", "cdecl"):
    get_midi_port_connections_state = _libs["shoopdaloop"].get("get_midi_port_connections_state", "cdecl")
    get_midi_port_connections_state.argtypes = [POINTER(shoopdaloop_midi_port_t)]
    get_midi_port_connections_state.restype = POINTER(shoop_port_connections_state_t)

# /Users/runner/work/shoopdaloop/shoopdaloop/src/libshoopdaloop/libshoopdaloop.h: 149
if _libs["shoopdaloop"].has("get_midi_port_driver_handle", "cdecl"):
    get_midi_port_driver_handle = _libs["shoopdaloop"].get("get_midi_port_driver_handle", "cdecl")
    get_midi_port_driver_handle.argtypes = [POINTER(shoopdaloop_midi_port_t)]
    get_midi_port_driver_handle.restype = POINTER(c_ubyte)
    get_midi_port_driver_handle.errcheck = lambda v,*a : cast(v, c_void_p)

# /Users/runner/work/shoopdaloop/shoopdaloop/src/libshoopdaloop/libshoopdaloop.h: 150
if _libs["shoopdaloop"].has("open_driver_midi_port", "cdecl"):
    open_driver_midi_port = _libs["shoopdaloop"].get("open_driver_midi_port", "cdecl")
    open_driver_midi_port.argtypes = [POINTER(shoop_backend_session_t), POINTER(shoop_audio_driver_t), String, shoop_port_direction_t, c_uint]
    open_driver_midi_port.restype = POINTER(shoopdaloop_midi_port_t)

# /Users/runner/work/shoopdaloop/shoopdaloop/src/libshoopdaloop/libshoopdaloop.h: 157
if _libs["shoopdaloop"].has("open_internal_midi_port", "cdecl"):
    open_internal_midi_port = _libs["shoopdaloop"].get("open_internal_midi_port", "cdecl")
    open_internal_midi_port.argtypes = [POINTER(shoop_backend_session_t), String, c_uint]
    open_internal_midi_port.restype = POINTER(shoopdaloop_midi_port_t)

# /Users/runner/work/shoopdaloop/shoopdaloop/src/libshoopdaloop/libshoopdaloop.h: 162
if _libs["shoopdaloop"].has("get_midi_port_input_connectability", "cdecl"):
    get_midi_port_input_connectability = _libs["shoopdaloop"].get("get_midi_port_input_connectability", "cdecl")
    get_midi_port_input_connectability.argtypes = [POINTER(shoopdaloop_midi_port_t)]
    get_midi_port_input_connectability.restype = c_uint

# /Users/runner/work/shoopdaloop/shoopdaloop/src/libshoopdaloop/libshoopdaloop.h: 163
if _libs["shoopdaloop"].has("get_midi_port_output_connectability", "cdecl"):
    get_midi_port_output_connectability = _libs["shoopdaloop"].get("get_midi_port_output_connectability", "cdecl")
    get_midi_port_output_connectability.argtypes = [POINTER(shoopdaloop_midi_port_t)]
    get_midi_port_output_connectability.restype = c_uint

# /Users/runner/work/shoopdaloop/shoopdaloop/src/libshoopdaloop/libshoopdaloop.h: 164
if _libs["shoopdaloop"].has("set_midi_port_ringbuffer_n_samples", "cdecl"):
    set_midi_port_ringbuffer_n_samples = _libs["shoopdaloop"].get("set_midi_port_ringbuffer_n_samples", "cdecl")
    set_midi_port_ringbuffer_n_samples.argtypes = [POINTER(shoopdaloop_midi_port_t), c_uint]
    set_midi_port_ringbuffer_n_samples.restype = None

# /Users/runner/work/shoopdaloop/shoopdaloop/src/libshoopdaloop/libshoopdaloop.h: 167
if _libs["shoopdaloop"].has("open_decoupled_midi_port", "cdecl"):
    open_decoupled_midi_port = _libs["shoopdaloop"].get("open_decoupled_midi_port", "cdecl")
    open_decoupled_midi_port.argtypes = [POINTER(shoop_audio_driver_t), String, shoop_port_direction_t]
    open_decoupled_midi_port.restype = POINTER(shoopdaloop_decoupled_midi_port_t)

# /Users/runner/work/shoopdaloop/shoopdaloop/src/libshoopdaloop/libshoopdaloop.h: 168
if _libs["shoopdaloop"].has("maybe_next_message", "cdecl"):
    maybe_next_message = _libs["shoopdaloop"].get("maybe_next_message", "cdecl")
    maybe_next_message.argtypes = [POINTER(shoopdaloop_decoupled_midi_port_t)]
    maybe_next_message.restype = POINTER(shoop_midi_event_t)

# /Users/runner/work/shoopdaloop/shoopdaloop/src/libshoopdaloop/libshoopdaloop.h: 169
if _libs["shoopdaloop"].has("send_decoupled_midi", "cdecl"):
    send_decoupled_midi = _libs["shoopdaloop"].get("send_decoupled_midi", "cdecl")
    send_decoupled_midi.argtypes = [POINTER(shoopdaloop_decoupled_midi_port_t), c_uint, POINTER(c_ubyte)]
    send_decoupled_midi.restype = None

# /Users/runner/work/shoopdaloop/shoopdaloop/src/libshoopdaloop/libshoopdaloop.h: 170
if _libs["shoopdaloop"].has("get_decoupled_midi_port_name", "cdecl"):
    get_decoupled_midi_port_name = _libs["shoopdaloop"].get("get_decoupled_midi_port_name", "cdecl")
    get_decoupled_midi_port_name.argtypes = [POINTER(shoopdaloop_decoupled_midi_port_t)]
    get_decoupled_midi_port_name.restype = c_char_p

# /Users/runner/work/shoopdaloop/shoopdaloop/src/libshoopdaloop/libshoopdaloop.h: 171
if _libs["shoopdaloop"].has("close_decoupled_midi_port", "cdecl"):
    close_decoupled_midi_port = _libs["shoopdaloop"].get("close_decoupled_midi_port", "cdecl")
    close_decoupled_midi_port.argtypes = [POINTER(shoopdaloop_decoupled_midi_port_t)]
    close_decoupled_midi_port.restype = None

# /Users/runner/work/shoopdaloop/shoopdaloop/src/libshoopdaloop/libshoopdaloop.h: 172
if _libs["shoopdaloop"].has("get_decoupled_midi_port_connections_state", "cdecl"):
    get_decoupled_midi_port_connections_state = _libs["shoopdaloop"].get("get_decoupled_midi_port_connections_state", "cdecl")
    get_decoupled_midi_port_connections_state.argtypes = [POINTER(shoopdaloop_decoupled_midi_port_t)]
    get_decoupled_midi_port_connections_state.restype = POINTER(shoop_port_connections_state_t)

# /Users/runner/work/shoopdaloop/shoopdaloop/src/libshoopdaloop/libshoopdaloop.h: 173
if _libs["shoopdaloop"].has("connect_external_decoupled_midi_port", "cdecl"):
    connect_external_decoupled_midi_port = _libs["shoopdaloop"].get("connect_external_decoupled_midi_port", "cdecl")
    connect_external_decoupled_midi_port.argtypes = [POINTER(shoopdaloop_decoupled_midi_port_t), String]
    connect_external_decoupled_midi_port.restype = None

# /Users/runner/work/shoopdaloop/shoopdaloop/src/libshoopdaloop/libshoopdaloop.h: 174
if _libs["shoopdaloop"].has("disconnect_external_decoupled_midi_port", "cdecl"):
    disconnect_external_decoupled_midi_port = _libs["shoopdaloop"].get("disconnect_external_decoupled_midi_port", "cdecl")
    disconnect_external_decoupled_midi_port.argtypes = [POINTER(shoopdaloop_decoupled_midi_port_t), String]
    disconnect_external_decoupled_midi_port.restype = None

# /Users/runner/work/shoopdaloop/shoopdaloop/src/libshoopdaloop/libshoopdaloop.h: 178
if _libs["shoopdaloop"].has("destroy_midi_event", "cdecl"):
    destroy_midi_event = _libs["shoopdaloop"].get("destroy_midi_event", "cdecl")
    destroy_midi_event.argtypes = [POINTER(shoop_midi_event_t)]
    destroy_midi_event.restype = None

# /Users/runner/work/shoopdaloop/shoopdaloop/src/libshoopdaloop/libshoopdaloop.h: 179
if _libs["shoopdaloop"].has("destroy_midi_sequence", "cdecl"):
    destroy_midi_sequence = _libs["shoopdaloop"].get("destroy_midi_sequence", "cdecl")
    destroy_midi_sequence.argtypes = [POINTER(shoop_midi_sequence_t)]
    destroy_midi_sequence.restype = None

# /Users/runner/work/shoopdaloop/shoopdaloop/src/libshoopdaloop/libshoopdaloop.h: 180
if _libs["shoopdaloop"].has("destroy_audio_channel_data", "cdecl"):
    destroy_audio_channel_data = _libs["shoopdaloop"].get("destroy_audio_channel_data", "cdecl")
    destroy_audio_channel_data.argtypes = [POINTER(shoop_audio_channel_data_t)]
    destroy_audio_channel_data.restype = None

# /Users/runner/work/shoopdaloop/shoopdaloop/src/libshoopdaloop/libshoopdaloop.h: 181
if _libs["shoopdaloop"].has("destroy_audio_channel_state_info", "cdecl"):
    destroy_audio_channel_state_info = _libs["shoopdaloop"].get("destroy_audio_channel_state_info", "cdecl")
    destroy_audio_channel_state_info.argtypes = [POINTER(shoop_audio_channel_state_info_t)]
    destroy_audio_channel_state_info.restype = None

# /Users/runner/work/shoopdaloop/shoopdaloop/src/libshoopdaloop/libshoopdaloop.h: 182
if _libs["shoopdaloop"].has("destroy_midi_channel_state_info", "cdecl"):
    destroy_midi_channel_state_info = _libs["shoopdaloop"].get("destroy_midi_channel_state_info", "cdecl")
    destroy_midi_channel_state_info.argtypes = [POINTER(shoop_midi_channel_state_info_t)]
    destroy_midi_channel_state_info.restype = None

# /Users/runner/work/shoopdaloop/shoopdaloop/src/libshoopdaloop/libshoopdaloop.h: 183
if _libs["shoopdaloop"].has("destroy_backend_state_info", "cdecl"):
    destroy_backend_state_info = _libs["shoopdaloop"].get("destroy_backend_state_info", "cdecl")
    destroy_backend_state_info.argtypes = [POINTER(shoop_backend_session_state_info_t)]
    destroy_backend_state_info.restype = None

# /Users/runner/work/shoopdaloop/shoopdaloop/src/libshoopdaloop/libshoopdaloop.h: 184
if _libs["shoopdaloop"].has("destroy_loop", "cdecl"):
    destroy_loop = _libs["shoopdaloop"].get("destroy_loop", "cdecl")
    destroy_loop.argtypes = [POINTER(shoopdaloop_loop_t)]
    destroy_loop.restype = None

# /Users/runner/work/shoopdaloop/shoopdaloop/src/libshoopdaloop/libshoopdaloop.h: 185
if _libs["shoopdaloop"].has("destroy_audio_port", "cdecl"):
    destroy_audio_port = _libs["shoopdaloop"].get("destroy_audio_port", "cdecl")
    destroy_audio_port.argtypes = [POINTER(shoopdaloop_audio_port_t)]
    destroy_audio_port.restype = None

# /Users/runner/work/shoopdaloop/shoopdaloop/src/libshoopdaloop/libshoopdaloop.h: 186
if _libs["shoopdaloop"].has("destroy_midi_port", "cdecl"):
    destroy_midi_port = _libs["shoopdaloop"].get("destroy_midi_port", "cdecl")
    destroy_midi_port.argtypes = [POINTER(shoopdaloop_midi_port_t)]
    destroy_midi_port.restype = None

# /Users/runner/work/shoopdaloop/shoopdaloop/src/libshoopdaloop/libshoopdaloop.h: 187
if _libs["shoopdaloop"].has("destroy_midi_port_state_info", "cdecl"):
    destroy_midi_port_state_info = _libs["shoopdaloop"].get("destroy_midi_port_state_info", "cdecl")
    destroy_midi_port_state_info.argtypes = [POINTER(shoop_midi_port_state_info_t)]
    destroy_midi_port_state_info.restype = None

# /Users/runner/work/shoopdaloop/shoopdaloop/src/libshoopdaloop/libshoopdaloop.h: 188
if _libs["shoopdaloop"].has("destroy_audio_port_state_info", "cdecl"):
    destroy_audio_port_state_info = _libs["shoopdaloop"].get("destroy_audio_port_state_info", "cdecl")
    destroy_audio_port_state_info.argtypes = [POINTER(shoop_audio_port_state_info_t)]
    destroy_audio_port_state_info.restype = None

# /Users/runner/work/shoopdaloop/shoopdaloop/src/libshoopdaloop/libshoopdaloop.h: 189
if _libs["shoopdaloop"].has("destroy_audio_channel", "cdecl"):
    destroy_audio_channel = _libs["shoopdaloop"].get("destroy_audio_channel", "cdecl")
    destroy_audio_channel.argtypes = [POINTER(shoopdaloop_loop_audio_channel_t)]
    destroy_audio_channel.restype = None

# /Users/runner/work/shoopdaloop/shoopdaloop/src/libshoopdaloop/libshoopdaloop.h: 190
if _libs["shoopdaloop"].has("destroy_midi_channel", "cdecl"):
    destroy_midi_channel = _libs["shoopdaloop"].get("destroy_midi_channel", "cdecl")
    destroy_midi_channel.argtypes = [POINTER(shoopdaloop_loop_midi_channel_t)]
    destroy_midi_channel.restype = None

# /Users/runner/work/shoopdaloop/shoopdaloop/src/libshoopdaloop/libshoopdaloop.h: 191
if _libs["shoopdaloop"].has("destroy_shoopdaloop_decoupled_midi_port", "cdecl"):
    destroy_shoopdaloop_decoupled_midi_port = _libs["shoopdaloop"].get("destroy_shoopdaloop_decoupled_midi_port", "cdecl")
    destroy_shoopdaloop_decoupled_midi_port.argtypes = [POINTER(shoopdaloop_decoupled_midi_port_t)]
    destroy_shoopdaloop_decoupled_midi_port.restype = None

# /Users/runner/work/shoopdaloop/shoopdaloop/src/libshoopdaloop/libshoopdaloop.h: 192
if _libs["shoopdaloop"].has("destroy_loop_state_info", "cdecl"):
    destroy_loop_state_info = _libs["shoopdaloop"].get("destroy_loop_state_info", "cdecl")
    destroy_loop_state_info.argtypes = [POINTER(shoop_loop_state_info_t)]
    destroy_loop_state_info.restype = None

# /Users/runner/work/shoopdaloop/shoopdaloop/src/libshoopdaloop/libshoopdaloop.h: 193
if _libs["shoopdaloop"].has("destroy_fx_chain", "cdecl"):
    destroy_fx_chain = _libs["shoopdaloop"].get("destroy_fx_chain", "cdecl")
    destroy_fx_chain.argtypes = [POINTER(shoopdaloop_fx_chain_t)]
    destroy_fx_chain.restype = None

# /Users/runner/work/shoopdaloop/shoopdaloop/src/libshoopdaloop/libshoopdaloop.h: 194
if _libs["shoopdaloop"].has("destroy_fx_chain_state", "cdecl"):
    destroy_fx_chain_state = _libs["shoopdaloop"].get("destroy_fx_chain_state", "cdecl")
    destroy_fx_chain_state.argtypes = [POINTER(shoop_fx_chain_state_info_t)]
    destroy_fx_chain_state.restype = None

# /Users/runner/work/shoopdaloop/shoopdaloop/src/libshoopdaloop/libshoopdaloop.h: 195
if _libs["shoopdaloop"].has("destroy_profiling_report", "cdecl"):
    destroy_profiling_report = _libs["shoopdaloop"].get("destroy_profiling_report", "cdecl")
    destroy_profiling_report.argtypes = [POINTER(shoop_profiling_report_t)]
    destroy_profiling_report.restype = None

# /Users/runner/work/shoopdaloop/shoopdaloop/src/libshoopdaloop/libshoopdaloop.h: 196
if _libs["shoopdaloop"].has("destroy_string", "cdecl"):
    destroy_string = _libs["shoopdaloop"].get("destroy_string", "cdecl")
    destroy_string.argtypes = [String]
    destroy_string.restype = None

# /Users/runner/work/shoopdaloop/shoopdaloop/src/libshoopdaloop/libshoopdaloop.h: 197
if _libs["shoopdaloop"].has("destroy_port_connections_state", "cdecl"):
    destroy_port_connections_state = _libs["shoopdaloop"].get("destroy_port_connections_state", "cdecl")
    destroy_port_connections_state.argtypes = [POINTER(shoop_port_connections_state_t)]
    destroy_port_connections_state.restype = None

# /Users/runner/work/shoopdaloop/shoopdaloop/src/libshoopdaloop/libshoopdaloop.h: 198
if _libs["shoopdaloop"].has("destroy_logger", "cdecl"):
    destroy_logger = _libs["shoopdaloop"].get("destroy_logger", "cdecl")
    destroy_logger.argtypes = [POINTER(shoopdaloop_logger_t)]
    destroy_logger.restype = None

# /Users/runner/work/shoopdaloop/shoopdaloop/src/libshoopdaloop/libshoopdaloop.h: 199
if _libs["shoopdaloop"].has("destroy_audio_driver_state", "cdecl"):
    destroy_audio_driver_state = _libs["shoopdaloop"].get("destroy_audio_driver_state", "cdecl")
    destroy_audio_driver_state.argtypes = [POINTER(shoop_audio_driver_state_t)]
    destroy_audio_driver_state.restype = None

# /Users/runner/work/shoopdaloop/shoopdaloop/src/libshoopdaloop/libshoopdaloop.h: 200
if _libs["shoopdaloop"].has("destroy_multichannel_audio", "cdecl"):
    destroy_multichannel_audio = _libs["shoopdaloop"].get("destroy_multichannel_audio", "cdecl")
    destroy_multichannel_audio.argtypes = [POINTER(shoop_multichannel_audio_t)]
    destroy_multichannel_audio.restype = None

# /Users/runner/work/shoopdaloop/shoopdaloop/src/libshoopdaloop/libshoopdaloop.h: 201
if _libs["shoopdaloop"].has("destroy_external_port_descriptors", "cdecl"):
    destroy_external_port_descriptors = _libs["shoopdaloop"].get("destroy_external_port_descriptors", "cdecl")
    destroy_external_port_descriptors.argtypes = [POINTER(shoop_external_port_descriptors_t)]
    destroy_external_port_descriptors.restype = None

# /Users/runner/work/shoopdaloop/shoopdaloop/src/libshoopdaloop/libshoopdaloop.h: 204
if _libs["shoopdaloop"].has("alloc_midi_event", "cdecl"):
    alloc_midi_event = _libs["shoopdaloop"].get("alloc_midi_event", "cdecl")
    alloc_midi_event.argtypes = [c_uint]
    alloc_midi_event.restype = POINTER(shoop_midi_event_t)

# /Users/runner/work/shoopdaloop/shoopdaloop/src/libshoopdaloop/libshoopdaloop.h: 205
if _libs["shoopdaloop"].has("alloc_midi_sequence", "cdecl"):
    alloc_midi_sequence = _libs["shoopdaloop"].get("alloc_midi_sequence", "cdecl")
    alloc_midi_sequence.argtypes = [c_uint]
    alloc_midi_sequence.restype = POINTER(shoop_midi_sequence_t)

# /Users/runner/work/shoopdaloop/shoopdaloop/src/libshoopdaloop/libshoopdaloop.h: 206
if _libs["shoopdaloop"].has("alloc_audio_channel_data", "cdecl"):
    alloc_audio_channel_data = _libs["shoopdaloop"].get("alloc_audio_channel_data", "cdecl")
    alloc_audio_channel_data.argtypes = [c_uint]
    alloc_audio_channel_data.restype = POINTER(shoop_audio_channel_data_t)

# /Users/runner/work/shoopdaloop/shoopdaloop/src/libshoopdaloop/libshoopdaloop.h: 207
if _libs["shoopdaloop"].has("alloc_multichannel_audio", "cdecl"):
    alloc_multichannel_audio = _libs["shoopdaloop"].get("alloc_multichannel_audio", "cdecl")
    alloc_multichannel_audio.argtypes = [c_uint, c_uint]
    alloc_multichannel_audio.restype = POINTER(shoop_multichannel_audio_t)

# /Users/runner/work/shoopdaloop/shoopdaloop/src/libshoopdaloop/libshoopdaloop.h: 210
if _libs["shoopdaloop"].has("initialize_logging", "cdecl"):
    initialize_logging = _libs["shoopdaloop"].get("initialize_logging", "cdecl")
    initialize_logging.argtypes = []
    initialize_logging.restype = None

# /Users/runner/work/shoopdaloop/shoopdaloop/src/libshoopdaloop/libshoopdaloop.h: 211
if _libs["shoopdaloop"].has("get_logger", "cdecl"):
    get_logger = _libs["shoopdaloop"].get("get_logger", "cdecl")
    get_logger.argtypes = [String]
    get_logger.restype = POINTER(shoopdaloop_logger_t)

# /Users/runner/work/shoopdaloop/shoopdaloop/src/libshoopdaloop/libshoopdaloop.h: 212
if _libs["shoopdaloop"].has("set_global_logging_level", "cdecl"):
    set_global_logging_level = _libs["shoopdaloop"].get("set_global_logging_level", "cdecl")
    set_global_logging_level.argtypes = [shoop_log_level_t]
    set_global_logging_level.restype = None

# /Users/runner/work/shoopdaloop/shoopdaloop/src/libshoopdaloop/libshoopdaloop.h: 213
if _libs["shoopdaloop"].has("set_logger_level_override", "cdecl"):
    set_logger_level_override = _libs["shoopdaloop"].get("set_logger_level_override", "cdecl")
    set_logger_level_override.argtypes = [POINTER(shoopdaloop_logger_t), shoop_log_level_t]
    set_logger_level_override.restype = None

# /Users/runner/work/shoopdaloop/shoopdaloop/src/libshoopdaloop/libshoopdaloop.h: 214
if _libs["shoopdaloop"].has("reset_logger_level_override", "cdecl"):
    reset_logger_level_override = _libs["shoopdaloop"].get("reset_logger_level_override", "cdecl")
    reset_logger_level_override.argtypes = [POINTER(shoopdaloop_logger_t)]
    reset_logger_level_override.restype = None

# /Users/runner/work/shoopdaloop/shoopdaloop/src/libshoopdaloop/libshoopdaloop.h: 215
if _libs["shoopdaloop"].has("shoopdaloop_log", "cdecl"):
    shoopdaloop_log = _libs["shoopdaloop"].get("shoopdaloop_log", "cdecl")
    shoopdaloop_log.argtypes = [POINTER(shoopdaloop_logger_t), shoop_log_level_t, String]
    shoopdaloop_log.restype = None

# /Users/runner/work/shoopdaloop/shoopdaloop/src/libshoopdaloop/libshoopdaloop.h: 216
if _libs["shoopdaloop"].has("shoopdaloop_should_log", "cdecl"):
    shoopdaloop_should_log = _libs["shoopdaloop"].get("shoopdaloop_should_log", "cdecl")
    shoopdaloop_should_log.argtypes = [POINTER(shoopdaloop_logger_t), shoop_log_level_t]
    shoopdaloop_should_log.restype = c_uint

# /Users/runner/work/shoopdaloop/shoopdaloop/src/libshoopdaloop/libshoopdaloop.h: 219
if _libs["shoopdaloop"].has("dummy_audio_port_queue_data", "cdecl"):
    dummy_audio_port_queue_data = _libs["shoopdaloop"].get("dummy_audio_port_queue_data", "cdecl")
    dummy_audio_port_queue_data.argtypes = [POINTER(shoopdaloop_audio_port_t), c_uint, POINTER(audio_sample_t)]
    dummy_audio_port_queue_data.restype = None

# /Users/runner/work/shoopdaloop/shoopdaloop/src/libshoopdaloop/libshoopdaloop.h: 220
if _libs["shoopdaloop"].has("dummy_audio_port_dequeue_data", "cdecl"):
    dummy_audio_port_dequeue_data = _libs["shoopdaloop"].get("dummy_audio_port_dequeue_data", "cdecl")
    dummy_audio_port_dequeue_data.argtypes = [POINTER(shoopdaloop_audio_port_t), c_uint, POINTER(audio_sample_t)]
    dummy_audio_port_dequeue_data.restype = None

# /Users/runner/work/shoopdaloop/shoopdaloop/src/libshoopdaloop/libshoopdaloop.h: 221
if _libs["shoopdaloop"].has("dummy_audio_port_request_data", "cdecl"):
    dummy_audio_port_request_data = _libs["shoopdaloop"].get("dummy_audio_port_request_data", "cdecl")
    dummy_audio_port_request_data.argtypes = [POINTER(shoopdaloop_audio_port_t), c_uint]
    dummy_audio_port_request_data.restype = None

# /Users/runner/work/shoopdaloop/shoopdaloop/src/libshoopdaloop/libshoopdaloop.h: 222
if _libs["shoopdaloop"].has("dummy_audio_enter_controlled_mode", "cdecl"):
    dummy_audio_enter_controlled_mode = _libs["shoopdaloop"].get("dummy_audio_enter_controlled_mode", "cdecl")
    dummy_audio_enter_controlled_mode.argtypes = [POINTER(shoop_audio_driver_t)]
    dummy_audio_enter_controlled_mode.restype = None

# /Users/runner/work/shoopdaloop/shoopdaloop/src/libshoopdaloop/libshoopdaloop.h: 223
if _libs["shoopdaloop"].has("dummy_audio_enter_automatic_mode", "cdecl"):
    dummy_audio_enter_automatic_mode = _libs["shoopdaloop"].get("dummy_audio_enter_automatic_mode", "cdecl")
    dummy_audio_enter_automatic_mode.argtypes = [POINTER(shoop_audio_driver_t)]
    dummy_audio_enter_automatic_mode.restype = None

# /Users/runner/work/shoopdaloop/shoopdaloop/src/libshoopdaloop/libshoopdaloop.h: 224
if _libs["shoopdaloop"].has("dummy_audio_is_in_controlled_mode", "cdecl"):
    dummy_audio_is_in_controlled_mode = _libs["shoopdaloop"].get("dummy_audio_is_in_controlled_mode", "cdecl")
    dummy_audio_is_in_controlled_mode.argtypes = [POINTER(shoop_audio_driver_t)]
    dummy_audio_is_in_controlled_mode.restype = c_uint

# /Users/runner/work/shoopdaloop/shoopdaloop/src/libshoopdaloop/libshoopdaloop.h: 225
if _libs["shoopdaloop"].has("dummy_audio_request_controlled_frames", "cdecl"):
    dummy_audio_request_controlled_frames = _libs["shoopdaloop"].get("dummy_audio_request_controlled_frames", "cdecl")
    dummy_audio_request_controlled_frames.argtypes = [POINTER(shoop_audio_driver_t), c_uint]
    dummy_audio_request_controlled_frames.restype = None

# /Users/runner/work/shoopdaloop/shoopdaloop/src/libshoopdaloop/libshoopdaloop.h: 226
if _libs["shoopdaloop"].has("dummy_audio_run_requested_frames", "cdecl"):
    dummy_audio_run_requested_frames = _libs["shoopdaloop"].get("dummy_audio_run_requested_frames", "cdecl")
    dummy_audio_run_requested_frames.argtypes = [POINTER(shoop_audio_driver_t)]
    dummy_audio_run_requested_frames.restype = None

# /Users/runner/work/shoopdaloop/shoopdaloop/src/libshoopdaloop/libshoopdaloop.h: 227
if _libs["shoopdaloop"].has("dummy_audio_n_requested_frames", "cdecl"):
    dummy_audio_n_requested_frames = _libs["shoopdaloop"].get("dummy_audio_n_requested_frames", "cdecl")
    dummy_audio_n_requested_frames.argtypes = [POINTER(shoop_audio_driver_t)]
    dummy_audio_n_requested_frames.restype = c_uint

# /Users/runner/work/shoopdaloop/shoopdaloop/src/libshoopdaloop/libshoopdaloop.h: 228
if _libs["shoopdaloop"].has("dummy_midi_port_queue_data", "cdecl"):
    dummy_midi_port_queue_data = _libs["shoopdaloop"].get("dummy_midi_port_queue_data", "cdecl")
    dummy_midi_port_queue_data.argtypes = [POINTER(shoopdaloop_midi_port_t), POINTER(shoop_midi_sequence_t)]
    dummy_midi_port_queue_data.restype = None

# /Users/runner/work/shoopdaloop/shoopdaloop/src/libshoopdaloop/libshoopdaloop.h: 229
if _libs["shoopdaloop"].has("dummy_midi_port_dequeue_data", "cdecl"):
    dummy_midi_port_dequeue_data = _libs["shoopdaloop"].get("dummy_midi_port_dequeue_data", "cdecl")
    dummy_midi_port_dequeue_data.argtypes = [POINTER(shoopdaloop_midi_port_t)]
    dummy_midi_port_dequeue_data.restype = POINTER(shoop_midi_sequence_t)

# /Users/runner/work/shoopdaloop/shoopdaloop/src/libshoopdaloop/libshoopdaloop.h: 230
if _libs["shoopdaloop"].has("dummy_midi_port_request_data", "cdecl"):
    dummy_midi_port_request_data = _libs["shoopdaloop"].get("dummy_midi_port_request_data", "cdecl")
    dummy_midi_port_request_data.argtypes = [POINTER(shoopdaloop_midi_port_t), c_uint]
    dummy_midi_port_request_data.restype = None

# /Users/runner/work/shoopdaloop/shoopdaloop/src/libshoopdaloop/libshoopdaloop.h: 231
if _libs["shoopdaloop"].has("dummy_midi_port_clear_queues", "cdecl"):
    dummy_midi_port_clear_queues = _libs["shoopdaloop"].get("dummy_midi_port_clear_queues", "cdecl")
    dummy_midi_port_clear_queues.argtypes = [POINTER(shoopdaloop_midi_port_t)]
    dummy_midi_port_clear_queues.restype = None

# /Users/runner/work/shoopdaloop/shoopdaloop/src/libshoopdaloop/libshoopdaloop.h: 232
if _libs["shoopdaloop"].has("dummy_driver_add_external_mock_port", "cdecl"):
    dummy_driver_add_external_mock_port = _libs["shoopdaloop"].get("dummy_driver_add_external_mock_port", "cdecl")
    dummy_driver_add_external_mock_port.argtypes = [POINTER(shoop_audio_driver_t), String, shoop_port_direction_t, shoop_port_data_type_t]
    dummy_driver_add_external_mock_port.restype = None

# /Users/runner/work/shoopdaloop/shoopdaloop/src/libshoopdaloop/libshoopdaloop.h: 233
if _libs["shoopdaloop"].has("dummy_driver_remove_external_mock_port", "cdecl"):
    dummy_driver_remove_external_mock_port = _libs["shoopdaloop"].get("dummy_driver_remove_external_mock_port", "cdecl")
    dummy_driver_remove_external_mock_port.argtypes = [POINTER(shoop_audio_driver_t), String]
    dummy_driver_remove_external_mock_port.restype = None

# /Users/runner/work/shoopdaloop/shoopdaloop/src/libshoopdaloop/libshoopdaloop.h: 234
if _libs["shoopdaloop"].has("dummy_driver_remove_all_external_mock_ports", "cdecl"):
    dummy_driver_remove_all_external_mock_ports = _libs["shoopdaloop"].get("dummy_driver_remove_all_external_mock_ports", "cdecl")
    dummy_driver_remove_all_external_mock_ports.argtypes = [POINTER(shoop_audio_driver_t)]
    dummy_driver_remove_all_external_mock_ports.restype = None

# /Users/runner/work/shoopdaloop/shoopdaloop/src/libshoopdaloop/libshoopdaloop.h: 237
if _libs["shoopdaloop"].has("resample_audio", "cdecl"):
    resample_audio = _libs["shoopdaloop"].get("resample_audio", "cdecl")
    resample_audio.argtypes = [POINTER(shoop_multichannel_audio_t), c_uint]
    resample_audio.restype = POINTER(shoop_multichannel_audio_t)

_shoopdaloop_loop = struct__shoopdaloop_loop# /Users/runner/work/shoopdaloop/shoopdaloop/src/libshoopdaloop/types.h: 98

_shoopdaloop_loop_audio_channel = struct__shoopdaloop_loop_audio_channel# /Users/runner/work/shoopdaloop/shoopdaloop/src/libshoopdaloop/types.h: 99

_shoopdaloop_loop_midi_channel = struct__shoopdaloop_loop_midi_channel# /Users/runner/work/shoopdaloop/shoopdaloop/src/libshoopdaloop/types.h: 100

_shoopdaloop_audio_port = struct__shoopdaloop_audio_port# /Users/runner/work/shoopdaloop/shoopdaloop/src/libshoopdaloop/types.h: 101

_shoopdaloop_midi_port = struct__shoopdaloop_midi_port# /Users/runner/work/shoopdaloop/shoopdaloop/src/libshoopdaloop/types.h: 102

_shoopdaloop_decoupled_midi_port = struct__shoopdaloop_decoupled_midi_port# /Users/runner/work/shoopdaloop/shoopdaloop/src/libshoopdaloop/types.h: 103

_shoopdaloop_backend_session = struct__shoopdaloop_backend_session# /Users/runner/work/shoopdaloop/shoopdaloop/src/libshoopdaloop/types.h: 104

_shoopdaloop_fx_chain = struct__shoopdaloop_fx_chain# /Users/runner/work/shoopdaloop/shoopdaloop/src/libshoopdaloop/types.h: 105

_shoopdaloop_logger = struct__shoopdaloop_logger# /Users/runner/work/shoopdaloop/shoopdaloop/src/libshoopdaloop/types.h: 106

_shoopdaloop_audio_driver = struct__shoopdaloop_audio_driver# /Users/runner/work/shoopdaloop/shoopdaloop/src/libshoopdaloop/types.h: 107

# No inserted files

# No prefix-stripping

