#Learn Python - Full Course for Beginners freeCodeCamp.org Youtube
#Lesson 2D Lists & Nested Loops: 

number_grid = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [0]
]

#print(number_grid[2] [2]) #Index starts with 0, row is first then column. 

for row in number_grid:
    for col in row:
        print(col)



