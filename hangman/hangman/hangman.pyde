#hangman
import random
import time
def setup():
    global gamemode, font, hangman, playerName, wrongGuesses, hangmanImage, guessLimit
    gamemode = "startMenu"
    font = loadFont("BradleyHandITC-48.vlw")
    words = getFileInfo("hangmanwords.txt")
    hangmanImage = {0:loadImage("hangman.png"), 1:loadImage("hangman1.png"), 2:loadImage("hangman2.png"), 3:loadImage("hangman3.png"), 4:loadImage("hangman4.png"), 5:loadImage("hangman5.png"), 6:loadImage("hangman6.png")} 
    print(words)
    size(800,600)
    playerName = []
    wrongGuesses = 0
    guessLimit = 7
    
def draw():
    imageMode(CENTER)
    if gamemode == "startMenu":
        startMenu()
    if gamemode == "playerMenu":
        playerMenu()
    if gamemode == "inGame":
        game()

def getFileInfo(fileName):
    file = open(fileName)
    fileInfo = []
    fileText = file.readlines()
    for x in fileText:
        x = x.strip()
        x = x.split(", ")
        fileInfo.append(x)
    print(fileInfo)
    return fileInfo

def startMenu(): #start menu
    background(255)
    textFont(font)
    textAlign(CENTER)
    textSize(48)
    fill(0)
    text("hangman", width/2, height/5)
    if width/2-50 <= mouseX <= width/2+50 and 200 <= mouseY <= 270:
        fill(225)
        text("play", width/2, (height/5)*2)
        fill(0)
    else:
        fill(0)
        text("play", width/2, (height/5)*2)
    if width/2-50 <= mouseX <= width/2+50 and 325 <= mouseY <= 380:
        fill(225)
        text("help", width/2, (height/5)*3)
        fill(0)
    else:
        fill(0)
        text("help", width/2, (height/5)*3)
    if width/2-60 <= mouseX <= width/2+60 and 460 <= mouseY <= 485:
        fill(225)
        text("scores", width/2, (height/5)*4)
        fill(0)
    else:
        fill(0)
        text("scores", width/2, (height/5)*4)
    
def playerMenu(): #where you select number of players and input names
    global minLimit
    background(255)
    minLimit = 3
    textFont(font)
    textAlign(CENTER)
    textSize(48)
    fill(0)
    text("type your name", width/2, height/3)
    text(getPlayerName(), width/2, height/2)
    if width/2-60 <= mouseX <= width/2+60 and 460 <= mouseY <= 485 or len(playerName) <= minLimit:
        fill(225)
        text("begin", width/2, (height/5)*4)
        fill(0)
    else:
        fill(0)
        text("begin", width/2, (height/5)*4)
    if 35 <= mouseX <= 64 and 24 <= mouseY <= 48:
        fill(225)
        text("<", 50, 50)
        fill(0)
    else:
        fill(0)
        text("<", 50, 50)
    
def getPlayerName():
    global curKey, playerName
    curKey = ""
    return str("".join(playerName))
    
def helpMenu(): #help menu
    pass

def scoresMenu(): #scores menu
    pass
    
def game():
    global wrongGuesses
    background(255)
    image(hangmanImage[wrongGuesses], width/2, height/2)

def restart(): #restarts the game
    pass
    
def mousePressed():
    global gamemode, minLimit, wrongGuesses
    print(mouseX, mouseY)
    if gamemode == "startMenu" and mouseButton == LEFT:
        if width/2-50 <= mouseX <= width/2+50 and 200 <= mouseY <= 270:
            gamemode = "playerMenu"
        if width/2-50 <= mouseX <= width/2+50 and 325 <= mouseY <= 380:
            gamemode = "helpMenu"
        if width/2-60 <= mouseX <= width/2+60 and 460 <= mouseY <= 485:
            gamemode = "scoresMenu"
    if gamemode == "playerMenu" and mouseButton == LEFT:
        if width/2-60 <= mouseX <= width/2+60 and 460 <= mouseY <= 485:
            if len(playerName) > minLimit:
                gamemode = "inGame"
        if 35 <= mouseX <= 64 and 24 <= mouseY <= 48:
            gamemode = "startMenu"
    
def keyPressed():
    global gamemode, playerName, wrongGuesses, guessLimit
    nameLimit = 20
    validKeys = "abcdefghijklmnopqrstuvwxyz "
    if gamemode == "playerMenu":
        if keyCode != SHIFT and key in validKeys and len(playerName) < nameLimit:
            curKey = key
            playerName.append(curKey)
            print(curKey)
        if key == BACKSPACE and len(playerName) > 0:
            playerName.pop()
    if gamemode == "inGame" and wrongGuesses <= guessLimit:
        wrongGuesses += 1
