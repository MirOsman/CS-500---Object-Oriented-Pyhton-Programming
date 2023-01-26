import math
from multiprocessing.sharedctypes import Value
from tokenize import Number

import math

class MyInteger:
#constructor
 def __init__(self,value=0):
   self.value=value
#getter method
 def getValue(self):
   return self.value
#checks whether number is even or not
 def isEven(self):
    return self.value%2==0
#checks whether number is odd or not
 def isOdd(self):
  return self.value%2==1
#checks whether number is prime number or not
 def isPrime(self):
#numbers less than one are not prime
   if self.value<=1:
    return False
   for i in range(2,int(math.sqrt(self.value))+1):
    if self.value%i==0:
      return False
    return True


#create object for test-1
num=MyInteger(22)
#call the methods
print("Number: ",num.getValue())
print("Is Odd: ",num.isOdd())
print("Is Even: ",num.isEven())
print("Is Prime: ",num.isPrime())

print()

#create object for test-2
num=MyInteger(28)
#call the methods
print("Number: ",num.getValue())
print("Is Odd: ",num.isOdd())
print("Is Even: ",num.isEven())
print("Is Prime: ",num.isPrime())

