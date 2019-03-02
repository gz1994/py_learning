#!/usr/bin/env python
# -*- coding: utf-8 -*-
#Kcoh
#Kcohraw.py
import turtle
def kcoh(size,n):    #size:线段的长度  n:阶数
    if n == 0:
        turtle.fd(size)
    else :
        for angle in [0, 60, -120, 60]:
            turtle.left(angle)
            kcoh(size/3,n-1)
def main():
    turtle.setup(600,600)
    turtle.penup()
    turtle.speed(2)
    turtle.goto(-200,100)
    turtle.pendown()
    turtle.pensize(2)
    level = 3       #三阶科赫雪花，阶数
    kcoh(400,level)
    turtle.right(120)
    kcoh(400, level)
    turtle.right(120)
    kcoh(400, level)
    turtle.right(120)
    turtle.hideturtle()
    turtle.done()

main()