def to_camel_case(snake_str):
    components = snake_str.split('_')
    # We capitalize the first letter of each component except the first one
    # with the 'title' method and join them together.
    print components[0], components[1]
    return components[0] + "".join(x.title() for x in components[1:])
print to_camel_case('snake_case_vase')
#Example:

#In [11]: to_camel_case('snake_case')
#Out[11]: 'snakeCase'
