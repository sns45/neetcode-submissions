import math

class AreaCalc:
    # TODO: Implement calculate method
    def calculate(self, length: int, width: int = None):
        if not width:
            return round(math.pi * (length**2), 2)
        return length * width

        
    pass
    

    
# Don't modify the following code
calc = AreaCalc()
print(calc.calculate(5))    
print(calc.calculate(4, 6))
