from abc import ABC, abstractmethod, abstractproperty
from re import S
from typing import List
from unicodedata import name

class Displayable(ABC):
    @abstractmethod
    def display(self):
        return None


class Employee(Displayable):
    def __init__(self,name : str, empId:int, salary:float, title : str) -> None:
        self.__name = name
        self.__empId = empId
        self.__salary = salary
        self.__title = title
        
    @property
    def name(self) -> str:
        return self.__name
    
    @name.setter
    def name(self, n):
        self.__name = n

    @property
    def salary(self) -> str:
        return self.__salary
    
    @salary.setter
    def salary(self, s):
        self.__salary = s
        
    @property                             #title : Officer, Supervisor, Manager
    def title(self) -> str:
        return self.__title
    
    @title.setter
    def title(self, t):
        self.__title = t
     

    def display(self) -> None:
        print("Employee name =", self.__name)
        print("Employee ID =", self.__empId)
        print("Salary =", self.__salary)
        print("Employee title =", self.__title)
        

class AbstractCompany:
    def __init__(self) -> None:
        self.__MAX_EMPLOYEE_SIZE = 10
        self.__names: List [name] = []

    @property
    def maxEmployeeSize(self):
        return self.__MAX_EMPLOYEE_SIZE
    
    #def get_employee_name_list() : list[str] = 0:
        #return super().get_employee_name_list()
        


class Company(Displayable, AbstractCompany):
    def __init__(self, compName:str,) -> None:
        self.__compName = compName
        self.__employees: List [Employee] = []
        self.__numEmployees = 0
    
    
    @property
    def product_type(self) -> str:
        return self.product_type

    def addEmployee(self, employee: Employee) -> None:
        if len(self.__employees) == AbstractCompany.maxEmployeeSize:
            print("Employee list is full")
        else:
            self.__employees.append(employee)
            self.__numEmployees += 1

    def display(self) -> None:
        super().display()
        print("Company Name = ", self.__compName)
        print("Number of Employees = ", self.__numEmployees)
        for employee in self.__employees:
            employee.display()
            print()

    def __iter__(self):
        self.__index = -1
        return self

    def __next__(self):
        if self.__index == len(self.__employees)-1:
            raise StopIteration
        self.__index += 1
        parts = self.__employees[self.__index]
        return parts

    #def remove_employee(self, empId: int) -> None:
        #new_employee = list()
        #for employee in self:
            #if employee.__empId == empId:
                #continue
            #else:
                #new_employee.append(employee)
        #self.__employees = new_employee
        
    def get_employees_high_salary(self, limit:float):
        high_salaryEmp = []
        for Employee in self:
            if Employee.salary > limit:
                high_salaryEmp.append(Employee)
        return high_salaryEmp
    
    def update_employee_salary(empid : int, salary : float) -> None :
        pass
    

class TradingCompany(Company):
    def __init__(self, product_type: str, num_of_offices :int) -> None:
        Company.__init__(self, product_type)
        self.num_of_offices = num_of_offices

    def get_employees_high_salary(self, limit:float):
        high_salaryEmp = []
        for Employee in self:
            if Employee.salary > limit:
                high_salaryEmp.append(Employee)
        return high_salaryEmp

    def display(self) -> None:
        Company.display(self)
        print("product_type = ", self.product_type)
        
        
class Stockbusiness(TradingCompany, Displayable):
    def __init__(self, research_tool : str, commission_rate : float, stock_name : str) -> None:
        self.research_tool = research_tool
        self.commission_rate = commission_rate
        self.stock_name = stock_name
        
    def display(self) -> None:
        super().display()
        print("Trading apple stocks = ", self.stock_name)
    


def main():
    p1 = Employee('John',11, 10000, 'Manager')
    p2 = Employee('Joseph',12, 20000, 'Engineer')
    p3 = Employee('Kytz',13, 30000, 'Assistant')
    p4 = Employee('Rony',20, 26000, 'Supervisor')
    p5 = Employee('Rahul',18, 28000,'Officer')
    c = Company("Adobe\n")
    c.addEmployee(p1)
    c.addEmployee(p2)
    c.addEmployee(p3)
    c.addEmployee(p4)
    c.addEmployee(p5)
    c.display()
    print()
    #c.remove_employee(p3)
    #print()

    print("\nGet the high salary employee :\n")
    high_salary = c.get_employees_high_salary(21000)
    for employee in high_salary:
        employee.display()
        print()
        
if __name__ == "__main__":
    main()