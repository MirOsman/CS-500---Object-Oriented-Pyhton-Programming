from Customer import Customer
from bank import Bank


class BankApp:
    def __init__(self) -> None:
        self.__bank = Bank("SFBU Bank")

    @property
    def bank(self) -> Bank:
        return self.__bank

    def showTitle(self) ->str:
        print("The Bank Customer Management Application")

    def showMenu(self) -> None:
        print("\ Command Menu")
        print("1. Print customers forward")
        print("2. Print customers backward")
        print("3. Add a new customer")
        print("4. Edit a customer information")
        print("5. Remove a customer")
        print("6. Print customers by last name")
        print("7. Print the customer with the largest balance")
        print("8. Print the customer with the smallest balance")
        print("9. Exit program")


    def printCustomers(self, reverse: bool):
        def getAccountNo(customer: Customer):
            return customer.accountNo

        customers = sorted(self.__bank.customers, key= getAccountNo, reverse = reverse)
        for cust in customers:
            print(cust)


def main() -> None:

    app = BankApp()
    app.showTitle()

    while True:
        app.showMenu()
        choice = int(input("Enter a choice :"))
        if choice == 1:
            app.printCustomers(False)
        elif choice == 2:
            app.printCustomers(True)
        elif choice == 3:
            while True:
                accountNo = int(input("Account No: "))
                firstName = input("First Name: ")
                lastName = input("Last Name:")
                accountBalance = float(input("Account Balance: "))
                newCustomer =Customer(accountNo,firstName,lastName,accountBalance)
                choice = input("Do you have another new customer? (y/n) ")
                if choice == 'y':
                    app.bank.addCustomer(newCustomer)
                    continue
                if choice == 'n':   
                    break
                else:
                    print("Wrong input!")  
            

            app.bank.addCustomer(newCustomer)

        elif choice == 4:
            accountNo = int(input("Enter Account No of the customer to edit the information: "))

            updatedAccountNo = (input("Enter updated account_no of the customer : "))
            updatedFirstName = (input("Enter updated first name of the customer : "))
            updatedLastName = (input("Enter updated last name of the customer : "))
            updatedAccountBalance = float(input("Enter updated account balance of the customer : "))
            updatedCustomer = Customer(updatedAccountNo, updatedFirstName, updatedLastName, updatedAccountBalance)

            app.bank.editCustomer(accountNo, updatedCustomer)

        elif choice == 5:
            accountNo = int(input("Enter Account No: "))
            app.bank.removeCustomer(accountNo)

        elif choice == 6:
            lastName = input("Enter last name of the customer in lower case letters :")
            app.bank.getCustomerByLastname(lastName)

        elif choice == 7:
            app.bank.getLargestBalance()

        elif choice == 8:
            app.bank.getSmallestBalance()
               
        elif choice == 9:
            print("Bye!")
            exit()


if __name__ == "__main__":
    main()