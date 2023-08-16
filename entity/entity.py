from abc import abstractmethod
import pygame


class Entity(pygame.sprite.Sprite):
    def __init__(self, x, y, path):
        super().__init__()
        self.frames = []
        self.setSprite(path)
        self.rect.x = x
        self.rect.y = y
        self._xvelocity = 0
        self._yvelocity = 0
        self._life = 1
        self.ACCELERATION = 3

    def draw(self, cnv):
        cnv.blit(self.surf, self.rect)

    def setFrame(self, index):
        self.surf = self.image = self.frames[index]

    def setSprite(self, path):
        for p in path:
            img = pygame.image.load(p).convert_alpha()
            self.frames.append(img)
        self.setFrame(0)
        self.rect = self.surf.get_rect()

    def removeLife(self):
        self._life -= 1
        if(self._life <= 0):
            self.kill()

    def checkColision(self, colliders):
        self.rect.x += self._xvelocity

        for collider in colliders:
            if pygame.sprite.collide_rect(self, collider):
                if self._xvelocity < 0:
                    self.rect.left = collider.rect.right
                elif self._xvelocity > 0:
                    self.rect.right = collider.rect.left
                break

        self.rect.y += self._yvelocity
        for collider in colliders:
            if pygame.sprite.collide_rect(self, collider):
                if self._yvelocity < 0:
                    self.rect.top = collider.rect.bottom
                elif self._yvelocity > 0:
                    self.rect.bottom = collider.rect.top
                break

        self._xvelocity = 0
        self._yvelocity = 0

    def update(self, colliders):
        self.move()
        self.checkColision(colliders)

    @abstractmethod
    def move(self):
        pass
