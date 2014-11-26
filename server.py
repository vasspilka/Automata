#!/usr/bin/python2.7
import bottle

from beaker.middleware import SessionMiddleware

from os import listdir, path
from sys import stderr

import backend.config as config
import backend.controllers as Controllers
import backend.db as DB

from IPython import embed ## For Debugging

session_opts = {
    'session.type': 'file',
    'session.data_dir': '.data',
    'session.auto': True
}

app = SessionMiddleware(bottle.app(), session_opts)
stderr.write("Application initialized with session\n")

"""Importing Controllers"""
Controllers.Hooks()
Controllers.StaticFiles()
Controllers.Routes()
Controllers.Automaton()
Controllers.Users()
stderr.write("Controllers imported\n")

bottle.debug(True)
bottle.run(app, host=config.HOST, port=config.PORT, reloader=True)

stderr.write("Automata server is shutting down\n")
