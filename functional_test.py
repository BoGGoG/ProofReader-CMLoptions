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

import unittest
import subprocess as sp

class NewUserTestCase(unittest.TestCase):
    def test_can_run_proofread_program(self):
        #  Mary is a new PhD student. She has worked hard during the past
        # months and she wants to publish the results. She is told by her
        # advisor that the article must be written in English. English!
        #  She can write in English, but sometimes she feels unsure concerning
        # prepositions. She knows technical words, but she would like to
        # have more vocabulary. She feels a bit worried.
        #  Fortunately, there is another PhD student that mentions something
        # called "ProofReader". It appears to be a piece of software that can help
        # her with her problems.
        #  After installing this tool, the first thing she does is, of course,
        # try to use it:
        proofread_run_result = sp.run(["proofread"], stderr=sp.PIPE)

        # # Wonderful! It seems to work ...but it returns an error:
        # self.assertNotEqual(0, proofread_run_result.returncode)
        
        # #  Thanksfully, she also gets a hint to use the tool:
        # self.assertIn(
        #     "the following argument is required: query",
        #     proofread_run_result.stderr.decode()
        # )

        #  Mary tries to provide an argument to "proofread". She wants to obtain
        # the synonyms of "compute":
        proofread_run_result = sp.run(["proofread", "#compute"], stdout=sp.PIPE)
        proofread_run_result_output = proofread_run_result.stdout.decode()
        # She gets, as output, a list of words, among them she sees "calculate", 
        # "reckon" and "work out":
        compute_synonyms = ("calculate", "reckon", "work out")
        for synonym in compute_synonyms:
            self.assertIn(synonym, proofread_run_result_output)

        # and the output contains information about how many occurrences of each
        # result have been found in the web
        lines = proofread_run_result_output.split("\n")
        for line in lines:
            if len(line) > 0:
                elements = line.split("\t")
                self.assertEqual(len(elements), 3)
                int(elements[0])

        # Nice! It seems that the program can be useful for her purposes.
        # She goes to sleep very happy: tomorrow she will try to proofread her first
        # paper with this tool!

    def test_can_accept_h(self):
        proofread_run_result = sp.run(["proofread", "-h"], stdout=sp.PIPE)
        proofread_run_result_output = proofread_run_result.stdout.decode()
        wanted_out = "usage: proofread"
        self.assertIn(wanted_out, proofread_run_result_output)
        

if __name__ == "__main__":
    unittest.main()
    
