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

#    def __str__(self):
#        return f'Студент:\n>>>Имя: {self.name}\n>>>Фамилия: {self.surname}\n'\
#                f'>>>Средняя оценка за домашние задания: {avg_student_grades}'
                 #f'>>>Курсы в процессе изучения: ')
                #f'{", ".join(best_student.courses_in_progress)}\n>>>Завершенные курсы: {", ".join(best_student.finished_courses)}'

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

#    def __str__(self):
#        return f'Лектор:\n>>>Имя: {self.name}\n>>>Фамилия: {self.surname}\n>>>Средняя оценка за лекции:{avg_lecturer_grades}'
        # {sum(lecturer.grades)/len(lecturer.grades)} '


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

    def __str__(self):
        return f'Проверяющий:\n>>>Имя: {self.name}\n>>>Фамилия: {self.surname}'

studentlist = [] #список студентов
lecturerlist = [] #список лекторов
courselist = ['Python','Java','Git'] #список курсов

#создаем экземпляры класса Student
student1 = Student('Roman','Podkorytov', 'Male')
student2 = Student('Olga','Chichilova', 'Female')

#добавляем наших студентов в список студентов
studentlist.append(student1)
studentlist.append(student2)

#создаем экземпляры класса Reviewer
reviewer1 = Reviewer('Sumit','Samanta')
reviewer2 = Reviewer('Stas','Moskvichev')

#создаем экземпляры класса Lecturer
lecturer1 = Lecturer('Paresh','Parich')
lecturer2 = Lecturer('Elena','Manuilova')

#добавляем наших лекторов в список лекторов
lecturerlist.append(lecturer1)
lecturerlist.append(lecturer2)

#определяем для наших студентов завершенные курсы и курсы в процессе изучения
student1.courses_in_progress += ['Python']
student1.courses_in_progress += ['Java']
student1.courses_in_progress += ['Git']
student1.finished_courses += ['Введение в программирование']

student2.courses_in_progress += ['Python']
student2.courses_in_progress += ['Java']
student2.courses_in_progress += ['Git']
student2.finished_courses += ['Введение в программирование']

#cool_reviewer = Reviewer('Some', 'Buddy')
#проверюящие проверяют задания по назначенным курсам
reviewer1.courses_attached += ['Python']
reviewer1.courses_attached += ['Git']

reviewer2.courses_attached += ['Java']

#лекторы читают следующие лекции
#best_lecturer = Lecturer('Ivan', 'Ivanov')
lecturer1.courses_attached += ['Java']
lecturer1.courses_attached += ['Python']

lecturer2.courses_attached += ['Git']

#вызов метода оценки домашнего задания проверюящими для указанных студентов
#для первого студента
reviewer1.rate_hw(student1, 'Python', 7)
reviewer1.rate_hw(student1, 'Git', 10)
reviewer1.rate_hw(student1, 'Python', 10)
reviewer1.rate_hw(student1, 'Git', 6)
reviewer2.rate_hw(student1, 'Java', 5)
reviewer2.rate_hw(student1, 'Java', 9)

#для второго студента
reviewer1.rate_hw(student2, 'Python', 9)
reviewer1.rate_hw(student2, 'Git', 10)
reviewer2.rate_hw(student2, 'Java', 8)
reviewer1.rate_hw(student2, 'Python', 4)
reviewer1.rate_hw(student2, 'Git', 8)
reviewer2.rate_hw(student2, 'Java', 7)

#студенты оценивают указанных лекторов
student1.lecturer_grade(lecturer1, 'Java', 5)
student1.lecturer_grade(lecturer2, 'Git', 10)
student1.lecturer_grade(lecturer1, 'Python', 8)
student1.lecturer_grade(lecturer1, 'Java', 9)
student1.lecturer_grade(lecturer2, 'Git', 7)
student1.lecturer_grade(lecturer1, 'Python', 4)

student2.lecturer_grade(lecturer2, 'Git', 10)
student2.lecturer_grade(lecturer1, 'Java', 7)
student2.lecturer_grade(lecturer1, 'Python', 9)
student2.lecturer_grade(lecturer2, 'Git', 6)
student2.lecturer_grade(lecturer1, 'Java', 10)
student2.lecturer_grade(lecturer1, 'Python', 5)

def avg_student_calculation(studentlist,course_name):
    '''функция подсчета среднего балла для студента'''
    for student in studentlist: #для каждого студента из списка
        if course_name in student.grades: #если курс имеется в словаре студента, то выполнякм расчет
            avg_student_grades = round(sum(student.grades[course_name]) / len(student.grades[course_name]),1)  # подсчет средней оценки по курсу Python для студента
            print(f'Студент:\n>>>Имя: {student.name} {student.surname}\n'\
                  f'>>>Средняя оценка за домашние задания по курсу {course_name}: {avg_student_grades}')
            print()

def avg_lecturer_calculation(lecturerlist,course_name):
    '''функция подсчета среднего балла для лектора'''
    for lecturer in lecturerlist: #для каждого лектора из списка
        if course_name in lecturer.grades: #если курс имеется в словаре лектора, то выполнякм расчет
            avg_lecturer_grades = round(sum(lecturer.grades[course_name]) / len(lecturer.grades[course_name]),1)  # подсчет средней оценки по курсу Python для студента
            print(f'Лектор:\n>>>Имя: {lecturer.name} {lecturer.surname}\n'\
                  f'>>>Средняя оценка за лекции по курсу {course_name}: {avg_lecturer_grades}')
            print()

#цикл - пробегаемся по каждому элементу- курсу из списка курсов courselist
for course in courselist:
    print("--- Курс:",course.upper(),"---")
    avg_student_calculation(studentlist,course) #вызываем функцию подсчета среднего значения, передавая в нее список студентов и название курса
    avg_lecturer_calculation(lecturerlist,course) #вызываем функцию подсчета среднего значения, передавая в нее список лекторов и название курса

#    print(course)
#avg_student_grades = round(sum(best_student.grades['Python'])/len(best_student.grades['Python']),1) #подсчет средней оценки по курсу Python для студента
#avg_lecturer_grades = round(sum(best_lecturer.grades['Java Script'])/len(best_lecturer.grades['Java Script']),1) #подсчет средней оценки по курсу Python для студента

#print(best_student.grades) #выводим словарь, где по ключу- дисцпилине имеются оценки
#print(best_lecturer.grades)

#print(reviewer1)
#print()
#print(lecturer1)
#print()
#print(student1) #выводим результат
#print(student2) #выводим результат