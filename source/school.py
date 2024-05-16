from datetime import date


class TooManyStudents(Exception):
    pass


class Person:
    def __init__(self, name, birthdate):
        self.name = name
        self.birthdate = birthdate

    def __repr__(self):
        return f'{self.__class__.__name__}({self.name!r}, {self.birthdate!r})'

    def __str__(self):
        return f'{self.name}, born on {self.birthdate.strftime('%d %B %Y')}'

    def age(self):
        today = date.today()
        years = today.year - self.birthdate.year
        if (self.birthdate.month, self.birthdate.day) > (today.month, today.day):
            years -= 1
        return years


class Student(Person):
    def __init__(self, name, birthdate, track):
        super().__init__(name, birthdate)
        self.track = track
        self.courses = []

    def __repr__(self):
        return super().__repr__()[:-1] + f', {self.track!r})'

    def print_courses(self):
        for course in self.courses:
            print(course)


class Teacher(Person):
    pass


class Course:
    number = 1
    MAX_REGISTRATIONS = 20

    def __init__(self, title, teacher):
        self.title = title
        self.teacher = teacher
        self.students = []
        self.number = Course.number
        Course.number += 1

    def __repr__(self):
        return f'{self.__class__.__name__}({self.title!r}, {self.teacher!r})'

    def __str__(self):
        return f'{self.number} - {self.title}'

    def register(self, new_student):
        if len(self.students) < Course.MAX_REGISTRATIONS:
            self.students.append(new_student)
            new_student.courses.append(self.title)
        else:
            raise TooManyStudents('Students limited to 20')

    def remove_student(self, name):
        for student in self.students:
            if student.name == name:
                self.students.remove(student)
                student.courses.remove(self.title)

    def change_teacher(self, new_teacher):
        self.teacher = new_teacher
