import bottle
from beaker.middleware import SessionMiddleware

from sys import stderr

import backend.config as config
import backend.controllers as Controllers

session_opts = {
    'session.type': 'file',
    'session.data_dir': '.data',
    'session.auto': True
}

app = SessionMiddleware(bottle.app(), session_opts)
stderr.write("Application initialized with session\n")

"""Importing Controllers"""
Controllers.Automaton()
Controllers.Users()
stderr.write("Controllers imported\n")

bottle.debug(True)
bottle.run(app, host=config.HOST, port=config.PORT, reloader=True)

stderr.write("Automata server is shutting down\n")
