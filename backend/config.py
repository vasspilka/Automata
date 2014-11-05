#!/usr/bin/python2.7
# -*- coding: utf-8 -*-

"""config.py: Default configuration."""

# Server:
SERVER = 'wsgiref'
HOST = 'localhost'
PORT = 8000

# Meta:
# Note on making it work in localhost:
# * Open a terminal, then do:
#   - sudo gedit /etc/hosts
# * Enter the desired localhost alias for 127.0.0.1:
#   - (e.g. 127.0.0.1 mydomain.tld)
# * Don't forget to save the file :)
BASE_URI = 'http://mydomain.tld'
GOOGLE_BASE_URI = 'http://localhost' # Google doesn't seem to accept
                                     # non-working urls, but accepts localhost

# Google:
GOOGLE_CLIENT_ID = '271248330496-mmuvpgpue8hkbukihr3dl3b3lrn3k7qh.apps.googleusercontent.com'
GOOGLE_CLIENT_SECRET = 'JL32d0Gcz35pwmvmLHGGLL-J'
