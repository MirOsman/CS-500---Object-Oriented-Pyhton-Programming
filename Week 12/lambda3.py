numbers = [2,4,5,10,12,15,30]
numbersby5 = (lambda nums :  [ x for x in numbers  if x % 5 == 0])(numbers)
print(numbersby5)