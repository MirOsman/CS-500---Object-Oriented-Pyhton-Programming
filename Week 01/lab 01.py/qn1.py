#print the program title
print("Calculating the sum of product prices")

#get user input
numProducts = int(input("Please enter the number of products: "))

#get all product prices
n = 0
sum = 0
while n < numProducts :
  price = float(input("Enter a product price: "))
  sum = sum + price
  n = n + 1
  
  #print the sum
print("The sum is $", round(sum,2), sep="")