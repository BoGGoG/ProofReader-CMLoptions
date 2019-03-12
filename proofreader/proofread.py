#!/bin/env python

#######################################################################
# Copyright (C) 2019 David Palao
#
# This file is part of ProofReader.
#
#  ProofReader is free software: you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.
#
#  ProofReader is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with ProofReader.  If not, see <http://www.gnu.org/licenses/>.
#
#######################################################################

import sys
from proofreader.netspeak import Netspeak


def main():
    #configuration = parse_input_from_command_line()
    netspeak = Netspeak()
    #configuration["input file"]
    #search_result = netspeak(configuration["query"])
    search_result = netspeak(sys.argv[1])
    print(search_result)
