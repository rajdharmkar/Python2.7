# example of assert statement;  syntax : assert (expression), argument
# if the expression on evaluation is true the function executes and returns the output else the 'argument' is printed with
# AssertionError..assert is a way of testing concepts?

def KelvinToFahrenheit(Temperature):
   assert (Temperature >= 0),"Colder than absolute zero!"
   return ((Temperature-273)*1.8)+32

print KelvinToFahrenheit(273)
print int(KelvinToFahrenheit(505.78))
print KelvinToFahrenheit(-5)
