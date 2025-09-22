#TurtleGraphics.py
#Name: Macy Dubes
#Date: 9/21/25
#Assignment: Lab 4

import turtle #needed generally but not in CodeHS
hideturtle() #hides the default turtle in CodeHS

def drawSquare(myTurtle, size):
    for i in range(4):
        myTurtle.forward(size)
        myTurtle.right(90)
def drawPolygon(myTurtle, sides):
    for s in range (sides):
        myTurtle.forward(50)
        myTurtle.left(360/sides)

def fillCorner(ralph, corner):
    drawSquare(ralph, 100)
    
    if corner == 1:
        ralph.begin_fill()
        drawSquare(ralph, 50)
        ralph.end_fill()
    elif corner == 2:
        ralph.forward(50)
        ralph.begin_fill()
        drawSquare(ralph, 50)
        ralph.end_fill()
    elif corner == 3:
        ralph.right(90)
        ralph.forward(50)
        ralph.right(270)
        ralph.begin_fill()
        drawSquare(ralph, 50)
        ralph.end_fill()
    elif corner == 4:
        ralph.forward(100)
        ralph.right(90)
        ralph.forward(50)
        ralph.begin_fill()
        drawSquare(ralph, 50)
        ralph.end_fill()
def squaresInSquares(miley, squares):
    maxSize = 200
    shrink = maxSize / squares
    size = maxSize
    for n in range (squares):
        drawSquare(miley, size)
        miley.penup()
        miley.right(90)
        miley.forward(shrink / 2)
        miley.left(90)
        miley.forward(shrink / 2)
        miley.pendown()
        size -= shrink
        
        
        
    
def main():
    myTurtle = turtle.Turtle()
    
    
    # drawPolygon(myTurtle, 5) #draws a pentagon
    # drawPolygon(myTurtle, 8) #draws an octogon

    # fillCorner(myTurtle, 2) #draws a square with top right corner filled in.
    # fillCorner(myTurtle, 4) #draws a square bottom left corner filled in.

    # squaresInSquares(myTurtle, 6) #draws 5 concentric squares
    # squaresInSquares(myTurtle, 3) #draws 3 concentric squares


main()
