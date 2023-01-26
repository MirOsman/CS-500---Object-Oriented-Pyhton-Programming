
def main():
  print("A Class simple calculator")
  number1 = int(input("Enter the first number: "))
  number2 = int(input("Enter the second number: "))
  operation = input("Enter the desired operation: ")
   
  valid = True
  if operation == "+":
    result = number1 + number2
  elif operation == "-":
      result = number1 - number2
  elif operation == "*":
      result = number1 * number2
  elif operation == "/":
    result = number1 / number2
    if number2 == 0:
           print("Divide by zero!")
           valid = False
  else:
      valid = False
      print("Invalid operation!")
  if valid == True:
    print("The result is", result)

if __name__=="__main__":
  main()

