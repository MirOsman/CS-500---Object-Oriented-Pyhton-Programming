class Product :
    def __init__(self, name : str, price : float) -> None:
        self.__name = name
        self.__price = price             #For diamond program use the class Product not super()
        
    def display(self) -> None:
        print(f"name = {self.__name}, price = {self.__price}")
        
class Phone(Product):
    def __init__(self, name: str, price: float, network : str) -> None:
        Product.__init__(self,name, price)              #For diamond program use the class name i.e., Product not super()
        self.__network = network
        
    def display(self) -> None:
        super().display()
        print(f"network = {self.__network}")
        
        
class Computer(Product):
    def __init__(self, name: str, price: float, speed : float) -> None:
        Product.__init__(self,name, price)
        self.__speed = speed
        
    def display(self) -> None:
        super().display()
        print(f"speed = {self.__speed}")
        
class SmartPhone(Phone,Computer):
    def __init__(self, name: str, price: float, network: str, speed: float, camera: str) -> None:
        Phone.__init__(self, name, price, network)
        Computer.__init__(self, name, price, speed)
        self.__camera = camera
        
    def display(self) -> None:
        super().display()
        print(f"camera = {self.__camera}")
        
def main() -> None:
    sp = SmartPhone("xPhone", 1000, "5G", 3.5, "8K")
    #print(vars(sp))      # pin out the data inside the function
    sp.display()
if __name__ == "__main__":
 main()

    