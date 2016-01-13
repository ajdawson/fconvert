"""Build and install the fconvert library and tools."""
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
from setuptools import setup


__version__ = '1.0.0'

packages = ['fconvert']

scripts = ['bin/bin2hex',
           'bin/bin2double',
           'bin/bin2float',
           'bin/double2bin',
           'bin/double2hex',
           'bin/float2bin',
           'bin/float2hex',
           'bin/hex2bin',]


if __name__ == '__main__':
    setup(name='fconvert',
          version=__version__,
          description='Floating-point base conversions',
          author='Andrew Dawson',
          url='https://github.com/ajdawson/fconvert',
          packages=packages,
          package_dir={'': '.'},
          scripts=scripts,)
