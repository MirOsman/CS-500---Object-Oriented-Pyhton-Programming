class Months:
    def __init__(self,  month_number: int) -> None:
        self.__month_number = month_number
    @property
    def month_number(self) ->int:
        return self.__month_number
    
    @month_number.setter
    def month_number(self, month_number: int) -> None:
        self.__month_number = month_number
    def advance(self) -> None:
        self.__month_number +=1
        # print("Next Month = " + month_txt[self.__month_number])
    def prev(self) -> None:
        self.__month_number -=1
        # print("Previous Month = " + month_txt[self.__month_number])

    def display(self) -> None:
            print("Currect Month number = " + str(self.__month_number) \
                + " Month = "+ month_txt[self.__month_number])
    def compare(self, Months) -> int:
        if  Months > self.__month_number:
            return 1
        elif Months < self.__month_number:
            return -1
        else:
            return 0
        
    def _str_(self) -> str:
        return "Initial Month Number = " + str(self._month_number) + ", Month = " + month_txt[self._month_number]
month_txt = ("Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec")
def main() -> None:
    
    m : Months = Months (0)
    print(m)
    m.advance()
    m.advance()

    m.display()

    m.prev()
    m.display()

    value = m.compare(2)
    print ("Returned : ", value)

if __name__ == "__main__":
    main()