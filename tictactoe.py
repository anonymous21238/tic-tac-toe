''' Tic Tac Toe game mini project
    made by:-
    1. Aakash Agarwal (2021222)
    2. Aryesh Shakya (2021238)'''

import turtle
import time
# from playsound import playsound


wn=turtle.Screen()
wn.screensize(canvwidth=500, canvheight=500)


t=turtle.Turtle()
global l 
l=[]

def instructions():
    t.speed(1)  
    wn.bgcolor("light blue")
    t.penup()
    t.goto(-350, 100)
    t.write("Instructions:-", font=("Verdana", 18, "normal"))
    t.goto(-350, 70)
    t.write("Key bindings for player 1:- [a, b, c, d, e, f, g, h, i]", font=("Verdana", 18, "normal"))
    t.goto(-350, 40)
    t.write("Key bindings for player 2:- [1, 2, 3, 4, 5, 6, 7, 8, 9]", font=("Verdana", 18, "normal"))
    t.goto(-350, 10)
    t.write("Boxes corresponding to keys binded will be visible on the grid!", font=("Verdana", 16, "normal"))
    t.goto(150, -50)
    t.write("Game made by:-", font=("Verdana", 10, "normal"))
    t.goto(150, -70)
    t.write("Aakash Agarwal (2021222)", font=("Beau Rivage", 10, "normal"))
    t.goto(150, -90)
    t.write("Aryesh Shakya (2021238)", font=("Beau Rivage", 10, "normal"))
    t.goto(-200, -150)
    t.write("Press 'space' to continue", font=("Verdana", 22, "normal"))

def checker(l):
    if len(l)==1:
        pass
    elif l[-1].isdigit() and l[-2].isdigit():
        time.sleep(1)
        t.clear()
        wn.bgcolor("black")
        t.penup()
        t.goto(-150, 0)
        t.color("red")
        # playsound('Gameover.mp3')
        t.write("It was not your turn!!!", font=("Verdana", 20, "normal"))
        time.sleep(1)
        exit()
    elif l[-1].isalpha() and l[-2].isalpha():
        time.sleep(1)
        t.clear()
        wn.bgcolor("black")
        t.penup()
        t.goto(-150, 0)
        t.color("red")
        # playsound('Gameover.mp3')
        t.write("It was not your turn!!!", font=("Verdana", 20, "normal"))
        time.sleep(1)
        exit()

def winner():
    win=0
    if '1' in l and '2' in l and '3' in l:
        win=1
    elif '4' in l and '5' in l and '6' in l:
        win=1
    elif '7' in l and '8' in l and '9' in l:
        win=1
    elif '1' in l and '4' in l and '7' in l:
        win=1
    elif '2' in l and '5' in l and '8' in l:
        win=1
    elif '3' in l and '6' in l and '9' in l:
        win=1
    elif '1' in l and '5' in l and '9' in l:
        win=1
    elif '3' in l and '5' in l and '7' in l:
        win=1
    elif 'a' in l and 'b' in l and 'c' in l:
        win=2
    elif 'd' in l and 'e' in l and 'f' in l:
        win=2
    elif 'g' in l and 'h' in l and 'i' in l:
        win=2
    elif 'a' in l and 'd' in l and 'g' in l:
        win=2
    elif 'b' in l and 'e' in l and 'h' in l:
        win=2
    elif 'c' in l and 'f' in l and 'i' in l:
        win=2
    elif 'a' in l and 'e' in l and 'i' in l:
        win=2
    elif 'c' in l and 'e' in l and 'g' in l:
        win=2
    if win==1:
        time.sleep(1)
        t.goto(-250,0)
        t.color("white")
        t.clear()
        wn.bgcolor("black")
        # playsound('Gameover.mp3')
        t.write("Player 2 is the winner! (Player with X)", font=("Verdana", 20, "normal"))
    elif win==2:
        time.sleep(1)
        t.goto(-250,0)
        t.color("white")
        t.clear()
        wn.bgcolor("black")
        # playsound('Gameover.mp3')
        t.write("Player 1 is the winner! (Player with O)", font=("Verdana", 20, "normal"))
    elif len(l)==9:
        time.sleep(1)
        t.goto(-150,0)
        t.color("white")
        t.clear()
        wn.bgcolor("black")
        # playsound('Gameover.mp3')
        t.write("The game is drawn!!", font=("Verdana", 20, "normal"))
    else:
        pass

def grid():
    t.speed(5)
    time.sleep(1)
    t.clear()
    wn.bgcolor("light green")
    t.penup()
    t.goto(-150, 150)
    t.pendown()
    t.forward(300)
    t.right(90)
    t.forward(300)
    t.right(90)
    t.forward(300)
    t.right(90)
    t.forward(300)
    t.penup()
    t.goto(-50, 150)
    t.right(180)
    t.pendown()
    t.forward(300)
    t.penup()
    t.goto(50, -150)
    t.right(180)
    t.pendown()
    t.forward(300)
    t.penup()
    t.goto(150, 50)
    t.left(90)
    t.pendown()
    t.forward(300)
    t.goto(-150, -50)
    t.right(180)
    t.forward(300)
    t.left(45)
    t.penup()
    t.goto(-135, 135)
    t.write("a, 1", font=("Verdana", 8, "normal"))
    t.goto(-35, 135)
    t.write("b, 2", font=("Verdana", 8, "normal"))
    t.goto(65, 135)
    t.write("c, 3", font=("Verdana", 8, "normal"))
    t.goto(-135, 35)
    t.write("d, 4", font=("Verdana", 8, "normal"))
    t.goto(-35, 35)
    t.write("e, 5", font=("Verdana", 8, "normal"))
    t.goto(65, 35)
    t.write("f, 6", font=("Verdana", 8, "normal"))
    t.goto(-135, -65)
    t.write("g, 7", font=("Verdana", 8, "normal"))
    t.goto(-35, -65)
    t.write("h, 8", font=("Verdana", 8, "normal"))
    t.goto(65, -65)
    t.write("i, 9", font=("Verdana", 8, "normal"))

def one():
    t.color("red")
    t.width(5)
    l.append('1')
    checker(l)
    t.penup()
    t.goto(-135, 135)
    t.right(90)
    t.pendown()
    # playsound('Move.mp3')
    t.forward(100)
    t.penup()
    t.goto(-135, 64.29)
    t.left(90)
    t.pendown()
    t.forward(100)
    winner()

def two():
    t.color("red")
    t.width(5)
    l.append('2')
    checker(l)
    t.penup()
    t.goto(-35, 135)
    t.right(90)
    t.pendown()
    # playsound('Move.mp3')
    t.forward(100)
    t.penup()
    t.goto(-35, 64.29)
    t.left(90)
    t.pendown()
    t.forward(100)
    winner()

def three():
    t.color("red")
    t.width(5)
    l.append('3')
    checker(l)
    t.penup()
    t.goto(65, 135)
    t.right(90)
    t.pendown()
    # playsound('Move.mp3')
    t.forward(100)
    t.penup()
    t.goto(65, 64.29)
    t.left(90)
    t.pendown()
    t.forward(100)
    winner()

def four():
    t.color("red")
    t.width(5)
    l.append('4')
    checker(l)
    t.penup()
    t.goto(-135, 35)
    t.right(90)
    t.pendown()
    # playsound('Move.mp3')
    t.forward(100)
    t.penup()
    t.goto(-135, -35.71)
    t.left(90)
    t.pendown()
    t.forward(100)
    winner()

def five():
    t.color("red")
    t.width(5)
    l.append('5')
    checker(l)
    t.penup()
    t.goto(-35, 35)
    t.right(90)
    t.pendown()
    # playsound('Move.mp3')
    t.forward(100)
    t.penup()
    t.goto(-35, -35.71)
    t.left(90)
    t.pendown()
    t.forward(100)
    winner()

def six():
    t.color("red")
    t.width(5)
    l.append('6')
    checker(l)
    t.penup()
    t.goto(65, 35)
    t.right(90)
    t.pendown()
    # playsound('Move.mp3')
    t.forward(100)
    t.penup()
    t.goto(65, -35.71)
    t.left(90)
    t.pendown()
    t.forward(100)
    winner()

def seven():
    t.color("red")
    t.width(5)
    l.append('7')
    checker(l)
    t.penup()
    t.goto(-135, -65)
    t.right(90)
    t.pendown()
    # playsound('Move.mp3')
    t.forward(100)
    t.penup()
    t.goto(-135, -135.71)
    t.left(90)
    t.pendown()
    t.forward(100)
    winner()

def eight():
    t.color("red")
    t.width(5)
    l.append('8')
    checker(l)
    t.penup()
    t.goto(-35, -65)
    t.right(90)
    t.pendown()
    # playsound('Move.mp3')
    t.forward(100)
    t.penup()
    t.goto(-35, -135.71)
    t.left(90)
    t.pendown()
    t.forward(100)
    winner()

def nine():
    t.color("red")
    t.width(5)
    l.append('9')
    checker(l)
    t.penup()
    t.goto(65, -65)
    t.right(90)
    t.pendown()
    # playsound('Move.mp3')
    t.forward(100)
    t.penup()
    t.goto(65, -135.71)
    t.left(90)
    t.pendown()
    t.forward(100)
    winner()

def c1():
    t.color("blue")
    t.width(5)
    l.append('a')
    checker(l)
    t.penup()
    t.goto(-80, 72.29)
    t.pendown()
    # playsound('Move.mp3')
    t.circle(30)
    winner()

def c2():
    t.color("blue")
    t.width(5)
    l.append('b')
    checker(l)
    t.penup()
    t.goto(20, 72.29)
    t.pendown()
    # playsound('Move.mp3')
    t.circle(30)
    winner()

def c3():
    t.color("blue")
    t.width(5)
    l.append('c')
    checker(l)
    t.penup()
    t.goto(120, 72.29)
    t.pendown()
    # playsound('Move.mp3')
    t.circle(30)
    winner()

def c4():
    t.color("blue")
    t.width(5)
    l.append('d')
    checker(l)
    t.penup()
    t.goto(-80, -25.71)
    t.pendown()
    # playsound('Move.mp3')
    t.circle(30)
    winner()

def c5():
    t.color("blue")
    t.width(5)
    l.append('e')
    checker(l)
    t.penup()
    t.goto(20, -25.71)
    t.pendown()
    # playsound('Move.mp3')
    t.circle(30)
    winner()

def c6():
    t.color("blue")
    t.width(5)
    l.append('f')
    checker(l)
    t.penup()
    t.goto(120, -25.71)
    t.pendown()
    # playsound('Move.mp3')
    t.circle(30)
    winner()

def c7():
    t.color("blue")
    t.width(5)
    l.append('g')
    checker(l)
    t.penup()
    t.goto(-80, -125.71)
    t.pendown()
    # playsound('Move.mp3')
    t.circle(30)
    winner()

def c8():
    t.color("blue")
    t.width(5)
    l.append('h')
    checker(l)
    t.penup()
    t.goto(20, -125.71)
    t.pendown()
    # playsound('Move.mp3')
    t.circle(30)
    winner()

def c9():
    t.color("blue")
    t.width(5)
    l.append('i')
    checker(l)
    t.penup()
    t.goto(120, -125.71)
    t.pendown()
    # playsound('Move.mp3')
    t.circle(30)
    winner()

instructions()

wn.listen()
wn.onkeypress(grid, "space")
wn.onkeypress(one, "1")
wn.onkeypress(two, "2")
wn.onkeypress(three, "3")
wn.onkeypress(four, "4")
wn.onkeypress(five, "5")
wn.onkeypress(six, "6")
wn.onkeypress(seven, "7")
wn.onkeypress(eight, "8")
wn.onkeypress(nine, "9")   
wn.onkeypress(c1, "a")
wn.onkeypress(c2, "b")
wn.onkeypress(c3, "c")
wn.onkeypress(c4, "d")
wn.onkeypress(c5, "e")
wn.onkeypress(c6, "f")
wn.onkeypress(c7, "g")
wn.onkeypress(c8, "h")
wn.onkeypress(c9, "i")
turtle.done()