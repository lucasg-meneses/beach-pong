import pygame
from entity.entity import Entity
from entity.block import Block
from entity.pad import Pad, PadPlayer


class Ball(Entity):
    def __init__(self, x, y):
        super().__init__(x, y, ['asset/sprites/ball/b_0.png'])
        self.ACCELERATION = 2
        self.initX = x
        self.initY = y
        self._xvelocity = self._yvelocity = 1 * self.ACCELERATION

    def checkColision(self, colliders):
        for collider in colliders:
            if pygame.sprite.collide_rect(self, collider) and isinstance(collider, Pad):
                if self._xvelocity < 0:
                    self._xvelocity = abs(self._xvelocity)
                elif self._xvelocity > 0:
                    self._xvelocity = -abs(self._xvelocity)
                break
        for collider in colliders:
            if pygame.sprite.collide_rect(self, collider) and type(collider) == Block:
                self._yvelocity = - self._yvelocity

    def update(self):
        self.move()

    def reset(self):
        self.rect.x = self.initX
        self.rect.y = self.initY
        self._xvelocity = self._yvelocity = 1 * self.ACCELERATION

    def isOutside(self):
        return self.rect.x > 320 or self.rect.x < 0

    def move(self):
        self.rect.y += self._yvelocity
        self.rect.x += self._xvelocity
