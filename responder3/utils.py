#!/usr/bin/env python
# This file is part of Responder, a network take-over set of tools 
# created and maintained by Laurent Gaffie.
# email: laurent.gaffie@gmail.com
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
import os
import sys
import re
import logging
import socket
import time
import datetime
import json
import enum

def HTTPCurrentDate():
		Date = datetime.datetime.utcnow().strftime('%a, %d %b %Y %H:%M:%S GMT').encode()
		return Date

class ServerFunctionality(enum.Enum):
	HONEYPOT = 0
	SERVER   = 1
	TARPIT   = 2
	
class ServerProtocol(enum.Enum):
	TCP = 0
	UDP = 1
	SSL = 2

#values MUST be lists!
defaultports = {
	"DNS"  : [53],
 	"HTTP" : [80],
	"HTTPS": [443],
	"FTP"  : [21],
	"SMTP" : [25],
	"POP3" : [110],
	"POP3S": [995],
	"IMAP" : [143],
	"IMAPS": [993],
	"SMB"  : [445],
	"NBTNS": [137],
	"LLMNR": [5355],
	"MDNS" : [5353]
}