from abc import ABC, abstractmethod

class Book:
    def __init__(self, isbn, title, author, price) -> None:
        self.__isbn = isbn
        self.__title = title
        self.__author = author
        self.__price = price
        
    @property
    def isbn(self)->str:
        return self.__isbn 
    @isbn.setter 
    def isbn(self,isbn)->str:
        return self.__isbn 

    @property
    def title(self)->str:
        return self.__title 
    @title.setter 
    def title(self,title)->str:
        return self.__title 
    
    @property
    def author(self)->str:
        return self.__author 
    @author.setter 
    def author(self,author)->str:
        return self.__author
    
    @property
    def price(self)->float:
        return self.__price 
    @price.setter 
    def author(self,price)->str:
        return self.__price

    def __str__(self):
        return f"Book isbn={self.__isbn}, title={self.__title}, author={self.__author}, price={self.__price:.2f}"

    def __repr__(self) -> str:
        return str(self)

class BookList:
    def __init__(self) -> None:
        self.__books: list[Book] = []
        
    def add_book(self, book):
        self.__books.append(book)
        
    def remove_book(self, book):
        self.__books.append(book)
        
    def booksList(self)->list[Book]:
        return self.__books
    
    def inStore(self)->list[Book]:
        return self.__books

    def __str__(self) -> str:
        output = "The List Of Books\n"
        for book in self.__books:
            output += str(book) + "\n"

        return output

class OrderItem:
    def __init__(self, isbn:str, quantity:int) -> None:
        self.__isbn = isbn
        self.__quantity = quantity
        self.__orderedItems:list[Book] = []
        
    @property
    def isbn(self) -> str:
        return self.__isbn

    @property
    def quantity(self) -> int:
        return self.__quantity

    def __str__(self):
        return "Ordered Item Isbn: " + self.__isbn + "order "


class Order:
    def __init__(self) -> None:
        self.__orderitems: list[OrderItem] = []

    def add_item(self, isbn, quantity):
        self.__orderitems.append(OrderItem(isbn, quantity))
        
    def remove_item(self, isbn, quantity):
        self.__orderitems.append(OrderItem(isbn, quantity))
        
class Order:
    def __init__(self) -> None:
        self.__orderItems: list[OrderItem] = []

    def add_item(self, isbn, quantity):
        self.__orderItems.append(OrderItem(isbn, quantity))
        
    def  SubmitOrderItem(self, SubmitItem:OrderItem)->None:
        self.__orderItems.Submit(SubmitItem)
        
    def getItemCount(self):
	    return len(self.__orderItems)
 
    def __str__(self):
        return "Ordered Item Isbn: " + self.__isbn + "order "
 
    def orderOrderPrice(self,order)->None:
        print(self.__orderItems)
        
    def displayOrder(self):
        for item in self.__orderItems:
            item.display()


class Invoice:
    def __init__(self, order:Order, booklist:BookList) -> None:
        self.__order = order
        self.__booklist = booklist

    def displayInvoice(self):
        if self.__order.getItemCount() == 0:
            print("There is no item in your order cart")
        else:
            self.__order.display()


class Command(ABC):
    @abstractmethod
    def execute(self) -> str:
        pass

class DisplayBookListCommand(Command):
    def __init__(self, booklist: BookList) -> None:
        self.__booklist = booklist

    def execute(self) -> str:
        return str(self.__booklist)


class AddOrderItemCommand(Command):
    def __init__(self, order: Order) -> None:
        self.__order = order

    def execute(self) -> str:
        isbn = input("Enter ISBN: ")
        quantity = int(input("Enter quantity: "))
        self.__order.add_item(isbn, quantity)
        return "Added successfully"

class RemoveOrderItemCommand(Command):
    def __init__(self, order: Order) -> None:
        self.__order = order

    def execute(self) -> str:
        isbn = input("Enter ISBN: ")
        quantity = int(input("Enter quantity: "))
        self.__order.add_item(isbn, quantity)
        return "Removed successfully"
    
class ExecuteOrderItemCommand(Command):
    def __init__(self, order: Order) -> None:
        self.__order = order

    def execute(self) -> str:
        isbn = input("Enter ISBN: ")
        quantity = int(input("Enter quantity: "))
        self.__order.add_item(isbn, quantity)
        return "Executed successfully"

class SubmitOrderCommand(Command):
    def __init__(self, order: Order) -> None:
        self.__order = order

    def execute(self) -> str:
        isbn = input("Enter ISBN: ")
        quantity = int(input("Enter quantity: "))
        self.__order.add_item(isbn, quantity)
        return "Submitted successfully"



class DisplayInvoiceCommand(Command):
    def __init__(self, invoice:Invoice) -> None:
        self.__invoice = invoice

    def execute(self) -> None:
        self.__invoice.displayInvoice()

class Invoker:
    def __init__(self):
        self.__command: list[Command] = []
        
    @property
    def commands(self)->list[Command]:
        return self.commands 
    
    #def add_booklist_display_command(self, command):
        #self.__display_booklist_command = command
       
    #def add_order_item_command(self, command):
        #self.__add_order_item_command = command 

    def add_command(self, command):
        self.__command.append(command)
        
    def remove_command(self, command):
        self.__command.append(command)

    def execute_command(self, command_no):
        return self.__command[command_no].execute()    
    
    def displayBookCommand(self, b):
        return DisplayBookListCommand(b).execute()

    def addBookToOrder(self, o):
        return AddOrderItemCommand(o).execute()

    def displayInvoice(self, i):
        return DisplayInvoiceCommand(i).execute()

    def removeAll(self):
         self.__command.remove()      

class ApplicationUserInterface:
    def __init__(self) -> None:
        self.__invoker = Invoker()

    def displayBook(self, b):
        return self.__invoker.displayBookCommand(b)

    def addItemToOrder(self, o):
        return self.__invoker.addBookToOrder(o)

    def getInvoice(self, i):
        return self.__invoker.displayInvoice(i)
    
class BookstoreApp:
    def showTitle(self):
	    print("\nThe SFBU library bookstore")
    
def show_menu():
        print("The SFBU library bookstore")
        print("======= Menu =========")
        print("1. Display Book List")
        print("2. Add Order Item")
        print("3. Remove Order Item")
        print("4. Submit Order")
        #print("4. Display the Order ")
        print("5. Display Invoice")
        #print("6. Execute all commands")
        print("6. Exit")

def process_command(choice, invoker):
    print(invoker.execute_command(choice - 1))
    #print(invoker.execute_command(choice - 2))

def main():
    b = BookList()
    #booklist.showTitle()
    #booklist.show_menu()
    b.add_book(Book("111", "Python", "John", 208.10)) 
    b.add_book(Book("112", "C++", "Peter", 108.99)) 
    b.add_book(Book("113", "Python", "Hobber", 318.99)) 
    b.add_book(Book("114", "JAVA", "Malcom", 180.99)) 
    
    #a = ApplicationUserInterface()
    #o = Order()
    #i = Invoice(o, b)

    order = Order()
    invoker = Invoker()
    invoker.add_command(DisplayBookListCommand(b))
    invoker.add_command(AddOrderItemCommand(order))
    invoker.remove_command(RemoveOrderItemCommand(order))
    #invoker.execute_command(ExecuteOrderItemCommand(order))

    while True:
        show_menu()
        choice = int(input("Please enter your choice: "))
        process_command(choice, invoker)
        


if __name__ == "__main__":
    main()