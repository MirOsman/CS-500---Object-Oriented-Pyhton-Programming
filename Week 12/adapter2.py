class OldMath:
    def divide(self,a,b) -> None:                    #old interface
        print("Quotient =", a // b)
        print("Reminder =", a % b)
        
class NewMath :
    def divide(self,a, b) -> tuple[int, int]:        #new interfcae
        quotient = a // b
        reminder = a % b
        return(quotient, reminder)
    
class MathAdapter :
    def __init__(self, math : NewMath) -> None:
        self.__math = math
        
    def divide(self,a,b) -> None:
        quotient, reminder = self.__math.divide(a,b)
        print("Quotient =", quotient) 
        print("Reminder =", reminder)
        
class Mathfactory:
    def get_math(self):
        #return OldMath()
        return MathAdapter(NewMath())
       
def main():
    math = Mathfactory().get_math()                   #math = OldMath()
    math.divide(5,2)
    
    
if __name__ == "__main__":
    main()
