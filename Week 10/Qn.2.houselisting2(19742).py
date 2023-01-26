from abc import ABC, abstractmethod

class Subject(ABC):
    @abstractmethod
    def registerObserver(self, o):
        pass

    @abstractmethod
    def removeObserver(self, o):
        pass

    @abstractmethod
    def notifyObserver(self):
        pass

class Observer(ABC):
    @abstractmethod
    def update(self, message, house):
        pass

class Displayable(ABC):
    @abstractmethod
    def display(self):
        pass

class House(Displayable):
    def __init__(self, address, squareFeet, numRooms, price):
        self.__address = address
        self.__squareFeet = squareFeet
        self.__numRooms = numRooms
        self.__price = price

    # add some public properties here if necessary
    @property
    def address(self) -> str:
        return self.__address

    @address.setter
    def address(self, address: str) -> None:
        self.__address = address

    @property
    def price(self) -> int:
        return self.__price

    @price.setter
    def price(self, price: int) -> None:
        self.__price = price

    def display(self):
        print("Address = {0}, Square Feet= {1}, Num of Rooms= {2}, Price = {3}".format(
            self.__address, self.__squareFeet, self.__numRooms, self.__price))


class Contact(Displayable):
    def __init__(self, firstName, lastName, phoneNumber, email):
        self.__lastName = lastName
        self.__firstName = firstName
        self.__email = email
        self.__phoneNumber = phoneNumber

    # add some public properties here if necessary
    @property
    def firstName(self) -> str:
        return self.__firstName

    @firstName.setter
    def firstName(self, firstName: str) -> None:
        self.__firstName = firstName

    def display(self):
        print("Last Name = {0}, First Name= {1}, Phone Number = {2}, Email = {3}".format(
            self.__lastName, self.__firstName, self.__phoneNumber, self.__email))


class Owner(Observer, Contact):
    def __init__(self, lastName, firstName, phoneNumber, email):
        super().__init__(lastName, firstName, phoneNumber, email)
        self.__houses = []
        
    @property
    def houses(self) -> list:
        return self.__houses

    def addHouse(self, house):
        self.__houses.append(house)

    def display(self):
        super().display()
        print("Owns the following houses:")
        for house in self.__houses:
            house.display()

    def update(self, message, house):
        print(f"\nOwner of House: {self.firstName}: Notified")
        print(message)
        house.display()
        


class Buyer(Observer, Contact):
    def __init__(self, lastName, firstName, phoneNumber, email):
        super().__init__(lastName, firstName, phoneNumber, email)
        self.__watchList = []

    @property
    def watchList(self):
        return self.__watchList

    #  Save the house in his watch list
    def saveForLater(self, house):
        self.__watchList.append(house)

    # Remove the house from his watch list
    def removeFromSaveForLater(self, house):
        self.__watchList.remove(house)

    def display(self):
        super().display()
        print("Watching the following houses:")
        for i in self.__watchList:
            i.display()

    def update(self, message, house):
        print("\nBuyers Notified\n")
        print(f"{self.firstName}: Notified")
        print(message)
        house.display() 


class Company(Subject, Displayable):
    def __init__(self, companyName):
        self.__companyName = companyName
        self.__owners = []
        self.__buyers = []
        self.__agents = []
        self.__houses = []
        self.__observers = []

    def registerObserver(self, o):
        self.__observers.append(o)

    def removeObserver(self, o):
        i = self.__observers.index(o)
        if i >= 0:
            self.__observers.pop(i)

    def addOwner(self, owner):
        if owner not in self.__owners:
            self.__owners.append(owner)

    def addBuyer(self, buyer):
        if buyer not in self.__buyers:
            self.__buyers.append(buyer)

    def addAgent(self, agent):
        if agent not in self.__agents:
            self.__agents.append(agent)

    def addHouseToListing(self, house):
        if house not in self.__houses:
            self.__houses.append(house)

    def getHouseByAddress(self, address):
        result = None
        for house in self.__houses:
            if house.address == address:
                result = house
        return result

    def removeHouseFromListing(self, house):
        self.__houses.remove(house)

    # Help to remove that house from all buyers' watch list.
    def removeHouseFromSaveForLater(self, house):
        [buyer.removeFromSaveForLater(
            house) for buyer in self.__buyers if house in buyer.watchList]

    def getBuyersByHouse(self, house):
        buyers = [buyer for buyer in self.__buyers if house in buyer.watchList]
        return buyers

    def display(self):
        print("\nCompany Name =", self.__companyName)
        print("\n============================ The list of agents: ============================")
        for agent in self.__agents:
            agent.display()

        print("\n============================ The house listing: =============================")
        for house in self.__houses:
            house.display()

        print("\n============================ The list of owners: ============================")
        for owner in self.__owners:
            owner.display()

        print("\n============================ The list of buyers: ============================")
        for buyer in self.__buyers:
            buyer.display()

    def notifyPriceChangeOrSold(self, house, message):
        [agent.update(message, house) for agent in self.__agents]
        buyers = self.getBuyersByHouse(house)
        [buyer.update(message, house) for buyer in buyers]
        [owner.update(message, house)
         for owner in self.__owners if house in owner.houses]


    def notifyObserver(self, house, message):
        for o in self.__observers:
            if isinstance(o, Owner):
                if house in o.houses:
                    o.update(message, house)
                    print()
            if isinstance(o, Buyer):
                o.update(message, house)
            if isinstance(o, Agent):
                o.update(message, house)

class Agent(Observer, Contact):
    def __init__(self, lastName, firstName, phoneNumber, email, position, company):
        super().__init__(lastName, firstName, phoneNumber, email)
        self.__position = position
        self.__company = company

    def addHouseToListingForOwner(self, owner, house):
        self.__company.addOwner(owner)
        self.__company.addHouseToListing(house)
        self.__company.notifyObserver(house, message = "New House Added")

    def helpBuyerToSaveForLater(self, buyer, house):
        self.__company.addBuyer(buyer)
        buyer.saveForLater(house)

    def editHousePrice(self, address, newPrice):
        house = self.__company.getHouseByAddress(address)
        if house:
            house.price = newPrice
            self.__company.notifyPriceChangeOrSold(
                house, message='House Price Is Updated')

    def soldHouse(self, house):
        self.__company.notifyPriceChangeOrSold(house, message="House is sold")
        self.__company.removeHouseFromListing(house)
        self.__company.removeHouseFromSaveForLater(house)
        

    # print all potential buyers who are interested in buying that house
    def printPotentalBuyers(self, house):
        buyers = self.__company.getBuyersByHouse(house)
        for buyer in buyers:
            buyer.display()

    def display(self):
        super().display()
        print("Position = ", self.__position)

    def update(self, message, house):
        print("\nAgents Notified\n")
        print(f"{self.firstName}: Notified")
        print(message)
        house.display()    


def main():
    owner1 = Owner('Peter', 'Li', '510-111-2222', 'peter@yahoo.com')
    owner2 = Owner('Carl', 'Buck', '408-111-2222', 'carl@yahoo.com')

    newOwner = Owner('Charlie', 'Jackson', '408-111-0000', 'jack@yahoo.com')

    house1 = House('1111 Mission Blvd', 1000, 2, 1000000)
    house2 = House('2222 Mission Blvd', 2000, 3, 1500000)
    house3 = House('3333 Mission Blvd', 3000, 4, 2000000)

    newHouse = House('4444 Warn Spring Drive', 4000, 5, 4488999)


    buyer1 = Buyer('Tom', 'Buke', '408-555-2222', 'tom@yahoo.com')
    buyer2 = Buyer('Lily', 'Go', '510-222-3333', 'lily@yahoo.com')

    buyer3 = Buyer('Jack', 'Dan', '000-111-2222', 'jack@gmail.com')

    company = Company('Good Future Real Estate')
    agent1 = Agent('Dave', 'Henderson', '408-777-3333',
                   'dave@yahoo.com', 'Senior Agent', company)
    company.addAgent(agent1)

    company.registerObserver(owner1)
    company.registerObserver(owner2)
    company.registerObserver(agent1)
    company.registerObserver(buyer1)
    company.registerObserver(buyer2)
    company.registerObserver(buyer3)

    owner1.addHouse(house1)
    owner2.addHouse(house2)
    owner2.addHouse(house3)
    newOwner.addHouse(newHouse)

    agent1.helpBuyerToSaveForLater(buyer1, house1)
    agent1.helpBuyerToSaveForLater(buyer1, house2)
    agent1.helpBuyerToSaveForLater(buyer1, house3)

    agent1.helpBuyerToSaveForLater(buyer2, house2)
    agent1.helpBuyerToSaveForLater(buyer2, house3)

    agent1.helpBuyerToSaveForLater(buyer3, newHouse)

    agent1.addHouseToListingForOwner(owner1, house1)
    agent1.addHouseToListingForOwner(owner2, house2)
    agent1.addHouseToListingForOwner(owner2, house3)

    agent1.addHouseToListingForOwner(newOwner, newHouse)
    
    
    agent1.editHousePrice('2222 Mission Blvd', 1200000)

    company.display()

    print('\nAfter one house was sold ..........................')
    agent1.soldHouse(house3)
    agent1.soldHouse(newHouse)
    company.display()

    print('\nDisplaying potential buyers for house 1 ..........................')
    agent1.printPotentalBuyers(house1)


if __name__ == "__main__":
    main()
