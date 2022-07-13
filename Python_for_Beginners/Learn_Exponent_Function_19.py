#Learn Python - Full Course for Beginners freeCodeCamp.org Youtube
#Lesson Exponent Function: allows us to take a certain number raise it to a power.

def raise_to_power(base_num, pow_num):
    result = 1
    for index in range(pow_num):
        result = result * base_num
    return result

print(raise_to_power(2, 5))
