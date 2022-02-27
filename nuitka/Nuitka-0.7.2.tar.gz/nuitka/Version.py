#     Copyright 2021, Kay Hayen, mailto:kay.hayen@gmail.com
#
#     Part of "Nuitka", an optimizing Python compiler that is compatible and
#     integrates with CPython, but also works on its own.
#
#     Licensed under the Apache License, Version 2.0 (the "License");
#     you may not use this file except in compliance with the License.
#     You may obtain a copy of the License at
#
#        http://www.apache.org/licenses/LICENSE-2.0
#
#     Unless required by applicable law or agreed to in writing, software
#     distributed under the License is distributed on an "AS IS" BASIS,
#     WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#     See the License for the specific language governing permissions and
#     limitations under the License.
#
""" Nuitka version related stuff.

"""

version_string = """\
Nuitka V0.7.2
Copyright (C) 2021 Kay Hayen."""


def getNuitkaVersion():
    """Return Nuitka version as a string.

    This should not be used for >= comparisons directly.
    """
    return version_string.split()[1][1:]


def getNuitkaVersionTuple():
    """Return Nuitka version as a string.

    This can also not be used for precise comparisons, last one might contain "rc"
    """

    version = getNuitkaVersion()

    if "rc" in version:
        rc_number = int(version[version.find("rc") + 2 :] or "0")
        version = version[: version.find("rc")]

        is_final = False
    else:
        rc_number = 0
        is_final = True

    result = version.split(".")
    if len(result) == 2:
        result.append("0")

    result = [int(digit) for digit in result]
    result.extend((is_final, rc_number))
    return tuple(result)


def getNuitkaVersionYear():
    """The year of Nuitka copyright for use in generations."""

    return int(version_string.split()[4])


def getCommercialVersion():
    """Return Nuitka commercial version if installed."""
    try:
        from nuitka.tools.commercial import Version
    except ImportError:
        return None
    else:
        return Version.__version__


def getNuitkaMsiVersion():
    major, minor, micro, is_final, rc_number = getNuitkaVersionTuple()
    # Pre-releases are always smaller, official releases get the "1".
    middle = 1 if is_final else 0

    return ".".join(
        "%s" % value
        for value in (
            int(major) * 10 + int(minor),
            middle,
            int(micro) * 10 + int(rc_number),
        )
    )
