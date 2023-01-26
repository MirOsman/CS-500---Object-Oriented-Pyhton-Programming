from abc import ABC, abstractmethod
from typing import List, Dict
from enum import Enum


class Displayable(ABC):

    @abstractmethod
    def display(self):
        raise NotImplementedError


class Employee(Displayable):
    def __init__(self, employee_name, salary):
        self.__employee_name = employee_name
        self.__salary = salary

    def get_salary(self):
        return self.__salary

    def display(self):
        print(f"Employee {self.__employee_name} has ${self.__salary} salary.")

    def __str__(self):
        return f"Employee: {self.__employee_name}"

    def __repr__(self):
        return f"Employee: {self.__employee_name}"


class BuildingType(Enum):
    HEAVY_INDUSTRIAL = 0
    WAREHOUSE = 1
    COLD_STORAGE = 2
    LIGHT_INDUSTRIAL = 3
    DATA_HOUSING = 4


class Building(Displayable):

    def __init__(
            self,
            buildingName: str,
            area: float,
            stories: int,
            type: str,
            employees: List[Employee] = None
    ):
        if not employees:
            employees = []
        self.__buildingName = buildingName
        self.__area = area
        self.__stories = stories
        self.__type = type
        self.__employees = employees

    def add_employee(self, emp: Employee):
        self.__employees.append(emp)

    def get_type(self):
        return self.__type

    def get_area(self):
        return self.__area

    def display(self):
        return f"Building {self.__buildingName}"

    def __str__(self):
        return f"Building {self.__buildingName}"

    def __repr__(self):
        return f"Building {self.__buildingName}"


class Company(Displayable, ABC):

    def __init__(
            self,
            company_name,
            employees: List[Employee] = None
    ):
        self.__company_name = company_name
        if not employees:
            employees = []
        self.__employees = employees

    def add_employee(self, employee: Employee):
        self.__employees.append(employee)

    def get_top_five(self) -> List[Employee]:
        return sorted(self.__employees, key=lambda x: x.get_salary(), reverse=True)[:5]

    def get_employee(self, index) -> Employee:
        ...

    def __str__(self):
        return f"{self.__company_name}"

    def __iter__(self):
        self.__index = 0
        return self

    def __next__(self):
        try:
            employee = self.__employees[self.__index]
            self.__index += 1
            return employee
        except Exception:
            raise Exception("No more empployees")


class ConstructionCompany(Company):

    def __init__(
            self,
            company_name: str,
            category: str,
            employees: List[Employee] = None,
            buildings: List[Building] = None
    ):
        super().__init__(company_name, employees)
        self.__category = category

        if not buildings:
            buildings = []
        self.__buildings = buildings

    def find_largest_building(self):
        if not self.__buildings:
            raise Exception("No building associated with this company")

        largest_building = self.__buildings[0]
        for building in self.__buildings:
            if largest_building.get_area() < building.get_area():
                largest_building = building

        return largest_building

    def assign_employees_to_building(self, employee: Employee, type: str) -> Employee:
        for building in self.__buildings:
            if building.get_type() == type:
                building.add_employee(employee)
                return employee

        raise Exception("No such type of building exists for this company")

    def get_buildings_by_type(self) -> Dict:
        building_type_dict = dict()
        for building in self.__buildings:
            building_type = building.get_type()
            if building_type not in building_type_dict:
                building_type_dict[building_type] = [building]
            else:
                building_type_dict[building_type].append(building)

        return building_type_dict

    def display(self):
        return f"Construction Company: {self.__company_name}"

    def __str__(self):
        return f"Construction Company: {self.__company_name}"


def main():
    emp1 = Employee("emp1", 10)
    emp2 = Employee("emp2", 30)
    emp3 = Employee("emp3", 140)
    emp4 = Employee("emp4", 15)
    emp5 = Employee("emp5", 1)
    emp6 = Employee("emp6", 13)
    emp7 = Employee("emp7", 100)
    emp8 = Employee("emp8", 150)
    emp9 = Employee("emp9", 102)
    emp10 = Employee("emp10", 310)

    building1 = Building("Building 1", 40, 5, BuildingType.HEAVY_INDUSTRIAL.name)
    building2 = Building("Building 2", 200, 1, BuildingType.COLD_STORAGE.name)
    building3 = Building("Building 3", 100, 10, BuildingType.LIGHT_INDUSTRIAL.name)
    building4 = Building("Building 4", 400, 5, BuildingType.HEAVY_INDUSTRIAL.name, [emp10])

    company1 = ConstructionCompany("Company 1", "construction", [emp1, emp2, emp3, emp4, emp5, emp6, emp7, emp10],
                                   [building1, building2])
    company2 = ConstructionCompany("Company 2", "construction", [emp3, emp4, emp5, emp6, emp7, emp10])

    print(company1.get_top_five())
    print(company1.get_buildings_by_type())

    print(company1.assign_employees_to_building(emp9, BuildingType.HEAVY_INDUSTRIAL.name))

    print("Iterator test")
    company_iter = iter(company1)
    print(next(company_iter))
    print(next(company_iter))
    print(next(company_iter))
    print(next(company_iter))
    print(next(company_iter))
    print(next(company_iter))
    print(next(company_iter))
    print(next(company_iter))


if __name__ == '__main__':
    main()