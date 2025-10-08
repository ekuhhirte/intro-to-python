#waiting

class Fraction:
    def __init__(self, numerator = 0, denominator = 1):
        divisor = gcd(numerator, denominator)
        self._numerator = numerator // divisor 
        self._denominator = denominator // divisor

    #getters
    @property
    def numerator(self):
        return self._numerator
    
    @property
    def denominator(self):
        return self._denominator
    
    #setters
    @denominator.setter
    def denominator(self, value):
        if value == 0:
           print("Incorrect input: Denominator cannot be zero")
           self._denominator = 1
        else: 
            divisor = gcd(self.numerator, value)
            self._denominator = value // divisor

    @numerator.setter
    def numerator(self, value):
        divisor = gcd(value, self._denominator)
        self._numerator = value // divisor

    def __str__(self):
        return f"{self.numerator}/{self.denominator}"
    
    def __mul__(self, other):
        return Fraction(self.numerator * other.numerator, self.denominator * other.denominator)
    
    def __sub__(self, other):
        numerator = self.numerator * other.denominator - other.numerator * self.denominator
        denominator = self.denominator * other.denominator
        return Fraction(numerator, denominator)
    
    def __cmp__(self, other):
        temp = self - other
        if temp.numerator < 0:
            return -1
        elif temp.numerator >0:
            return 1
        else:
            return 0
    
    def __lt__(self, other): #Less than
        return self.__cmp__(other) < 0
    


def gcd(numerator, denominator):
    gcd = 1
    i = 1

    while i <= numerator and i <= denominator:
        if numerator % i == 0 and denominator & i == 0:
            gcd = i
        
        i += 1

    return gcd


f1 = Fraction(2,3)
print(f1.numerator)
print(f1.denominator)

f1.numerator = 7
print(f1)

f2 = Fraction(3,7)
print(f2)

print (f"{f1} * {f2} = {f1 * f2}") # f1 * f2 -> f1.__mul__(f2)
print(f"{f1} < {f2} is {f1 < f2}") 
