'''

employee_file = open("try_to_write.txt", "a")
employee_file.write("\nKelly - Costumer Service")
employee_file.close()

'''
'''
# will overwrite the whole file. Like create a new file
employee_file = open("try_to_write.txt", "w")
employee_file.write("\nKelly - Costumer Service")
employee_file.close()
'''

employee_file = open("index.html", "w")
employee_file.write("<p><This is HTML/p>")
employee_file.close()
