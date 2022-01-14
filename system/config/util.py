import pygame , sys
import math
from pygame.locals import *

def renderBGFill(display,BGImg,color=(146,244,255),BGImgCoord = (0,0)):
    display.fill(color)
    display.blit(BGImg,BGImgCoord)

def renderHudFont(font,lives,ammunition, display,hudHead,hudKunai,color = (180,17,74)):
    fontRenderLives=font.render(str(lives),True,color)
    fontRenderAmmunition=font.render(str(ammunition),True,color)
    drawHud(display,hudHead,hudKunai,fontRenderLives,fontRenderAmmunition)

def drawHud(display,hudHead,hudKunai,fontRenderLives,fontRenderAmmunition):
    display.blit(hudHead,(0,0))
    display.blit(fontRenderLives,(60,20))
    display.blit(hudKunai,(0,50))
    display.blit(fontRenderAmmunition,(60,70))

def updateScroll(player,trueScroll,scroll):
    trueScroll[0] += ((player.rect.x-trueScroll[0])-200)/3
    trueScroll[1] += ((player.rect.y-trueScroll[1])-200)/3
    scroll[0]=int(trueScroll[0])
    scroll[1]=int(trueScroll[1])
    return trueScroll,scroll

def calcDistance(xa,xb,ya,yb):
    distance=math.sqrt((xa-xb)**2+(ya-yb)**2)
    return distance

def calcPlayerBoundaries(player,TILE_SIZE):
    top = math.floor(player.rect.top / TILE_SIZE)
    bottom = math.ceil(player.rect.bottom / TILE_SIZE)
    left = math.floor(player.rect.left / TILE_SIZE)
    right = math.ceil(player.rect.right / TILE_SIZE)
    return left, right, bottom , top

def calcDrawBoundaries(left,right,bottom,top,renderingDist,gamemap):
    lowerBoundX = left -renderingDist[0] if (left - renderingDist[0]) >= 0 else 0
    upperBoundX = right + renderingDist[1] if (right + renderingDist[1]) <= len(gamemap[0]) else len(gamemap[0])
    lowerBoundY = top - renderingDist[3] if (top - renderingDist[3]) >= 0 else 0
    upperBoundY = bottom + renderingDist[2] if (bottom + renderingDist[2]) <= len(gamemap) - 1 else len(gamemap) - 1
    return lowerBoundX , upperBoundX, lowerBoundY, upperBoundY


def renderGameMap(gamemap,player,scroll,tilesImgs,TILE_SIZE,renderingDist,display):
    left,right,bottom,top =  calcPlayerBoundaries(player,TILE_SIZE)
    lowerBoundX, upperBoundX, lowerBoundY, upperBoundY = calcDrawBoundaries(left,right,bottom,top,renderingDist,gamemap)
    for i in range(lowerBoundY,upperBoundY):
        for j in range(lowerBoundX,upperBoundX):
            if gamemap[i][j] == '1':
                display.blit(tilesImgs[0],(j*TILE_SIZE-scroll[0],i*TILE_SIZE-scroll[1]))
            elif gamemap[i][j] == '2':
                 display.blit(tilesImgs[1],(j*TILE_SIZE-scroll[0],i*TILE_SIZE-scroll[1]))
            elif gamemap[i][j] == '3':
                 display.blit(tilesImgs[2],(j*TILE_SIZE-scroll[0],i*TILE_SIZE-scroll[1]))
            elif gamemap[i][j] == '4':
                 display.blit(tilesImgs[3],(j*TILE_SIZE-scroll[0],i*TILE_SIZE-scroll[1]))
            elif gamemap[i][j] == '5':
                 display.blit(tilesImgs[4],(j*TILE_SIZE-scroll[0],i*TILE_SIZE-scroll[1]))
            elif gamemap[i][j] == '6':
                 display.blit(tilesImgs[5],(j*TILE_SIZE-scroll[0],i*TILE_SIZE-scroll[1]))
            elif gamemap[i][j] == '7':
                 display.blit(tilesImgs[6],(j*TILE_SIZE-scroll[0],i*TILE_SIZE-scroll[1]))
            elif gamemap[i][j] == '8':
                 display.blit(tilesImgs[7],(j*TILE_SIZE-scroll[0],i*TILE_SIZE-scroll[1]))
            elif gamemap[i][j] == '9':
                 display.blit(tilesImgs[8],(j*TILE_SIZE-scroll[0],i*TILE_SIZE-scroll[1]))
            elif gamemap[i][j] == 'A':
                 display.blit(tilesImgs[9],(j*TILE_SIZE-scroll[0],i*TILE_SIZE-scroll[1]))
            elif gamemap[i][j] == 'B':
                 display.blit(tilesImgs[10],(j*TILE_SIZE-scroll[0],i*TILE_SIZE-scroll[1]))
            elif gamemap[i][j] == 'C':
                 display.blit(tilesImgs[11],(j*TILE_SIZE-scroll[0],i*TILE_SIZE-scroll[1]))
            elif gamemap[i][j] == 'D':
                 display.blit(tilesImgs[12],(j*TILE_SIZE-scroll[0],i*TILE_SIZE-scroll[1]))  
            elif gamemap[i][j] == 'E':
                 display.blit(tilesImgs[13],(j*TILE_SIZE-scroll[0],i*TILE_SIZE-scroll[1]))
            elif gamemap[i][j] == 'F':
                 display.blit(tilesImgs[14],(j*TILE_SIZE-scroll[0],i*TILE_SIZE-scroll[1]))
            elif gamemap[i][j] == 'G':
                 display.blit(tilesImgs[15],(j*TILE_SIZE-scroll[0],i*TILE_SIZE-scroll[1]))
            elif gamemap[i][j] == 'H':
                 display.blit(tilesImgs[16],(j*TILE_SIZE-scroll[0],i*TILE_SIZE-scroll[1]))  
            elif gamemap[i][j] == 'I':
                 display.blit(tilesImgs[17],(j*TILE_SIZE-scroll[0],i*TILE_SIZE-scroll[1]))   
            elif gamemap[i][j] == 'J':
                 display.blit(tilesImgs[18],(j*TILE_SIZE-scroll[0],i*TILE_SIZE-scroll[1]))            

def getKeyboardInputs(player,kunai,scroll,throwSound,display):
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == KEYDOWN and not player.freeze:
            if event.key == K_RIGHT:
                player.movingRight = True
            if event.key == K_LEFT:
                player.movingLeft = True
            if event.key == K_UP:
                if player.airTimer < 6:
                    player.YMomentum=-6
                    if player.throwing:
                        player.throwing=False
            if event.key == K_v and kunai.state == False and player.kunaiAmmunition > 0:
                player.throwing=True
                player.kunaiAmmunition-=1
                throwSound.play()
                kunai.rect.x=player.rect.right+5
                kunai.rect.y=player.rect.y+18
                if player.flipRight:
                    kunai.right=True
                    kunai.left=False
                    kunai.movement=[7,0]
                    kunaiThrow(kunai,kunai.rect.x-scroll[0],kunai.rect.y-scroll[1],display) 
                elif player.flipLeft:
                    kunai.left=True
                    kunai.right=False
                    kunai.movement =[-7,0]
                    kunaiThrow(kunai,kunai.rect.x-scroll[0],kunai.rect.y-scroll[1],display,True)
            if event.key == K_LSHIFT and not player.running:
                player.running=True
        if event.type == KEYUP and not player.freeze:
            if event.key == K_RIGHT:
                player.frame=0
                player.movingRight = False
            if event.key == K_LEFT:
                player.frame=0
                player.movingLeft = False   
            if event.key == K_LSHIFT and player.running:
                player.running=False

#Funcao para verificar se ocorreu alguma colisao, de um certo retangulo em relacao a todos os tiles
def collisionTest(rect,tiles):
    hitList=[] 
    for tile in tiles:
        if rect.colliderect(tile):
            hitList.append(tile)
    return hitList

#Funcao para movimentar um retangulo 'rect' , de acordo com seu movimento[x,y] , caso nao esteja colidindo com nenhum tile
def moveRect(rect,movement,collisionRects):
    collisionTypes = {'top': False, 'bottom': False , 'right': False , 'left': False}
    rect.x+=movement[0] #realiza movimento em x
    hitList=collisionTest(rect,collisionRects)
    for tile in hitList: #retangulo colidiu
        if movement[0] > 0: #colidiu com algo à direita
            rect.right = tile.left # .right = coord. x da borda direita , .left = coord.x da borda esquerda
            collisionTypes['right'] = True
        elif movement[0] < 0:#colidiu com algo à esquerda
            rect.left = tile.right
            collisionTypes['left']=True
    rect.y+=movement[1] #realiza movimento em y
    hitList=collisionTest(rect,collisionRects)
    for tile in hitList:
        if movement[1] > 0:
            rect.bottom=tile.top
            collisionTypes['bottom']= True
        elif movement[1] < 0:
            rect.top =tile.bottom
            collisionTypes['top']=True
    return rect, collisionTypes

def kunaiThrow(kunai,x,y,display,flip = False):
    kunai.state = True
    if flip:
        display.blit(kunai.ImgFlip,(x-10,y+18))
    else:
        display.blit(kunai.Img,(x+10,y+18))