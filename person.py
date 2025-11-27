import random

class Person:
    def __init__(self, name):
        self.name = name


class Teacher(Person):
    def __init__(self, name):
        super().__init__(name)

    def evaluate_exam(self):
        return random.randint(1, 100)


class Student(Person):
    def __init__(self, name, classroom):
        super().__init__(name)
        self.classroom = classroom
        self.marks = {}
        self.subject_grade = {}
        self._id = None
        self.grade = 0
    def calculate_final_grade(self):
        from school import School
        sum = 0
        for grade in self.subject_grade.values():
            point = School.grade_to_value(grade) # 5.00
            sum += point
        if sum == 0:
            gpa = 0.00
            self.grade = 'F'
        else:
            gpa = sum / len(self.subject_grade) # 7/2 = 3.50
            self.grade = School.value_to_grade(gpa)
        return f"{self.name} Final Grade : {self.grade} with GPA = {gpa:.2f}"

    # def calculate_final_grade(self):
    #     from school import School  # FIX: Local import avoids circular import

    #     total = 0
    #     for grade in self.subject_grade.values():
    #         point = School.grade_to_value(grade)
    #         total += point

    #     if len(self.subject_grade) == 0:
    #         self.grade = "F"
    #         return

    #     gpa = total / len(self.subject_grade)
    #     self.grade = School.value_to_grade(gpa)
        

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, sid):
        if not sid:
            raise ValueError("ID cannot be empty")
        if sid < 0:
            raise ValueError("ID cannot be negative")
        self._id = sid
