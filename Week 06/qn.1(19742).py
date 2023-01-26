from abc import ABC, abstractmethod
from operator import indexOf
#from typing import list
import typing

class Movable(ABC):
    @abstractmethod
    def move(self) -> None:
        pass
    
class Displayable(ABC):
    @abstractmethod
    def display(self) -> None:
        pass
    
class Flyable(ABC):
    @abstractmethod
    def fly(self) -> None:
        pass
    
    
class Part(Displayable):
    def __init__(self, partno : int, price : float) -> None:
        self.__partno = partno
        self.__price = price
        
    @property
    def partno(self) -> int:
        return self.__partno
    
    @partno.setter
    def partno(self, i : int):
        self.__partno = i
    
    @property
    def price(self) -> float:
        return self.__price

    @price.setter
    def price(self, price: float) -> None:
        self.__price = price
    
        
    def display(self) -> None:
        print(f"partno = {self.__partno}")
        print(f"price = {self.__price}")
        
class MovablePart(Part, Movable):
    def __init__(self, partno : int, price: float,type : str) -> None:
        Part.__init__(self, partno, price)
        self.__type = type
        
    @property
    def type(self) -> str:
        return self.__type
        
    def display(self) -> None:
        super().display()
        print(f"type = {self.__type}")
        
    def move(self) -> None:
        print(f"partno: {self.partno} is moving fast!")
        
        
class Jetfighter(Displayable, Flyable):
    def __init__(self, model : str, speed : int) -> None:
        self.__model = model
        self.__speed = speed
        
    @property
    def model(self) -> str:
        return self.__model
    
    @model.setter
    def model(self, m):
        self.__model = m
        
    @property
    def speed(self):
        return self.__speed
    
    @speed.setter
    def speed(self, s):
        self.__speed = s
    
    
    def fly(self) -> None:
        print(f"The JetFigher {self.__model} is flying in the sky!")
        
        
    def display(self) -> None:
        print(f"model = {self.__model}")
        print(f"speed = {self.__speed}")
        
class Machine(Displayable):
        
    def __init__(self,machine_name : str) -> None:
        self.__machine_name = machine_name
        self.__parts : list[Part] = []
        
    @property
    def machine_name(self) -> str :
        return self.__machine_name
    
    @machine_name.setter
    def machine_name(self, i):
        self.__machine_name = i
        
    def add_part(self, part : Part) -> None:
        self.__parts.append(part)
        
    def remove_part(self, partNo) -> None:
        for part in self.__parts:
            if(part.partno == partNo):
                self.__parts.remove(part)
                
    #def remove_part(self, partNo):
        #self.__parts.pop(partNo)

        
    @abstractmethod
    def doWork(self) -> None:
        pass
    
    def display(self) -> None:
        print(f"machine_name = {self.__machine_name}")
        print("The machine has these parts:")
        for part in self.__parts:
            part.display()
            print()
            
    def find_duplicated_parts(self) -> dict:
        partFreq = {}
        for part in self.__parts:
            if part.partno in partFreq.keys():
                partFreq[part.partno] +=1
            else:
                partFreq[part.partno] =1
        for k, v in list(partFreq.items()):
            if v == 1:
                del partFreq[k]
        return partFreq        

    def get_movable_parts(self) -> list[MovablePart]:
        movableParts : list[MovablePart]= []
        for part in self:
            if  isinstance(part, MovablePart):
                movableParts.append(part)
        return movableParts
    
            
    
    def __iter__(self):
        self.__index = -1          #initialize index for each iteration
        return self

#define the method that gets the next object
    def __next__(self):
        if self.__index == len(self.__parts)-1:
            raise StopIteration
        self.__index += 1
        parts = self.__parts[self.__index]
        return parts
            
class Robot(Machine, Jetfighter):
    def __init__(self, machine_name : str, cpu : str,model : str, speed : int) -> None:
        Machine.__init__(self, machine_name)
        Jetfighter.__init__(self, model, speed)
        self.__cpu = cpu
        self.__parts : list[Part] = []
        #self.__part = Part
        #Part.__init__(self, partno, price)
        
    @property
    def cpu(self):
        return self.__cpu
    
    @cpu.setter
    def cpu(self, c):
        self.__cpu = c
        
    #@property
    #def Part(self) -> str :
        #return self.Part
        
    def fly(self) -> None:
        super().fly()
        print(f"The Robot {self.machine_name} is flying over the ocean!")
    
    def doWork(self) -> None:
        print(f"The Robot {self.machine_name} is assembling a big truck.")
        
    def display(self) -> None:
        print(f" cpu = {self.__cpu}")
        Machine.display(self)
        Jetfighter.display(self)
        
    def get_expensive_parts(self, t_price):
        expensiveparts = []
        for part in self:
            if part.price >= t_price:
                expensiveparts.append(part)
        return expensiveparts
    
    def get_movable_parts_bytype(self) -> dict[str, list[Part]]: #list[MovablePart]:
        movable_parts_bytype : dict[str, list[Part]]  = {}                 # : #list[MovablePart] = {}
        print(self.__parts)
        for part in self.__parts:
            if isinstance(part, MovablePart):
                print(part)
                if part.type not in movable_parts_bytype:
                   movable_parts_bytype[part.type] = [part]
                else:
                   movable_parts_bytype[part.type].append(part)
        return movable_parts_bytype
    
    #def remove_part(self, partno) -> None:
        #for part in self.__parts:
            #if(part.partno == partno):
                #self.__parts.remove(part)
    
    #def find_duplicated_parts(self) -> dict:
        #partFreq = {}
        #for partno in partno.keys():
         #print(partno,'=>', partno[partno], 'times')
        #if partFreq.partno in partFreq.keys():
                #partFreq[partFreq.partno] +=1
        #else:
                #partFreq[partFreq.partno] =1
        #for k, v in list(partFreq.items()):
            #if v == 1:
                #del partFreq[k]
        #return partFreq      
        
    def get_movable_parts(self) -> list[MovablePart]:
        movableParts : list[MovablePart]= []
        for part in self:
            if  isinstance(part, MovablePart):
                movableParts.append(part)
        return movableParts
            
        
        
def main() -> None:
        robo = Robot('MTX', 'M1X', 'F-16', 10000)
        robo.add_part(Part(111, 100))
        robo.add_part(Part(222, 200))
        robo.add_part(Part(333, 300))
        robo.add_part(Part(222, 300))
        robo.add_part(MovablePart(555, 300, "TypeA"))
        robo.add_part(Part(111, 100))
        robo.add_part(Part(111, 100))
        robo.add_part(MovablePart(777, 300, "TypeB"))
        robo.add_part(MovablePart(655, 300, "TypeA"))
        robo.add_part(MovablePart(755, 300, "TypeA"))
        robo.add_part(MovablePart(977, 300, "TypeB"))       

        robo.display()
        print()

        print("\nRobot test flight----")
        robo.fly()
        print("\nRobot dowork() test ----")
        robo.doWork()
        print("\nDuplicated part list----")
        partfreq = robo.find_duplicated_parts()
        for partno in partfreq.keys():
         print(partno,'=>', partfreq[partno], 'times')
        print("\nExpensive part list----")
        expensive_parts = robo.get_expensive_parts(200)
        for part in expensive_parts:
         part.display()
         
        print("\nMovable part list----")
        movable_parts : dict[str, list[Part]] = robo.get_movable_parts_bytype()
        print(movable_parts)
        for type, parts in movable_parts.items():
            print("type =", type)
            for part in parts:
                part.display()
        print()
        
        print("\nAsk movable to move----")
        movable_parts = robo.get_movable_parts()
        for part in movable_parts:
            part.move()
            
        print("\nTest remove_part() ----")
        robo.remove_part(333)
        for part in robo:
            if part.partno == 333:
              print('Found 333')
              break;


if __name__ == "__main__":
 main()
            