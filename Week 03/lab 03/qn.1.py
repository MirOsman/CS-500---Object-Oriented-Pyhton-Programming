# hexadecimal equivalent
hexa_conversions = {0: '0', 1: '1', 2: '2', 3: '3', 4: '4',
                    5: '5', 6: '6', 7: '7',
                    8: '8', 9: '9', 10: 'A', 11: 'B', 12: 'C',
                    13: 'D', 14: 'E', 15: 'F'}
def to_hex(decimal):
    hexa = ''
    while(decimal > 0):
        remainder = decimal % 16
        hexa += hexa_conversions[remainder] 
        decimal = decimal // 16
 
    return hexa
#prompt user to enter a decimal value from 0 to 15
num = int(input('Enter a decimal value (0 to 15): '))
print(f'The hex value is {to_hex(num)}')
