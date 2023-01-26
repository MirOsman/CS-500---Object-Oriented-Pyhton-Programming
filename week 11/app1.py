from computers import ComputerFactory, ComputerType, Computer

def show_type():
    print("Computer Types")
    for tp in ComputerType:
        print(f"{tp.value}.{tp.name}")
    print()

def main():
    show_type()
    computer_type = int(input("Please select a computer type number: "))
    cpu = input("Please enter a CPU: ")
    
    c = ComputerFactory.create_computer(ComputerType(Computer,type), cpu)
    c.compute()
    
    
    
    
if __name__ == "__main__":
    main()