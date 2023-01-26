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

    @salary.setter
    def getSalary(self, salary:float) -> None:
        self.__salary = salary

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
    def __init__(self, compName:str,) -> None:
        self.__compName = compName
        self.__employees: List [Employee] = []
        self.__numEmployees = 0

    

    def addEmployee(self, employee: Employee):
        if len(self.__employees) == 10:
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


class InternetCompany(Comapny):
    def __init__(self, compName: str, url:str) -> None:
        Comapny.__init__(self, compName)
        self.__url = url

    def getEmployeesHighSalary(self, limit:float):
        high_salaryEmp = []
        for employee in self:
            if employee.getSalary > limit:
                high_salaryEmp.append(employee)
        return high_salaryEmp

    def display(self) -> None:
        Comapny.display(self)
        print("URL = ", self.__url)


def main():
    p1 = Employee(11, 10000)
    p2 = Employee(12, 20000)
    p3 = Employee(13, 30000)
    p4 = Employee(20, 26000)
    p5 = Employee(18, 28000)
    c = InternetCompany("Cisco", "www.cisco.com")
    c.addEmployee(p1)
    c.addEmployee(p2)
    c.addEmployee(p3)
    c.addEmployee(p4)
    c.addEmployee(p5)
    c.display()
    print()

    print("\n Get the high salary employee ")
    high_salary = c.getEmployeesHighSalary(21000)
    for employee in high_salary:
        employee.display()
        print()
        
main()