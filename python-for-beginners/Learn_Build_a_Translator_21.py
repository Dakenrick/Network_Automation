#Learn Python - Full Course for Beginners freeCodeCamp.org Youtube
#Lesson Build a Translator: define a translate function, 

def translate(phrase):
    translation = ""
    for letter in phrase:
        if letter.lower() in "aeiou":
            if letter.isupper():
                translation = translation + "G"
            else:
                translation = translation + "g"
        else: 
            translation = translation + letter
    return translation

print(translate(input("Enter a phrase: ")))

