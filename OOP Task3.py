class Student:
    '''класс Студент'''
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = [] #список завершенных курсов
        self.courses_in_progress = [] #список курсов на изучении
        self.grades = {} #словарь в котором по ключу- дисциплине будет соответствовать список оценок

    def lecturer_grade(self, lecturer, course, grade):
        #если объект lecturer принадлежит классу Lecturer и указанный курс есть в списке курсов, которые читает лектор и указанный курс также в процессе изучения студентом
        if isinstance(lecturer,Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress:
            #если указанный курс имеется в словаре, то добавляем оценку по ключу- дисциплине, иначе возвращаем ошибку
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        return f'Студент:\n>>>Имя: {self.name}\n>>>Фамилия: {self.surname}\n' \
                f'>>>Средняя оценка за домашние задания: {avg_student_grades}\n>>>Курсы в процессе изучения: ' \
                f'{", ".join(best_student.courses_in_progress)}\n>>>Завершенные курсы: {", ".join(best_student.finished_courses)}'

    def __gt__(self, other: 'Lecturer'): #метод сравнения greater than
        st = avg_student_grades #помещаем в переменную st среднее значение оценок студента по курсу
        lct = avg_lecturer_grades #помещаем в переменную lct среднее значение оценок лектора по курсу
        return self.st > other.lct #возвращаем результат. Вернет True, если средняя оценка студента лучше средней оценки лектора

    def __lt__(self, other: 'Lecturer'): #метод сравнения less than
        st = avg_student_grades
        lct = avg_lecturer_grades
        return self.st < other.lct #возвращаем результат. Вернет True, если средняя оценка студента ниже средней оценки лектора

    def __ge__(self, other: 'Lecturer'): #метод сравнения greater or equal
        st = avg_student_grades
        lct = avg_lecturer_grades
        return self.st >= other.lct #возвращаем результат. Вернет True, если средняя оценка студента лучше или равна средней оценки лектора

    def __le__(self, other: 'Lecturer'):
        st = avg_student_grades
        lct = avg_lecturer_grades
        return self.st <= other.lct #возвращаем результат. Вернет True, если средняя оценка студента ниже или равна средней оценки лектора

class Mentor:
    def __init__(self, name, surname):
        # print(f"Инициализатор класса {self.__class__}")
        self.name = name
        self.surname = surname
        self.courses_attached = []
        self.grades = {}


class Lecturer(Mentor): #наследуемый класс Lecturer от основного класса Mentor
    '''класс лектор'''
    def __init__(self, name, surname):
        super().__init__(name, surname)

    def __str__(self): #метод __str__ преобразующий вывод результата
        return f'Лектор:\n>>>Имя: {self.name}\n>>>Фамилия: {self.surname}\n>>>Средняя оценка за лекции: {avg_lecturer_grades}'

#    def __gt__(self, other):
#        v = avg_lecturer_grades
#        return self.v > other.v
class Reviewer(Mentor):
    '''класс проверяющий'''
    def __init__(self, name, surname):
        super().__init__(name, surname)

    def rate_hw(self, student, course, grade):
        # если созданный объект student (в нашем случае best_student), принадлежит классу Student и переданное название курса
        # имеется в списке курсов преподавателя, а также переданный курс имеется в списке курсов обучающегося, то проверяем есть ли это курс в словаре с оценками
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades: #добавляем в словарь по ключу- дисциплине оценки
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self): #метод __str__ преобразующий вывод результата
        return f'Проверяющий:\n>>>Имя: {self.name}\n>>>Фамилия: {self.surname}'

best_student = Student('Ruoy', 'Eman', 'your_gender') #экземпляр класса Student
best_student.courses_in_progress += ['Python'] #добавляем в список courses_in_progress дисциплину Python
best_student.courses_in_progress += ['Java Script'] #добавляем в список courses_in_progress дисциплину Java Script
best_student.courses_in_progress += ['Git'] #добавляем в список courses_in_progress дисциплину Git
best_student.finished_courses += ['Введение в программирование'] #добавляем в список finished_courses дисциплину 'Введение в программирование' как завершенную

cool_reviewer = Reviewer('Some', 'Buddy') #экземпляр класса Reviewer
cool_reviewer.courses_attached += ['Python'] #добавляем в список courses_attached дисциплину Python

best_lecturer = Lecturer('Ivan', 'Ivanov') #экземпляр класса Lecturer
best_lecturer.courses_attached += ['Java Script'] #добавляем в список courses_attached дисциплину Java Script

cool_reviewer.rate_hw(best_student, 'Python', 10) #вызываем метод rate_hw в который передается значение best_student = Ruoy Eman , название курса = Python и оценка = 10 баллов
cool_reviewer.rate_hw(best_student, 'Python', 10) #вызываем метод rate_hw в который передается значение best_student = Ruoy Eman , название курса = Python и оценка = 10 баллов
cool_reviewer.rate_hw(best_student, 'Python', 9) #вызываем метод rate_hw в который передается значение best_student = Ruoy Eman , название курса = Python и оценка = 9 баллов

best_student.lecturer_grade(best_lecturer, 'Java Script', 8) #вызываем метод rate_hw в который передается значение best_lecturer = Ruoy Eman , название курса = Java Script и оценка = 5 баллов
best_student.lecturer_grade(best_lecturer, 'Java Script', 5) #вызываем метод rate_hw в который передается значение best_lecturer = Ruoy Eman , название курса = Java Script и оценка = 8 баллов

#подсчет средней оценки по курсу Python для студента.
#Считаем сумму элементов списка для ключа=Python и делим на кол-во элементов этгго списка для этого же ключа. Округляем до одного знака почле запятой
avg_student_grades = round(sum(best_student.grades['Python'])/len(best_student.grades['Python']),1)

#подсчет средней оценки по курсу Java Script для лектора.
#Считаем сумму элементов списка для ключа=Java Script и делим на кол-во элементов этгго списка для этого же ключа. Округляем до одного знака почле запятой
avg_lecturer_grades = round(sum(best_lecturer.grades['Java Script'])/len(best_lecturer.grades['Java Script']),1)

#print(best_student.grades) #выводим словарь, где по ключу- дисцпилине имеются оценки
#print(best_lecturer.grades)

#выводим результат с помощью метода
print(cool_reviewer)
print()
print(best_lecturer)
print()
print(best_student)
print()
if avg_student_grades > avg_lecturer_grades:
    print(f'Оценка студента лучше: {avg_student_grades} оценки лектора: {avg_lecturer_grades}')
elif avg_student_grades < avg_lecturer_grades:
    print(f'Оценка лектора лучше: {avg_lecturer_grades} оценки студента: {avg_student_grades}')
elif avg_student_grades >= avg_lecturer_grades:
    print(f'Оценка студента не хуже: {avg_student_grades} оценки лектора: {avg_lecturer_grades}')
elif avg_student_grades <= avg_lecturer_grades:
    print(f'Оценка лектора не хуже: {avg_lecturer_grades} оценки студента: {avg_student_grades}')

#else:
#    print('Оценки равны')
#print(f'Оценка студента лучше: {avg_student_grades}') if avg_student_grades > avg_lecturer_grades else print(f'Оценка лектора лучше: {avg_lecturer_grades}')