import bottle
import random
import string
import json
import rauth
import config
import models
from sys import stderr
from models import User

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

redirect_uri = '{uri}:{port}/success'.format(
    uri=config.GOOGLE_BASE_URI,
    port=config.PORT
)

page_data = dict(
  STATE = None,
  user = None
)
template = bottle.template
page = open('index.tpl',"r").read()

class Hooks:
  def __init__(self):
    @bottle.hook('before_request')
    def global_session():
       session = bottle.request.environ.get('beaker.session')
       # Random 32byte state and Session intialazation
       page_data['STATE'] = ''.join(random.choice(string.ascii_uppercase + string.digits)for x in xrange(32))
       session['state'] = page_data['STATE']
       session.save()


class StaticFiles:
  def __init__(self):
    @bottle.route('/:path#(images|css|js)\/.+#')
    def server_static(path):
      return bottle.static_file(path, root='site')

class Routes:
    def __init__(self):
      @bottle.route('/', methods=['GET'])
      def index():
        session = bottle.request.environ.get('beaker.session')
        user=User()
        if 'user' in session:
          page_data['user'] = session['user']
        else:
          page_data['user'] = None


        return template(page,page_data)

class Automaton:
    def __init__(self):
        @bottle.route('/api/automaton/create', method='POST')
        def create():
            stderr.write("Processing automaton/create request\n")

            name = bottle.request.forms.name
            data = bottle.request.forms.data

            stderr.write("Creating new automaton")
            id = models.automaton_create(name, data)
            stderr.write("\nNew automaton was created with id %i\n" % (id))

            return str(id)

        @bottle.route('/api/automaton/<id:int>',method='GET')
        def api_view(id):
            stderr.write("Processing automaton/view request with id %s\n" % (id))

            stderr.write("Retrieving automaton\n")
            item = models.automaton_item(id)
            stderr.write("Automaton successfully retrieved\n")

            return item

        @bottle.route('api/automaton/delete/<id:int>', method='POST')
        def delete(id):
            pass

        @bottle.route('api/automaton/update/<id:int>', method='POST')
        def update(id):
            pass


class Users:
    def __init__(self):
      @bottle.route('/login<:re:/?>')
      def login():
        params = dict(
            scope='email profile',
            response_type='code',
            redirect_uri=redirect_uri)
        url = google.get_authorize_url(**params)

        bottle.redirect(url)


      @bottle.route('/logout')
      def logout():
        session = bottle.request.environ.get('beaker.session')
        if 'user' in session:
          del session['user']

        bottle.redirect('/')

      @bottle.route('/success<:re:/?>')
      def login_success():
        user=User()
        session = bottle.request.environ.get('beaker.session')

        auth_session = google.get_auth_session(
            data=dict(code=bottle.request.params.get('code'),
                      redirect_uri=redirect_uri,
                      grant_type='authorization_code'),
            decoder=json.loads)

        session_json = auth_session.get('https://www.googleapis.com/oauth2/v1/userinfo').json()
        session_json = dict((k, unicode(v).encode('utf-8')) for k, v in session_json.iteritems())# For non-Ascii characters
        # Checks if user exists, if not creates new one
        if (user.get(session_json['id']) == None):
          user_info = dict(
              google_id= session_json['id'],
              name= session_json['name'],
              email = session_json['email'],
              picture = session_json['picture'])
          stderr.write("Creating new user\n")
          user.create(user_info)
          stderr.write("Success\n")

        # Creates user session
        session['user'] = session_json['id']

        bottle.redirect('/')

      @bottle.route('/api/user/<gid:int>',method='GET')
      def info(gid):
        user=User()
        return user.get(gid)

      @bottle.route('/api/user/<gid:int>/automatons',method='GET')
      def automatons(gid):
        user=User()
        automatons = user.automata(gid)

        return automatons
