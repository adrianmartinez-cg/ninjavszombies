import pygame, sys
import random
import math
from system.config.initialize import pygameConfig
from system.config.initialize import loadMapConfig
from system.config.initialize import initGameConfig
from system.config.initialize import loadMiscImg
from system.config.initialize import initSounds
from system.config.initialize import initSystemVars
from system.config.util import renderBGFill
from system.config.util import updateScroll
from system.config.util import renderHud
from system.config.util import renderGameMap
from system.config.util import getKeyboardInputs
from system.entity.player import Player
from system.entity.animation import Animation


clock , WINDOW_SIZE, screen , display = pygameConfig()

(player, kunai ,mapselection, maploaded, renderingDist,
tilesImgs, TILE_SIZE, COLLIDE_OFF, DANGER, ADDED_TILE_RECTS, ADDED_ZOMBIES_RECTS)= initGameConfig()

(gameoverImg, fadeImg , BGImg, bushImgs, treeImgs, 
mushImgs, stoneImgs, signImgs,hudHead, hudKunai) = loadMiscImg()

(gameoverSound , throwSound , stabSound) = initSounds()

(blockfade,FADEOUT,alphaF,alphaG,babyFont,babyFontRenderLives,babyFontRenderAmmunition,scroll,
trueScroll) = initSystemVars()

while True:
    if not maploaded:
        gameover, gamemap, dangerTiles, tileRects, maploaded = loadMapConfig(player,mapselection,DANGER,COLLIDE_OFF, TILE_SIZE)
    
    renderBGFill(display,BGImg)
    trueScroll,scroll = updateScroll(player,trueScroll,scroll)
    
    babyFontRenderLives,babyFontRenderAmmunition= renderHud(babyFont,player.lives,player.kunaiAmmunition)
    renderGameMap(gamemap,player,scroll,tilesImgs,TILE_SIZE,renderingDist,display)
    
    getKeyboardInputs(player,kunai,scroll,throwSound,display)

    player.move(tileRects)
    player.animate(display,scroll,kunai)
    kunai.move(player,tileRects,scroll,display,stabSound)

    surface = pygame.transform.smoothscale(display,WINDOW_SIZE) # Aumenta o tamanho da superficie que estamos desenhando o jogo para o tamanho da janela
    screen.blit(surface,(0,0))
    pygame.display.update()        
    clock.tick(60)