class Product:
    def __init__(self, productid, product_name, price) -> None:
        self.__productid = productid
        self.__product_name = product_name
        self.__price = price          #protected
        
    def display(self):
        print("productid = ", self.__productid)
        print("product_name = ", self.__product_name)
        print("price = ", self.__price)
        
class Cover:
    def __init__(self, material) -> None:
        self.__material = material
        
    def display(self):
        print("material =", self.__material)
        
        
class Author:
    def __init__(self, name) -> None:
        self.__name = name
        
    def display(self):
        print("name =", self.__name)
        
class Book(Product):
    def __init__(self, productid, product_name, price, title, material, Author) -> None:
        super().__init__(productid, product_name, price)
        self.__title = title
        self.__cover = Cover(material)          #composition
        self.__author = Author
        
    def display(self):
        super().display()
        print("title = ", self.__title)
        self.__cover.display()
        self.__author.display()
        
def main():
    author = Author("Peter")
    book = Book(1000, "Book", 100, "C++", "Hard Cover", author)
    book.display()
    
if __name__ == "__main__":
    main()
    

        