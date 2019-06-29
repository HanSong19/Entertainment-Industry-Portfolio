class Calculator:
    def __init__(self):
        self.value = 0
    
    def add(self,val):
        self.value += val
        

class UpgradeCulculator(Calculator):

    def minus(self, val):
        self.value -= val

cal = UpgradeCulculator()
cal.add(10)
cal.minus(7)
print(cal.value)

class Calculator:
    def __init__(self):
        self.value = 0
    def add (self, val):
        self.value += val
        
class MaxLimitCalculator(Calculator):
    def add(self, val):
        self.value += val
        if self.value <= 100:
            return self.value
        else:
            self.value = 100
            return self.value

cal = MaxLimitCalculator()
cal.add(50)
cal.add(60)

print(cal.value)


