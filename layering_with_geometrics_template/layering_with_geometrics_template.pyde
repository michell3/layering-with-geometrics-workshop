# Layering with Geometrics
# Template Code
# Color palettes can be found at Adobe Color CC
# https://color.adobe.com/create/color-wheel/
# PyProcessing Reference
# http://py.processing.org/reference/

def setup(): #called once at the beginning of the program

    #set the size of the canvas in pixels
    size(<WIDTH>, <HEIGHT>)
    
    #make a background color
    background(color(<REDVALUE>, <GREENVALUE>, <BLUEVALUE>))
    
    #call a function that can draw the shapes using random colors,
    #gradient colors, or palette (hard-coded) colors
    drawWith?????Colors(<FUNCTIONNAME>, <RADIUS>, <AMOUNT>,
                        <RANDOMNESS>, <XSTEP>, <NUMROWS>)
    
def draw():
    pass

def drawWith?????Colors(function, radius, amount, randomness, xStep, numRows):
    
    #iterate through the number of rows
    for row in xrange(<FIRSTROW>, <LASTROW>):
        
        #set the fill color of the shapes
        fill(color(<REDVALUE>, <GREENVALUE>, <BLUEVALUE>))
        
        #make y position a function of the row number
        y = <YVALUE>
        
        #call the function across the width of the canvas with a step of xStep
        for x in xrange(<FIRSTPIXEL>, <LASTPIXEL>, <STEP>):
            drawMultiple(function, x, y, r, amount, randomness)

def drawMultiple(function, x, y, radius, amount, randomness):
    for i in xrange(<AMOUNTOFSHAPES>):
        x2 = <XVALUE>
        y2 = <YVALUE>
        r2 = <RADIUSVALUE>
        function(x2, y2, r2)

def drawCircle(x, y, r):
    ellipse(<XVALUE>, <YVALUE>, <WIDTH>, <HEIGHT>)

def drawSquare(x, y, r):
    rect(<XVALUE>, <YVALUE>, <WIDTH>, <HEIGHT>)

def drawTriangle(x, y, r):
    triangle(<X1>, <Y1>, <X2>, <Y2>, <X3>, <Y3>)

def keyPressed():
    print(key)
    #case on the character value of key in order to draw something

def mousePressed():
    drawMultiple(<FUNCTIONNAME>, <XVALUE>, <YVALUE>, <RADIUS>,
                 <AMOUNT>, <RANDOMNESS>)
