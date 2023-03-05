employee_file = open("trytoread.txt", "r") # read file
'''
open("trytoread.txt", "w") # write file
open("trytoread.txt", "a") # append to file
open("trytoread.txt", "r+") # read and write file
'''

print(employee_file.readable())

# print(employee_file.read())

# print(employee_file.readline())
# print(employee_file.readline())

#print(employee_file.readlines())
for employee in employee_file.readlines():
    print(employee)
employee_file.close()