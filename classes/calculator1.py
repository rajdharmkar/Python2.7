class Calculator:
    current = 9# class variable?

    def add(self, amount):
        self.current += amount
    def subtract(self, amount):
        self.current -= amount

    def multiply(self, amount):
            self.current *= amount

    def get_current(self):
        return self.current
c = Calculator()
c.add(111)
c.subtract(8)
c.add(213)
c.multiply(2)
print (c.get_current())
