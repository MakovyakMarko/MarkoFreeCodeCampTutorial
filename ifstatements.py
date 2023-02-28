"""
I wake up
If Im hungry
    I eat breakfast

I leave my house
If its cloudy
    I bring an umbrella
otherwise
    I bring sunglasses

Im at a restaurant
If I want meat
    I order a steak
otherwise
If i want pasta
    I order spaghetti & meatballs
otherwise
     I order the salad.
"""
is_male = True
if is_male:
    print("You are a male")

is_male1 = False
if is_male1:
    print("You are a male")
else:
    print("You are not a male")

is_male2 = True
if is_male2:
    print("You are a male")
else:
    print("You are not a male")

is_male3 = True
is_tall= True
if is_male3 or is_tall:
    print("You are a male or tall or both")
else:
    print("You neither male not tall")

is_male4 = False
is_tall1= True
if is_male4 or is_tall:
    print("You are a male or tall or both")
else:
    print("You neither male not tall")

is_male5 = False
is_tall2= False
if is_male5 or is_tall2:
    print("You are a male or tall or both")
else:
    print("You neither male not tall")

is_male6 = False
is_tall3= False
if is_male6 and is_tall3:
    print("You are a tall male")
else:
    print("You either not male or not tall or both")


is_male7 = True
is_tall4= False
if is_male7 and is_tall4:
    print("You are a tall male")
else:
    print("You either not male or not tall or both")


is_male8 = True
is_tall5= True
if is_male8 and is_tall5:
    print("You are a tall male")
else:
    print("You either not male or not tall or both")

is_male9 = True
is_tall6= True
if is_male9 and is_tall6:
    print("You are a tall male")
elif is_male9 and not(is_tall6):
    print("You are a short male")
elif not(is_male9) and is_tall6:
    print("You are not a male but are tall")
else:
    print("You not male and not tall")

is_male10 = False
is_tall7= True
if is_male10 and is_tall7:
    print("You are a tall male")
elif is_male10 and not(is_tall7):
    print("You are a short male")
elif not(is_male10) and is_tall7:
    print("You are not a male but are tall")
else:
    print("You not male and not tall")

is_male11 = True
is_tall8= False
if is_male11 and is_tall8:
    print("You are a tall male")
elif is_male11 and not(is_tall8):
    print("You are a short male")
elif not(is_male11) and is_tall8:
    print("You are not a male but are tall")
else:
    print("You not male and not tall")

is_male12 = False
is_tall9 = False
if is_male12 and is_tall9:
    print("You are a tall male")
elif is_male12 and not(is_tall9):
    print("You are a short male")
elif not(is_male12) and is_tall9:
    print("You are not a male but are tall")
else:
    print("You not male and not tall")
