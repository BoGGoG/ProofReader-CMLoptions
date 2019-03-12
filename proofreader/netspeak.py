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

from urllib import parse, request


NETSPEAK_REST_BASE_URL = "http://api.netspeak.org/netspeak3/search"


class Netspeak:
    _base_query_url = NETSPEAK_REST_BASE_URL
    
    def __call__(self, user_input):
        query = self._encode_query(user_input)
        url = self._make_request(query)
        return self._read_result(url)
        
    def _encode_query(self, query):
        params = {"query": query, "format": "text"}
        return parse.urlencode(params)

    def _make_request(self, query):
        return request.urlopen(self._base_query_url+"?"+query)

    def _read_result(self, url):
        return url.read().decode()
    
