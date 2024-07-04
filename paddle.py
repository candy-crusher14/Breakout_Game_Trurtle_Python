from turtle import Turtle


class Paddle(Turtle):

    def __init__(self, position):
        super().__init__()
        self.shape('square')
        self.color('white')
        self.shapesize(stretch_wid=1, stretch_len=5)
        self.penup()
        self.goto(position)

    def paddle_left(self):
        x = self.xcor()
        x -= 40
        if x < -350: # if x is -350 do nothing
            x = -350
        self.setx(x)

    def paddle_right(self):
        x = self.xcor()
        x += 40
        if x > 350:
            x = 350
        self.setx(x)
