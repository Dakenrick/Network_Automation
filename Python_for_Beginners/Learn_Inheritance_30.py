#Learn Python - Full Course for Beginners freeCodeCamp.org Youtube
#An inheritance is when you define a bunch of different functions, attributes and things inside a class.
#then create another class an inherit those functions, attributes and other things into it. 
#Instead of copying and pasting funtions from one class Chef into another class ChineseChef we can inherit the functions with

from Chef import Chef
from ChineseChef import ChineseChef

myChef = Chef()
myChef.make_chicken()

myChineseChef = ChineseChef()
myChineseChef.make_special_dish
myChineseChef.make_fried_rice()