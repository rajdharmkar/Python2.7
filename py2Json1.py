import json
a = {'name':'Jayson', 'age': 27, 'isEmployed': True }
def retjson():
      # type: () -> object
      python2json = json.dumps(a)
      print python2json
retjson()
