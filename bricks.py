from turtle import Turtle
from random import choice


class Bricks():
    
    def __init__(self, colors):
        super().__init__()
        self.all_bricks = []
        # colors = ['red','green','blue','white','navyblue']
        for i in range(5):
            for j in range(9):
                brick = Turtle()
                brick.shape(f'{colors[i]}')
                # brick.color(f'{colors[i]}')
                # brick.color('blue')
                brick.shapesize(stretch_wid=1, stretch_len=4)
                brick.penup()
                brick.goto(-350 + j*90, 250 - i*30)

                self.all_bricks.append(brick)


