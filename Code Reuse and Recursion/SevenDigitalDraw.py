#!/usr/bin/env python
# -*- coding: utf-8 -*- 
import turtle,time,pytz     #绘制七段数码管
def drawGap():  #绘制数码管间隔
    turtle.penup()
    turtle.fd(5)
def drawLine(draw): #绘制单个数码管
    drawGap()
    turtle.pendown() if draw else turtle.penup()
    turtle.fd(40)
    drawGap()
    turtle.right(90)

def drawDigit(digit):   #根据数字绘制7段数码管
    drawLine(True) if digit in [2, 3, 4, 5, 6, 8, 9] else drawLine(False)
    drawLine(True) if digit in [0, 1, 3, 4, 5, 6, 7, 8, 9] else drawLine(False)
    drawLine(True) if digit in [0, 2, 3, 5, 6, 8, 9] else drawLine(False)
    drawLine(True) if digit in [0, 2, 6, 8] else drawLine(False)
    turtle.left(90)
    drawLine(True) if digit in [0, 4, 5, 6, 8, 9] else drawLine(False)
    drawLine(True) if digit in [0, 2, 3, 5, 6, 7, 8, 9] else drawLine(False)
    drawLine(True) if digit in [0, 1, 2, 3, 4, 7, 8, 9] else drawLine(False)
    turtle.left(180)
    turtle.penup()
    turtle.fd(20)
def drawDate(date):
    turtle.pencolor("red")
    for i in date:
        if i == '-':
            turtle.write('年',font=("Arial",18,"normal"))
            turtle.pencolor("green")
            turtle.fd(40)
        elif i == '=':
            turtle.write('月', font=("Arial", 18, "normal"))
            turtle.pencolor("blue")
            turtle.fd(40)
        elif i == '+':
            turtle.write('日', font=("Arial", 18, "normal"))
            turtle.fd(40)
        elif i == ':':
            turtle.write(':', font=("Arial", 18, "normal"))
            turtle.fd(40)
        else:
            drawDigit(eval(i))
def main():

    turtle.setup(1600, 350, 200, 200)
    turtle.penup()
    turtle.speed(10)
    turtle.fd(-500)
    turtle.pensize(5)
    #drawDate("1994-01=17+")
    drawDate(time.strftime('%Y-%m=%d+%H:%M:%S',time.localtime()))  #打印系统时间
    turtle.hideturtle()
    turtle.done()

main()#测试主函数
