# Layering with Geometrics
# Written by Michelle Ma
# Inspired by Jenean Morrison
# http://adobe.tumblr.com/post/110840747141/layering-with-geometrics
# Color palettes can be found at Adobe Color CC
# https://color.adobe.com/create/color-wheel/
# PyProcessing Reference
# http://py.processing.org/reference/

def setup(): #called once at the beginning of the program

    #setting functions that are applied to every piece of code until overwritten
    size(600, 600, P2D) #sets width and height variables, P2D allows for shapes
    smooth()            #helps with smoothing the edges
    rectMode(CENTER)    #changes mode of rect function to centered
    frameRate(12)       #changes the frame rate of draw() from 60 frames per second
    
    #make a palette list so we have some predefined colors
    global palette
    palette = [color(15, 15, 75),   #dark blue
               color(35, 45, 100), #light blue
               color(230, 0, 140),  #magenta
               color(235, 175, 0),  #gold
               color(255)]          #white
    
    #default settings
    changeOpacity(30)
    changeFillColor(255)
    changeStrokeColor(255)
    changeStrokeWeight(1)
    changeFunction(drawCircle) #for the brush
    
    background(palette[0])     #sets the background to white
    
    #draw only once in setup
    #iterate through all but the first color indices
    for col in xrange(1,len(palette)):
        changeFillColor(palette[col])
        
        #make y position a function of the color index
        y = (col - 0.5) * float(height)/(len(palette)-1)
        for x in xrange(0, width, 10):
            #call the function across the width of the canvas
            drawMultiple(drawSquare, x, y, 50, 1, 100)
    
def draw(): #called at 60 frames per second, allows for interaction
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

#     for col in xrange(1,len(palette)):
#         changeFillColor(palette[col])
#         y = (col - 0.5) * float(height)/(len(palette)-1)
#         for x in xrange(0, width, 10):
#             drawMultiple(drawSquare, x, y, 50 * sin(TWO_PI/frameRate), 1, 50)

############# Draw Multiple Functions #############

def drawMultiple(function, x, y, r, amount, randomness):
    #randomness can be replaced with noise or a sinusoidal function
    for i in xrange(amount):
        x2 = x + random(-randomness, randomness)
        y2 = y + random(-randomness, randomness)
        r2 = r + random(-randomness, randomness)/3.0
        #the '/3.0' is just a preference of mine...
        function(x2, y2, r2)

########### Change Setting Functions ###########
# We kind of have to use global variable for specially
# defined shapes.
# If you have more keyboard or mouse interactions,
# you will probably need more global variables to
# control overall settings

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

# Just for the mouse interaction
def changeFunction(function):
    global currentFunction
    currentFunction = function

############# Draw Shape Functions #############
# The goal is to get them all to follow the same format

def drawCircle(x, y, r):
    ellipse(x, y, 2*r, 2*r)

def drawConcentricCircle(x, y, r):
    ellipse(x, y, 2*r, 2*r)
    ellipse(x, y, 1.25*r, 1.25*r)
    ellipse(x, y, .75*r, .75*r)

def drawSquare(x, y, r):
    rect(x, y, 2*r, 2*r)
    
def drawHexagon(x, y, r):
    sz = r/2.0 * sqrt(3.0)
    h = createShape()
    h.beginShape()
    h.fill(currentFillColor, currentOpacity)
    h.stroke(currentStrokeColor)
    h.strokeWeight(currentStrokeWeight)
    h.vertex(-r/2.0, sz)
    h.vertex(r/2.0, sz)
    h.vertex(r, 0)
    h.vertex(r/2.0, -sz)
    h.vertex(-r/2.0, -sz)
    h.vertex(-r, 0)
    h.endShape(CLOSE)
    shape(h, x, y)

########### Keyboard Mouse Interactions ###########

def keyPressed():
    print(key) #key is a string
    
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
    elif (keyCode == UP):
        changeOpacity(currentOpacity + 10)
        if (currentOpacity > 250):
            changeOpacity(250)
        print currentOpacity
    elif (keyCode == DOWN):
        changeOpacity(currentOpacity - 10)
        if (currentOpacity < 10):
            changeOpacity(10)
        print currentOpacity

def mousePressed():
    changeFillColor(currentFillColor)
    drawMultiple(currentFunction, mouseX, mouseY, 10, 20, 50)
