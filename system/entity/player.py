import pygame
from system.entity.animation import Animation
from system.config.util import collisionTest
from system.config.util import moveRect

class Player:
    def __init__(self,x,y):
        self.freeze = False
        self.draw = True
        self.running = False
        self.frame = 0
        self.lives = 3
        self.kunaiAmmunition = 30
        self.idleAnimation = Animation('sprites/ninja/',9,'Idle',3.2)
        self.idleAnimationFlip = Animation('sprites/ninja/',9,'Idle',3.2,(255,255,255),True)
        self.runAnimation=Animation('sprites/ninja/',9,'Run',3.2)
        self.runAnimationFlip=Animation('sprites/ninja/',9,'Run',3.2,(255,255,255),True)
        self.jumpAnimation=Animation('sprites/ninja/',9,'Jump',3.2)
        self.jumpAnimationFlip=Animation('sprites/ninja/',9,'Jump',3.2,(255,255,255),True)
        self.throwAnimation=Animation('sprites/ninja/',9,'Throw',3.2)
        self.throwAnimationFlip=Animation('sprites/ninja/',9,'Throw',3.2,(255,255,255),True)
        self.jumpthrowAnimation=Animation('sprites/ninja/',9,'Jump_Throw',3.2)
        self.jumpthrowAnimationFlip=Animation('sprites/ninja/',9,'Jump_Throw',3.2,(255,255,255),True)
        self.rect = pygame.Rect(x,y,self.idleAnimation.imgList[0].get_width(),self.idleAnimation.imgList[0].get_height())
        self.movingLeft = False
        self.movingRight = False
        self.flipLeft = False
        self.flipRight = True
        self.movement = [0,0]
        self.YMomentum = 0
        self.airTimer = 0
        self.throwing = False
        self.collisions = {'top': False, 'bottom': False , 'right': False , 'left': False}

    def restart(self):
        self.freeze = False
        self.draw = True
        self.running = False
        self.frame = 0
    
    def move(self,solidRects,display,scroll,kunai):
        self.movement = [0,0]
        if self.movingRight and not self.freeze:
            if self.running:
                self.movement[0] += 4.5
            else:
                self.movement[0] += 3
            if self.flipLeft:
                self.flipLeft = False
                self.flipRight = True
                self.throwing = False
        if self.movingLeft and not self.freeze:
            if self.running:
                self.movement[0] -= 4.5
            else:
                self.movement[0] -= 3
            if self.flipRight:
                self.flipRight = False
                self.flipLeft = True
                self.throwing = False
        if not self.freeze:
            self.movement[1] += self.YMomentum
        self.YMomentum += 0.2
        if self.YMomentum > 3: 
            self.YMomentum = 3
        self.rect , self.collisions = moveRect(self.rect,self.movement,solidRects)
        if self.collisions['bottom']:
            self.YMomentum = 0
            self.airTimer = 0
        elif self.collisions['top']:
            self.YMomentum = 0
        else:
            self.airTimer += 1
        self.animate(display,scroll,kunai)
    
    def animate(self,display,scroll,kunai):
        if self.frame<=44:
            self.frame+=1
        elif self.frame == 45:
            if self.airTimer == 0:
                self.frame=0
            else:
                self.frame=45
        if self.draw:
            if self.movingRight:
                if self.airTimer <= 5:
                    if self.flipRight:
                        display.blit(self.runAnimation.imgList[self.frame//5],(self.rect.x-scroll[0],self.rect.y-scroll[1]))
                elif self.airTimer > 5:
                    if self.flipRight:
                        if self.throwing and kunai.state and kunai.stateCount<45:
                            display.blit(self.jumpthrowAnimation.imgList[self.frame//5],(self.rect.x-scroll[0],self.rect.y-scroll[1]))
                        else:
                            display.blit(self.jumpAnimation.imgList[self.frame//5],(self.rect.x-scroll[0],self.rect.y-scroll[1]))
            elif self.movingLeft:
                if self.airTimer <= 5:
                    if self.flipLeft:
                        display.blit(self.runAnimationFlip.imgList[self.frame//5],(self.rect.x-scroll[0],self.rect.y-scroll[1]))
                elif self.airTimer > 5:
                    if self.flipLeft:
                        if self.throwing and kunai.state and kunai.stateCount <45: 
                            display.blit(self.jumpthrowAnimationFlip.imgList[self.frame//5],(self.rect.x-scroll[0],self.rect.y-scroll[1]))
                        else:
                            display.blit(self.jumpAnimationFlip.imgList[self.frame//5],(self.rect.x-scroll[0],self.rect.y-scroll[1]))
            else:
                if self.airTimer <= 5:
                    if self.flipRight:
                        if self.throwing and kunai.state and kunai.stateCount< 45:
                            display.blit(self.throwAnimation.imgList[self.frame//5],(self.rect.x-scroll[0],self.rect.y-scroll[1]))
                        else:
                            display.blit(self.idleAnimation.imgList[self.frame//5],(self.rect.x-scroll[0],self.rect.y-scroll[1]))
                    elif self.flipLeft:
                        if self.throwing and kunai.state and kunai.stateCount< 45:
                            display.blit(self.throwAnimationFlip.imgList[self.frame//5],(self.rect.x-scroll[0],self.rect.y-scroll[1]))
                        else:
                            display.blit(self.idleAnimationFlip.imgList[self.frame//5],(self.rect.x-scroll[0],self.rect.y-scroll[1]))
                elif self.airTimer > 5:
                    if self.flipRight:
                        if self.throwing and kunai.state and kunai.stateCount<45:
                            display.blit(self.jumpthrowAnimation.imgList[self.frame//5],(self.rect.x-scroll[0],self.rect.y-scroll[1]))
                        else:
                            display.blit(self.jumpAnimation.imgList[self.frame//5],(self.rect.x-scroll[0],self.rect.y-scroll[1]))
                    elif self.flipLeft:
                        if self.throwing and kunai.state and kunai.stateCount<45:
                            display.blit(self.jumpthrowAnimationFlip.imgList[self.frame//5],(self.rect.x-scroll[0],self.rect.y-scroll[1]))
                        else:
                            display.blit(self.jumpAnimationFlip.imgList[self.frame//5],(self.rect.x-scroll[0],self.rect.y-scroll[1]))
    def debug(self):
        print(self.rect.x)
        print(self.rect.y)
        
        
if __name__ == "__main__":
    player = Player(100,100)
