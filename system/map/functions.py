import pygame
#Funcoes relacionadas ao mapa

#Funcao para carregar o arquivo de texto contendo o mapa
def loadMap(path):
    f=open(path + '.txt','r')
    data=f.read()
    f.close()
    data=data.split('\n')
    gamemap=[]
    for row in data:
        gamemap.append(list(row))
    return gamemap

#Guarda as coordenadas dos tiles que causam "game over"
def loadDangerTiles(DANGER,gamemap):
    dangerCoord=[]
    for i in range(len(gamemap)-1):
        for j in range(len(gamemap[0])):
            if gamemap[i][j] in DANGER:
                dangerCoord.append((32*j,32*i))
    return dangerCoord

#Carrega os graficos dos tiles (32x32) da pasta path
def loadTiles(path,finalnum):
    tilesImg=[]
    for i in range(1,finalnum+1):
        tileImg=pygame.image.load(path+str(i)+'.png')
        tileImg=pygame.transform.smoothscale(tileImg,(32,32))
        tilesImg.append(tileImg)
    return tilesImg

def loadTileRects(gamemap,COLLIDE_OFF,TILE_SIZE):
    tileRects =[]
    for i in range(len(gamemap)-1):
        for j in range(len(gamemap[0])):
            if gamemap[i][j] not in COLLIDE_OFF:
                tileRects.append(pygame.Rect(j*TILE_SIZE,i*TILE_SIZE,TILE_SIZE,TILE_SIZE))
    return tileRects



if __name__ == "main":
    gamemap = loadMap('map1')
    

