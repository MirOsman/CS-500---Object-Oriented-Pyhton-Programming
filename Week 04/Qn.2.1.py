from ctypes import sizeof
from turtle import Screen, screensize


class Garage:
    def __init__(self, type: str, size: int, door_type: str) -> None:
        self.__type = type
        self.__size = size
        self.__door_type = door_type

    @property
    def type(self) ->str:
        return self.__type
    @property
    def size(self):
        return self.__size
    @property
    def door_type(self)-> str:
        return self.__door_type

    @type.setter
    def type(self, type: str) -> None:
        self.__type = type
    @type.setter
    def size(self, size: int) -> None:
        self.__size = size 
    def __str__(self) -> str:
        return "Garage type = " + self.__type + ", size = "+ str(self.__size) + ", door_type = " + self.__door_type

class Room:
    def __init__(self, type: str, size: int) -> None:
        self.__type = type
        self.__size = size

    @property
    def type(self) -> str:
        return self.__type

    @property
    def size(self) ->int:
        return self.__size

    def __str__(self) -> str:
        return "Room  type = " + str(self.__type)\
            + ", size = " + str(self.__size)

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
class House:
    def __init__(self, address: str, square_feet : int, garage: Garage) -> None:
        self.__address = address
        self.__square_feet = square_feet
        self.__room_items : list[Room] = []
        self.__garage : Garage = Garage(garage.type, garage.size, garage.door_type)
        self.__television_item: list[Television] = []
    def get_biggest_room(self) -> Room:
        #Based on the size of the room, find the largest one
        found : bool = False
        large = 1
        for item in self.__television_item:
            if  item.screen_size>large:
                large = item.screen_size
        print("Large size is : "+ large)
        return item.__screen_size
    
    def change_garage_size(self, size: int) -> None:
        self.garage_size = size
        
   
    def is_siimilar_house(self, other) -> bool:
        return bool(self.__square_feet == other.__square_feet and len(self.__rooms) == len(other.__rooms))
        
    def add_item(self, rooms : Room, television: Television) ->None:
        found : bool = False
        for item in self.__television_item:
            if  item.screen_type == television.screen_type and item.screen_type == television.screen_type:
              
                found = True
                break

        if found is False:
            self.__television_item.append(Television(television.screen_type, television.screen_size, television.resolution, television.price))
            self.__room_items.append(Room(rooms.type,rooms.size))
        
        # found : bool = False
        
        # for item in self.__room_items:
        #     if  item._room_type == rooms._type:
        #         # item.size = rooms.size
        #         # item.type = rooms.size 
        #         found = True
        #         break

        # if found is False:
        #     self._room_items.append(Room(item.type,item._size))
              
        # found : bool = False
        # for item in self.__television_item:
        #     if item.television.screen_type == television.screen_type:
        #         item.__screen_type = television.screen_type
        #         item.__screen_size = television.screen_size
        #         item.__resolution = television.resolution
        #         item.__price = television.price
        #         found = True
        #         break
        # if found is False:
        #     self.__television_item.append(television)
        
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
    g : Garage = Garage("single", 230, "auto")
    print(g)
    t1: Television = Television("LCD", 65, "1080p", 90000)
    t2: Television = Television("LED", 75, "1080p", 95000)
    t3: Television = Television("OLED", 95, "4k", 190000.50)
    print(t1)
    print(t2)
    print(t3)
    r1 : Room = Room ("Bedroom", 2500)
    r2 : Room = Room ("storeroom", 500)
    r3 : Room = Room ("den", 200)
    print(r1)
    print(r2)
    print(r3)
    house : House = House("Warm Springs", 3500,g)
    house.add_item(r1,t1)
    house.add_item(r2,t2)
    house.add_item(r3,t3)
    # order.add_item(p2, 11)
    # order.add_item(p3, 12)
    # order.add_item(p1, 2)
    # print(order)
    # order.add_item
    # item : OrderItem = OrderItem (p, 10)
    print(house)
    

   

if __name__ == "__main__":
    main()