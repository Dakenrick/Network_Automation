#Learn Python - Full Course for Beginners freeCodeCamp.org Youtube
#Lesson Classes and Objects. You can define your own data types with classes.
#They can represent real world things like phones that cannot be represented with strings, numbers, and boolean.
#Creating a student data type class Ex. Student.py. In classes you define attributes about student example.
#We can create an actual student which will be an object.

from Student import Student

student1 = Student("Jim", "Business", 3.1, False)
student2 = Student("Pam", "Art", 2.5, True)

print(student1.name)
print(student2.gpa)