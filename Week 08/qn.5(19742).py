from abc import ABC, abstractmethod, abstractproperty
from tokenize import Double
from typing import Dict, List, Type
import enum

class Displayable(ABC):
    @abstractmethod
    def display(self):
        return None


class BuildingType(enum.Enum):
    HEAVY_INDUSTRIAL = 0
    WAREHOUSE = 1
    COLD_STORAGE = 2
    LIGHT_INDUSTIAL = 3
    DATA_HOUSING = 4
    
class Company(Displayable):
    def __init__(self, company_Name:str) -> None:
        self.company_Name = company_Name
        self.Employees: List[Employee] = [] 
    
    @property
    def company_Name(self) -> str:
        return self.company_Name

    #def add_employee(self, Employee : Employees) -> None:
        #self.Employees.append(Employee)
        
        
    # def get_top_five_employees(self) -> list[Employee]:
         #def get.salary(employee):
         # return employee.salary
         
         
        #top_employees = sorted(self.__employees,key = get_salary, reverse=True)
        #return top_employees[:5]

    def get_Top_Five_Employees(self):
        Employee:List[Employee] = []
        for Employees in self.__employee_name:
            if isinstance(Employee, Employees):
                Employees.append(Employee)
        return Employees

    #def get_employee(self, index:int) -> Employees:
        '''for Employee in self.__Employee:
            try:
                if employee[index] == self.__Employee[index]:
                    return Employee
                elif index >= len(self.__Employee):
                    raise IndexError
            except IndexError as e:
                print('message = ', e)
                exit()
        return self.__Employee[index]'''

        if index < 0 or index > len(self.Employees):
            raise IndexError("Index out of range")
        else:
            return self.Employees[index]          

    def display(self):
        print("Company Name:", self.company_Name)
        print("The", self.company_Name, "has these employees: \n")
        for Employee in self.Employees:
            Employee.display()
            print()

    def __iter__(self):
        self.__index = -1
        return self

    def __next__(self):
        if self.__index == len(self.Employees)-1:
            raise StopIteration
        self.__index += 1
        products = self.Employees[self.__index]
        return Employee

    def next(self):
        return self.__next__()
    

class Employee(Displayable) :
    def __init__(self, employee_name : str, salary : float)-> None :
        self.__employee_name = employee_name
        self.__salary = salary
        
    @property
    def employee_name(self) -> str:
        return self.__employee_name
    
    @property
    def salary(self) -> float:
        return self.__salary
        
    def __str__(self) -> str:
        return "Employee name : {0}, salary: {1}".format(self.__employee_name, self.__salary)
    
    def display(self) -> None:
        print(self)
        
    def __repr__(self) -> str:
        return str(self)
    
    def __eq__(self, __o: object) -> bool:
        if isinstance(__o, Employee):
            return self.__employee_name == __o.__employee_name
        return False
        
class Building(Displayable):
    def __init__(self, buildingName: str, area: float, stories: int, type: BuildingType) -> None:
        self.__buildingName = buildingName
        self.__area = area
        self.__stories = stories
        self.__type = type
        self.__Employees : list[Employee] = [] 

    @property
    def buildingName(self) -> str:
        return self.__buildingName

    @property
    def area(self) -> float:
        return self.__area

    @property
    def stories(self) -> int:
        return self.__stories

    @property
    def type(self) -> BuildingType:
        return self.__type
    
    def add_employee(self, Employee : Employee) -> None:
        self.__Employees.append(Employee)


    def display(self):
        print("Building Name: {}".format(self.__buildingName))
        print("Area: {:.2f}".format(self.__area))
        print("Stories: {}".format(self.__stories))
        print("Type: {}".format(self.__type.value))
        print("Employees: {}".format(self.__Employees))
        
    def __str__(self) -> str:
        return "Building name : {0}, Area: {1}, Stories : {2}, Type : {3}, Employees : list[Employees] : {4}".format(self.__buildingName, self.__area, self.__stories, self.__type, self.__Employees)
        

class Product(Displayable):
    def __init__(self, productName: str, basePrice: float) -> None:
        self.__productName = productName
        self.__basePrice = basePrice

    @property
    def productName(self) -> str:
        return self.__productName

    @property
    def basePrice(self) -> float:
        return self.__basePrice

    @abstractmethod
    def getFinalPrice(self) -> float:
        return None

    def display(self):
        print("Product Name: {}".format(self.__productName))
        print("Base Price: {:.2f}".format(self.__basePrice))

class ConstructionCompany(Company):
    def __init__(self, company_Name: str, category:str) -> None:
        Company.__init__(self, company_Name)
        self.__category = category
        self.__buildings: List[Building] = []

    @property
    def category(self) -> str:
        return self.__category

    def find_largest_building(self) -> Building:
        largeBuilding = None
        for building in self.__buildings:
            if largeBuilding is None:
                largeBuilding = building
            elif building.area > largeBuilding.area:
                largeBuilding = building
        return largeBuilding
    
    def assign_employees_to_building(self, employee: Employee, b: Building):
        b.add_employee(employee)

    #def assign_employees_to_building(self, Employee: str, type : BuildingType) -> List[Employee]:
       # Employee:List[Employee] = []
       # for Employee in self:
            #if Employee.getbuilding() > BuildingType:
                #Employee.append(Employee)
       # return Employee

    def get_buildings_by_type(self) -> Dict[BuildingType, List[Building]]:
        buildingDict:Dict[BuildingType, List[Building]] = {}
        for building in self.__buildings:
            if building.type not in buildingDict:
                buildingDict[building.type] = []
            buildingDict[building.type].append(building)
        return buildingDict

    def building(self, build) -> List:
        buildings = []
        for building in self.__buildings:
            if building.type == build:
                buildings.append(building)
        return buildings

    def display(self):
        Company.display(self)
        print("Company Category:", self.__category)
        print("\nBuilding List:")
        for building in self.__buildings:
            building.display()
            print()

    def __str__(self) -> str:
        return "Company Category : {0}, Building list: {1}".format(self.__category, self.__buildings)


def main():
    building1 = Building("IT Center", 200, 4, BuildingType.DATA_HOUSING)
    building1.display()
    print()
    c = Company[e, e2,e3, e4, e5, e6]
    e = Employee("John", 33)
    e2 = Employee("Kytz", 37)
    e3 = Employee("jony", 39)
    e4 = Employee("Nnay", 43)
    e5 = Employee("joh", 45)
    e6 = Employee("hary", 29)

    print("Top five fastest employees in the list")
    Employee:List[Employee] = c.get_Top_Five_Employees()
    for computer in Employee:
        print("Name:", Employee.Name, "Salary:", Employee.salary)
    print()

    print("List of building by type")
    for factoryType, buildings in c.get_buildings_By_type().items():
        print(factoryType)
        for building in buildings:
            print("Building Name:", building.buildingName)
        print()

    print("\nThe index of the company in the list")
    try:
        c = e.getProduct(18)
        c.display()
    except IndexError as e:
        print(e)

    

if __name__ == "__main__":
    main()    
