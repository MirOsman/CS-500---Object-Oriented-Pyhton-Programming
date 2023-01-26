from __future__ import annotations # for showing later observer use this future method
from abc import ABC, abstractmethod

class SubjectInterface(ABC):
    @abstractmethod
    def register_observer(self, observer: Observer):
        pass

    @abstractmethod
    def remove_observer(self, observer: Observer):
        pass

    @abstractmethod
    def notify_observer(self):
        pass

class Observer(ABC):
    @abstractmethod
    def update(self, data: str):
        pass

class AcademicOffice(SubjectInterface):
    def __init__(self) -> None:
        self.__observers: list[Observer] = []
        self.__exam_date: str = ""

    def update_exam_date(self, exam_date: str):
        self.__exam_date = exam_date
        self.notify_observer()

    def register_observer(self, observer: Observer):
        self.__observers.append(observer)

    def remove_observer(self, observer: Observer):
        self.__observers.remove(observer)

    def notify_observer(self):
        for observer in self.__observers:
            observer.update(self.__exam_date)

class Student(Observer):
    def __init__(self, name:str, gpa: float) -> None:
        self.__name = name
        self.__gpa = gpa

    def study_exam(self, exam_date: str):
        print(f"Student {self.__name} is studying hard for the exam on {exam_date}")

    def update(self, data: str):
        self.study_exam(data)

class Professor(Observer):
    def __init__(self, name:str, department: str) -> None:
        self.__name = name
        self.__department = department

    def writing_exam(self, exam_date: str):
        print(f"Professor {self.__name} is writing questions for the exam on {exam_date}")

    def update(self, data: str):
        self.writing_exam(data)

def main() -> None:
    office = AcademicOffice()
    s1 = Student("Peter", 4.0)
    s2 = Student("Lily", 3.0)
    p1 = Professor("Henry", "CS")

    office.register_observer(s1)
    office.register_observer(s2)
    office.register_observer(p1)

    office.update_exam_date("Dec 10")

    office.remove_observer(s2)
    print()
    office.update_exam_date("Dec 20")


if __name__ == "__main__":
    main()