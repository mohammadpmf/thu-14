from turtle import *
import random

def check():
    if "?" not in guess:
        return "end"
def correct(c, answer):
    pass

def f0():
    p2.circle(40)

def f1():
    p2.rt(90)
    p2.fd(70)
def f2():
    p2.lt(135)
    p2.fd(70)
    p2.bk(70)
def f3():
    p2.lt(90)
    p2.fd(70)
    p2.bk(70)
def f4():
    p2.lt(135)
    p2.fd(70)
def f5():
    p2.lt(45)
    p2.fd(70)
    p2.bk(70)
def f6():
    p2.rt(90)
    p2.fd(70)

    p2.pensize(5)
    p2.color("brown")
    p2.rt(45)
    p2.up()
    p2.fd(60)
    p2.rt(90)
    p2.bk(40)
    p2.down()
    p2.rt(90)
    p2.fd(150)
    p2.bk(150)
    p2.lt(90)
    p2.fd(340)
    p2.rt(90)
    p2.fd(110)
    p2.rt(90)
    p2.fd(30)
    p2.ht()

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
for i in range(len(answer)):
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
print(answer)

for i in range(7):
    c = textinput("", "Enter a character:")
    while len(c)!=1:
        c = textinput("", "Enter Exactly one single character:")
    if c in answer:
        correct(c, answer)
    else:
        wrong(i)
    if check()=="end":
        exit()
done()
