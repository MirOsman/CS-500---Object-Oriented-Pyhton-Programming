
from typing import List
#from __future__ import annotations rather putting " "

class Garage:
    def __init__(self,type : str, size : int, door_type : str) -> None:
     self.__type = type
     self.__size = size
     self.__door_type = door_type
     
    @property
    def type(self) -> str:
         return self.__type
    
    @type.setter
    def type(self, type : str) -> None:
         self._type_ = type
     
    @property
    def size(self) -> int:
         return self.__size
    
    @size.setter
    def size(self, size : int) -> None:
         self._size_ = size
     
    @property
    def door_type(self) -> str:
         return self.__door_type
     
    @door_type.setter
    def door_type(self, door_type : str) -> None:
         self._door_type_ = door_type
     
    def __str__(self) -> str:
        return "Garage: type = {}, size(sqft) = {} and door_type = {}".format(
            self.type, self.size, self.door_type)
            
            
class Television:
    def __init__(self, telId: int, screen_type: str, screen_size: int, resolution: str, price: float) -> None:
        self.__screen_type = screen_type
        self.__screen_size = screen_size
        self.__resolution = resolution
        self.__price = price
        self.__telId = telId

    @property
    def telId(self) -> int:
        return self.__telId

    @property
    def screen_type(self) -> str:
        return self.__screen_type

    @screen_type.setter
    def screen_type(self, screen_type: str) -> None:
        self.__screen_type = screen_type

    @property
    def screen_size(self) -> int:
        return self.__screen_size

    @screen_size.setter
    def screen_size(self, screen_size: int) -> None:
        self.__screen_size = screen_size

    @property
    def resolution(self) -> str:
        return self.__resolution

    @resolution.setter
    def resolution(self, resolution: str) -> None:
        self.__resolution = resolution

    @property
    def price(self) -> float:
        return self.__price

    @price.setter
    def price(self, price: float) -> None:
        self.__price = price

     
     
    def __str__(self) -> str:
           return "Screen_type = {}, Screen_size = {}, resolution = {} and price = {}".format(
            self.screen_type, self.screen_size, self.resolution, self.price)

            
class Room:
    def __init__(self,type : str, size : int, Roomno : int) -> None:
     self.__type = type
     self.__size = size
     self.__Roomno = Roomno
          
    @property
    def type(self) -> str:
         return self.__type
     
    @type.setter
    def type(self, type : str) -> None:
         self._type_ = type
    
    @property
    def size(self) -> int:
         return self.__size
    
    @size.setter
    def size(self, size : int) -> None:
         self._size_ = size
         
    @property
    def Roomno(self) -> int:
         return self.__Roomno
     
    @Roomno.setter
    def Roomno(self, Roomno : int) -> None:
         self._Roomno_ = Roomno
          
    
     
    def __str__(self) -> str:
        return " type = {} , size(sq.ft) = {} , Roomno = {} ".format(self.type, self.size, self.Roomno)
            
            
class House:
     def __init__(self, address : str, square_feet : int, garage : Garage) -> None:
      self.__address = address
      self.__square_feet = square_feet
      self.__rooms : list[Room] =[]
      self.__garage : Garage = Garage(garage.type, garage.size, garage.door_type)
      self.__televisions : list[Television] = []
     
     
     @property
     def address(self) -> str:
         return self.__address
     
     @address.setter
     def address(self, address : str) -> None:
         self._address_ = address
         
     @property
     def square_feet(self) -> int:
         return self.__square_feet
     
     @square_feet.setter
     def square_feet(self, square_feet : int) -> None:
         self.__square_feet = square_feet
         
     @property
     def garage(self) -> Garage:
         return self.__garage
    
     def add_Room(self, type: str, size :int, Roomno : int) -> None:      #composition
         if len(self.__rooms) >= 4:
          print("Cannot add more than 4")
          self.__rooms.append(Room(type, size, Roomno))
          

     def remove_Room(self, Roomno: int) -> None:
        index = next((index for (index, d) in enumerate(
            self.__rooms) if d.Roomno == Roomno), -1)
        if index != -1:
            self.__rooms.pop(index)

     def add_television(self, telId: int, screen_type: str, screen_size: int, resolution: str, price: float) -> None:      #aggregation
        self.__televisions.append(Television(telId, screen_type, screen_size, resolution, price))

     def remove_television(self, telId: int) -> None :
        index = next((index for (index, d) in enumerate(
            self.__televisions) if d.telId == telId), -1)
        if index != -1:
            self.__televisions.pop(index)

     def change_garage_size(self, size: int) -> None:
        self.garage.size = size

         
         
     def get_biggest_room(self) -> Room:
          bigRoom : Room = len(self.__rooms) >= 4
          for room in self.__rooms:
            if room.size > bigRoom.size:
                bigRoom = room
                return bigRoom 
     def get_oled_televisions(self) -> List[Television]:
           return list(filter(lambda x: x.screen_type == 'OLED', self.__televisions))
          
     def is_similar_house(self, other: "House") -> bool:
          return bool(self.__square_feet == other.__square_feet and len(self.__rooms) == len(other._rooms))

         
         
     def __str__(self) -> str:
        houselist: str = " "
        houselist += "House Details:\nGarage details:\n{}".format( self.garage)
        houselist += "\nRoom details:\n {}".format(self.get_biggest_room)

        for room in self.__rooms:
            houselist += str(room) + "\n"

        if self.__televisions:
            houselist += "\nTelevisions:\n"
            for tel in self.__televisions:
                houselist += str(tel) + "\n"
        return houselist

def main():
    print("House 1\n")
    g: Garage = Garage("single", 50, "Pantry")
    #print(g)
    h: House = House("Blacow street", 228, g)
    #print(h)
    h.add_Room(103, "Pantry", 200)
    h.add_Room(104,"Storeroom", 300)
    #print(h)
    h.remove_Room(103)
    #print(h)
    h.add_television(125, "LED", 48, '1080px', 2300)
    h.add_television(126, "OLED", 48, '1080px', 800)
    h.remove_television(123)
    print(h)
    h.change_garage_size(300)
    print("Biggest room: ", h.get_biggest_room())
    oled_tvs = h.get_oled_televisions()
    if oled_tvs:
        print("\nTelevision having OLED displays: ")
        for tv in oled_tvs:
            print(tv)
    
    print("\n\nHouse 2\n")
    g2: Garage = Garage("double", 100, "Shop")
    h2: House = House("Eggers street", 200, g2)
    h2.add_Room(204, "Bedroom", 500)
    print(h2)
    print("\n")
    print("Are the houses similar ", h.is_similar_house(h2))

    
    
if __name__ == "__main__":
    main()