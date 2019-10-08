class CustomException(ValueError): # raised if data conversion fails
    def __init__(self, message):
        self.message = message;
        print("There was a problem converting data")


try:
    try:
        staffId = int(['staffId'])
        openingSalary = 19#int(row['initialSalary'])
        monthsWorked = 23#float(row['monthsWorked'])
    except ValueError as e:
        raise CutomException(e);
except CustomException(staffId):
    pass


