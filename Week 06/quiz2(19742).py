from tkinter.messagebox import NO, YES


class Student:                    #class school
    def __init__(self,student_name : int,graduate : bool, program : str) -> None: #constructor
        self.student_name= student_name
        self.graduate= graduate
        self.program = program
        
    @property
    def student_name(self) -> int:
        return self.student_name
    
    @student_name.setter
    def student_name(self, name: int ):
        self.student_name = name
        
    @property
    def graduate(self) -> bool:
        return self.graduate
    
    @graduate.setter
    def graduate(self, g : bool):
        self.graduate = g
        
    @property
    def program(self) -> str:
        return self.program
        
    @program.setter
    def program(self, p : str):
        self.program
    
    def __str__(self) -> str:
        is_graduated = "graduated" if self.graduate else "not graduacted"
        return f"{self.student_name} studying {self.program} and {is_graduated}"

class School:                    #class school
    def __init__(self,school_name : str,students : list[Student]) -> None: #constructor
        self.school_name= school_name
        self.students : list[Student] = []
        
    @property
    def school_name(self) -> str:
        return self.school_name
    
    @school_name.setter
    def school_name(self, name: str ):
        self.school_name = name
        
    @property
    def students(self) -> list[Student]:
        return self.students
    
    @students.setter
    def students(self, s : list[students]):
        self.students = s
    def __str__(self) -> str:
        output = f"School Name = {self.school_name}"
        output += "\nHas programs: \n"
        output += ", ".join(self.programs)
        output += "\nHas students: \n"
        output += ", ".join([student.student_name for student in self.students])
        return output
   
    

class College:                    #class college
    def __init__(self,college_name : str,School : list[School], Student : list[Student]) -> None: #constructor
        self.college_name= college_name
        self.students : list[Student] = []
        self.school : list[School] = []
        
        
    @property
    def college_name(self) -> str:
        return self.college_name
    
    @college_name.setter
    def college_name(self, name: str ):
        self.college_name = name
        
    @property
    def schools(self) -> list[School]:
        return self.schools
    
    @schools.setter
    def schools(self, sch : list[School]):
        self.schools = sch
        
    @property
    def students(self) -> list[Student]:
        return self.students
    
    @students.setter
    def students(self, s : list[students]):
        self.students = s
        
    def __str__(self) -> str:
        output = f"College Name = {self.college_name}"
        output += "\nHas Schools: \n"
        output += ", ".join([school.school_name for school in self.schools])
        output += "\nHas students: \n"
        output += ", ".join([student.student_name for student in self.students])
        return output
    
    def add_school(self, school: School) -> None:
        self.schools.append(school)

    def add_student(self, student: Student) -> None:
        self.students.append(student)

    def get_students_by_program(self, program: str) -> list[Student]:
        output = []
        for student in self.students:
            if student.program == program:
                output.append(student)

        return output

    def get_schools_by_program(self, program: str) -> list[School]:
        output = []
        for school in self.schools:
            if program in school.programs:
                output.append(school)

        return output

    def get_schools_by_student(self, student_name: str) -> list[School]:
        output = []
        for school in self.schools:
            for student in school.students:
                if student_name == student.student_name:
                    output.append(school)

        return output

def main() -> None:
    john = Student("John", YES, "Mscs")
    kytz = Student("kytz", NO, "MSEE")
    mari = Student("mari", YES, "MBA")
    print(john)
    print(kytz)
    print(mari)
    print()
    
    highschool = School("Paragon", [john, mari], ["MBA", "MSCS"])
    print(highschool)
    print()

    lowschool = School("Standard", [kytz], ["MSEE"])
    print(lowschool)
    print()
    
if __name__ == "__main__":
 main()