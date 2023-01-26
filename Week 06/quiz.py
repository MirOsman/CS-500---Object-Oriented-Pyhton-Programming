class Student:
    def __init__(self, student_name: str, graduate: bool, program: str) -> None:
        self.graduate = graduate
        self.student_name = student_name
        self.program = program

    def __str__(self) -> str:
        is_graduated = "graduated" if self.graduate else "not graduacted"
        return f"{self.student_name} studying {self.program} and {is_graduated}"

    @property
    def graduate(self):
        return self._graduate

    @graduate.setter
    def graduate(self, val):
        self._graduate = val

    @property
    def student_name(self):
        return self._student_name

    @student_name.setter
    def student_name(self, val):
        self._student_name = val

    @property
    def program(self):
        return self._program

    @program.setter
    def program(self, val):
        self._program = val


class School:
    def __init__(
        self,
        school_name: str = None,
        students: list[Student] = None,
        programs: list[str] = None,
    ) -> None:
        self.school_name = school_name
        self.students = students
        self.programs = programs

    def __str__(self) -> str:
        output = f"School Name = {self.school_name}"
        output += "\nHas programs: \n"
        output += ", ".join(self.programs)
        output += "\nHas students: \n"
        output += ", ".join([student.student_name for student in self.students])
        return output

    @property
    def school_name(self):
        return self._school_name

    @school_name.setter
    def school_name(self, val):
        self._school_name = val

    def add_student(self, student: Student) -> None:
        self.students.append(student)

    def __iter__() -> None:
        pass

    def __next__() -> Student:
        pass


class College:
    def __init__(
        self,
        college_name: str,
        schools: list[School] = None,
        students: list[Student] = None,
    ) -> None:
        self.college_name = college_name
        self.schools = schools
        self.students = students

    def __str__(self) -> str:
        output = f"College Name = {self.college_name}"
        output += "\nHas Schools: \n"
        output += ", ".join([school.school_name for school in self.schools])
        output += "\nHas students: \n"
        output += ", ".join([student.student_name for student in self.students])
        return output

    @property
    def college_name(self):
        return self._college_name

    @college_name.setter
    def college_name(self, val):
        self._college_name = val

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
    john = Student("John", True, "Mscs")
    kytz = Student("kytz", False, "MSEE")
    mari = Student("mari", True, "MBA")
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

    stateuniveristy = College("san francisco bay university", [highschool, lowschool], [kytz, john, mari])
    print(stateuniveristy)
    print()

    students = stateuniveristy.get_students_by_program("MBA")
    for student in students:
        print(student.student_name)
    print()

    schools = stateuniveristy.get_schools_by_student("John")
    for school in schools:
        print(school.school_name)
    print()
    
if __name__ == "__main__":
 main()