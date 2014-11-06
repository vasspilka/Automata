import db
import config
from IPython import embed ## For Debugging

db=db.Database(config.SQL.HOST, config.SQL.USERNAME, config.SQL.PASSWORD, config.SQL.DATABASE)

def automaton_create(name, data):
    return db.insert('automata', {'name': name, 'data': data})

def automaton_item(id):
    return db.selectOne('automata', {'id': id}, ('id', 'name', 'data'))
