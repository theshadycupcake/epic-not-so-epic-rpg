import sys,time

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
input()
vs_print("in this world you either die or live, like in any other world")
input()
vs_print("provide me your name")
name = input()
s_print(name)
ff_print("didnt know there was anyone called like that, sounds kinda dumb if im honest")