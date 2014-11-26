import db
import config
from sys import stderr

DB=db.Database(config.SQL.HOST, config.SQL.USERNAME, config.SQL.PASSWORD, config.SQL.DATABASE)
stderr.write("Connected to Google Cloud SQL database\n")

def automaton_create(name, data, uid = ''):
    return DB.insert('automata', {'name': name, 'data': data, 'uid': uid})

def automaton_item(id):
    return DB.selectOne('automata', {'id': id}, ('id', 'name', 'data', 'uid'))

class User(object):

  def get(self,gid):
    return DB.selectOne("users",{'gid': gid})

  def automata(self,gid):
    user = DB.selectOne("users",{'gid': gid})
    if user:
      user_automata = DB.select("automata",{'uid': user['gid']})

    return user_automata

  def create(self,info):
    return DB.insert('users', {'gid':info['google_id'],'name': info['name'],
                     'email': info['email'],'picture': info['picture']})
