import db
from sqlalchemy import create_engine
import config
from IPython import embed ## For Debugging
from sys import stderr

database = "mysql+mysqldb://"+config.SQL.USERNAME+":"+config.SQL.PASSWORD+"@"+config.SQL.HOST+"/"+config.SQL.DATABASE+"?charset=utf8&use_unicode=0"
db=db.Database(config.SQL.HOST, config.SQL.USERNAME, config.SQL.PASSWORD, config.SQL.DATABASE)
create_engine(database)
stderr.write("Connected to Google Cloud SQL database\n")

def automaton_create(name, data):
    return db.insert('automata', {'name': name, 'data': data})

def automaton_item(id):
    return db.selectOne('automata', {'id': id}, ('id', 'name', 'data'))

class User:

  def automatons():
    pass;
