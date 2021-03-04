circleSize = 130
selectorX = 200

One = False
Two = False
Three = False
Four = False
Five = False
Six = False
Seven = False

Drop = False


def setup():
    size(1500, 1200)
    background(255)
    noStroke()
    global selectorX, circleSize, One, Two, Three, Four, Five, Six, Seven, Drop

        
def draw():
    global selectorX, circleSize, One, Two, Three, Four, Five, Six, Seven, Drop
    
    gameboard()

    if One:
        background(255)
        gameboard()
        fill(255,0,0)
        player1 = ellipse(200, 100, circleSize, circleSize)
        One = False

    elif Two:
        background(255)
        gameboard()
        fill(255,0,0)
        player1 = ellipse(380, 100, circleSize, circleSize)
        Two = False
    
    elif Three:
        background(255)
        gameboard()
        fill(255,0,0)
        player1 = ellipse(560, 100, circleSize, circleSize)
        Three = False
        
    elif Four:
        background(255)
        gameboard()
        fill(255,0,0)
        player1 = ellipse(740, 100, circleSize, circleSize)
        Four = False
        
    elif Five:
        background(255)
        gameboard()
        fill(255,0,0)
        player1 = ellipse(920, 100, circleSize, circleSize)
        Five = False
        
    elif Six:
        background(255)
        gameboard()
        fill(255,0,0)
        player1 = ellipse(1100, 100, circleSize, circleSize)
        Six = False
        
    elif Seven:
        background(255)
        gameboard()
        fill(255,0,0)
        player1 = ellipse(1280, 100, circleSize, circleSize)
        Seven = False
        
    #elif Drop:
        #background(255)
        #gameboard()
        #Drop = False


def gameboard():
    fill(18, 7, 178) #blue
    rect(100, 200, width-200, height-200, 20)
    #outline of gameboard holes
    for y in range(300, height, 160):
        for x in range(200, width-200, 180):
            stroke(18, 7, 130)
            strokeWeight(5)
            fill(18, 7, 178) #lighter blue
            ellipse(x, y, circleSize*1.15, circleSize*1.15)
    #gameboard holes
    for y in range(300, height, 160):
        for x in range(200, width-200, 180):
            noStroke()
            fill(255) #white
            ellipse(x, y, circleSize, circleSize)


def keyPressed():
    global selectorX, circleSize, player1, One, Two, Three, Four, Five, Six, Seven, Drop
    
    if key == '1':
        One = True
    if key == '2':
        Two = True
    if key == '3':
        Three = True
    if key == '4':
        Four = True
    if key == '5':
        Five = True
    if key == '6':
        Six = True
    if key == '7':
        Seven = True
        
    #if key == ' ':
        #Drop = True
