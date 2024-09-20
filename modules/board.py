import pygame as pg

class Board:
    def __init__(self,win_ref) -> None:
        self.win=win_ref
        self.board_img=pg.image.load("assets/board1.png").convert_alpha()
        self.board_img_rect=self.board_img.get_rect(center=(500,450))
        self.board_matrix=[[0,0,0,0,0,0,0,0,0,0,0,0],
                           [0,1,"l1e",1,"s1s",1,"s2s",1,1,"l2e",1,0],
                           [0,1,1,1,1,1,1,1,"s3s",1,1,0],
                           [0,"l1s",1,"s1e",1,"l4e",1,1,1,1,"l2s",0],
                           [0,1,"s4s",1,1,1,1,"l3e",1,1,1,0],
                           [0,1,1,1,1,"s2e",1,1,1,1,1,0],
                           [0,1,"l5e",1,1,1,1,1,"s6s",1,"l3s",0],
                           [0,1,1,"l6e","s5s",1,1,1,1,"s7s",1,0],
                           [0,"l5s",1,1,"s3e",1,"s6e",1,"l4s",1,"l8e",0],
                           [0,1,1,"s4e",1,1,1,"l7e",1,1,1,0],
                           [0,"l6s",1,1,"l7s","s5e",1,1,"l8s",1,"s7e",0],
                           [0,0,0,0,0,0,0,0,0,0,0,0],]
    
    def drawBoard(self):
        self.win.fill((30,30,30))
        self.win.blit(self.board_img,self.board_img_rect)