#
# linter.py
# Linter for SublimeLinter3, a code checking framework for Sublime Text 3
#
# Written by Jan T. Sott
# Copyright (c) 2017 Jan T. Sott
#
# License: MIT
# Ported to CudaLint by Alexey T.
#

from cuda_lint import Linter, util

class Iscc(Linter):
    """Provides an interface to the ISCC executable."""

    cmd = ('ISCC.exe', '/Q', '/O-', '@')
    syntax = 'Inno Setup'
    regex = (
        r'^Error on line (?P<line>\d+) in (?P<file>.*\.iss): (?P<message>.+)$'
    )
    multiline = True
    error_stream = util.STREAM_STDERR
    line_col_base = (1, 1)
