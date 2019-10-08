import re  #  eg of import of regular expression module
def convert(name):
    s1 = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', name)
    print s1
    return re.sub('([a-z0-9])([A-Z])', r'\1_\2', s1).lower()
#Works with all these (and doesn't harm already-un-cameled versions):

print convert('CamelCase')
#'camel_case'
print convert('CamelCamelCase')
#'camel_camel_case'
