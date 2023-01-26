from abc import ABC, abstractmethod, abstractproperty
from typing import List

class Displayable(ABC):
    @abstractmethod
    def display(self):
        return None

class Employee(Displayable):
    def __init__(self, empId:int, salary:float) -> None:
        self.__empId = empId
        self.__salary = salary

    @property
    def salary(self) -> str:
        return self.__salary

    def display(self) -> None:
        print("Employee ID =", self.__empId)
        print("Salary =", self.__salary)

class CompanyContants:
    def __init__(self) -> None:
        self.__MAX_EMPLOYEE_SIZE = 10

    @property
    def maxEmployeeSize(self):
        return self.__MAX_EMPLOYEE_SIZE


class Comapny(Displayable, CompanyContants):
    def __init__(self, compName:str) -> None:
        CompanyContants.__init__(self)
        self.__compName = compName
        self.__employees: List [Employee] = []
        self.__numEmployees = 0
        
    def addEmployee(self, employee: Employee):
        if len(self.__employees) >= self.maxEmployeeSize:
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

    # define the Employee object as the iterator
    def __iter__(self):
        self.__index = -1  # initialize index for each iteration
        return self

    # define the method that gets the next object
    def __next__(self):
        if self.__index == len(self.__employees)-1:
            raise StopIteration
        self.__index += 1
        employees = self.__employees[self.__index]
        return employees


class InternetCompany(Comapny):
    def __init__(self, compName: str, url:str) -> None:
        Comapny.__init__(self, compName)
        self.__url = url

    def getEmployeesHighSalary(self, limit:float):
        high_salaryEmp = []
        for employee in self:
            if employee.salary > limit:
                high_salaryEmp.append(employee)
        return high_salaryEmp

    def display(self) -> None:
        Comapny.display(self)
        print("URL = ", self.__url)


def main():
    p1 = Employee(1, 10000)
    p2 = Employee(2, 20000)
    p3 = Employee(3, 30000)
    p4 = Employee(4, 26000)
    p5 = Employee(5, 28000)
    p6 = Employee(6, 31000)
    p7 = Employee(7, 32000)
    p8 = Employee(8, 27000)
    p9 = Employee(9, 33000)
    p10 = Employee(10, 33500)
    p11 = Employee(11, 31300)
    c = InternetCompany("Cisco", "www.cisco.com")
    c.addEmployee(p1)
    c.addEmployee(p2)
    c.addEmployee(p3)
    c.addEmployee(p4)
    c.addEmployee(p5)
    c.addEmployee(p6)
    c.addEmployee(p7)
    c.addEmployee(p8)
    c.addEmployee(p9)
    c.addEmployee(p10)
    c.addEmployee(p11)
    c.display()
    print()

    print("\nGet the high salary employee ")
    high_salary = c.getEmployeesHighSalary(21000)
    for employee in high_salary:
        employee.display()
        print()
        
main()