"""Tests for float-binary conversions."""
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

from fconvert import float_to_bin, bin_to_float
from fconvert import _pad_to


class Test_float_to_bin(object):

    def test_zero(self):
        expected = '0b00000000000000000000000000000000'
        result = float_to_bin(0.0)
        assert result == expected

    def test_negative_zero(self):
        expected = '0b10000000000000000000000000000000'
        result = float_to_bin(-0.0)
        assert result == expected

    def test_nan(self):
        round_tripped = bin_to_float(float_to_bin(float('nan')))
        assert math.isnan(round_tripped)
    
    def test_inf(self):
        expected = '0b01111111100000000000000000000000'
        result = float_to_bin(float('inf'))
        assert result == expected

    def test_negative_inf(self):
        expected = '0b11111111100000000000000000000000'
        result = float_to_bin(-float('inf'))
        assert result == expected

    def test_round_trip(self):
        test_data = [struct.unpack('<f', os.urandom(4))[0]
                     for _ in range(1000)]
        for value in test_data:
            round_tripped = bin_to_float(float_to_bin(value))
            if math.isnan(value):
                assert math.isnan(round_tripped)
            else:
                assert round_tripped == value


class Test_bin_to_float(object):

    def test_zero(self):
        expected = 0.0
        result = bin_to_float('0b00000000000000000000000000000000')
        assert result == expected

    def test_negative_zero(self):
        expected = -0.0
        result = bin_to_float('0b10000000000000000000000000000000')
        assert result == expected

    def test_nan(self):
        result = bin_to_float('0b01111111100000000000000000000001')
        assert math.isnan(result)

    def test_inf(self):
        result = bin_to_float('0b01111111100000000000000000000000')
        assert math.isinf(result)
        assert result > 0

    def test_negative_inf(self):
        result = bin_to_float('0b11111111100000000000000000000000')
        assert math.isinf(result)
        assert result < 0

    def test_round_trip(self):
        test_data = [
            _pad_to(bin(struct.unpack('<I', os.urandom(4))[0]), 32)
            for _ in range(1000)]
        for value in test_data:
            frombin = bin_to_float(value)
            if math.isnan(frombin):
                continue
            round_tripped = float_to_bin(frombin)
            assert round_tripped == value
