import pygame
from entity.entity import Entity


class Pad(Entity):
    def __init__(self, x, y):
        super().__init__(x, y, ['asset/sprites/pad/pd.png'])
        self.ACCELERATION = 2
    def update(self, colliders, ballPoint: pygame.math.Vector2):
        self.move(ballPoint)
        self.checkColision(colliders)

    def move(self, ballPoint: pygame.math.Vector2):
        if(ballPoint.x >= 320 / 2):
            if ballPoint.y <= 180 / 2:
                self._yvelocity = -1 * self.ACCELERATION
            else:
                self._yvelocity = 1 * self.ACCELERATION


class PadPlayer(Pad):
    def __init__(self, x, y, id=0):
        super().__init__(x, y)
        self.__id = id
    
    def update(self, colliders):
        self.move()
        self.checkColision(colliders)
    
    def move(self):
        keyspress = pygame.key.get_pressed()
        if(self.__id == 0):
            if((keyspress[pygame.K_d])):
                self._yvelocity = 1 * self.ACCELERATION
            elif((keyspress[pygame.K_a])):
                self._yvelocity = -1 * self.ACCELERATION
        else:
            if((keyspress[pygame.K_RIGHT])):
                self._yvelocity = 1 * self.ACCELERATION
            elif((keyspress[pygame.K_LEFT])):
                self._yvelocity = -1 * self.ACCELERATION
