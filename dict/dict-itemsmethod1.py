'''
The items() method returns a view object. The view object contains the
key-value pairs of the dictionary, as tuples in a list.
The view object will reflect any changes done to the dictionary,
see example below.
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

x = car.items()

print(x)

Syntax
dictionary.items()
Parameter Values
No parameters

More Examples
Example
When an item in the dictionary changes value, the view object also gets
 updated:

car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

x = car.items()

car["year"] = 2018

print(x)


'''
car1 = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

x = car1.items()

print(x)

car = {
  "brand": "Merc",
  "model": "S class",
  "year": 1984}
#car2["year"] = 2016# updating here
y = car.items()
car["year"] = 2019# not updating?

print(y)