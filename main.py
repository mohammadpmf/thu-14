from turtle import *
import random

def check():
    if "?" not in guess:
        return "end"

def correct(c, answer):
    n = answer.count(c)
    i = answer.index(c)
    guess[i] = c
    for t in range(n-1):
        i=answer.index(c, i+1)
        guess[i] = c
    g = ''.join(guess)
    p1.clear()
    p1.write(g, font=("", 40), align='center')


def f0():
    p2.circle(40)

def f1():
    p2.rt(90)
    p2.fd(75)

def f2():
    p2.rt(90)
    p2.fd(50)

def f3():
    p2.bk(100)

def f4():
    p2.fd(50)
    p2.lt(90)
    p2.fd(50)

def f5():
    pass

def f6():
    pass

def wrong(i):
    if i==0:
        f0()
    elif i==1:
        f1()
    elif i==2:
        f2()
    elif i==3:
        f3()
    elif i==4:
        f4()
    elif i==5:
        f5()
    elif i==6:
        f6()

word_list = ['cat', 'dog', 'cow', 'wolf', 'iguana', 'came', 'cayot', 'rabbit']
answer = random.choice(word_list)
guess = []
for i in answer:
    guess.append('?')
p1 = Pen()
p1.up()
p1.goto(0, 150)
p2 = Pen()
p2.up()
p2.goto(-200, 50)
p2.down()
g = ''.join(guess)
p1.write(g, font=("", 40), align='center')

i=0
while i<7:
    c = textinput("", "Enter a character:")
    while len(c)!=1:
        c = textinput("", "Enter Exactly one single character:")
    if c in answer:
        correct(c, answer)
    else:
        wrong(i)
        i = i+1
    if check()=="end":
        exit()
