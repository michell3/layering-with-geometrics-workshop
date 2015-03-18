# Layering with Geometrics
# Written by Michelle Ma
# Inspired by Jenean Morrison
# http://adobe.tumblr.com/post/110840747141/layering-with-geometrics
# Color palettes can be found at Adobe Color CC
# https://color.adobe.com/create/color-wheel/
# PyProcessing Reference
# http://py.processing.org/reference/

# For the brush
# Press 0-3 to change color
# Press 'c' for circles
# Press 'C' for concentric circles
# Press 's' for squares
# Press 'h' for hexagons
# Press DOWN to decrease opacity
# Press UP to increase opacity
# Press LEFT to decrease randomness
# Press RIGHT to increase randomness
# Press '[' to decrease radius
# Press ']' to increase radius
# Press '-' to decrease amount
# Press '=' to increase amount

def setup():
    size(600, 600, P2D)
    smooth()
    rectMode(CENTER)
    background(255)
    frameRate(12)
    
    global palette             #for the brush
    palette = [color(15, 15, 75),  #dark blue
               color(230, 0, 140), #magenta
               color(235, 175, 0), #gold
               color(255)]         #white
    
    #default settings
    changeOpacity(50)
    changeFillColor(255)
    changeStrokeColor(255)
    changeStrokeWeight(1)
    changeRadius(20)           #for the brush
    changeAmount(10)           #for the brush
    changeRandomness(50)       #for the brush
    changeFunction(drawCircle) #for the brush
    
    #background drawings
#     background(palette[0])
#     changeStrokeColor(palette[0])
#     forLoopDemo(drawConcentricCircle, 40, 80, 3, 150, 6)

    background(palette[0])
    changeOpacity(80)
    changeStrokeWeight(0)
    rotationDemo(drawHexagon, 40, 80, 30, 10, 8)
    
def draw():
    pass

############# Examples #############

def forLoopDemo(function, r, opacity, amount, randomness, numRows):
    offset = 10
    colorChange = 200.0/numRows
    
    for i in xrange(1, numRows+1):
        newOpacity = float(i)/numRows * opacity
        newR = float(i)/numRows * r
        y = float(i)/numRows * height + offset
        
        changeOpacity(newOpacity)
        changeFillColor(color(colorChange * i, 50, 255 - colorChange * i))
        
        for x in xrange(0, width, 10):
            drawMultiple(function, x, y, newR, amount, randomness)

def rotationDemo(function, r, opacity, amount, randomness, numRows):
    colorChange = 200.0/numRows
    
    for i in xrange(1, numRows+1):
        newR = float(i)/numRows * r
        y = float(i)/numRows * height/2

        changeFillColor(color(colorChange * i, 50, 255 - colorChange * i))

        drawMultipleCircle(function, y, newR, amount, randomness)

############# Draw Multiple Functions #############

def drawMultiple(function, x, y, r, amount, randomness):
    for i in xrange(amount):
        x2 = x + random(-randomness, randomness)
        y2 = y + random(-randomness, randomness)
        r2 = r + random(-randomness, randomness)/3.0
        function(x2, y2, r2)

def drawMultipleCircle(function, y, r, amount, randomness):
    rotateAmount = TWO_PI/amount
    pushMatrix()
    translate(width/2, height/2)
    for i in xrange(amount):
        pushMatrix()
        rotate(rotateAmount * i)
        translate(0, y + random(-randomness, randomness))
        function(0, 0, r + random(-randomness, randomness))
        popMatrix()
    popMatrix()

########### Change Setting Functions ###########

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

def changeRadius(radius):
    global currentRadius
    currentRadius = radius
    
def changeAmount(amount):
    global currentAmount
    currentAmount = amount
    
def changeRandomness(randomness):
    global currentRandomness
    currentRandomness = randomness

def changeFunction(function):
    global currentFunction
    currentFunction = function

############# Draw Shape Functions #############

def drawCircle(x, y, r):
    ellipse(x, y, 2*r, 2*r)

def drawConcentricCircle(x, y, r):
    ellipse(x, y, 2*r, 2*r)
    ellipse(x, y, 1.25*r, 1.25*r)
    ellipse(x, y, .75*r, .75*r)

def drawSquare(x, y, r):
    rect(x, y, 2*r, 2*r)
    
def drawLine(x, y, r):
    line(x, y-r, x, y+r)
    
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
    elif (key == '['):
        changeRadius(currentRadius - 10)
        if (currentRadius < 5):
            changeRadius(5)
        print currentRadius
    elif (key ==']'):
        changeRadius(currentRadius + 10)
        if (currentRadius > 200):
            changeRadius(200)
        print currentRadius
    elif (key == '-'):
        changeAmount(currentAmount - 10)
        if (currentAmount < 1):
            changeAmount(1)
        print currentAmount
    elif (key =='='):
        changeAmount(currentAmount + 10)
        if (currentAmount > 200):
            changeAmount(200)
        print currentAmount
    elif (0 <= int(key) < len(palette)): 
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
    elif (keyCode == LEFT):
        changeRandomness(currentRandomness - 10)
        if (currentRandomness < 5):
            changeRandomness(5)
        print currentRandomness
    elif (keyCode == RIGHT):
        changeRandomness(currentRandomness + 10)
        if (currentRandomness > 200):
            changeRandomness(200)
        print currentRandomness

def mousePressed():
    drawMultiple(currentFunction, mouseX, mouseY,
                 currentRadius, currentAmount, currentRandomness)
