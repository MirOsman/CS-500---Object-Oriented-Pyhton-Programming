print('The CD Calculator')
# Take the inputs
initial = float(input('Enter the initial deposit amount: '))
perc_yield = float(input('Enter annual percentage yield: '))
maturity = int(input('Enter maturity priod (number of months): '))
# Initialze the CD for month 0 as the initial deposit
cd = initial

# Calculate the CD for each month upto maturity and display it
print('Month CD')
for i in range(1, maturity+1):
    cd = cd + cd * perc_yield / 1200
    print(i, round(cd, 2))
