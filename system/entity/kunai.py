import pygame
from system.config.util import moveRect
from system.config.util import kunaiThrow

class Kunai:
    def __init__(self,x,y, stabSound):
        self.Img=pygame.image.load('sprites/tileset/Object/Kunai_0.png')
        self.Img=pygame.transform.smoothscale(self.Img,(int(self.Img.get_width()/3),int(self.Img.get_height()/3)))
        self.ImgFlip=pygame.transform.flip(self.Img,True,False)
        self.state = False
        self.stateCount = 0
        self.left = False
        self.right = True
        self.rect=pygame.Rect(x,y,self.Img.get_width(),self.Img.get_height())
        self.movement=[0,0]
        self.collisions = {'top': False, 'bottom': False , 'right': False , 'left': False}
        self.stabSound = stabSound
    #Variáveis de disparo do kunai
    #state : Foi jogado o kunai. Nao podemos atirar novamente até esperar alguns frames , ou até que ele colida
    #stateCount contador, ao atingir um certo valor o kunai some e podemos atirar novamente

    def move(self,player,solidRects,scroll,display,stabSound):
        if self.state:
            if self.stateCount < 60:
                if self.right:
                    self.rect,self.collisions=moveRect(self.rect,self.movement,solidRects)
                    kunaiThrow(self,self.rect.x-scroll[0],self.rect.y-scroll[1],display)
                    if self.collisions['left'] or self.collisions['right'] or self.collisions['bottom']:
                        self.stabSound.play()
                        self.stateCount=0
                        self.state=False
                        player.throwing=False
                        self.rect=pygame.Rect(2000,2000,self.Img.get_width(),self.Img.get_height())
                elif self.left:
                    self.rect,self.collisions=moveRect(self.rect,self.movement,solidRects)
                    kunaiThrow(self,self.rect.x-scroll[0],self.rect.y-scroll[1],display,True)
                    if self.collisions['left'] or self.collisions['right'] or self.collisions['bottom']:
                        self.stabSound.play()
                        self.stateCount=0
                        self.state=False
                        player.throwing=False
                        self.rect=pygame.Rect(2000,2000,self.Img.get_width(),self.Img.get_height())
                self.stateCount+=1
            elif self.stateCount == 60:
                self.stateCount=0
                self.rect=pygame.Rect(2000,2000,self.Img.get_width(),self.Img.get_height())
                self.state=False
                player.throwing=False
    
    def playStabSound(self):
        self.stabSound.play()

    def reset(self):
        self.stateCount=0
        self.state=False
        self.rect=pygame.Rect(2000,2000,self.Img.get_width(),self.Img.get_height())
