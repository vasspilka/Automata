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

stderr.write("Initializing bottle with session\n")
app = SessionMiddleware(bottle.app(), session_opts)
stderr.write("Bottle app initialized\n")

# with open('../.htaccess', 'w') as htaccess:
#     htaccess.write("""<IfModule mod_rewrite.c>
#     RewriteEngine On
#     RewriteRule api/(.*) http://%s:%s/$1 [P,QSA]
# </IfModule>""" % (host, port))

stderr.write("Connecting to Google Cloud SQL datatabase\n")
DB.init(config.SQL.HOST, config.SQL.USERNAME, config.SQL.PASSWORD, config.SQL.DATABASE)
stderr.write("Connected to Google Cloud SQL database\n")

stderr.write("Importing controllers\n")
Controllers.StaticFiles()
Controllers.Routes()
Controllers.Automaton()
# Controllers.Hooks()
# Controlers.Users()
stderr.write("Controllers imported\n")

bottle.debug(True)
bottle.run(app, host=config.HOST, port=config.PORT, reloader=True)

stderr.write("Automata server is shutting down\n")
