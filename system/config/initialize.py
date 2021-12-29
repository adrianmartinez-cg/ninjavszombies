import pygame, sys
import random
import math
from system.entity.player import Player
from system.entity.kunai import Kunai
from system.entity.animation import Animation
from system.map.functions import loadMap
from system.map.functions import loadTiles
from system.map.functions import loadDangerTiles
from system.map.functions import loadTileRects
from pygame import mixer
from pygame.locals import *


def pygameConfig():
    pygame.init()
    clock=pygame.time.Clock() #variavel que será usada para limitar o jogo à 60 fps
    pygame.display.set_caption('Ninja vs Zombies') #definindo o título
    WINDOW_SIZE=(1024,614) #definindo tamanho da janela
    screen = pygame.display.set_mode(WINDOW_SIZE,0,32) #definindo janela
    display = pygame.Surface((640,384)) #superficie onde iremos desenhar os graficos do jogo
    pygame.mixer.pre_init(44100, -16, 2, 512)
    pygame.mixer.set_num_channels(64)
    return clock, WINDOW_SIZE , screen , display

def loadMapConfig(player,mapselection,DANGER,COLLIDE_OFF,TILE_SIZE):
    player.restart()
    gameover = False
    gamemap = loadMap('./maps/map'+mapselection)
    dangerTiles = loadDangerTiles(DANGER,gamemap)
    tileRects = loadTileRects(gamemap,COLLIDE_OFF,TILE_SIZE)
    maploaded = True
    return gameover,gamemap, dangerTiles, tileRects , maploaded

def loadTilesImg():
    tilesImg = loadTiles('sprites/tileset/Tiles/',19)
    TILE_SIZE = tilesImg[0].get_width()
    return tilesImg, TILE_SIZE

def initGameConfig():
    player = Player(286,224)
    kunai = Kunai(2000,2000) 
    mapselection = '1'
    maploaded = False
    renderingDist = [8,14,5,8]     # left, right , bottom , top
    tilesImgs , TILE_SIZE = loadTilesImg()
    COLLIDE_OFF=['H','I','0','J','5']
    DANGER=['H','J']
    ADDED_TILE_RECTS = False
    ADDED_ZOMBIES_RECTS=False 
    return (player, kunai ,mapselection, maploaded, renderingDist,
            tilesImgs, TILE_SIZE, COLLIDE_OFF, DANGER, ADDED_TILE_RECTS, ADDED_ZOMBIES_RECTS)

def loadMiscImg():
    gameoverImg=pygame.image.load('sprites/gameover.jpg')
    fadeImg=pygame.image.load('sprites/fade.png')
    BGImg=pygame.image.load('sprites/tileset/BG/BG.png') #Imagem de fundo 
    bushImgs=Animation('sprites/tileset/Object/',3,'Bush',1)
    treeImgs=Animation('sprites/tileset/Object/',3,'Tree',1)
    mushImgs=Animation('sprites/tileset/Object/',1,'Mushroom',1)
    stoneImgs=Animation('sprites/tileset/Object/',1,'Stone',1)
    signImgs=Animation('sprites/tileset/Object/',1,'Sign',1)
    hudHead=pygame.image.load('sprites/hud_head.png')
    hudHead=pygame.transform.smoothscale(hudHead,(hudHead.get_width()//2,hudHead.get_height()//2))
    hudKunai=pygame.image.load('sprites/hud_kunai.png')
    hudKunai=pygame.transform.smoothscale(hudKunai,(hudKunai.get_width()//2,hudKunai.get_height()//2))
    return (gameoverImg, fadeImg , BGImg, bushImgs, treeImgs, mushImgs, 
            stoneImgs, signImgs,hudHead, hudKunai)

def initSystemVars():
    blockfade=False
    FADEOUT=False
    fadeEvent=False
    alphaF=0
    alphaG=0
    babyFont=pygame.font.Font('sprites/Baby Lovely.ttf',40)
    babyFontRenderLives=babyFont.render("3",True,(130,7,74))
    babyFontRenderAmmunition=babyFont.render("30",True,(150,7,74))
    scroll = [0,0]
    trueScroll = [0,0]
    
    return (blockfade,FADEOUT,alphaF,alphaG,babyFont,babyFontRenderLives,babyFontRenderAmmunition,scroll,
            trueScroll)

def initSounds():
    mixer.music.load('sounds/guitar1.mp3')
    mixer.music.play(-1) #-1: Carrega musica em loop
    gameoverSound=mixer.Sound('sounds/gameover.wav')
    throwSound=mixer.Sound('sounds/knifethrow.wav')
    stabSound=mixer.Sound('sounds/knifestab.wav')
    return (gameoverSound , throwSound , stabSound)