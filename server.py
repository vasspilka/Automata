import bottle
from beaker.middleware import SessionMiddleware
import logging
import backend.config as config
import backend.controllers as Controllers

session_opts = {
    'session.type': 'file',
    'session.data_dir': '.data',
    'session.auto': True
}

app = SessionMiddleware(bottle.app(), session_opts)
logging.warning("Application initialized with session\n")

"""Importing Controllers"""
Controllers.StaticFiles()
Controllers.Routes()
Controllers.Automaton()
Controllers.Session()
Controllers.Users()
logging.warning("Controllers imported\n")

if config.DEVELOPMENT:
    bottle.debug(True)

bottle.run(app, host=config.HOST, port=config.PORT, reloader=True)

logging.warning("Automata server is shutting down\n")
