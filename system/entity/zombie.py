import pygame
import random
from system.entity.animation import Animation
from system.config.util import collisionTest
from system.config.util import moveRect
from system.config.util import calcDistance

class Zombie:
    def __init__(self,x,y):
        self.id = None
        self.frame = 0
        self.dead = False
        self.deadPosX = 0
        self.deadPosY = 0
        self.idleAnimation = Animation('sprites/zombie_m/',14,'Idle',3.4)
        self.idleAnimationFlip = Animation('sprites/zombie_m/',14,'Idle',3.4,(255,255,255),True)
        self.walkAnimation = Animation('sprites/zombie_m/',9,'Walk',3.4)
        self.walkAnimationFlip = Animation('sprites/zombie_m/',9,'Walk',3.4,(255,255,255),True)
        self.deadAnimation = Animation('sprites/zombie_m/',12,'Dead',3.3)
        self.deadAnimationFlip = Animation('sprites/zombie_m/',12,'Dead',3.3,(255,255,255),True)
        self.health = random.randint(3,5)
        self.damageControl = True
        self.collisionTime = 0
        self.state = {'idle_r' : False , 'idle_l' : True , 'walk_r' : False, 'walk_l': False , 'dead_l': False, 'dead_r': False}
        self.stateCount = 0
        self.rect = pygame.Rect(x,y,self.idleAnimation.imgList[0].get_width(),self.idleAnimation.imgList[0].get_height())
        self.movement = [0,0]
        self.collisions = {'top': False, 'bottom': False , 'right': False , 'left': False}

    def updateStatus(self):
        if self.health > 0:
            if self.state['idle_l']:
                if self.stateCount < 50:
                    self.movement=[0,0]
                    self.stateCount += random.randint(0,1)
                else:
                    self.state['idle_l']= False
                    self.state['walk_r']= True
                    self.stateCount = 0
            elif self.state['idle_r']:
                if self.stateCount < 50:
                    self.movement=[0,0]
                    self.stateCount += random.randint(0,1)
                else:
                    self.state['idle_r'] = False
                    self.state['walk_l'] = True
                    self.stateCount = 0
            elif self.state['walk_l']:
                if self.stateCount < 60:
                    self.movement = [-2,0]
                    self.stateCount+= 1
                else:
                    self.state['walk_l'] = False
                    self.state['idle_l'] = True
                    self.stateCount = 0
            elif self.state['walk_r']:
                if self.stateCount < 60:
                    self.movement = [2,0]
                    self.stateCount+=1
                else:
                    self.state['walk_r'] = False
                    self.state['idle_r'] = True
                    self.stateCount = 0
        else:
            if self.state['idle_l'] or self.state['walk_l'] :
                self.state['idle_l'] = False
                self.state['walk_l'] = False
                self.stateCount = 0
                self.movement = [0,0]
                self.frame= 0
                self.state['dead_l'] = True
            elif self.state['idle_r'] or self.state['walk_r']:
                self.state['idle_r'] = False
                self.state['walk_r'] = False
                self.stateCount = 0
                self.movement = [0,0]
                self.frame = 0
                self.state['dead_r'] = True
            elif self.state['dead_l'] or ['dead_r']:
                self.movement = [0,0]

    def animate(self,display,scroll):
        if self.state['idle_l']:
            if self.frame < 69:
                self.frame+=1
            else:
                self.frame=0
            display.blit(self.idleAnimationFlip.imgList[self.frame//5],(self.rect.x-scroll[0],self.rect.y-scroll[1]))
        elif self.state['idle_r']:
            if self.frame < 69:
                self.frame+=1
            else:
                self.frame=0
            display.blit(self.idleAnimation.imgList[self.frame//5],(self.rect.x-scroll[0],self.rect.y-scroll[1]))
        elif self.state['walk_l']:
            if self.frame<49:
                self.frame+=1
            else:
                self.frame=0
            display.blit(self.walkAnimationFlip.imgList[self.frame//5],(self.rect.x-scroll[0],self.rect.y-scroll[1]))
        elif self.state['walk_r']:
            if self.frame<49:
                self.frame+=1
            else:
                self.frame=0
            display.blit(self.walkAnimation.imgList[self.frame//5],(self.rect.x-scroll[0],self.rect.y-scroll[1]))
        elif self.state['dead_l']:
            if self.frame < 48:
                self.frame+=1
            else:
                self.frame = 48
                if not self.dead:
                    self.deadPosX = self.rect.x
                    self.deadPosY = self.rect.y - 3
                    self.rect.x = self.id * self.idleAnimation.imgList[0].get_width()
                    self.rect.y = 9000
                    self.dead = True
            if not self.dead:
                display.blit(self.deadAnimationFlip.imgList[self.frame//4],(self.rect.x-scroll[0],self.rect.y-scroll[1]))
            else:
                display.blit(self.deadAnimationFlip.imgList[self.frame//4],(self.deadPosX-scroll[0],self.deadPosY-scroll[1]))
        elif self.state['dead_r']:
            if self.frame < 48:
                self.frame+=1
            else:
                self.frame = 48
                if not self.dead:
                    self.deadPosX = self.rect.x
                    self.deadPosY = self.rect.y - 3
                    self.rect.x = self.id * self.idleAnimation.imgList[0].get_width()
                    self.rect.y = 9000
                    self.dead = True
            if not self.dead:
                display.blit(self.deadAnimation.imgList[self.frame//4],(self.rect.x-scroll[0],self.rect.y-scroll[1]))
            else:
                display.blit(self.deadAnimation.imgList[self.frame//4],(self.deadPosX-scroll[0],self.deadPosY-scroll[1]))
        
    def move(self,solidRects,kunai,display,scroll):
        self.updateStatus()   
        self.rect,self.collisions = moveRect(self.rect,self.movement,solidRects)
        self.animate(display,scroll)
        self.checkCollisionWithKunai(kunai) 
       

    def checkCollisionWithKunai(self,kunai):
        if kunai.right:
            distanceZkunai=calcDistance(kunai.rect.right,self.rect.left,kunai.rect.y,self.rect.y)
        elif kunai.left:
            distanceZkunai=calcDistance(kunai.rect.left,self.rect.right,kunai.rect.y,self.rect.y)
        if distanceZkunai < 35:  
            actualTime = pygame.time.get_ticks()
            if self.health > 0 and self.damageControl:
                self.health -= 1
                self.collisionTime = pygame.time.get_ticks()
                kunai.playStabSound()
                self.damageControl = False
            if actualTime - self.collisionTime > 40 :
                self.damageControl = True
    
    def checkCollisionWithPlayer(self,player):
        pass
            

        
    def debug(self):
        print(f'Health {self.health}')