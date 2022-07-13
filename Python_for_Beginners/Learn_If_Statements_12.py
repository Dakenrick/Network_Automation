#Learn Python - Full Course for Beginners freeCodeCamp.org Youtube
#Lesson If Statements: we can help our program make decisions. Execute certain code when certain conditions are true. You can have as
#many lines in an if statement as you want. The or operator is one or more matches. The and operation all must match.

is_male = False
is_tall = False

if is_male and is_tall:
    print("You are a tall male")
elif is_male and not(is_tall):
    print("You are a short male")
elif not(is_male) and is_tall:
    print("You are not a male but are tall")
else: 
    print("You are either not male or not tall")