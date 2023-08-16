import pygame
from entity.entity import Entity

class Block(Entity):
    def __init__(self, x, y):
        super().__init__(x, y, ['asset/sprites/scene/scn_2.png'])


