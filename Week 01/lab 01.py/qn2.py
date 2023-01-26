print("A simple Payroll System")
payRate = 14.5
numEmployees = 2

for i in range(numEmployees):
    hours = int(input("Please enter the number of work hours: "))
    grossPay = 0
    if hours <= 40:
        grossPay = hours * payRate
    elif hours <= 45:
         grossPay =( 40 * payRate) + (hours - 40) * (payRate * 1.5)
    else:
         grossPay =( 40 * payRate) + (5 * payRate * 1.5) + (hours - 45) * (payRate * 2)
         
    tax = grossPay * 0.28
    print("The gross pay is $", round(grossPay, 2), sep="")
    print("The tax is $", round(tax, 2), sep="")
    print("The net pay is $", round(grossPay - tax, 2), sep="")
    