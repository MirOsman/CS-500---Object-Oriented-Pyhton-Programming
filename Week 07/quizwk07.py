class Student:
    def __init__(self, program : str) -> None:
        self.__program = program
        
    @property
    def program(self) -> str:
        return self.__program


    def __str__(self) -> str:
        return f"program = {self.__program}"
    
    def __repr__(self) -> str:
        return str(self)

class School:
    def __init__(self, school_name : str, programs : list[str] = []) -> None:
        self.__school_name = school_name
        self.__students : list[Student] = []
        self.__programs : list[str] = []
        
        for program in programs:
            self.__programs.append(Student)
        
        
    def add_student(self, student):
        self.__students.append(student)
        
    def has_program(self, program : str) -> bool:
        return program in self.__programs

    def __str__(self) -> str:
        return f"school_name = {self.__school_name}, students = {self.__students}"
    
    def __repr__(self) -> str:
        return str(self)

class College:
    def __init__(self, college_name : str) -> None:
        self.__college_name = college_name
        self.__students : list[Student] = []
        self.__schools : list[School] = []
        
        
    def add_student(self, student : Student):
        self.__students.append(student)
        
        
        for school in self.__schools:
            if school.has_program(student.program):
                school.add_student(student)
                
    def add_school(self, school_name : str, program : list[str]) -> None:
        self.__schools.append(School(school_name, program))
        
    def __str__(self) -> str:
        return f"college_name = {self.__college_name}, students = {self.__students}, schools = {self.__schools}"
    
    def __repr__(self) -> str:
        return str(self)
    
    def init_student(self):
        self.__index2 = -1     # initialize index for each iteration
        return self
    
    def next_student(self) -> Optional[Student]:
        if self.__index2 >= len(self.__students) -1:
            return None
        self.__index2 += 1
        student = self.__students[self.__index2]
        return student

def main() -> None:
    s1 = Student('MSCS')
    s2 = Student('MSEE')
    s3 = Student('MBA')
    s4 = Student('BA')
    s5 = Student('MBA')
    
    college = College("SFBU")
    college.add_school("Business", ["BA","MBA"])
    college.add_school("Engineering", ["MSCS","MSEE"])
    college.add_student(s1)
    college.add_student(s2)
    college.add_student(s3)
    college.add_student(s4)
    college.add_student(s5)
    
    
   # print(college)
    College.init_student()
    student = college.next_student()
    while student is not None:
       print(student)
       student = College.next__student()



if __name__ == "__main__":
    main()
    