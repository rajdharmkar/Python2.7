def to_camel_case(snake_str):  # snake_case; CamelCase: self-explanatory
    components = snake_str.split('_')
    print components
    # We capitalize the first letter of each component with the 'title' method and join them together.
    for i in range(len(components)):
        print components[i]
    return "".join(x.title() for x in components)# components = components[:], iterable list or just iterable
  

print to_camel_case('snake_case_vase')

snake_str = raw_input("Enter any snake_case string:")
print to_camel_case(snake_str)
