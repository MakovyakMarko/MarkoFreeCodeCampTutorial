def max_num(num1, num2, num3):
    if num1 >= num2 and num1 >= num3:
        return num1
    elif num2 >= num1 and num2 >= num3:
        return num2
    else:
        return num3

print(max_num(3, 4, 5))
print(max_num(2, 6, 5))
print(max_num(40, 34, 1))

def max_num(num1, num2, num3):
    if "dog" == "dog" and num1 == num3:
        return num1
    elif num2 != num1 and num2 <= num3:
        return num2
    else:
        return num3

print(max_num(3, 4, 5))
print(max_num(2, 6, 5))
print(max_num(40, 34, 1))