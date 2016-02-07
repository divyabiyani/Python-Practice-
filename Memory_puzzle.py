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

	mouseX=0
	mouseY=0

	mainBoard=getRandomizedBoard()
	revealedBoxes=generateRevealedBoxesData(False)

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

