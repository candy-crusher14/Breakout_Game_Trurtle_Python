from turtle import Turtle

FONT = ("Courier", 24, "normal")


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.color('white')
        self.hideturtle()
        self.penup()
        self.y_move = 0
        self.score = 0
        self.lives = 3
        self.update_score()

    def update_score(self):
        self.clear()
        self.goto(350, 260)
        self.write(f'Score {self.score}', align='center', font=('Courier', 20, 'normal'))
        self.goto(-350, 260)
        self.write(f'Lives {self.lives}', align='center', font=('Courier', 20, 'normal'))

    def points(self):
        self.score += 1
        self.update_score()

    def decrease_lives(self):
        self.lives -= 1
        self.update_score()

    def increase_lives(self):
        self.lives += 1
        self.update_score()

    def game_finished(self):
        self.goto(0, 0)
        self.write(f'Game Finished... You Won!!!', align = 'center', font=FONT)
    def game_over(self):
        self.goto(0, 0)
        self.write(f'Game Over', align = 'center', font=FONT)




