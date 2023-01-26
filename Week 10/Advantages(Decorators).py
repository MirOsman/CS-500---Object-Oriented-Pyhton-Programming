class ExampleClass:
    def __init__(self, name) -> None:
        self.name = name
    
    def act(self):
        print(self.name, "is acting...")

    def fly(self):
        print(self.name, "is flying")

class Decorator:
    def __init__(self, Obj:ExampleClass) -> None:
        self.Obj = Obj

    def act(self):
        print("Decorator is acting", end= " - ")
        self.Obj.act()

    def fly(self):
        print("Decorator is flying", end = ' - ')
        self.Obj.fly()

def main():
    s = ExampleClass("Peter")
    s.act()
    s.fly()
    print("================================")

    d = Decorator(s)
    d.act()
    print("================================")
    d.fly()


if __name__ == "__main__":
    main() 
    
