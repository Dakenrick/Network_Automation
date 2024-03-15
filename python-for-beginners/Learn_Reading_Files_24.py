#Learn Python - Full Course for Beginners freeCodeCamp.org Youtube
#Lesson Reading Files: read from external files outside of your Python program. Files like .csv, .txt or .html etc. You can use these
#files to get information or to parse through the file. In the open() function we can use a relative path, absolute path or file name 
#if both files are in the same directory. Put the modes like read "r", write "w" and append "a", read & write "r+". Generally you 
#want to store the open(file) inside of a variable. Always make sure to close the file. Check to make sure the file is readable
# function is called readable().


employee_file = open("Employees1.txt", "r")
for employee in employee_file.readlines():
    print(employee)

#print(employee_file.readable())
#print(employee_file.read()) 
#print(employee_file.readline()) #Put readline twice to read next line.
#print(employee_file.readlines()) #Put lines in a list.

employee_file.close()