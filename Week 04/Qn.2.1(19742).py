class Myinteger: 
    def __init__(self,Value : int ) -> None:
        self.Value=Value
    
    def getValue(self):
      return self.Value
  
    def setValue(self,value):
        self.Value=value
        
    def iseven(self)->bool:
        if self.Value % 2==0:
            print(True)
        else:
            print(False)
    def isodd(self)->bool:
        if self.Value % 2==0:
            print(False)
        else:
            print(True)
    def isprime(self)->bool:
        flag=False
        for i in range(2, self.Value):
            if (self.Value % i) == 0:
            # if factor is found, set flag to True
                flag = True
            # break out of loop
                break
        if flag==True:
            print(False)
        else:
            print(True)
    def __eq__(self, other) -> bool:
        if self.Value==other:
            print(True)
        else:
            print(False)
    def __str__(self) -> str:
        return "the last value entered is ="+str(self.Value)
    def add(self,other)->int:
        return "value after addition is  ="+ str(self.Value+other)
    def sub(self,other)->int:
        return "value after subtraction is =" +str(self.Value-other)
    def __gt__(self,other):
        if self.Value>other:
            print(True)
        else:
            print(False)

            
        
        
        


def main():
    
    n=Myinteger(10)
    n.setValue(4)
    print(n.getValue())
    n.isodd()
    n.iseven()
    n.isprime()
    n.__eq__(8)
    print(n.__str__())
    print(n.add(3))
    print(n.sub(2))
    n.__gt__(4)
    
    n=Myinteger(4)
    n.setValue(9)
    print(n.getValue())
    n.isodd()
    n.iseven()
    n.isprime()
    n.__eq__(10)
    print(n.__str__())
    print(n.add(7))
    print(n.sub(8))
    n.__gt__(9)
if __name__ =="__main__":
    main()