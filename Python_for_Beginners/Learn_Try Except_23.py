#Learn Python - Full Course for Beginners freeCodeCamp.org Youtube
#Lesson Try Except: catching errors in Python. We can watch out for errors and handle them and take action when they occur.
#Try except allows your program to run a piece of code. If everything works out good but if not then we can account for that.
#Best practice in Python is to use specific errors like ZeroDivisionError and ValueError.

try:
    answer = 10/0
    number = int(input("Enter a number: "))
    print(number)
except ZeroDivisionError as err:
    print(err) 
except ValueError:
    print("invalid input")      