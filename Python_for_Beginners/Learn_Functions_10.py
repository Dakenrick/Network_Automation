#Learn Python - Full Course for Beginners freeCodeCamp.org Youtube
#Lesson Functions: A function is a collection of code which performs a specific task. Call the function for a task.
#Best practice use lowercase for function name. Two or more words use underscore. Pass additional information into function(paramenters).
#You can have as many parameters as you want. Good to break up code into different functions when they perform different tasks.

def say_hi(name, age): 
    print("Hello User " + name + ", you are " + str(age))

def say_hi_2(name, age):
    print("Hey, User's name and age is: " + name + ", " + age)

say_hi("Mike", 35)
say_hi_2("Steve", "70")