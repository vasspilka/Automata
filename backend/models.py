import db


class User:
  def __init__(self):
    pass

class Automaton:
  def __init__(self):

    def create(name, data):
      return db().insert('automata', {'name': name, 'data': data})

    def item(id):
      return db().selectOne('automata', {'id': id}, ('id', 'name', 'data'))
