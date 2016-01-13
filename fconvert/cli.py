"""Command line interface components for fconvert."""
# (c) Copyright 2016 Andrew Dawson. All Rights Reserved.
#
# This file is part of fconvert.
#
# fconvert is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# fconvert is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with fconvert.  If not, see <http://www.gnu.org/licenses/>.
from __future__ import absolute_import, print_function

from argparse import ArgumentParser
import sys


def input_iterator(input_value, input_converter=None):
    """A generator of input items.

    Returns the input item, unless it is `None` then returns lines from
    stdin until end-of-file is reached.

    **Argument:**

    * input_value
        Any value or `None`.

    **Optional argument:**

    * input_converter
        A function for transforming values before they are returned. For
        example one could pass a function that converts strings to
        floats.

    """
    if input_converter is None:
        input_converter = lambda x: x
    if input_value is None:
        for line in sys.stdin.readlines():
            yield input_converter(line.strip())
    else:
        yield input_converter(input_value)


def main(name, value_type, help, converter, input_converter=None):
    """A generic 'main' function for command line converters."""
    ap = ArgumentParser()
    ap.add_argument(name, type=value_type, nargs='?', help=help)
    argns = ap.parse_args(sys.argv[1:])
    try:
        for value in input_iterator(getattr(argns, name), input_converter):
            print(converter(value))
    except ValueError:
        errmsg = ("conversion error on '{!s}', "
                  "check that input is the correct type").format(value)
        print(errmsg, file=sys.stderr)
        print("  use -h or --help for help", file=sys.stderr)
        return 1
    else:
        return 0
