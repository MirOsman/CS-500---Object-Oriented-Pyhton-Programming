from typing import List

class Person:
    def __init__(self, name:str) -> None:
        self.__name = name

    def doWork(self) -> None:
        print('Person:', self.__name, 'doing nothing')

    def display(self) -> None:
        print('Name:', self.__name)
    
    @property
    def name(self) -> str:
        return self.__name

class Programmer(Person):
    def __init__(self, name: str, skills:str, salary:float) -> None:
        Person.__init__(self, name)
        self.__skills = skills
        self.__salary = salary
    
    def doWork(self) -> None:
        print('Programmer',self.name, 'is writing a program')

    def display(self) -> None:
        super().display()
        print('Skills:', self.__skills)
        print('Salary:', self.__salary)
    
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

    def getAnnualIncome(self):
        return self.__salary * 12 

class Manager(Programmer):
    def __init__(self, name: str, skills: str, salary: float, bonus:float) -> None:
        Programmer.__init__(self, name, skills, salary)
        self.__bonus = bonus

    def getAnnualIncome(self) -> float:
        return super().getAnnualIncome() + self.__bonus

    def display(self) -> None:
        super().display()
        print('Bonus:', self.__bonus)

    def doWork(self) -> None:
        print('Manager', self.name, 'is supervising a team of programmers.')
    
class Project():
    def __init__(self, projName:str, budget=0.0, active=False) -> None:
        self.__projName = projName
        self.__budget = budget
        self.__active = active
    
    def dispaly(self):
        print("Project Name:", self.__projName)
        print("Budget:", self.__budget)
        print("Active:", self.__active)

    @property
    def active(self) -> bool:
        return self.__active

    @property
    def budget(self) -> float:
        return self.__budget

    

class Group():
    def __init__(self, name:str) -> None:
        self.__name = name
        self.__members: List[Manager] = []

    @property
    def name(self) -> str:
        return self.__name

    def addMember(self, member):
        self.__members.append(member)

    def askAnyoneDoWork(self): 
        for i in self.__members:
          i.doWork()

    '''def askManagerDoWork(self):
        for i in self.__members:
            if i.skills == "Management":
                i.doWork()'''

    def askManagerDoWork(self):
        for i in self.__members:
            if isinstance(i, Manager):
                i.doWork()


    '''def getAllMembersMoreThan(self, income):
        for member in self.__members:
            if member.getAnnualIncome() > income:
                member.display()
                print()'''

    def getAllMembersMoreThan(self, income):
        members = []
        for member in self.__members:
            if member.getAnnualIncome() > income:
                members.append(member)
        return members

    def display(self) -> None:
        print('\nThe {0} has these members:'.format(self.__name))
        for member in self.__members:
            member.display()
            print()   


class ITGroup(Group):
    def __init__(self, name: str) -> None:
        Group.__init__(self, name)
        self.__projects: List[Project] = []

    def addProject(self, project: Project):
        self.__projects.append(project)

    def display(self) -> None:
        super().display()
        print('\nThe {0} has these projects:'.format(self.name))
        for project in self.__projects:
            project.dispaly()
            print()

    '''def findLargestProject(self):
        for lrgtProject in self.__projects:
            if lrgtProject.budget >= 500000:
                lrgtProject.dispaly()
                print()'''

    def findLargestProject(self):
        largeProj = None
        for lrgtProject in self.__projects:
            if largeProj is None:
                largeProj = lrgtProject
            elif lrgtProject.budget > largeProj.budget:
                largeProj = lrgtProject
        return largeProj

    def getActiveProjects(self):
        for i in self.__projects:
            if i.active is True:
                i.dispaly()
                print()

    '''def getActiveProjects(self):
        projects = []
        for i in self.__projects:
            if i.active == True:
                projects.append(i)
        return projects'''
        
def main(): 
    p1 = Programmer("Lily", "C++, Java", 10000) 
    p2 = Programmer("Judy", "Python, Java", 18000) 
    m = Manager("Peter", "Management", 20000, 20000) 
    proj1 = Project("MAX-5", 200000, True) 
    proj2 = Project("FOX-4", 100000, False) 
    proj3 = Project("FOX-XP", 500000, True) 
 
    itgrp = ITGroup("ATX Group") 
    itgrp.addMember(p1) 
    itgrp.addMember(p2) 
    itgrp.addMember(m) 
    itgrp.addProject(proj1) 
    itgrp.addProject(proj2) 
    itgrp.addProject(proj3) 
    itgrp.display() 
 
    itgrp.askAnyoneDoWork() 
    print() 
    itgrp.askManagerDoWork() 
 
    print("\nGet the largest project...") 
    maxProj = itgrp.findLargestProject() 
    maxProj.display() 
 
    print("\nGet the acive projects...") 
    projects = itgrp.getActiveProjects() 
    for proj in projects: 
     proj.display() 
     print() 
 
    print("\nGet the members with high income...") 
    members = itgrp.getAllMembersMoreThan(200000) 
    for member in members: 
     member.display() 
     print()
        
        
if __name__ == "__main__":
 main()
