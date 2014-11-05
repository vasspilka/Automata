#!/usr/bin/python2.7
# -*- coding: utf-8 -*-

"""config.py: Default configuration."""

# Server:
SERVER = 'wsgiref'
BASE_URI = 'http://automata.discrete.gr/'
HOST = 'localhost'
PORT = 8080

# MySQL (Local or Remote)
class SQL:
  HOST     = "localhost"          # Here configure your mysql database.
  USERNAME = "user"               #
  PASSWORD = "password"           # Google cloud SQL can be used
  DATABASE = "automata"           # Just use the appropriate setup

# Google:
GOOGLE_BASE_URI = 'http://localhost'
GOOGLE_CLIENT_ID = 'your-client-id'
GOOGLE_CLIENT_SECRET = 'your-client-secret'
