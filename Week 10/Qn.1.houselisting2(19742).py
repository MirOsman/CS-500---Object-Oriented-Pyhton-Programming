from abc import ABC, abstractmethod


class Displayable(ABC):
    @abstractmethod
    def display():
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
    def address(self, address: str) -> None :
        self.__address = address

    @property
    def price(self) -> int:
        return self.__price

    @price.setter
    def price(self, price: int) -> None:
        self.__price = price 

    def display(self):
        print("Address = {0}, Square Feet= {1}, Num of Rooms= {2}, Price = {3}".format(self.__address, self.__squareFeet, self.__numRooms, self.__price))
        

    def __eq__(self, __o: object) -> bool:
        if isinstance(__o, House):
            return self.__address == __o.__address
        
        return False
    
class Contact(Displayable):
    def __init__(self, firstName, lastName, phoneNumber, email):
        self.__lastName = lastName
        self.__firstName = firstName
        self.__email = email
        self.__phoneNumber = phoneNumber

    # add some public properties here if necessary 

    def display(self):
        print("Last Name = {0}, First Name= {1}, Phone Number = {2}, Email = {3}".format(self.__lastName, self.__firstName, self.__phoneNumber, self.__email))


class Owner(Contact):
    def __init__(self, lastName, firstName, phoneNumber, email):
        super().__init__(lastName, firstName, phoneNumber, email)
        self.__houses = []

    def addHouse(self, house):
        self.__houses.append(house)

    def display(self):
        super().display()
        print("Owns the following houses:")
        for house in self.__houses:
            house.display()


class Buyer(Contact):
    def __init__(self, lastName, firstName, phoneNumber, email):
        super().__init__(lastName, firstName, phoneNumber, email)
        self.__watchList = []

    @property
    def watchList(self):
        return self.__watchList

    #  Save the house in his watch list 
    def saveForLater(self, house):
        if house not in self.__watchList:
            self.__watchList.append(house)

    # Remove the house from his watch list
    def removeFromSaveForLater(self, house):
        if house in self.__watchList:
            self.__watchList.remove(house)

    def display(self):
        super().display()
        print("Watching the following houses:")
        for i in self.__watchList:
            i.display()     


class Company(Displayable):
    def __init__(self, companyName):
        self.__companyName = companyName
        self.__owners = []
        self.__buyers = []
        self.__agents = []
        self.__houses = []
        

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
        [buyer.removeFromSaveForLater(house) for buyer in self.__buyers if house in buyer.watchList]


    def getBuyersByHouse(self, house):
        #buyers = []
        #for buyer in self.__buyers:
            #if house in buyer.watchlist:
                #buyers.append(buyer)
        #return buyers
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


class Agent(Contact):
    def __init__(self, lastName, firstName, phoneNumber, email, position, company):
        super().__init__(lastName, firstName, phoneNumber, email)
        self.__position = position
        self.__company = company

    def addHouseToListingForOwner(self, owner, house):
        self.__company.addOwner(owner)
        self.__company.addHouseToListing(house)
      

    def helpBuyerToSaveForLater(self, buyer, house):
        self.__company.addBuyer(buyer)
        buyer.saveForLater(house)

    def editHousePrice(self, address, newPrice):
        house = self.__company.getHouseByAddress(address)
        if house:
            house.price = newPrice

    def soldHouse(self, house):
        self.__company.removeHouseFromListing(house)
        self.__company.removeHouseFromSaveForLater(house)


    # print all potential buyers who are interested in buying that house
    def printPotentalBuyers(self, house):
        buyers = self.__company.getBuyersByHouse(house)
        for buyer in buyers:
            buyer.display()

    def display(self):
        super().display()
        print("Position = ",self.__position)


def main():
    owner1 = Owner('Peter', 'Li', '510-111-2222', 'peter@yahoo.com')
    owner2 = Owner('Carl', 'Buck', '408-111-2222', 'carl@yahoo.com')

    house1 = House('1111 Mission Blvd', 1000, 2, 1000000)
    house2 = House('2222 Mission Blvd', 2000, 3, 1500000)
    house3 = House('3333 Mission Blvd', 3000, 4, 2000000)

    owner1.addHouse(house1)
    owner2.addHouse(house2)
    owner2.addHouse(house3)

    buyer1 = Buyer('Tom', 'Buke', '408-555-2222', 'tom@yahoo.com')
    buyer2 = Buyer('Lily', 'Go', '510-222-3333', 'lily@yahoo.com')

    company = Company('Good Future Real Estate')
    agent1 = Agent('Dave', 'Henderson', '408-777-3333',
                   'dave@yahoo.com', 'Senior Agent', company)
    company.addAgent(agent1)

    agent1.addHouseToListingForOwner(owner1, house1)
    agent1.addHouseToListingForOwner(owner2, house2)
    agent1.addHouseToListingForOwner(owner2, house3)

    agent1.helpBuyerToSaveForLater(buyer1, house1)
    agent1.helpBuyerToSaveForLater(buyer1, house2)
    agent1.helpBuyerToSaveForLater(buyer1, house3)

    agent1.helpBuyerToSaveForLater(buyer2, house2)
    agent1.helpBuyerToSaveForLater(buyer2, house3)

    agent1.editHousePrice('2222 Mission Blvd', 1200000)

    company.display()


    print('\nAfter one house was sold ..........................')
    agent1.soldHouse(house3)
    company.display()

    print('\nDisplaying potential buyers for house 1 ..........................')
    agent1.printPotentalBuyers(house1)



if __name__ == "__main__":
    main()
