# In this program a json object which is a string is passed as a parameter to a python function
import json
json_string = '{"name":"Ralson", "age": 25, "desig":"developer"}'
a =json.loads(json_string)
print a
def func(strng):
     for i in strng:
         print i,
func(json_string)

