# -*- coding: utf-8 -*-
# bbchain - Simple extendable Blockchain implemented in Python
#
# Copyright (C) 2017-present Jeremies Pérez Morata
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

import requests
from bbchain.net.network import Client

class HttpClient(Client):
	def __init__(self):
		pass

	def get_node_type(self, addr):
		r = requests.get(addr + "/get_node_type")
		json_resp = r.json()
		return json_resp["type"]

	def get_nodes(self, addr):
		r = requests.get(addr + "/get_nodes")
		json_resp = r.json()
		return json_resp["masters"], json_resp["miners"]

	def connect(self, addr, node_addr, node_type):
		r = requests.post(addr + "/connect", json={
			'host': node_addr,
			'type': node_type
		})
		json_resp = r.json()
		return json_resp["result"] == "OK"

	def add_data(self, nodes, data):
		# We only select one master node
		master = nodes[0]
		master_addr = "http://" + master
		r = requests.post(master_addr, data={
		
		})
		json_resp = r.json()
		return json_resp["result"] == "OK"
