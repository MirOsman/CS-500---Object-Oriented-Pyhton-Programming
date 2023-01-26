class Month : 
    month_Number = 0
    def __init__(self, month : str) -> None :
        if(month == 'January'):
            self.month_Number = 0
        elif(month == 'February'):
            self.month_Number = 1
        elif(month == 'March'):
            self.month_Number = 2
        elif(month == 'April'):
            self.month_Number = 3
        elif(month == 'May'):
            self.month_Number = 4
        elif(month == 'June'):
            self.month_Number = 5
        elif(month == 'July'):
            self.month_Number = 6
        elif(month == 'August'):
            self.month_Number = 7
        elif(month == 'September'):
            self.month_Number = 8
        elif(month == 'October'):
            self.month_Number = 9
        elif(month == 'November'):
            self.month_Number = 10
        elif(month == 'December'):
            self.month_Number = 11
        
    
    
    def advance(self) -> None:
        self.month_Number += 1
        if self.month_Number > 11:
            self.month_Number = 0
    
    def prev(self) -> None:
        self.month_Number -= 1
        if self.month_Number < 0:
            self.month_Number = 11
    
    def display(self, month_number : str) -> None:
        if(self.month_Number == 0):
            print("January")
        elif(self.month_Number == 1):
            print("February")
        elif(self.month_Number == 2):
            print("March")
        elif(self.month_Number == 3):
            print("April")
        elif(self.month_Number == 4):
            print("May")
        elif(self.month_Number == 5):
            print("June")
        elif(self.month_Number == 6):
            print("July")
        elif(self.month_Number == 7):
            print("August")
        elif(self.month_Number == 8):
            print("September")
        elif(self.month_Number == 9):
            print("October")
        elif(self.month_Number == 10):
            print("November")
        elif(self.month_Number == 11):
            print("December")

    def compare(self, m):
        if m.month_Number > self.month_Number:
            return 1
        elif m.month_Number < self.month_Number:
            return -1
        else:
            return 0


def main() -> None:
    m = Month('June')
    #displaying the month
    m.display (month_number = 5)
    # advancing the month
    m.advance()
    #previous month
    m.prev()
    n = Month('July')
    #display the month
    n.display(month_number = 6)
    #Compare the months
    print("Compare result: ", m.compare(n))

if __name__ == "__main__":
    main()


