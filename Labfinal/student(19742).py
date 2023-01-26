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

# open all 4 csv files
def read_files(students: list[Student], courses:list[Course] ) -> None:
    with open('students.csv', 'r') as student_file, open('CS500.csv', 'r') as cs500_file, open('CS480.csv', 'r') as cs480_file, open('CS360.csv', 'r') as cs360_file:
    # create csv readers for each file
        student_reader = csv.reader(student_file)
        cs500_reader = csv.reader(cs500_file)
        cs480_reader = csv.reader(cs480_file)
        cs360_reader = csv.reader(cs360_file)

    # create empty dictionary to store student data
    students = {}

    # loop through students.csv and store student data in dictionary
    for row in student_reader:
        students[row[0]] = {
            "name": row[1],
            "cs500_grade": None,
            "cs480_grade": None,
            "cs360_grade": None
        }

    # loop through CS500.csv and update student dictionary
    for row in cs500_reader:
        students[row[0]]["cs500_grade"] = row[1]

    # loop through CS480.csv and update student dictionary
    for row in cs480_reader:
        students[row[0]]["cs480_grade"] = row[1]

    # loop through CS360.csv and update student dictionary
    for row in cs360_reader:
        students[row[0]]["cs360_grade"] = row[1]

def write_summary(students: list[Student], courses:list[Course]) -> None:
    # write summary to output file
    with open('summary.csv', 'w') as summary_file:
        summary_writer = csv.writer(summary_file)

        # write header row
        summary_writer.writerow(["ID", "Name", "CS500", "CS480", "CS360"])

        # loop through students and write summary row
        for student_id, student_data in students.items():
            summary_writer.writerow([
                student_id,
                student_data["name"],
                student_data["cs500_grade"],
                student_data["cs480_grade"],
                student_data["cs360_grade"]
            ])
            

def main():
    r = read_files()
    w = write_summary()
    print(r)
    print(w)
    
if __name__ == "__main__":
    main()
