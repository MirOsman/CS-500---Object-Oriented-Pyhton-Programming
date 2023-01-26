from abc import ABC, abstractmethod

class Tv:
    def play_channel(self):
        print("The tv is playing a program on a channel.")
        
class Washer:
    def settemp_wash(self):
        print("The washer is setting a water temperature to wash clothes.")
        
class Command(ABC):
    @abstractmethod
    def execute(self):
        pass
    
class TVCommand(Command):
    def __init__(self, tv : Tv) -> None:
        self.__tv = tv
        
    def execute(self):
        self.__tv.play_channel()
        
class WasherCommand(Command):
    def __init__(self, washer : Washer) -> None:
        self.__washer = washer
        
    def execute(self):
        self.__washer.settemp_wash()
        
def main():
    tv = Tv()
    washer = Washer()
    
    
    #Invoker
    Invoker = []                
    Invoker.append(TVCommand(tv))
    Invoker.append(WasherCommand(washer))
    Invoker.append(TVCommand(tv))
    
    
    # do something else
    
    
    for com in Invoker:
        com.execute()
         


if __name__ == "__main__":
    main() 
    
