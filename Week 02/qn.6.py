height = 4
fillchar = '*'
def triangleOfSymbols(height, symbol):
 for i in range(height):
    print(' ' * (height - i - 1) + fillchar * (2 * i + 1))
      
def main():
    print("Print a rectangle of symbols")
    height = int(input("Enter the height: "))
    symbol = input("Enter the symbol: ")
    triangleOfSymbols(height, symbol)

  
if __name__=="__main__":
    main()

