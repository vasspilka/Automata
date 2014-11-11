import bottle
import random
import string
import json
import rauth
import config
import models
from sys import stderr

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

autom_page = bottle.template(open('index.tpl',"r").read())

# class Hooks:
#   def __init__(self):
#     @bottle.hook('before_request')
#     def global_session():
#        # Random 32byte state and Session intialazation
#        state = ''.join(random.choice(string.ascii_uppercase + string.digits)for x in xrange(32))
#        bottle.request.session = bottle.request.environ.get('beaker.session')
#        bottle.request.session['state'] = state
#        bottle.request.session.save()


class StaticFiles:
  def __init__(self):
    @bottle.route('/:path#(images|css|js)\/.+#')
    def server_static(path):
      return bottle.static_file(path, root='site')

class Routes:
    def __init__(self):
      @bottle.route('/', methods=['GET'])
      def index():
        return autom_page

class Automaton:
    def __init__(self):
        @bottle.route('/api/automaton/create', method='POST')
        def create():
            stderr.write("Processing automaton/create request\n")

            name = bottle.request.forms.name
            data = bottle.request.forms.data

            stderr.write("Creating new automaton\n")
            id = models.automaton_create(name, data)
            stderr.write("New automaton was created with id %i\n" % (id))

            return autom_page

        @bottle.route('/automaton/delete', method='POST')
        def delete():
            pass

        @bottle.route('/automaton/update', method='POST')
        def update():
            pass

        @bottle.route('/api/automaton/<id:int>',method='GET')
        def view(id):
            stderr.write("Processing automaton/view request with id %s\n" % (id))

            stderr.write("Retrieving automaton\n")
            item = models.automaton_item(id)
            stderr.write("Automaton successfully retrieved\n")

            return item

        @bottle.route('/automaton/list', method='GET')
        def list():
            pass


class Users:
    def __init__(self):
      @bottle.route('/login<:re:/?>')
      def login():
        params = dict(
            scope='email profile',
            response_type='code',
            redirect_uri=redirect_uri
        )
        url = google.get_authorize_url(**params)

        bottle.redirect(url)

      @bottle.route('/success<:re:/?>')
      def login_success():
        code = bottle.request.params.get('code')
        auth_session = google.get_auth_session(
            data=dict(
                code=code,
                redirect_uri=redirect_uri,
                grant_type='authorization_code'
            ),
            decoder=json.loads
        )



        json_path = 'https://www.googleapis.com/oauth2/v1/userinfo'
        session_json = auth_session.get(json_path).json()
        # For non-Ascii characters to work properly!
        session_json = dict((k, unicode(v).encode('utf-8')) for k, v in session_json.iteritems())

        user_info = dict(
            email = session_json['email'],
            name= session_json['name'],
            google_id= session_json['id'],
            picture = session_json['picture']
        )
        embed()
        return autom_page
