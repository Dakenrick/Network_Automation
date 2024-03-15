#Learn Python - Full Course for Beginners freeCodeCamp.org Youtube
#Lesson Lists function: Lists can store 100,000s and 1,000,000s of data values. 
#Extend function allows you to append a list onto another list. Append function always adds item at the end of a list.
#Remove elements with remove() funtion. Clear() resests the list. Pop() pops an element off the list always the last one.

lucky_numbers = [4, 15, 8, 26, 16, 42]
friends = ["Kevin", "Karen", "Jim", "Oscar", "Oscar", "Toby"]
friends2 = friends.copy()

friends.extend(lucky_numbers)
friends.append("Creed")
friends.insert(1, "Kelly")
friends.remove("Jim")
#friends.clear()   
lucky_numbers.sort()
#lucky_numbers.reverse()

print(friends)
print(friends.index("Kevin"))
print(friends.count("Oscar"))
print(lucky_numbers)
print(friends2)


