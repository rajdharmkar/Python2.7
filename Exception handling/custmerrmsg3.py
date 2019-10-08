class CustomValueError(ValueError):
 def __init__(self, arg):
    self.arg = arg
try:
    a = int(input("Enter a number:"))
    if not 1 < a < 10:
       raise CustomValueError("Value must be within 1 and 10.")
except CustomValueError as e:
 print("CustomValueError Exception!", e.arg)