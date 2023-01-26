import enum
#from functools import Enum
#from enum import Enum


class ComputerType(enum,Enum):
    Computer = 1
    SuperComputer = 2
    UltraComputer = 3
    MaxComputer = 4
    
class Computer:
    def __init__(self, cpu) -> None:
        self.__cpu = cpu
        
    def computer(self):
        print("The computer is solving a problem.")
        
class SuperComputer(Computer):
    def __init__(self, cpu) -> None:
        super().__init__(cpu)
        
    def computer(self):
        super().compute()
        print("The computer is running a simulation.")
        
class UltraComputer(SuperComputer):
    def __init__(self, cpu) -> None:
        super().__init__(cpu)
        
    def computer(self):
        super().compute()
        print("The computer is running a 3-D modelling.")
        
class MaxComputer(UltraComputer):
    def __init__(self, cpu) -> None:
        super().__init__(cpu)
        
    def computer(self):
        super().compute()
        print("The computer is creating a new world .")
        
class ComputerFactory:
    def create_computer(type: ComputerType, cpu):
        c = None
        if type == ComputerType.Computer:
            c = Computer(cpu)
        elif type == ComputerType.SuperComputer:
            c = SuperComputer(cpu)
        elif type == ComputerType.UltraComputer:
            c = UltraComputer(cpu)
        elif type == ComputerType.MaxComputer:
            c = MaxComputer(cpu)
            
        return c
        
        
        