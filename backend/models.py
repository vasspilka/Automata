import db
import config
import logging

logging.basicConfig(format='%(asctime)s %(levelname)s:%(message)s',
                    filename='automata.log', level=logging.DEBUG)

DB = db.Database(config.SQL.HOST, config.SQL.USERNAME,
                 config.SQL.PASSWORD, config.SQL.DATABASE)
logging.info("Connected to SQL database\n")


class Automaton(object):

    def create(self, name, data, uid=''):
        return DB.insert('automata', {'name': name, 'data': data, 'uid': uid})

    def view(self, id):
        return DB.selectOne('automata', {'id': id}, ('id', 'name', 'data', 'uid'))

    def delete(self, id):
        pass

    def update(self, id, name, data):
        pass

class User(object):

    def get(self, gid):
        return DB.selectOne("users", {'gid': gid})

    def create(self, info):
        return DB.insert('users', {'gid': info['google_id'], 'name': info['name'],
                         'email': info['email'], 'picture': info['picture']})

    def automata(self, gid):
        user = DB.selectOne("users", {'gid': gid})
        if user:
            return DB.select("automata", {'uid': user['gid']})
