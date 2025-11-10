#Abstract methods

from abc import ABC, abstractmethod
class Student(ABC):
    @abstractmethod
    def calculate_grade(self):
        pass
class UndergraduateStudent(Student):
    def __init__(self, marks):
        self.marks = marks
    def calculate_grade(self):
        if self.marks >= 90:
            return 'A'
        elif self.marks >= 80:
            return 'B'
        elif self.marks >= 70:
            return 'C'
        elif self.marks >= 60:
            return 'D'
        else:
            return 'F'