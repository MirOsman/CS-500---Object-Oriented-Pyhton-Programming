height, weight = 5, 4 
fillchar = '*'
def rectangleOfSymbols(height, weight, symbol):
  print()
  for i in range(height):
    for j in range(weight):
      print(symbol, end='')
    print()


def main():
    print("Print a rectangle of symbols")
    height = int(input("Enter the height: "))
    weight = int(input("Enter the weight: "))
    symbol = input("Enter the symbol: ")
    
    rectangleOfSymbols(height, weight, symbol)

if __name__=="__main__":
        main()
