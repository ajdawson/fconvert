"""Tests for hexadecimal-binary conversions."""
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

import math
import os
import struct

from fconvert import hex_to_bin, bin_to_hex
from fconvert import _pad_to


class Test_hex_to_bin(object):

    def test_zero_single(self):
        expected = '0b00000000000000000000000000000000'
        result = hex_to_bin('0x00000000')
        assert result == expected

    def test_zero_le(self):
        expected = '0b00000000000000000000000000000000'
        result = hex_to_bin('0x00000000')
        assert result == expected

    def test_negative_zero(self):
        expected = '0b10000000000000000000000000000000'
        result = hex_to_bin('0x80000000')
        assert result == expected

    def test_round_trip(self):
        test_data = [
            _pad_to(hex(struct.unpack('<I', os.urandom(4))[0]), 8)
            for _ in range(1000)]
        for value in test_data:
            round_tripped = bin_to_hex(hex_to_bin(value))
            assert round_tripped == value


class Test_bin_to_float(object):

    def test_zero(self):
        expected = '0x00000000'
        result = bin_to_hex('0b00000000000000000000000000000000')
        assert result == expected

    def test_negative_zero(self):
        expected = '0x80000000'
        result = bin_to_hex('0b10000000000000000000000000000000')
        assert result == expected

    def test_round_trip(self):
        test_data = [
            _pad_to(bin(struct.unpack('<I', os.urandom(4))[0]), 32)
            for _ in range(1000)]
        for value in test_data:
            round_tripped = hex_to_bin(bin_to_hex(value))
            assert round_tripped == value
