class Hand:
    def __init__(self,num_fingers : int):
        self.__num_fingers = num_fingers

    def __str__(self) -> str:
            return "Hand has " + str(self.__num_fingers) +" fingers"

class Person:
    def __init__(self,name : str,age : int,):
        self.__name = name
        self.__age = age
        self.__lhand : Hand = Hand(5)     #composition
        self.__rhand : Hand = Hand(5)     #composition
        

    def get_name(self) -> str:
        return self.__name

    def __str__(self) -> str:
        return "Person's name = " +self.__name \
        +", age = "+ str(self.__age) \
        +", lhand = "+ str(self.__lhand) \
        +", rhand = "+ str(self.__rhand) \

def main():
    lhand = Hand(5)
    print(lhand)
    rhand = Hand(5)
    
    person1 = Person("Dave",25)
    print(person1)
    
    person2 = Person("Jim", 25)
    
    
    
if __name__== "__main__":
     main()
