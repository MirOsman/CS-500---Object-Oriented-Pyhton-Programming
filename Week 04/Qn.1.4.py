class Person:
    def __init__(self, name ) -> None:
        self.__name = name
        
    @property
    def name(self):
         return self.__name
     
        
    def display(self):
        print("name =", self.__name)
        
    def dowork(self):
        print("Person", self.__name, "is doing nothing")

class Programmer(Person):
    def __init__(self, name, skills, salary) -> None:
        super().__init__(name)
      
        self.__skills = skills
        self.__salary = salary
        
    def display(self):
         super().display()
         print("skills=", self.__skills)
         print("salary=", self.__salary)
         
    def dowork(self):
        print("programmer ", self.name, "is writing a program")
        
    def get_annual_income(self) -> float:
        return self.__salary * 12
    
class Manager(Programmer):
    def __init__(self, name, skills, salary, bonus) -> None:
        super().__init__(name, skills, salary)
        self.__bonus = bonus
        
    def display(self):
         super().display()
         print("bonus=", self.__bonus)

    def dowork(self):
        print("Manager ", self.name, "is superwising a team of programmers")
        
    def get_annual_income(self) -> float:
        return super().get_annual_income() + self.__bonus
    
class Project:
    def __init__(self, projname : str, budget: float = 0.0, active: bool = False) -> None:
        self.__projname = projname
        self.__budget = budget
        self.__active = active
        
    def display(self):
        print("projname=", self.__projname)
        print("budget=", self.__budget)
        print("active=", self.__active)
        
        
        

class Group:
    def __init__(self, groupname: str) -> None:
        self.__groupname = groupname
        self.__members:list[Programmer] = []
        
    def add_member(self, member: Programmer) -> None:
        self.__members.append(member)
        
    def remove_member(self, name:str) -> None:
        pass
        
        
    def display(self):
        print("The group has these members")
        for member in self.__members:
            member.display()
            print()
    
class ITGroup(Group):
    def __init__(self, groupname: str) -> None:
        super().__init__(groupname)
        self.__projects :list[Project] = []
        
    def add_project(self, project : Project):
        self.__projects.append(project)
     
     
     
    def display(self):
        super().display()
        print("The group has these projetcs")
        for project in self.__projects:
            project.display()
            print()
   
        
        
            
            
def main():
   p1: Programmer = Programmer("Lily", "C++, Java", 10000)
   p2: Programmer = Programmer("Judy", "Python, Java", 18000)
   m: Manager = Manager("Peter", "Management", 20000, 20000)
   proj1: Project = Project("MAX-5", 200000, True)
   proj2: Project = Project("FOX-4", 100000, False)
   proj3: Project = Project("FOX-XP", 500000, True)
   itgrp: ITGroup = ITGroup("ATX Group")
   itgrp.add_member(p1)
   itgrp.add_member(p2)
   itgrp.add_member(m)
   itgrp.add_project(proj1)
   itgrp.add_project(proj2)
   itgrp.add_project(proj3)
   itgrp.display()
   p3: Programmer = Programmer("Jone", "Python, Java", 1118000)
   itgrp.add_member(p3)
 
   
if __name__ == "_main_":
    main()