# fconvert

Tools for converting floating-point number representations between bases.
Supports conversions between decimal (float/double), binary and hexadecimal.

## Usage

The packages provides 8 separate programs, each of which is invoked in the same way.
A program can take as input a single representation, or read multiple representations
from stdin making it handy for pipelines.
To convert a 32-bit float to binary:

    $ float2bin 3.2743
    0b01000000010100011000111000100010

If you want to work with 64-bit floating-point then use the equivalent *double*
programs instead:

    $ double2bin 3.2743
    0b0100000000001010001100011100010000110010110010100101011110101000

For conversions between binary and hexadecimal it is not necessary to specify
32- or 64-bit precision as it will be inferred.
The inference is based on length of the input string, so if you want to convert
a representation with only a few bits to 64-bit you need to specify it to at
least 33 digits for binary input and 9 digits for hexadecimal input using leading
zeros.
For example, converting the hexadecimal string "0x11" to binary will assume
32-bit:

    $ hex2bin 0x11
    0b00000000000000000000000000010001

If we wanted a 64-bit binary representation we'd need to pad with leading zeros:

    $ hex2bin 0x0000000000000011
    0b0000000000000000000000000000000000000000000000000000000000010001
