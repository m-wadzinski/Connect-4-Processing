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

#Menu Variables
Menu = True
P1vCpu = False
P1vP2 = False


def setup():
    size(1500, 1200)
    background(255)
    noStroke()
    global selectorX, circleSize, One, Two, Three, Four, Five, Six, Seven, Drop, player1

        
def draw():
    global selectorX, circleSize, One, Two, Three, Four, Five, Six, Seven, Drop, player1
    
    
    mode = None
    if Menu:
        while mode not in ("1", "2"):
            mode = input("Press 1 for P1vCPU Press 2 for P1vP2: ")
            if mode == "1":
                P1vCpu = True
                break
            elif mode == "2":
                P1vP2 = True
                break
            else:
                print("Please select a game mode")
                continue
    
    
    elif P1vP2:
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
    
    #elif P1vCPU:

def gameboard():
    fill(18, 7, 178) #blue
    stroke(18, 7, 130)
    strokeWeight(5)
    quad(105, 205, 130, 180, 1370, 180, 1395, 205)
    fill(255)
    noStroke()
    for x in range(135, 1350, 180):
        quad(x, 195, x + 15, 185, x + 115, 185, x + 130, 195)
    fill(18, 7, 178) #blue
    stroke(18, 7, 130)
    strokeWeight(5)
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
            
#def player1(x, y, s, s):
    #fill(255,0,0)
    #ellipse(x, y, circleSize, circleSize)



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
