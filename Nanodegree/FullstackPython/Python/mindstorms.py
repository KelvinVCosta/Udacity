#!/usr/bin/python
#coding: utf-8
import turtle

def draw_square(turtle):
    for x in range(0, 4):
        turtle.forward(100)
        turtle.right(90)

def draw_circle_with_squares(brad, vezes, graus):
    for x in range (0, vezes):
        draw_square(brad)
        brad.right(graus)

brad = turtle.Turtle()
brad.shape("turtle")
brad.color("green")
brad.pencolor("black")
brad.speed(0)
window = turtle.Screen()
window.bgcolor("white")
draw_circle_with_squares(brad, 45, 8)
brad.right(90)
brad.forward(300)
window.exitonclick()

#Possiveis
#45,8 **
#30,12
#20,18 **
