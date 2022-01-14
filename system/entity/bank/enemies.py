from system.entity.zombie import Zombie

class EnemyRepository:
    def __init__(self):
        self.zombieId = 0
        self.zombies = []
    
    def addZombies(self,zombieCoordList):
        for i in range(len(zombieCoordList)):
            zombie = Zombie(zombieCoordList[i][0],zombieCoordList[i][1])
            zombie.id = self.zombieId
            self.zombies.append(zombie)
            self.zombieId += 1
    
    def moveAllZombies(self,solidRects,kunai,display,scroll):
        for zombie in self.zombies:
            zombie.move(solidRects,kunai,display,scroll)

    def debugAll(self):
        for zombie in self.zombies:
            zombie.debug()