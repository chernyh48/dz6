list_student = []
list_lecturer = []


class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        self.avg = 0
        list_student.append(self)

    def __str__(self):
        return f'Имя: \033[38;5;208m{self.name}\033[0;0m\n' \
               f'Фамилия: \033[38;5;208m{self.surname}\033[0;0m\n' \
               f'Средняя оценка за домашние задания: \033[34;5;208m{self.avg}\033[0;0m\n' \
               f'Курсы в процессе изучения: \033[38;5;208m{", ".join(self.courses_in_progress)}\033[0;0m\n' \
               f'Завершенные курсы: {", ".join(self.finished_courses)}\n'

    def rate_hw(self, lecturer, course, grade):
        if isinstance(lecturer,
                      Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
            n = []
            for i in lecturer.grades:
                n.extend(lecturer.grades[i])
            lecturer.avg = round(sum(n) / len(n), 2)
        else:
            return 'Ошибка'


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Reviewer(Mentor):
    def __str__(self):
        return f'Имя: \033[38;5;208m{self.name}\033[0;0m\n' \
               f'Фамилия: \033[38;5;208m{self.surname}\033[0;0m\n'

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
            n = []
            for i in student.grades:
                n.extend(student.grades[i])
            student.avg = round(sum(n) / len(n), 2)
        else:
            return 'Ошибка'


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}
        self.avg = 0
        list_lecturer.append(self)

    def __str__(self):
        return f'Имя: \033[38;5;208m{self.name}\033[0;0m\n' \
               f'Фамилия: \033[38;5;208m{self.surname}\033[0;0m\n' \
               f'Средняя оценка за лекции: \033[34;5;208m{self.avg}\033[0;0m\n'


def comparison(operand_1, operand_2):
    if isinstance(operand_1, Student) and isinstance(operand_2, Student):
        if operand_1.avg == operand_2.avg:
            print('Средние баллы студентов равны.')
        elif operand_1.avg > operand_2.avg:
            print(f'Средний балл студента: {operand_1.name} {operand_1.surname} '
                  f'выше чем у {operand_2.name} {operand_2.surname}.')
        elif operand_1.avg < operand_2.avg:
            print(f'Средний балл студента: {operand_1.name} {operand_1.surname} '
                  f'ниже чем у {operand_2.name} {operand_2.surname}.')
    elif isinstance(operand_1, Lecturer) and isinstance(operand_2, Lecturer):
        if operand_1.avg == operand_2.avg:
            print('Средние баллы лекторов равны.')
        elif operand_1.avg > operand_2.avg:
            print(f'Средний балл лектора: {operand_1.name} {operand_1.surname} '
                  f'выше чем у {operand_2.name} {operand_2.surname}.')
        elif operand_1.avg < operand_2.avg:
            print(f'Средний балл лектора: {operand_1.name} {operand_1.surname} '
                  f'ниже чем у {operand_2.name} {operand_2.surname}.')
    else:
        print('Сравнение невозможно!')


# не понимаю зачем в задании написано создать 2 функции, если 1 можно обойтись:
def avg_grades(lst, cours):
    n = []
    for i in lst:
        if cours in i.grades:
            n.extend(i.grades[cours])
    if not n:
        return None
    else:
        return sum(n) / len(n)


student_1 = Student('Ваcилий', 'Пупкин', 'муж')
student_1.courses_in_progress += ['Python', 'Git']
student_1.finished_courses += ['SQL']
student_2 = Student('Валентина', 'Иванова', 'жен')
student_2.courses_in_progress += ['Python', 'Git']
student_2.finished_courses += ['SQL']
lecturer_1 = Lecturer('Петр', 'Ильич')
lecturer_1.courses_attached += ['Python']
lecturer_2 = Lecturer('Николай', 'Сидоров')
lecturer_2.courses_attached += ['Git']
reviewer_1 = Reviewer('Анатолий', 'Неклюев')
reviewer_1.courses_attached += ['Python']
reviewer_2 = Reviewer('Сергей', 'Антипов')
reviewer_2.courses_attached += ['Git']

student_1.rate_hw(lecturer_1, 'Python', 8)
student_1.rate_hw(lecturer_2, 'Git', 9)
student_2.rate_hw(lecturer_1, 'Python', 7)
student_2.rate_hw(lecturer_2, 'Git', 10)

reviewer_1.rate_hw(student_1, 'Python', 10)
reviewer_2.rate_hw(student_1, 'Git', 7)
reviewer_1.rate_hw(student_2, 'Python', 9)
reviewer_2.rate_hw(student_2, 'Git', 9)

print(student_1)
print(student_2)
print(lecturer_1)
print(lecturer_2)
print(reviewer_1)
print(reviewer_2)

comparison(student_1, student_2)
comparison(lecturer_1, lecturer_2)
comparison(student_1, lecturer_2)

print(avg_grades(list_student, 'Python'))
print(avg_grades(list_lecturer, 'Python'))
print(avg_grades(list_lecturer, 'SQL'))
print(avg_grades(list_lecturer, 'Git'))
print(avg_grades(list_student, 'Git'))
