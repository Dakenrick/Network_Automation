#Learn Python - Full Course for Beginners freeCodeCamp.org Youtube
#Lesson For Loops: is a special loop in Python which allows us to loop over a collection of items.

friends = ["Jim", "Karen", "Kevin"]
len(friends)

for friend in friends:
    print(friend)

for index in range(3, 10):
    print(index)

for index in range(len(friends)):
    print(friends[index])

for index in range(5):
    if index == 0:
        print("First Interation")
    else:
        print("Not first.")