import ADD.addition
print(ADD.addition.add(100,200))
print("another way to call package")
from SUB.substraction import substract
print(substract(300,10))
print("---------subpackage------------")
from ADD.advance.multiplication import mul
print(mul(10,30))
