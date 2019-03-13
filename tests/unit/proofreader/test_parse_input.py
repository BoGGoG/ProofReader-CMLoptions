#!/bin/env python

#######################################################################
# Copyright (C) 2019 Hendrik and Marco 
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

import unittest
from unittest.mock import patch, Mock, MagicMock

from proofreader.proofread import main

@patch("proofreader.parse_input.argparse")
class ParseInputExe(unittest.TestCase):
    def test_main_creates_ArgumentParser_instance(self, argparse):
        main()
        argparse.ArgumentParser.assert_called_once_with()

    def test_main_calls_parse_args_of_instance(self, argparse):
        parser = Mock()
        argparse.ArgumentParser.return_value = parser
        main()
        parser.parse_args.assert_called_once_with()

