#Learn Python - Full Course for Beginners freeCodeCamp.org Youtube
#Lesson Writing to Files: append to and write to files. 

employee_file = open("Employees1.txt", "w")

employee_file.write("Toby - Human Resources")

employee_file = open("Employees1.txt", "a")

employee_file.write("\nKelly - Customer Service") 

employee_file.close()