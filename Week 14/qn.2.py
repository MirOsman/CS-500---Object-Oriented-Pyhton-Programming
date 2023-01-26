if __name__ == "__main__":

   # Read three numbers
   
    num1=3
    num2=2
    num3=4
   
   # Find median

    if num1 > num2:
        if num1 < num3:
           median = num1
        elif num2 > num3:
           median = num2
        else:
           median = num3
    else:
       if num1 > num3:
           median = num1
       elif num2 < num3:
           median = num2
       else:
           median = num3

   # Print the number 
    print("The median number is", median)