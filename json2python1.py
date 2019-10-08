#  how to convert JSON into a Python value (i.e. Dictionary).
import json
jsonData = '{"name": "Frank", "age": 39}'
jsonToPython = json.loads(jsonData)
print jsonToPython
print jsonToPython['name']