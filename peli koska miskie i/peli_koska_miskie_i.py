import sys,time

name = ""

def vs_print(str):
    for letter in str:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(1)

def s_print(str):
    for letter in str:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(0.5)

def f_print(str):
    for letter in str:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(0.1)

f_print("welcome thy fool to this world of suffering")
f_print(" ")
print("")
f_print("in this world you either die or live, like in any other world")
f_print(" ")
print("")
f_print("what is your gender")
print("")
print("1. male")
print("2. female")
print("3. neither, fuck you")
gender = input()
if gender == "3":
    f_print("well thats rude but i apologize for assuming")

f_print(" ")
print("")
f_print("how old are you")
print("")
age = int(input)
if age < 12:
    f_print("arent you kinda young for this?")
    f_print(" ")
    print("")
    f_print("well have fun kiddo")
elif age < 12:
    f_print("so old, soon youre even about to die")
else:
    f_print("is giving me a number so hard")

f_print(" ")
print("")
f_print("provide me your name")
print("")
name = input()
print("")
if name == "no":
    name = "sylvia"
    f_print("well thats a dick move")
    f_print(" ")
    print("")
    f_print("your name is")
    print("")
    vs_print(name)
    f_print(" ")
else:
    f_print(name)
    f_print("didnt know there was anyone called like that, sounds kinda dumb if im honest")
    f_print(" ")
    f_print("well whatever")
f_print(" ")
print("")
f_print("")