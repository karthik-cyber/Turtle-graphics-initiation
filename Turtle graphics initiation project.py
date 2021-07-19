# -*- coding: utf-8 -*-
"""
Created on Mon Jul 19 13:24:37 2021

@author: karthik sarikonda
"""

# import turtle
import turtle
 
# defining colors
colors = ['red', 'white', 'green', 'purple', 'blue', 'violet', 'white']
 
# setup turtle pen
t= turtle.Pen()
 
# changes the speed of the turtle
t.speed(200)
 
# changes the background color
turtle.bgcolor("black")
 
# make spiral_web
for x in range(200):
    t.pencolor(colors[x%7]) # setting color
    t.width(x/10000 + 0.5) # setting width
    t.forward(x) # moving forward
    t.left(99) # moving left
 
turtle.done()
t.speed(200)
 
turtle.bgcolor("black") # changes the background color
 
# make spiral_web
for x in range(200):
    t.pencolor(colors[x%7]) # setting color
    t.width(x/10000 + 0.5) # setting width
    t.forward(x) # moving forward
    t.left(99) # moving left
 