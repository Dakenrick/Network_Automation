#Learn Python - Full Course for Beginners freeCodeCamp.org Youtube
#Lesson If Statements & Comparison: compare a couple numbers or strings. You can compare strings ex. "dog" == "dogs" using double equals. You can do a not equal 
#comparison with ex. num1 != num2. Other comparison operators are: <= less than or equal to.

def max_num(num1, num2, num3):
    if num1 >= num2 and num1 >= num3: 
        return num1
    elif num2 >= num1 and num2 >= num3:
        return num2
    else:
        return num3

print(max_num(0, 15, 82)) 
