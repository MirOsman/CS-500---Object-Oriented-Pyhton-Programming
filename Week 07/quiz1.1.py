class Student:

    # constructor that accepts the student name, graduate and program as parameter
    def __init__(self, student_name, graduate, program):

        # initialize the class attributes to the respective parameters passed to the constructor
        self.student_name = student_name
        self.graduate = graduate
        self.program = program

    def __str__(self) -> str:
        # return a string containing the student name, graduate and program
        return f"Student Name: {self.student_name}, Graduate: {self.graduate}, Program: {self.program}"


class School:

    # constructor that accepts the school name and the list of programs
    def __init__(self, school_name, programs):

        # initialize the school name and programs attributes to the respective parameter passed to the constructor
        self.school_name = school_name
        self.programs = programs

        # initialize the students attribute to an empty list
        self.students = []

    def __str__(self) -> str:
        # construct a string containing the school name, the students and the programs
        s = f"School Name: {self.school_name}\n"
        s += "Students:\n"

        for stud in self.students:
            s += str(stud) + "\n"

        s += f"Programs: {self.programs}"

        # return the string
        return s

    def add_student(self, student: Student) -> None:
        # append the student to the students attribute
        self.students.append(student)

    def __iter__(self):
        # initialize the index for the students list
        self.index = 0

        # return the class
        return self

    def __next__(self):
        # check if the index is less than the number of students in the students list
        if self.index < len(self.students):

            # get the student at the current index
            student = self.students[self.index]

            # increment the index
            self.index += 1

            # return the student
            return student

        # the index exceeds the number of students in the list, throw a StopIteration exception
        raise StopIteration


class College:
    # constructor that accepts the college name as parameter.
    def __init__(self, college_name):

        # initialize the class attributes to the respective parameters passed to the constructor
        self.college_name = college_name
        self.schools = []
        self.students = []

    def __str__(self) -> str:

        # construct a string containing the college name, the schools and the students
        s = f"College Name: {self.college_name}\n"
        s += "Schools:\n"

        for school in self.schools:
            s += str(school) + "\n"

        s += "Students:\n"

        for stud in self.students:
            s += str(stud) + "\n"

        # return the string
        return s

    def add_school(self, school: School) -> None:
        # append the school to the schools list
        self.schools.append(school)

    def add_student(self, student: Student) -> None:
        # append the student to the students list
        self.students.append(student)

    def get_students_by_program(self, program):

        # create a list that will store the students that belong to the specified program
        student_list = []

        # loop through each student in the students list
        for student in self.students:

            # check if the student program matches the specified program
            if student.program == program:

                # add the student to the list
                student_list.append(student)

        # return the list
        return student_list

    def get_schools_by_program(self, program):

        # create a list that will store the schools that belong to the specified program
        school_list = []

        # loop through each school in the schools list
        for school in self.schools:

            # check if the specified program is included in the list of the school programs
            if program in school.programs:

                # add the school to the list
                school_list.append(school)

        # return the list
        return school_list

    def get_schools_by_student(self, student_name):

        # create a list that will store the schools of the specified students
        school_list = []

        # loop through each school in the schools list
        for school in self.schools:

            # check if the specified student is included in the list of the school students
            for student in school.students:
                if student.student_name == student_name:

                    # append the school to the list
                    school_list.append(school)

        # return the list
        return school_list


def main():

    print("Create a Student object:")

    st1 = Student("Bradley Leonard", False, "MBA")

    print(st1)

    print("-" * 80 + "\n")

    print("Create a School object:")

    sch1 = School("ABC College", ["MBA", "MSCS"])
    print(sch1)

    sch1.add_student(st1)

    print(sch1)

    print("-" * 80 + "\n")

    print("Test __iter__ and __next__ methods using for-loop:")

    st2 = Student("Kate Lawrence", True, "MBA")
    sch1.add_student(st2)

    for s in sch1:
        print(s)

    print("-" * 80 + "\n")

    print("Test __iter__ and __next__ methods using iter() and next() function")
    i = iter(sch1)

    s1 = next(i)
    print(s1)

    s2 = next(i)
    print(s2)

    print("-" * 80 + "\n")

    print("Create a College object")

    coll1 = College("ABC Colleges")

    print(coll1)

    print("-" * 80 + "\n")

    print("Add a school:")

    coll1.add_school(sch1)

    print(coll1)

    print("-" * 80 + "\n")

    print("Add a student:")

    st3 = Student("Jane Pittman", True, "MBA")

    coll1.add_student(st3)

    print(coll1)

    print("-" * 80 + "\n")

    print("Get student by program:")

    mba_students = coll1.get_students_by_program("MBA")

    for student in mba_students:
        print(student)

    print("-" * 80 + "\n")

    print("Get schools by program:")

    msee_schools = coll1.get_schools_by_program("MBA")

    for sch in msee_schools:
        print(sch)

    print("-" * 80 + "\n")

    print("Get schools by student:")

    schools = coll1.get_schools_by_student("Bradley Leonard")

    for s in schools:
        print(s)

    print("-" * 80 + "\n")


if __name__ == "__main__":
    main()