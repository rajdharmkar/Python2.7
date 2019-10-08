# #  how to convert python dictionary into a JSON object.
# Thus, JSON is a simple way to create and store data structures within JavaScript. The reason you see JavaScript in the acronym is due to the fact that a JavaScript object is created when storing data with JSON. But, don't worry, you don't need to know JavaScript to work with JSON files, rather it is about the JSON syntax (format) itself.
#
# In brief, JSON is a way by which we store and exchange data, which is accomplished through its syntax, and is used in many web applications. The nice thing about JSON is that it has a human readable format, and this may be one of the reasons for using it in data transmission, in addition to its effectiveness when working with APIs.
# An example of JSON-formatted data is as follows:
# {"name": "Frank", "age": 39,
#  "isEmployed": true}
# In this tutorial, I will show you how to use Python to work with JSON files. So, let's get started!
# Python and JSON
# Python makes it simple to work with JSON files. The module used for this purpose is the json module. This module should be included (built-in) within your Python installation, and you thus don't need to install any external modules as we did when working with PDF and Excel files, for instance. The only thing you need in order to use this module is to import it:
# import json
# But, what does the json library do? This library mainly parses JSON from files or strings. It also parses JSON into a dictionary or list in Python and vice versa, that is converting a Python dictionary or list into JSON strings.
# JSON to Python
# Reading JSON means converting JSON into a Python value (object). As mentioned above, the json library parses JSON into a dictionary or list in Python. In order to do that, we use the loads() function (load from a string), as follows:
# import json
# jsonData = '{"name": "Frank", "age": 39}'
# jsonToPython = json.loads(jsonData)
# If you want to see the output, do a print jsonToPython, in which case you will get the following output:
# {u'age': 39, u'name': u'Frank'}
# That is, the data is returned as a Python dictionary (JSON object data structure). So, will the statement print jsonToPython['name'] return any output? Go ahead, try it out.
# Python to JSON
# In the previous section, we saw how to convert JSON into a Python value (i.e. Dictionary). In this section, I will show you how we can convert (encode) a Python value to JSON.
# Say that we have the following Dictionary in Python:
# import json
# pythonDictionary = {'name':'Bob', 'age':44, 'isEmployed':True}
# dictionaryToJson = json.dumps(pythonDictionary)
# If we print dictionaryToJson, we get the following JSON data:
#  {"age": 44, "isEmployed": true, "name": "Bob"}
# So this output is considered the data representation of the object (Dictionary). The method dumps() was the key to such operation.
# It is important to note at this point that JSON cannot store all types of Python objects, but only the following types: Lists; Dictionaries; Booleans; Numbers; Character strings; and None. Thus, any other types need to be converted in order to be stored in JSON.
# Let's say we have the following class:
#  class Employee(object):
#     def __init__(self, name):
#         self.name = name
# Let's say we created a new object abder, as follows:
#
# abder = Employee('Abder')
#
# What if we wanted to convert this object to JSON? That is json.dumps(abder)? In this case, you would get an error similar to the following:
# Traceback (most recent call last):
#   File "test.py", line 8, in <module>
#     abderJson = json.dumps(abder)
#   File "/usr/local/Cellar/python/2.7.10_2/Frameworks/Python.framework/Versions/2.7/lib/python2.7/json/__init__.py", line 243, in dumps
#     return _default_encoder.encode(obj)
#   File "/usr/local/Cellar/python/2.7.10_2/Frameworks/Python.framework/Versions/2.7/lib/python2.7/json/encoder.py", line 207, in encode
#     chunks = self.iterencode(o, _one_shot=True)
#   File "/usr/local/Cellar/python/2.7.10_2/Frameworks/Python.framework/Versions/2.7/lib/python2.7/json/encoder.py", line 270, in iterencode
#     return _iterencode(o, 0)
#   File "/usr/local/Cellar/python/2.7.10_2/Frameworks/Python.framework/Versions/2.7/lib/python2.7/json/encoder.py", line 184, in default
#     raise TypeError(repr(o) + " is not JSON serializable")
# TypeError: <__main__.Employee object at 0x10e74b750> is not JSON serializable
# But, is there a workaround? Fortunately there is. I like the workaround described on the Python Tips website. To solve this issue, we can define a method similar to the following:
# def jsonDefault(object):
#     return object.__dict__
# Then encode the object into JSON as follows:
# jsonAbder = json.dumps(abder, default=jsonDefault)
# If you print jsonAbder, you should get the following output:
# {"name": "Abder"}
# We have now encoded a Python object (abder) into JSON.
# From this tutorial, we can notice that Python again and again is proving not only its ability to work with different applications, but also its flexibility to work with different issues while working with an application, as we saw in the last part of the tutorial.
import json
a = {'name':'Bob', 'age':44, 'isEmployed':True}
b = json.dumps(a)
print b
#print b['name'] cos it is a json object
#print b['isEmployed']
#print b['age']
print b[2] # json is iterable and has index starting zero...we have iterated over the json object in code below
for i in b:
    print i,
