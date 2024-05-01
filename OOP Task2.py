class Student:
  def __init__(self, name, surname, gender):
      self.name = name
      self.surname = surname
      self.gender = gender
      self.finished_courses = []  #список завершенных курсов
      self.courses_in_progress = [] #список курсов на изучении
      self.grades = {} #словарь в котором по ключу- дисциплине будет соответствовать список оценок

  def lecturer_grade(self,lecturer,course,grade):
    #если объект lecturer принадлежит классу Lecturer и указанный курс есть в списке курсов, которые читает лектор и указанный курс также в процессе изучения студентом
    if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress:
      #если указанный курс имеется в словаре, то добавляем оценку по ключу- дисциплине, иначе возвращаем ошибку
      if course in lecturer.grades:
        lecturer.grades[course] += [grade]
      else:
          lecturer.grades[course] = [grade]
    else:
      return 'Ошибка'

class Mentor:
  def __init__(self, name, surname):
      #print(f"Инициализатор класса {self.__class__}")
      self.name = name
      self.surname = surname
      self.courses_attached = []
      self.grades = {}

class Lecturer(Mentor): #наследуемый класс Lecturer
  def __init__(self, name, surname):
      super().__init__(name, surname)

class Reviewer(Mentor): #наследуемый класс Reviewer
  def __init__(self, name, surname):
      super().__init__(name, surname)

  def rate_hw(self, student, course, grade): #метод оценки студента
      #если объект student принадлежит классу Student и указанный курс есть в списке курсов, который проверяет Проверяющий и указанный курс также в процессе изучения студентом
      if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
          #если указанный курс имеется в словаре, то добавляем оценку по ключу- дисциплине, иначе возвращаем ошибку
          if course in student.grades:
              student.grades[course] += [grade]
          else:
              student.grades[course] = [grade]
      else:
          return 'Ошибка'

best_student = Student('Ruoy', 'Eman', 'your_gender') #экземпляр класса Student
best_student.courses_in_progress += ['Python'] #добавляем в список courses_in_progress дисциплину Python
best_student.courses_in_progress += ['Java Script'] #добавляем в список courses_in_progress дисциплину Java Script

cool_reviewer = Reviewer('Some', 'Buddy') #экземпляр класса Reviewer
cool_reviewer.courses_attached += ['Python'] #добавляем в список courses_attached дисциплину Python

best_lecturer = Lecturer('Ivan','Ivanov') #экземпляр класса Lecturer
best_lecturer.courses_attached += ['Java Script'] #добавляем в список courses_attached дисциплину Java Script

cool_reviewer.rate_hw(best_student, 'Python', 10) #вызываем метод rate_hw в который передается значение best_student = Ruoy Eman , название курса = Python и оценка = 10 баллов
cool_reviewer.rate_hw(best_student, 'Python', 10) #вызываем метод rate_hw в который передается значение best_student = Ruoy Eman , название курса = Python и оценка = 10 баллов
cool_reviewer.rate_hw(best_student, 'Python', 10) #вызываем метод rate_hw в который передается значение best_student = Ruoy Eman , название курса = Python и оценка = 10 баллов
#в методе rate_hw произойдет сверка на наличие курса, если его нет в словаре, то будет создан словарь с ключом Python и значнием- списком, где элементы этого списка будут оценки

best_student.lecturer_grade(best_lecturer, 'Java Script', 5) #вызываем метод rate_hw в который передается значение best_lecturer = Ruoy Eman , название курса = Java Script и оценка = 5 баллов
best_student.lecturer_grade(best_lecturer, 'Java Script', 8) #вызываем метод rate_hw в который передается значение best_lecturer = Ruoy Eman , название курса = Java Script и оценка = 8 баллов
#в методе lecturer_grade произойдет сверка на наличие курса, если его нет в словаре, то будет создан словарь с ключом Python и значнием- списком, где элементы этого списка будут оценки

print(best_student.grades) #выводим результат в виде словаря, где ключом будет название дисцпилины, а значениями - список, состоящий из элементов оценок студенту по этой дисциплине
print(best_lecturer.grades) #выводим дисциплину и оценки студентов лектору по ней