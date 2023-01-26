from ast import Pass
from typing_extensions import Self


class Person:
    def __init__(self, name ) -> None:
        self._name = name
        
    @property
    def name(self):
         return self._name
     
        
    def display(self):
        print("name =", self._name)
        
    def dowork(self):
        print("Person", self._name, "is doing nothing")

class Programmer(Person):
    def __init__(self, name, skills, salary) -> None:
        super().__init__(name)
        self.__skills = skills
        self.__salary = salary
        
    @property
    def salary(self) -> float:
        return self.__salary
    
    @salary.setter
    def salary(self, salary:float) -> None:
        self.__salary = salary

    @property
    def skills(self) -> str:
        return self.__skills

    @skills.setter
    def skills(self, skills: str) -> None:
        self.__skills = skills
        
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
        print("Manager ", self.name, "is supervising a team of programmers")
        
    def get_annual_income(self) -> float:
        return super().get_annual_income() + self.__bonus
    
class Project:
    def __init__(self, projname : str, budget: float = 0.0, active: bool = False) -> None:
        self.__projname = projname
        self.__budget = budget
        self.__active = active
        
    @property
    def active(self) -> bool:
        return self.__active

    @property
    def budget(self) -> float:
        return self.__budget
        
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
        for member in self.__members:
            if member.name == name:
                self.__members.remove(member) # check
        #self.__members.remove(member)
        
    def ask_anyone_doWork(self) -> None: 
          for member in self.__members:
            member.dowork() #check
        #for i in self.__members:
            #i.doWork()
            
    def ask_manager_doWork(self) -> None:
        for member in self.__members:
            member.Manager.dowork() #check
        #return super().ask_manager_doWork
        #for i in self.__members:
            #if isinstance(i, Manager):
                #i.doWork()
                
    def get_allMembers_morethan(self, income : float) :
        members = []
        for member in self.__members:
            if member.get_annual_income() > income:
                members.append(member)
        return members
        
        
    def display(self):  
        print("The group has these members")
        for member in self.__members:
            member.display()
            print()
    def work(self):
        for member in self.__members:
            member.dowork()
    def mngwork(self):
         for member in self.__members:
            if member=="Peter":
                member.dowork()
            
        
        
    
    
class ITGroup(Group):
    def __init__(self, groupname: str) -> None:
        super().__init__(groupname)
        self.__projects :list[Project] = []
        
    def add_project(self, project : Project):
        self.__projects.append(project)
        
    def find_largest_project(self):
        largeProj = None
        for lrgtProject in self.__projects:
            if largeProj is None:
                largeProj = lrgtProject
            elif lrgtProject.budget > largeProj.budget:
                largeProj = lrgtProject
        return largeProj
    

    

    def get_active_projects(self) -> list[Project]:
        for i in self.__projects:
            if i.active is True:
                i.display()
                print()
                
    def display(self):
        super().display()
        print("The group has these projetcs")
        for project in self.__projects:
            project.display()
            print()
    def ask_anyone_dowork(self):
        super().work()
    def ask_manager_dowork(self):
        super().mngwork()
        
        
            
            
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
   itgrp.ask_anyone_dowork()
   print()
   itgrp.ask_manager_dowork()
   
   print("\nGet the largest project...")
   maxProj: Project = itgrp.find_largest_project()
   maxProj.display()
   print("\nGet the acive projects...")
   projects: list[Project] = itgrp.get_active_projects()
   #for proj in projects:
    #proj.display()
   print()
   itgrp.remove_member(p3.name)
   p1: Programmer = Programmer("Lily", "C++, Java", 10000)
   p2: Programmer = Programmer("Judy", "Python, Java", 18000)
   p3: Programmer = Programmer("Jone", "Python, Java", 1118000)
   m: Manager = Manager("Peter", "Management", 20000, 20000)
   proj1: Project = Project("MAX-5", 200000, True)
   proj2: Project = Project("FOX-4", 100000, False)
   proj3: Project = Project("FOX-XP", 500000, True)
   itgrp: ITGroup = ITGroup("ATX Group")
   itgrp.add_member(p1)
   itgrp.add_member(p2)
   itgrp.add_member(p3)
   itgrp.add_member(m)
   itgrp.add_project(proj1)
   itgrp.add_project(proj2)
   itgrp.add_project(proj3)
   itgrp.display()
   #p3: Programmer = Programmer("Jone", "Python, Java", 1118000)
   #itgrp.add_member(p3)
   print("\nGet the members with high income...")
   members: list[Programmer] = itgrp.get_allMembers_morethan(200000)
   for member in members:
     member.display()
     print()
   
if __name__ == "__main__":
    main()