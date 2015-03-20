# Layering with Geometrics
# Written by Michelle Ma
# Inspired by Jenean Morrison
# http://adobe.tumblr.com/post/110840747141/layering-with-geometrics
# Color palettes can be found at Adobe Color CC
# https://color.adobe.com/create/color-wheel/
# PyProcessing Reference
# http://py.processing.org/reference/

# For the brush
# Press 0 through len(palette)-1 to change color
# Press 'c' for circles
# Press 'C' for concentric circles
# Press 's' for squares
# Press 'h' for hexagons
# Press DOWN to decrease opacity
# Press UP to increase opacity

def setup(): #called once at the beginning of the program

    #setting functions that are applied to every piece of code until overwritten
    size(600, 600, P2D) #sets width and height variables, P2D allows for shapes
    smooth()            #helps with smoothing the edges
    rectMode(CENTER)    #changes mode of rect function to centered
    frameRate(12)       #changes the frame rate of draw() from 60 frames per second
    
    #make a palette list so we have some predefined colors
    global palette
    palette = [color(35, 45, 100),  #blue
               color(230, 0, 140),  #magenta
               color(235, 175, 0),  #gold
               color(255)]          #white
    
    #default settings
    changeOpacity(30)
    changeFillColor(255)
    changeStrokeColor(255)
    changeStrokeWeight(1)
    changeFunction(drawCircle) #for the brush
    
    #make the background a random color
    background(color(random(255), random(255), random(255)))
    drawWithRandomColors(drawTriangle, 20, 1, 10, 10, 6)
    
#     #make the background white
#     background(255)
#     drawWithGradientColors(drawSquare, 100, 2, 150, 10, 4)

#     #make the background the first palette color
#     background(color(15, 15, 75)) #dark blue
#     drawWithPaletteColors(drawConcentricCircle, 50, 1, 150, 10, 4)
    
def draw(): #called at the frame rate, allows for interaction and animation
    pass
    
#     fill(palette[0])
    
#     ellipse(width/2, height/2, 100, 100) #using width and height variables
    
#     ellipse(mouseX, mouseY, 100, 100) #using mouseX and mouseY variables
    
#     triangle(mouseX, mouseY, mouseX+10, mouseY, mouseX, mouseY+10)
    
#     if (mousePressed):
#         drawHexagon(mouseX, mouseY, 100, 50)
    
#     #refreshing background
#     fill(palette[0], 20)
#     rect(width/2, height/2, width, height)
# 
#     drawWithPaletteColors(drawSquare, 50 * sin(TWO_PI/frameRate), 1, 50, 10)

############# Draw Everything Functions #############

def drawWithRandomColors(function, r, amount, randomness, xStep, numRows):
    #iterate through the number of rows
    for row in xrange(1, numRows+1):
        changeFillColor(color(random(255), random(255), random(255)))
        
        #make y position a function of the row number
        y = (row - 0.5) * float(height)/numRows
        
        #call the function across the width of the canvas with a step of xStep
        for x in xrange(0, width, xStep):
            drawMultiple(function, x, y, r, amount, randomness)
            
def drawWithGradientColors(function, r, amount, randomness, xStep, numRows):
    colorChange = 200.0/numRows
    #iterate through the number of rows
    for row in xrange(1, numRows+1):
        redValue = colorChange * row
        greenValue = 255 - redValue
        blueValue = 50
        changeFillColor(color(redValue, blueValue, greenValue))
        
        #make y position a function of the row number
        y = (row - 0.5) * float(height)/numRows
        
        #call the function across the width of the canvas with a step of xStep
        for x in xrange(0, width, xStep):
            drawMultiple(function, x, y, r, amount, randomness)

def drawWithPaletteColors(function, r, amount, randomness, xStep, numRows):
    #iterate through the colors in the palette except the
    #background color at palette[0]
    for col in xrange(1, numRows+1):
        changeFillColor(palette[col%len(palette)])
        
        #make y position a function of the color index
        y = (col - 0.5) * float(height)/numRows
        
        #call the function across the width of the canvas with a step of xStep
        for x in xrange(0, width, xStep):
            drawMultiple(function, x, y, r, amount, randomness)

############# Draw Multiple Functions #############

def drawMultiple(function, x, y, r, amount, randomness):
    for i in xrange(amount):
        x2 = x + random(-randomness, randomness)
        y2 = y + random(-randomness, randomness)
        r2 = r + random(-randomness, randomness)/3.0 #the '/3.0' is just a preference
        function(x2, y2, r2)

########### Change Setting Functions ###########
# We kind of have to use global variable for specially
# defined shapes like the hexagon.
# If you have more keyboard or mouse interactions,
# you will probably need more global variables to
# control other settings like randomness or amount
# of shapes drawn at a time

def changeOpacity(opacity):
    global currentOpacity
    currentOpacity = opacity
    
def changeFillColor(col):
    global currentFillColor
    currentFillColor = col
    fill(currentFillColor, currentOpacity)

def changeStrokeColor(col):
    global currentStrokeColor
    currentStrokeColor = col
    stroke(currentStrokeColor)

def changeStrokeWeight(weight):
    global currentStrokeWeight
    currentStrokeWeight = weight
    strokeWeight(currentStrokeWeight)

# Just for the keyboard/mouse interactions
def changeFunction(function):
    global currentFunction
    currentFunction = function

############# Draw Shape Functions #############
# In order to format all of the shape primitives
# in the same way

def drawCircle(x, y, r):
    ellipse(x, y, 2*r, 2*r)

def drawConcentricCircle(x, y, r):
    ellipse(x, y, 2*r, 2*r)
    ellipse(x, y, 1.25*r, 1.25*r)
    ellipse(x, y, .75*r, .75*r)

def drawSquare(x, y, r):
    rect(x, y, 2*r, 2*r)

def drawTriangle(x, y, r):
    triangle(x, y, x+r, y, x, y-r)
    
def drawHexagon(x, y, r):
    sz = r/2.0 * sqrt(3.0)
    h = createShape()
    h.beginShape()
    h.vertex(-r/2.0, sz)
    h.vertex(r/2.0, sz)
    h.vertex(r, 0)
    h.vertex(r/2.0, -sz)
    h.vertex(-r/2.0, -sz)
    h.vertex(-r, 0)
    h.endShape(CLOSE)
    shape(h, x, y)

########### Keyboard Mouse Interactions ###########
# Optional: if you want to be able to click and
# draw things on the screen for a more natural touch

def keyPressed():
    print(key) #key is a string
    
    if (key == CODED):
        if (keyCode == UP):
            changeOpacity(currentOpacity + 10)
            if (currentOpacity > 250):
                changeOpacity(250)
            print currentOpacity
        elif (keyCode == DOWN):
            changeOpacity(currentOpacity - 10)
            if (currentOpacity < 10):
                changeOpacity(10)
            print currentOpacity
    else:
        if (key == 'c'):
            changeFunction(drawCircle)
        elif (key == 'C'):
            changeFunction(drawConcentricCircle)
        elif (key == 's'):
            changeFunction(drawSquare)
        elif (key == 'h'):
            changeFunction(drawHexagon)
        elif (key.isdigit() and 0 <= int(key) < len(palette)): 
            changeFillColor(palette[int(key)])
    
def mousePressed():
    changeFillColor(currentFillColor)
    drawMultiple(currentFunction, mouseX, mouseY, 10, 20, 50)
