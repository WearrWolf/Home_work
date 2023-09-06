class Student:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        self.average_rating = float()

    def rate_hw(self, lecturer, course, grade):
        #Возможность выставления оценки лектору студентом.
        if isinstance(lecturer, Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        grades_count = 0
        courses_in_progress_string = ', '.join(self.courses_in_progress)
        finished_courses_string = ', '.join(self.finished_courses)
        for r in self.grades:
            grades_count += len(self.grades[r])
        self.average_rating = sum(map(sum, self.grades.values())) / grades_count
        res = f'Имя: {self.name}\n' \
              f'Фамилия: {self.surname}\n' \
              f'Средняя оценка за домашнее задание: {self.average_rating}\n' \
              f'Курсы в процессе обучения: {courses_in_progress_string}\n' \
              f'Завершенные курсы: {finished_courses_string}'
        return res

    def __lt__(self, other):
        if not isinstance(other, Student):
            print('Такое сравнение некорректно')
            return
        return self.average_rating < other.average_rating
class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

class Lecturer(Mentor): #Лекторы
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.average_rating = float()
        self.grades = {}
    def __str__(self):
        grades_count = 0
        for r in self.grades:
            grades_count += len(self.grades[r])
        self.average_rating = sum(map(sum, self.grades.values())) / grades_count
        res = f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {self.average_rating}'
        return res
    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            print('Такое сравнение некорректно')
            return
        return self.average_rating < other.average_rating
class Reviewer(Mentor):#Эксперты
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'
    def __str__(self):
        res = f'Имя: {self.name}\nФамилия: {self.surname}'
        return res
# Список Лекторов
best_lecturer_1 = Lecturer('Zina', 'Ivanov')
best_lecturer_1.courses_attached += ['Python']

best_lecturer_2 = Lecturer('Olga', 'Olegovna')
best_lecturer_2.courses_attached += ['Java']

best_lecturer_3 = Lecturer('Semen', 'Axe')
best_lecturer_3.courses_attached += ['Python']
# Список Проверяющих
cool_reviewer_1 = Reviewer('Some', 'Buddy')
cool_reviewer_1.courses_attached += ['Python']
cool_reviewer_1.courses_attached += ['Java']

cool_reviewer_2 = Reviewer('Anna', 'Ryzan')
cool_reviewer_2.courses_attached += ['Python']
cool_reviewer_2.courses_attached += ['Java']
# Список Студентов
student_1 = Student('Denis', 'Sizov')
student_1.courses_in_progress += ['Python']
student_1.finished_courses += ['Введение в программирование']

student_2 = Student('Ivan', 'Slonovski')
student_2.courses_in_progress += ['Java']
student_2.finished_courses += ['Введение в программирование']

student_3 = Student('Vano', 'Zamai')
student_3.courses_in_progress += ['Python']
student_3.finished_courses += ['Введение в программирование']
# Выставляем оценки Лекторам за лекции
student_1.rate_hw(best_lecturer_1, 'Python', 10)
student_1.rate_hw(best_lecturer_1, 'Python', 10)
student_1.rate_hw(best_lecturer_1, 'Python', 10)

student_1.rate_hw(best_lecturer_2, 'Python', 4)
student_1.rate_hw(best_lecturer_2, 'Python', 9)
student_1.rate_hw(best_lecturer_2, 'Python', 9)

student_1.rate_hw(best_lecturer_1, 'Python', 7)
student_1.rate_hw(best_lecturer_1, 'Python', 8)
student_1.rate_hw(best_lecturer_1, 'Python', 9)

student_2.rate_hw(best_lecturer_2, 'Java', 8)
student_2.rate_hw(best_lecturer_2, 'Java', 6)
student_2.rate_hw(best_lecturer_2, 'Java', 1)

student_3.rate_hw(best_lecturer_3, 'Python', 8)
student_3.rate_hw(best_lecturer_3, 'Python', 2)
student_3.rate_hw(best_lecturer_3, 'Python', 3)

# Выставляем оценки студентам за домашние задания
cool_reviewer_1.rate_hw(student_1, 'Python', 7)
cool_reviewer_1.rate_hw(student_1, 'Python', 8)
cool_reviewer_1.rate_hw(student_1, 'Python', 10)

cool_reviewer_2.rate_hw(student_2, 'Java', 8)
cool_reviewer_2.rate_hw(student_2, 'Java', 7)
cool_reviewer_2.rate_hw(student_2, 'Java', 9)

cool_reviewer_2.rate_hw(student_3, 'Python', 6)
cool_reviewer_2.rate_hw(student_3, 'Python', 8)
cool_reviewer_2.rate_hw(student_3, 'Python', 7)
cool_reviewer_2.rate_hw(student_3, 'Python', 2)
cool_reviewer_2.rate_hw(student_3, 'Python', 6)
cool_reviewer_2.rate_hw(student_3, 'Python', 2)

print(f'Перечень студентов:\n\n{student_1}\n\n{student_2}\n\n{student_3}')
print()
print()
print(f'Перечень лекторов:\n\n{best_lecturer_1}\n\n{best_lecturer_2}\n\n{best_lecturer_3}')
print()
print()
print(f'Результат сравнения студентов (по средним оценкам за ДЗ): '
      f'{student_1.name} {student_1.surname} < {student_2.name} {student_2.surname} = {student_1 > student_2}')
print()
print(f'Результат сравнения лекторов (по средним оценкам за лекции): '
      f'{best_lecturer_1.name} {best_lecturer_1.surname} < {best_lecturer_2.name} {best_lecturer_2.surname} = {best_lecturer_1 > best_lecturer_2}')
print()
student_list = [student_1, student_2, student_3]
lecturer_list = [best_lecturer_1, best_lecturer_2, best_lecturer_3]
def student_rating(student_list, course_name):
    sum_all = 0
    count_all = 0
    for stud in student_list:
        if stud.courses_in_progress == [course_name]:
            sum_all += stud.average_rating
            count_all += 1
    average_for_all = sum_all / count_all
    return average_for_all
def lecturer_rating(lecturer_list, course_name):
    sum_all = 0
    count_all = 0
    for lect in lecturer_list:
        if lect.courses_attached == [course_name]:
            sum_all += lect.average_rating
            count_all += 1
    average_for_all = sum_all / count_all
    return average_for_all
print(f"Средняя оценка для всех студентов по курсу {'Python'}: {student_rating(student_list, 'Python')}")
print()
print(f"Средняя оценка для всех лекторов по курсу {'Python'}: {lecturer_rating(lecturer_list, 'Python')}")
print()