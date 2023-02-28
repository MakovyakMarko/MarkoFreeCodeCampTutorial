def say_hi():
    print("Hello User")

say_hi()

print("Top")
say_hi()
print("Bottom")

def say_my_name(name):
    print("Hello " + name)

say_my_name("Marko")
say_my_name("Not Marko")


def say_my_name_and_age(name, age):
    print("Hello " + name + ", you are " + age)

say_my_name_and_age("Marko", "32")
say_my_name_and_age("Not Marko", "Not 31")

def input_say_my_name_and_age(name, age):
    print("Hello " + name + ", you are " + age)
your_name = input("Enter your name: ")
your_age = input("Enter your age: ")
input_say_my_name_and_age(your_name, your_age)

def say_hi1(name,age):
    print("Hello " + name + ", you are " + str(age))
my_name = input("Enter your name: ")
my_age = input("Enter your age: ")
say_hi1(my_name, my_age)