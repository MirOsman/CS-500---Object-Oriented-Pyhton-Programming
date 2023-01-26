Number = int(input("Please enter a number up to 100: "))

multiples = [ x      for x in range(1, 101)    if x % Number == 0 ]     # or multiples = [ x   for x in range(number, 101, number) ]
print(multiples)





