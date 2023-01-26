import csv
        
class Course:
    def __init__(self, Courses : float) -> None:
         self.Courses:list[Course] = []
        
    def getCourses(runData: dict[str, list[float]]) -> dict[str, list[str]]:
        getCourses: dict[str, list[str]] = {}
        for part in runData:
            if part.studentid not in getCourses:
                    getCourses[part.serialNumber] = []
        getCourses[part.studentid].append(part)
        return getCourses

class Student:
    def __init__(self, name : str ) -> None:
        self.name = name
        self.Courses:list[Course] = []
        
    def __str__(self):
        return self.name + ": " + str

    def __repr__(self):
        return self.__str__()
    
class Diver:
   def read_files(students: list[Student], courses:list[Course] ) -> None:
        with open(students) as file:
            for line in file:
                line = line.replace("\n", "")
                courses.append(line)
        return courses
 
class Summary:
    def write_summary(students: list[Student], courses:list[Course]) -> None:
        with open(students, "w") as file:
            for diver in courses:
                file.write(diver + "\n")

def main():
    d = Diver()
    s = Summary()
    t = d.read_files("students.csv, CS500.csv, CS480.csv, CS360.csv")
    w = s.write_summary("students.csv, CS500.csv, CS480.csv, CS360.csv")
    print(t)
    print(w)