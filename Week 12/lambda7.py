from functools import reduce
fruits = ["apple","orange","pear","banana"]
fruits2 = reduce(lambda sum, x: sum.title() + ", " +  x.title(), fruits)
print(fruits2)