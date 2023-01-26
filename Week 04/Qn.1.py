from unicodedata import name

class Customer:
    def __init__(self,name : str, address : str) -> None:
      self.__name = name
      self.__address = address
     
    @property
    def name(self) -> str:
         return self.__name
     
    @name.setter
    def name(self, name : str) -> None:
         self.__name__ = name
         
    @property
    def address(self) -> str:
         return self.__address
     
    @address.setter
    def address(self, address : str) -> None:
         self.__address__ = address
     
    def __str__(self) -> str:
        return "Customer name = " + self.__name + ", address = " + self.__address
    
class Product:
    def __init__(self,productid : int, product_name : str, price : float) -> None:
     self.__productid = productid
     self.__product_name = product_name
     self.__price = price
     
    @property
    def productid(self) -> int:
         return self.__productid
     
    @property
    def product_name(self) -> str:
         return self.__product_name
     
    @property
    def price(self) -> float:
         return self.__price
     
     
    def __str__(self) -> str:
        return "Product productid = " + str(self.__productid)\
            +", product_name = " + self.__product_name \
            +", price = " + str(self.__price)
            
                
    
     

class Orderitem:
    def __init__(self,product : Product, quantity : int) -> None:
     self.__product = product
     self.__quantity = quantity
     
    @property
    def product(self) -> Product:
         return self.__product
     
    @property
    def quantity(self) -> int:
         return self.__quantity
     
    @quantity.setter
    def quantity(self, quantity : int) -> None:
         self.__quantity = quantity
     
    def __str__(self) -> str:
        return "Orderitem product = " + str(self.__product) + ", quantity = " + str(self.__quantity) 

class Order:
    def __init__(self,orderid : int, customer : Customer) -> None:
     self.__orderid = orderid
     self.__customer = customer
     self.__order_items : list[Orderitem] = []
     
     
     
    def add_item(self, product : Product, quantity : int) -> None:
         found : bool = False
         for item in self.__order_items:
               if item.product.productid == product.productid:
                   item.quantity = quantity
                   found = True
                   break
              
         if found is False:
                self.__order_items.append(Orderitem(product, quantity))
                
    def remove_item(self, productid : int) -> None:
         index = next((index for (index, d) in enumerate( 
            self.__order_items) if d.product.productid == productid), -1)
         if index != -1:
             self.__order_items.pop(index)
              
    def find_largest_item(self) -> Orderitem:
        maxQuantity = 0
        largestItem: Orderitem = self.__order_items[0]
        for item in self.__order_items:
            if item.quantity > maxQuantity:
                maxQuantity = item.quantity
                largestItem = item
        return largestItem
    
    def get_discount_value(self, discount_rate: float) -> float:
        return self.__total - (self.__total * discount_rate)
    
    def get_total(self) -> float:
        self.__total = 0.0
        for item in self.__order_items:
            self.__total += (item.quantity * item.product.price)
        return self.__total
               
        
    def __str__(self) -> str:
        itemlist : str = ""
        for item in self.__order_items:
            itemlist += str(item) + "\n"
            
        return "Order orderid = " + str(self.__orderid) + ", customer = " + str(self.__customer) + "\n" + itemlist
    


def main() -> None:
    c : Customer = Customer("Saboor", "Sunnyvale")
    p1 : Product = Product(111, "Book", 199.99)
    p2 : Product = Product(121, "Computer", 1099.99)
    p3 : Product = Product(131, "Bag", 19.99)
    
    order : Order = Order(2228,c)
    order.add_item(p1,20)
    order.add_item(p2,21)
    order.add_item(p3,22)
    order.add_item(p1,24)
    order.remove_item(131)
    print(order)
    
    largest_item = order.find_largest_item()
    print("largest item\n", largest_item)
    print("\n Total = ", order.get_total())
    print("\n Total after discount =", order.get_discount_value(0.2))
    
    
if __name__ == "__main__":
    main()