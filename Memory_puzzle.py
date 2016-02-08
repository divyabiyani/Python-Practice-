import pygame,sys,random
from pygame.locals import *

FramesPerSecond=30
WindowWidth=640
WindowHeight=480
RevealSpeed=8
BoxSize=40
GapSize=10
BoardWidth=10
BoardHeight=7

XMargin=int((WindowWidth-(BoardWidth*(BoxSize+GapSize)))/2)
YMargin=int((WindowHeight-(BoardHeight*(BoxSize+GapSize)))/2)

GRAY=(100,100,100)
NAVYBLUE=(60,60,100)
WHITE=(255,255,255)
RED=(255,0,0)
GREEN=(0,255,0)
BLUE=(0,0,255)
YELLOW=(255,255,0)
ORANGE=(255,128,0)
PURPLE=(255,0,255)
CYAN=(0,255,255)

BgColor=NAVYBLUE
LightBgColor=GRAY
BoxColor=WHITE
HighlightColor=BLUE

Donut='donut'
Square='square'
Diamond='diamond'
Lines='lines'
Oval='oval'

AllColors=(RED,GREEN,BLUE,YELLOW,ORANGE,PURPLE,CYAN)
AllShapes=(Donut,Square,Diamond,Lines,Oval)

def main():
	global FramesPerSecondClock,DisplaySurf
	pygame.init()
	FramesPerSecond=pygame.time.Clock()
	DisplaySurf=pygame.display.set_mode((WindowWidth,WindowHeight))
	pygame.display.caption('Memory Game')
	DisplaySurf.fill(BgColor)

	mouseX=0
	mouseY=0

	mainBoard=getRandomizedBoard()
	revealedBoxes=generateRevealedBoxesData(False)

	firstSelection=None


def getRandomizedBoard():
	icons=[]
	for color in AllColors:
		for shape in AllShapes:
			icons.append((shape,color))

	random.shuffle(icons)
	noIconsNeeded=int((BoardWidth*BoardHeight)/2)
	icons=icons[:noIconsNeeded]*2
	random.shuffle(icons)

	board=[]
	for x in range(BoardWidth):
		column=[]
		for y in range(BoardHeight):
			columns.append(icon[0])
			del icon[0]
		board.append(column)
	return board

def generateRevealedBoxesData(val):
	revealedBoxes=[]
	for i in range(BoardWidth):
		revealedBoxes.append([val]*BoardHeight)
	return revealedBoxes

def startGameAnimation(mainBoard):
	coveredBoxes=generateRevealedBoxesData(False)
	boxes=[]
	for x in range(BoardWidth):
		for y in range(BoardHeight):
			boxes.append((x,y))
	random.shuffle(boxes)
	boxIntoGroups=splitIntoGroupsOf(8,boxes)

def splitIntoGroupsOf(size,List):
	result=[]
	for i in range(0,len(List),size):
		result.append(List[i:i+size])
	return result

def drawBoard(mainBoard,revealed):
	for boxX in range(BoardWidth):
		for boxY in range(BoardHeight):
			left,top=leftTopCoordsOfBox(boxX,boxY)
			if not revealed[boxX][boxY]:
				pygame.draw.rect(DisplaySurf,BoxColor,(left,top,BoxSize,BoxSize))
			else:
				shape,color=getShapeAndColor(mainBoard,boxX,boxY)

def leftTopCoordsOfBox(boxX,boxY):
	left=boxX*(BoxSize+GapSize)+XMargin
	top=boxY*(BoxSize+GapSize)+YMargin
	return left,top

def getShapeAndColor(mainBoard,boxX,boxY):
	return mainBoard[boxX][boxY][0],mainBoard[boxX][boxY][1]

def drawIcon(shape,color,boxX,boxY):
	quarter=int(BoxSize*0.25)
	half=int(BoxSize*0.5)

	left,top=leftTopCoordsOfBox(boxX,boxY)

	if shape==Donut:
		pygame.draw.circle(DisplaySurf,color,(left+half,top+half),half-5)
		pygame.draw.circle(DisplaySurf,BgColor,(left+quarter,top+quarter),quarter-5)
	elif shape==Square:
		pygame.draw.rect(DisplaySurf,color,(left+quarter,top+quarter,BoxSize-half,BoxSize-half))
	elif shape==Diamond:
		pygame.draw.polygon(DisplaySurf,color,(left+half,top),)
		


