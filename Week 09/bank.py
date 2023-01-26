from Customer import Customer
from db import CustomerRepository
import csv

class Bank:
    def __init__(self, bankName: str) -> None:
        self.__bankName = bankName
        self.__db = CustomerRepository()
        self.__customers:list[Customer] = self.__db.getCustomers()

    
    @property
    def bankName(self) -> str:
        return self.__bankName


    @property
    def customers(self) -> list[Customer]:
        return self.__customers

    def addCustomer(self, customer: Customer) -> None:    
        self.__customers.append(customer)
        for cust in self.__customers:
            print("New Customer: \n")
            print(cust)
        self.saveCustomer()

    def editCustomer(self, accountNo: int, updated: Customer) -> None:
        for cust in self.__customers:
            if accountNo == cust.accountNo:
                print("Here is the customer record you want to edit ")
                print(cust)
                cust.accountNo = updated.accountNo
                cust.firstName = updated.firstName
                cust.lastName = updated.lastName
                cust.accountBalance = updated.accountBalance
                self.saveCustomer()
            if accountNo != cust.accountNo:
                print("Wrong or invalid account no!")
    
    def removeCustomer(self, accountNo: int) ->None:
        for cust in self.__customers:
            if accountNo == cust.accountNo:
                self.__customers.remove(cust)
                self.saveCustomer()
                print("Account No : ", cust.accountNo , " record was deleted.\n")
                

    def getCustomerByLastname(self, lastName:str) ->list[Customer]:
        for cust in self.__customers:
            if cust.lastName == lastName:
                print("Last Name :" , lastName, "\n", cust)

    def getLargestBalance(self) ->None:
        maxBalance = 0.0
        index = 0
        for i in range (len(self.__customers)): 
            if self.__customers[i].accountBalance > maxBalance :
                maxBalance = self.__customers[i].accountBalance
                index = i 
        print("Account with the largest account balance is: ", self.__customers[index])
                
            
    def getSmallestBalance(self) ->None:
        minBalance= 2000000000
        index = 0
        for i in range (len(self.__customers)): 
            if self.__customers[i].accountBalance < minBalance :
                minBalance = self.__customers[i].accountBalance
                index = i 
        print("Account with the smallest account balance is: ", self.__customers[index])


    def saveCustomer(self) ->None:
        self.__db.saveCustomers(self.__customers)
