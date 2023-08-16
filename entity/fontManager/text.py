import pygame


class Text:
    def __init__(self, text: str,  font: pygame.font.Font, position: tuple = (0, 0), color: tuple = (255, 255, 255)):
        self.text = text
        self.font = font
        self.position = position
        self.color = color

    def draw(self, surface):
        surface.blit(self.font.render(str(self.text), False, self.color),
                     self.position
                     )
