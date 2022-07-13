#Learn Python - Full Course for Beginners freeCodeCamp.org Youtube
#Lesson Object Funtions. You can define your own data types with classes.
#Modifiying Classess with a function inside of a class Student.py.

from Student import Student

student1 = Student("Oscar", "Accounting", 3.1, False)
student2 = Student("Phyllis", "Businees", 3.8, False)

print(student1.on_honor_roll())
print(student2.on_honor_roll())