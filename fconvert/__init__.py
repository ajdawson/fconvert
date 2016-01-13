"""Conversions between floating-point base representations."""
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
from __future__ import absolute_import
import struct


def float_to_hex(f):
    """Convert a 32-bit float to hexadecimal."""
    bytes = struct.pack('<f', f)
    base10 = struct.unpack('<I', bytes)[0]
    return _pad_to(hex(base10), 8)


def hex_to_float(h):
    """Convert a 32-bit hexadecimal to a 32-bit float."""
    try:
        base10 = int(h, 16)
        bytes = struct.pack('<I', base10)
    except (TypeError, struct.error):
        raise ValueError('input cannot be converted to float')
    return struct.unpack('<f', bytes)[0]


def double_to_hex(f):
    """Convert a 64-bit double to hexadecimal."""
    bytes = struct.pack('<d', f)
    base10 = struct.unpack('<Q', bytes)[0]
    # Remove the trailing 'L' suffix on Python 2.
    base16 = hex(base10).rstrip('L')
    return _pad_to(base16, 16)


def hex_to_double(h):
    """Convert a 64-bit hexadecimal to a 64-bit double."""
    base10 = int(h, 16)
    bytes = struct.pack('<Q', base10)
    return struct.unpack('<d', bytes)[0]


def float_to_bin(f):
    """Convert a 32-bit float to binary."""
    try:
        bytes = struct.pack('<f', f)
        base10 = struct.unpack('<I', bytes)[0]
    except (TypeError, struct.error):
        raise ValueError('input cannot be converted to binary')
    return _pad_to(bin(base10), 32)


def bin_to_float(b):
    """Convert a 32-bit binary string to a 32-bit double."""
    try:
        base10 = int(b, 2)
        bytes = struct.pack('<I', base10)
    except (TypeError, struct.error):
        raise ValueError('input cannot be converted to float')
    return struct.unpack('<f', bytes)[0]


def double_to_bin(f):
    """Convert a 64-bit double to binary."""
    try:
        bytes = struct.pack('<d', f)
        base10 = struct.unpack('<Q', bytes)[0]
    except (TypeError, struct.error):
        raise ValueError('input cannot be converted to binary')
    return _pad_to(bin(base10), 64)


def bin_to_double(b):
    """Convert a 64-bit binary string to a 64-bit double."""
    try:
        base10 = int(b, 2)
        bytes = struct.pack('<Q', base10)
    except (TypeError, struct.error):
        raise ValueError('input cannot be converted to double')
    return struct.unpack('<d', bytes)[0]


def bin_to_hex(b):
    """Convert a binary representation to hexadecimal."""
    pad_length = 16 if len(b.replace('0b', '')) > 32 else 8
    base16 = hex(int(b, 2))
    return _pad_to(base16, pad_length)


def hex_to_bin(h):
    """Convert a hexadecimal representation to binary."""
    pad_length = 64 if len(h.replace('0x', '')) > 8 else 32
    base2 = bin(int(h, 16))
    return _pad_to(base2, pad_length)


def _pad_to(number_string, pad_length):
    """Pad a hexadecimal or binary string with leading zeros."""
    leader, number = number_string[:2], number_string[2:]
    return '{:2s}{:s}{:s}'.format(leader,
                                  '0' * (pad_length - len(number)),
                                  number)
