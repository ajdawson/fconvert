"""Tests for float-hexadecimal conversions."""
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

from fconvert import float_to_hex, hex_to_float
from fconvert import _pad_to


class Test_float_to_hex(object):

    def test_zero(self):
        expected = '0x00000000'
        result = float_to_hex(0.0)
        assert result == expected

    def test_negative_zero(self):
        expected = '0x80000000'
        result = float_to_hex(-0.0)
        assert result == expected

    def test_nan(self):
        round_tripped = hex_to_float(float_to_hex(float('nan')))
        assert math.isnan(round_tripped)
    
    def test_inf(self):
        expected = '0x7f800000'
        result = float_to_hex(float('inf'))
        assert result == expected

    def test_negative_inf(self):
        expected = '0xff800000'
        result = float_to_hex(-float('inf'))
        assert result == expected

    def test_round_trip(self):
        test_data = [struct.unpack('<f', os.urandom(4))[0]
                     for _ in range(1000)]
        for value in test_data:
            round_tripped = hex_to_float(float_to_hex(value))
            if math.isnan(value):
                assert math.isnan(round_tripped)
            else:
                assert round_tripped == value


class Test_hex_to_float(object):

    def test_zero(self):
        expected = 0.0
        result = hex_to_float('0x00000000')
        assert result == expected

    def test_negative_zero(self):
        expected = -0.0
        result = hex_to_float('0x80000000')
        assert result == expected

    def test_nan(self):
        result = hex_to_float('0x7f800001')
        assert math.isnan(result)

    def test_inf(self):
        result = hex_to_float('0x7f800000')
        assert math.isinf(result)
        assert result > 0

    def test_negative_inf(self):
        result = hex_to_float('0xff800000')
        assert math.isinf(result)
        assert result < 0

    def test_round_trip(self):
        test_data = [
            _pad_to(hex(struct.unpack('<I', os.urandom(4))[0]), 8)
            for _ in range(1000)]
        for value in test_data:
            fromhex = hex_to_float(value)
            if math.isnan(fromhex):
                continue
            round_tripped = float_to_hex(fromhex)
            assert round_tripped == value
