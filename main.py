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
from system.config.util import renderHudFont
from system.config.util import renderGameMap
from system.config.util import getKeyboardInputs
from system.entity.player import Player
from system.entity.animation import Animation
from system.entity.bank.enemies import EnemyRepository


clock , WINDOW_SIZE, screen , display = pygameConfig()

(mapselection, maploaded, renderingDist,
tilesImgs, TILE_SIZE, COLLIDE_OFF, DANGER, ADDED_TILE_RECTS, ADDED_ZOMBIES_RECTS)= initGameConfig()

(gameoverImg, fadeImg , BGImg, bushImgs, treeImgs, 
mushImgs, stoneImgs, signImgs,hudHead, hudKunai) = loadMiscImg()

(gameoverSound , throwSound , stabSound) = initSounds()

(blockfade,FADEOUT,alphaF,alphaG,babyFont,babyFontRenderLives,babyFontRenderAmmunition,scroll,
trueScroll) = initSystemVars()

while True:
    if not maploaded:
        (player,kunai,enemyRepository,gameover, 
        gamemap,dangerTiles, solidRects,tileRects, maploaded) = loadMapConfig(mapselection,DANGER,COLLIDE_OFF, TILE_SIZE,stabSound)
    
    renderBGFill(display,BGImg)
    trueScroll,scroll = updateScroll(player,trueScroll,scroll)
    
    renderGameMap(gamemap,player,scroll,tilesImgs,TILE_SIZE,renderingDist,display)
    
    getKeyboardInputs(player,kunai,scroll,throwSound,display)

    player.move(solidRects,display,scroll,kunai)
    kunai.move(player,solidRects,scroll,display,stabSound)
    enemyRepository.moveAllZombies(tileRects,kunai,display,scroll)
    

    renderHudFont(babyFont,player.lives,player.kunaiAmmunition,display,hudHead,hudKunai)

    surface = pygame.transform.smoothscale(display,WINDOW_SIZE) # Aumenta o tamanho da superficie que estamos desenhando o jogo para o tamanho da janela
    screen.blit(surface,(0,0))
    pygame.display.update()        
    clock.tick(60)