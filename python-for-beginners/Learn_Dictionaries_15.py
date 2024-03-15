#Learn Python - Full Course for Beginners freeCodeCamp.org Youtube
#Lesson Dictionaries: is a special data structure in Python that allows us to store info in key:value pairs. Ex. convert 3 letter 
#month name into full month name.

monthConversions= {
    "Jan": "January",
    "Feb": "February",
    "Mar": "March",
    "Apr": "April",
    "May": "May",
    "Jun": "June",
    "Jul": "July",
    "Aug": "August",
    "Sep": "September",
    "Oct": "October",
    "Nov": "November",
    "Dec": "December",
}

print(monthConversions["Nov"])
print(monthConversions.get("Dec"))