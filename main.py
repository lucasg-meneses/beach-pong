import json
import pygame as pyg
from entity.ball import Ball

from entity.pad import Pad, PadPlayer
from entity.block import Block
from entity.entity import Entity
from entity.fontManager.text import Text


class Game:
    def __init__(self, title="My Game", width=300, height=300, fullscreen=True):
        pyg.init()

        self.__canvas = pyg.display.set_mode(
            (width, height), (pyg.SCALED | pyg.FULLSCREEN if fullscreen else pyg.SCALED | pyg.RESIZABLE))

        pyg.display.set_caption(title)
        self.__clock = pyg.time.Clock()
        # raquetes
        self.__pads = pyg.sprite.Group()
        self.__ball = Ball((self.__canvas.get_width() / 2) - 8,
                           (self.__canvas.get_height() / 2) - 8)

        # cenario
        self.__bricks = pyg.sprite.Group()
        self.__net = pyg.sprite.Group()
        self.createScene()
        self.scores = [0, 0]

        self.pad01 = PadPlayer(8, 16, 0)
        self.pad02 = Pad(self.__canvas.get_width()-16-8, 16)
        self.__pads.add(self.pad01)
        self.__pads.add(self.pad02)

        caminho_fonte = "asset/font/VT323-Regular.ttf"
        tamanho_fonte = 40
        self.fonte = pyg.font.Font(caminho_fonte, tamanho_fonte)

        self.scoreP1Text = Text(
            self.scores[0], self.fonte, (320/4, 16), (249, 168, 117))
        self.scoreP2Text = Text(
            self.scores[1], self.fonte, ((320/4)*3, 16), (249, 168, 117))

    def createScene(self):
        # Rede
        for i in range(0, self.__canvas.get_height(), 16):
            self.__net.add(
                Entity((self.__canvas.get_width() / 2) - 8, i, ['asset/sprites/scene/scn_1.png']))

        for i in range(0, self.__canvas.get_width(), 16):
            self.__bricks.add(Block(i, -16))
            self.__bricks.add(Block(i, 180))

    def gameLoop(self):
        self.__exit = False

        while not self.__exit:
            self.__setQuitGame()
            self.__canvas.fill(pyg.Color(255, 246, 211))

            self.update()
            self.draw()

            pyg.display.flip()
            self.__clock.tick(60)

    def __setQuitGame(self):
        for event in pyg.event.get():
            if event.type == pyg.QUIT or event.type == pyg.KEYDOWN and event.key == pyg.K_ESCAPE:
                self.__exit = True

    def draw(self):
        self.__net.draw(self.__canvas)
        self.__bricks.draw(self.__canvas)

        self.scoreP1Text.draw(self.__canvas)
        self.scoreP2Text.draw(self.__canvas)

        self.__ball.draw(self.__canvas)
        self.__pads.draw(self.__canvas)

    def update(self):

        for pad in self.__pads:
            if not type(pad) == PadPlayer:
                pad.update(self.__bricks, pyg.math.Vector2(
                    self.__ball.rect.center))
            else:
                pad.update(self.__bricks)

        self.__ball.checkColision(self.__bricks)
        self.__ball.checkColision(self.__pads)
        if self.__ball.isOutside():
            if(self.__ball.rect.x >= 320):
                self.scores[0] += 1
            elif(self.__ball.rect.x <= 0):
                self.scores[1] += 1
            self.__ball.reset()
            self.scoreP1Text.text = self.scores[0]
            self.scoreP2Text.text = self.scores[1]
        else:
            self.__ball.update()


if __name__ == '__main__':
    file = open('config.json')
    config = json.load(file)
    file.close()

    game = Game(title="Beach Pong",
                width=config['resolution']['width'], height=config['resolution']['height'], fullscreen=config['fullscreen'])
    game.gameLoop()
