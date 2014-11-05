#!/usr/bin/python2.7

import bottle

import json
import rauth
from beaker.middleware import SessionMiddleware

import random
import string
from os import listdir, path
from sys import stderr

import backend.config as config

from IPython import embed ## For Debugging


oauth2 = rauth.OAuth2Service

google = oauth2(
    client_id=config.GOOGLE_CLIENT_ID,
    client_secret=config.GOOGLE_CLIENT_SECRET,
    name='google',
    authorize_url='https://accounts.google.com/o/oauth2/auth',
    access_token_url='https://accounts.google.com/o/oauth2/token',
    base_url='https://accounts.google.com/o/oauth2/auth',
)
session_opts = {
    'session.type': 'file',
    'session.data_dir': '.data',
    'session.auto': True
}
redirect_uri = '{uri}:{port}/success'.format(
    uri=config.GOOGLE_BASE_URI,
    port=config.PORT
)

stderr.write("Initializing bottle with session\n")
app = SessionMiddleware(bottle.app(), session_opts)
autom_page = bottle.template(open('index.tpl',"r").read())
stderr.write("Bottle app initialized\n")

host = config.HOST
port = config.PORT
# with open('../.htaccess', 'w') as htaccess:
#     htaccess.write("""<IfModule mod_rewrite.c>
#     RewriteEngine On
#     RewriteRule api/(.*) http://%s:%s/$1 [P,QSA]
# </IfModule>""" % (host, port))


# def initdb():
#     hostname = config.get('db', 'hostname')
#     username = config.get('db', 'username')
#     password = config.get('db', 'password')
#     database = config.get('db', 'database')
#     models.db.init(hostname, username, password, database)

# stderr.write("Connecting to MySQL datatabase\n")
# initdb()
# stderr.write("Connected to MySQL database\n")

# stderr.write("Loading controllers\n")
# for controller in listdir('controllers'):
#     if controller[-3:] == '.py' and controller != '__init__.py':
#         controllerName = controller[:-3]
#         controllerModule = __import__('controllers.' + controllerName)
#         controllerClass = getattr(controllerModule,
#                                   controllerName).controller
#         controllerClass(app, request)
#
# stderr.write("Controllers loaded\n")

bottle.debug(True)
bottle.run(app, host=host, port=port, reloader=True)

stderr.write("Automata server is shutting down\n")
