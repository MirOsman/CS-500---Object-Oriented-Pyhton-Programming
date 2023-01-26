# Take the inputs
nights = int(input('Enter number of nights: '))
people = int(input('Enter number of people: '))
meal = float(input('Enter meal charges: '))

# Find the room charge
if people == 1:
    room_charges = 155
elif people == 2:
    room_charges = 160
else:
    room_charges = 165

# Calculate the charges and the charge after including the meal
total_room_charges = room_charges * nights
total_charges = total_room_charges + meal

# Calculate the charge after including the tax
total_charges_tax = total_charges + (total_charges * 0.12)

# Display the bill
print('BILL')
print('-------------------------------')
print('Total room charge: ${}'.format(total_room_charges))
print('Total after meal: {}'.format(total_charges))
print('Total after including tax: {}'.format(total_charges_tax))

