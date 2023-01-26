from abc import ABC, abstractmethod

class Book:
    def __init__(self, isbn:str, title:str, author:str, price:float) -> None:
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
        
    def booksList(self)->list[Book]:
        return self.__books
        
    def inStore(self)->list[Book]:
        return self.__books
    
    def getBooksByISBN(self, isbn:str) -> Book:
        result = None
        for book in self.__books:
            if book.isbn == isbn:
                result = book
        return result

    def __str__(self) -> str:
        output = "The List Of Books\n"
        for book in self.__books:
            output += str(book) + "\n"

        return output
    
    def displayBooks(self):
        [book.display() for book in self.__books]

class OrderItem:
    def __init__(self,isbn:str, quantity:int) -> None:
        self.__isbn = isbn
        self.__quantity = quantity
        self.__orderedItems:list [Book] = []

    @property
    def isbn(self)->str:
        return self.__isbn 
    
    @isbn.setter
    def isbn(self,isbn:str)->None:
        self.__isbn = isbn 
    
    @property
    def quantity(self)->str:
        return self.__quantity 
    
    @quantity.setter
    def quantity(self,quantity:str)->None:
        self.__quantity = quantity

    def __str__(self):
        return "Ordered Item Isbn: " + self.__isbn + "order "

class Order:
    def __init__(self) -> None:
        self.__orderitems: list[OrderItem] = []

    def add_item(self, isbn, quantity):
        self.__orderitems.append(OrderItem(isbn, quantity))
        
    #def  remove_item(self, removeItem:OrderItem)->None:
        #self.__orderitems.append(OrderItem(removeItem))
        
    def  SubmitOrderItem(self, SubmitItem:OrderItem)->None:
        self.__orderItems.Submit(SubmitItem)
        
    def getItemCount(self):
	    return len(self.__orderItems)
 
    #def displayBooks(self):
        #[book.display() for book in self.__books]

        

def display(self):
    for item in self.__orderItems:
        item.display()


class Invoice:
    def __init__(self, order: Order, booklist: BookList) -> None:
        self.__order = order 
        self.__bookList = booklist
        
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

class SubmitOrderCommand(Command):
    def __init__(self, order: Order, orderItem:OrderItem) -> None:
        self.__order = order 
        self.__orderItem = orderItem
    
    def execute(self)->None:
        self.__order.SubmitOrderItem(self.__orderItem)



class DisplayInvoiceCommand(Command):
    def __init__(self, invoice:Invoice) -> None:
        self.__invoice = invoice

    def execute(self) -> None:
        self.__invoice.displayInvoice()

class Invoker:
    def __init__(self):
        self.__command: list[Command] = []

    def add_command(self, command):
        self.__command.append(command)

    def execute_command(self, command_no):
        return self.__command[command_no].execute()        

def show_menu():
    print("======= Menu =========")
    print("Welcome to SFBU Bookstore ")
    print("1. Display Book List")
    print("2. Add Order Item")
    print("3. Remove a book from the order")
    print("4. Display the Order ")
    print("5. Display the invoice")
    print("6. Execute all commands")
    print("7. Exit")

def process_command(choice, invoker):
    print(invoker.execute_command(choice - 1))

def main():
    b1 = Book("111", "C Programming", "Peter", 122.89)
    b2 = Book("222", "C++ Programming", "Peter", 132.89)
    booklist = BookList()
    booklist.add_book(b1)
    booklist.add_book(b2)

    order = Order()
    invoker = Invoker()
    invoker.add_command(DisplayBookListCommand(booklist))
    invoker.add_command(AddOrderItemCommand(order))

    while True:
        show_menu()
        choice = int(input("Please enter your choice: "))
        process_command(choice, invoker)


if __name__ == "__main__":
    main()