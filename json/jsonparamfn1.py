# In this program we are passing a json object or string as a param to a function after converting it to a dictionary
import json
json_string = '{"name":"Ralson", "age": 25, "desig":"developer"}'
a =json.loads(json_string)
print a
def func(dict):
     for k, v in dict.iteritems():
                   print k + ':', v,
                   print ','
func(a)
#func(json_string) ;  will get an AttributeError: string object has no attribute 'iteritems'
