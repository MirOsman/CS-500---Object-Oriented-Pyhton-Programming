class Person:
    # constructor
    def __init__(self, name):
        self.__name = name      #private attribute => _Person__name
        self.age = 20           # public attribute => age
        
    def __str__(self): 
         return"Person name = " +self.__name
    
    def display(self):          # public method
        print(self)
          
        
        
        
def main():
        a = Person("Peter")
        #print(a.__name)
        a.__name = "Jim"
        a.age = 27             # OK
        print(vars(a))         # {'_Person__name': 'Peter', '__name': 'Jim'}
                               # {'_Person__name': 'Peter', 'age': 27, '__name': 'Jim'}
        print(a.__name)        # Jim
            
           
        a.display()            # Person name = Peter
        Person.display(a)
        
        b = Person    
if __name__=="__main__":
     main()
     