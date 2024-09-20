import pygame as pg
import time
import sys
from .board import Board
from .dice import Dice
from .player import Player
pg.init()

class GameManager:
    def __init__(self):
        self.win_width=1200
        self.win_height=900
        self.win=pg.display.set_mode((self.win_width,self.win_height))
        self.clock = pg.time.Clock()

        #Creating board and dice
        self.board=Board(self.win)
        self.dice=Dice(self.win)

        #Creating players
        self.createPlayers()

        #Player list
        self.createPlayerList()

        self.gameLoop()

    def createPlayers(self):
        self.player_red=Player(self.win,"red",self.board.board_matrix,"Devansh")
        self.player_yellow=Player(self.win,"yellow",self.board.board_matrix,"Ankit")
        self.player_blue=Player(self.win,"blue",self.board.board_matrix,"Dhananjay")
        self.player_green=Player(self.win,"green",self.board.board_matrix,"Suryansh")

    def createPlayerList(self):
        self.player_list=[self.player_red,self.player_yellow,self.player_blue,self.player_green]
        self.current_player=0

    def gameLoop(self):
        while True :
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    sys.exit()
                if event.type==pg.MOUSEBUTTONDOWN and self.dice.rect.collidepoint(pg.mouse.get_pos()) and self.dice.dice_roll :
                    self.dice.startAnim()
                    self.dice.dice_roll=False
                   
                if event.type==Dice.DICE_ANIM_STOP_EVENT :
                    self.player_list[self.current_player].createMovePath(self.dice.total_value)
                    self.dice.total_value=0
                    print("event hit")
                if event.type==Player.PLAYER_MOVEMENT_STOPPED:
                    self.dice.dice_roll=True
                    
                    self.changeCurrentPlayer()


            #Update Everything
            self.updateEverything()

            #Draw Everything
            self.drawEverything()

            pg.display.update()
            self.clock.tick(60) 

    def changeCurrentPlayer(self):
        self.current_player+=1
        if self.current_player>3:
            self.current_player=0
    
    def updateEverything(self):
        self.dice.update()
        self.player_red.update()
        self.player_yellow.update()
        self.player_blue.update()
        self.player_green.update()
    
    def drawEverything(self):
        self.board.drawBoard()
        self.dice.drawDice()
        self.player_red.drawPlayer()
        self.player_yellow.drawPlayer()
        self.player_blue.drawPlayer()
        self.player_green.drawPlayer()