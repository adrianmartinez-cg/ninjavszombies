import pygame

class Animation:
    
    #Funcao para carregar uma lista de figuras para criar uma animacao
    def loadImgs(self,path,finalframe,name,scale=1,colorkey=(255,255,255),invertx=False): 
        imgList=[]
        for i in range(finalframe+1):
            image=pygame.image.load(path+name+'__'+str(i)+'.png')
            image=pygame.transform.smoothscale(image,(int(image.get_width()/scale),int(image.get_height()/scale)))
            image.set_colorkey(colorkey)
            if invertx:
                image=pygame.transform.flip(image,True,False)
            imgList.append(image)
        return imgList
    
    def __init__(self,path,finalframe,name,scale=1,colorkey=(255,255,255), invertx = False):
        self.imgList = self.loadImgs(path,finalframe,name,scale,colorkey,invertx)
