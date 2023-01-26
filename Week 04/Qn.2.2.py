from ctypes.wintypes import LARGE_INTEGER
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
    def __init__(self, screen_type: str, screen_size : int, resolution: str, price: float) -> None:
        self.__screen_type = screen_type
        self.__screen_size = screen_size
        self.__resolution = resolution
        self.__price = price
    @property
    def screen_type(self) -> str:
        return self.__screen_type
    @property
    def screen_size(self) -> int:
        return self.__screen_size
    @property
    def  resolution(self) -> str:
        return self.__resolution
    @property
    def price(self) -> float:
        return self.__price
    @screen_type.setter
    def screen_type(self, screen_type : str) -> None:
        self.__screen_type = screen_type
    def __str__(self) -> str:
        return "Television screen_type = " + self.__screen_type + ", screen_size = " + str(self.__screen_size)\
            + ", resolution = " + self.__resolution + ", price = " + str(self.__price)

            
class Room:
    def __init__(self,type : str, size : int) -> None:
     self.__type = type
     self.__size = size
          
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
    
     
    def __str__(self) -> str:
        return " type = {} and size(sq.ft) = {}".format(self.type, self.size)
            
            
class House:
    def __init__(self, address: str, square_feet : int, garage: Garage) -> None:
        self.__address = address
        self.__square_feet = square_feet
        self.__room_items : list[Room] = []
        self.__garage : Garage = Garage(garage.type, garage.size, garage.door_type)
        self.__television_item: list[Television] = []
        
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
     
    def get_biggest_room(self) -> Room:
        #Based on the size of the room, find the largest one
        found : bool = False
        large = 1
        for item in self.__television_item:
            if  item.screen_size>large:
                large = item.screen_size
        print("Large size is : "+ large)
        return item.__screen_size
    
    #def add_Room(self, Roomno: int, type:str, size: int) -> None:      #composition
         #if len(self.__rooms) >= 4:
          #print("Cannot add more than 4")
          #self.__rooms.append(Room(Roomno, type, size))
          

    #def remove_Room(self, Roomno: int) -> None:
        #index = next((index for (index, d) in enumerate(
            #self.__rooms) if d.Roomno == Roomno), -1)
        #if index != -1:
            #self.__rooms.pop(index)
    
    #def add_television(self, telId: int, screen_type: str, screen_size: int, resolution: str, price: float) -> None:      #aggregation
        #self.__televisions.append(Television(telId, screen_type, screen_size, resolution, price))

    #def remove_television(self, telId: int) -> None :
        #index = next((index for (index, d) in enumerate(
            #self.__televisions) if d.telId == telId), -1)
        #if index != -1:
            #self.__televisions.pop(index)
    
    def change_garage_size(self, size: int) -> None:
        self.garage.size = size
        
    def get_oled_televisions(self) -> list[Television]:
         return list(filter(lambda x: x.screen_type == 'OLED', self.__television_item))
    def is_similar_house(self, other : "House") -> bool:
        return bool(self.__square_feet == other.__square_feet and len(self.__rooms) == len(other.__rooms))
            
    def add_item(self, rooms : Room, television: Television) ->None:
        found : bool = False
        for item in self.__television_item:
            if  item.screen_type == television.screen_type and item.screen_type == television.screen_type:  
                found = True
                break

       # for item in self.__room_items:
            
            #if  item.__type == rooms.__type and rooms.__size == rooms.__size:  
               # found = True
                #break

        if found is False:
            self.__television_item.append(Television(television.screen_type, television.screen_size, television.resolution, television.price))
            self.__room_items.append (Room(rooms.type,rooms.size))
        
            
    def __str__(self) -> str:
        itemlist : str = ""
        tvlist : str = ""
        for item in self.__room_items:
            itemlist += str(item) + "\n"
        for tv in self.__television_item:
            tvlist += str(item) + "\n"

        return "House address = " + str(self.__address) + ", square_feet = "+ str(self.__square_feet) \
            + ",rooms =\n" + itemlist 
            
            
def main() -> None:
    g1 : Garage = Garage("single", 230, "auto")
    print(g1)
    t1: Television = Television("LCD", 55, "1080p", 60000)
    t2: Television = Television("OLED", 60, "4k", 95000.10)
    t3: Television = Television("OLED", 44, "4k", 18000)
    print(t1)
    print(t2)
    print(t3)
    r1 : Room = Room ("Bedroom", 3500)
    r2 : Room = Room ("storeroom", 2500)
    r3 : Room = Room ("den", 400)
    print(r1)
    print(r2)
    print(r3)
    h1 : House = House("Warm Springs", 3500,g1)
    h1.add_item(r1,t1)
    h1.add_item(r2,t2)
    h1.add_item(r3,t3)
    # order.add_item(p2, 11)
    # order.add_item(p3, 12)
    # order.add_item(p1, 2)
    # print(order)
    # order.add_item
    # item : OrderItem = OrderItem (p, 10)
    print(h1)
    h1.change_garage_size(300)
    #print("Largest size is : ", house.get_biggest_room())
    oled_tvs = h1.get_oled_televisions()
    if oled_tvs:
        print("\nTelevision having OLED displays: ")
        for tv in oled_tvs:
            print(tv)
    print("\n")
    g2 : Garage = Garage("double", 250, "Auto")
    print(g2)  
    t4: Television = Television("LCD", 55, "4k", 9000)
    t5: Television = Television("LED", 25, "1080p", 5000)
    t6: Television = Television("OLED", 75, "4k", 190000)
    print(t4)
    print(t5)
    print(t6)
    r4 : Room = Room ("Bedroom", 500)
    r5 : Room = Room ("storeroom", 2500)
    r6 : Room = Room ("den", 100)
    print(r4)
    print(r5)
    print(r6)
    h2 : House = House("Blacow", 2500,g2)
    h2.add_item(r1,t1)
    h2.add_item(r2,t2)
    h2.add_item(r3,t3)
    
    print(h2)
    print("\n")
    oled_tvs = h2.get_oled_televisions()
    if oled_tvs:
        print("\nTelevision having OLED displays: ")
        for tv in oled_tvs:
            print(tv)
    
    print("\n")
    
    print("Are the houses similar ", h1.is_similar_house(h2))
    
    

   

if __name__ == "__main__":
    main()