import time
from random import randint, choice
from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from bricks import Bricks
from scoreboard import ScoreBoard
from powerups import PowerUp


screen = Screen()
screen.setup(width=860, height=600)
screen.bgcolor('black')
screen.title('Breakout Game')
screen.tracer(0)

screen.listen()
paddle = Paddle((0, -250))  # Create Paddle Class instance
ball = Ball()
score = ScoreBoard()

# Set background image
screen.bgpic("images/background.gif")  # Ensure you have a background.gif image
# # Register custom shapes

screen.addshape("images/paddle1.gif")
screen.addshape("images/paddle3.gif")


screen.addshape("images/ball22.gif")
screen.addshape("images/ball33.gif")

screen.addshape("images/brick1.gif")
screen.addshape("images/brick2.gif")
screen.addshape("images/brick3.gif")
screen.addshape("images/brick4.gif")
screen.addshape("images/brick5.gif")


screen.addshape("images/live1.gif")
screen.addshape("images/extra_paddle1.gif")
screen.addshape("images/score1.gif")





ball.shape('images/ball22.gif')

paddle.shape("images/paddle1.gif")

screen.onkeypress(fun=paddle.paddle_right, key='d')
screen.onkeypress(fun=paddle.paddle_left, key='a')

lives = 3
powers_list = []
milestone_reached = False  # To track if milestone score was reached

power_style = ['images/extra_paddle1.gif', 'images/live1.gif', "images/score1.gif"]

power_types = ['extra_paddle', 'extra_life', "score"]


bricks_colors = ['images/brick1.gif','images/brick2.gif','images/brick3.gif','images/brick4.gif',
                 'images/brick5.gif']

bricks = Bricks(bricks_colors)

while lives > 0:
    time.sleep(0.04)
    screen.update()
    ball.move_ball()

    # Detect collision with ball
    # if ball.distance(paddle) < 50:
    if (-240 < ball.ycor() < -230) and (paddle.xcor() - 50 < ball.xcor() < paddle.xcor() + 50):
        ball.bounce_y()

    # detect collision with walls and bounce it
    if ball.xcor() > 380 or ball.xcor() < -380:
        ball.bounce_x()



    # Detect if ball is not hit by paddle and decrease lives and reset the position
    if ball.ycor() < -300:
        ball.reset_position()
        score.decrease_lives()

    # if ball is reaching above than bricks than bounce it back
    if ball.ycor() > 300:
        ball.bounce_y()

    for num, brick in enumerate(bricks.all_bricks):
        # brick.shape("bricks.gif")
        if brick.distance(ball) < 40:
            ball.bounce_y()  # Bounce the ball down when hit by brick
            # random_chance = randint(2,4)
            random_chance = [True, False]
            if choice(random_chance): # Make powers very rare so it becomes challanging
                power = PowerUp((brick.xcor(), brick.ycor()), choice(power_types),
                            power_style=power_style)
                powers_list.append(power)
            brick.goto(900, 900)  # place outside of screen
            bricks.all_bricks.remove(brick)  # Remove the brick from list
            score.points()  # Increase Score When get hit

        if not bricks.all_bricks:
            score.game_finished()
            lives = 0

    if powers_list:
        for power in powers_list:
            power.move_powers()
            if (-240 < power.ycor() < -230) and (paddle.xcor() - 50 < power.xcor() < paddle.xcor() + 50):

                random_chance = randint(0,6)
                if power.power_type == 'extra_paddle':
                    paddle.shape('images/paddle3.gif')
                    paddle.shapesize(stretch_wid=1, stretch_len=7)
                elif power.power_type == 'extra_life':
                    score.increase_lives()
                elif power.power_type == 'score':
                    score.points()
                # else:
                    # score.points() # increase score if ball is hit by paddle

                power.goto(900,900) # Move it out of screen
                powers_list.remove(power) # Remove after point gain

        # Speed adjustment based on score milestones
        if score.score % 5 == 0 and score.score != 0:
            if not milestone_reached:
                # ball.x_move *= 1.1
                # ball.y_move *= 1.1a

                ball.level_up()
                ball.shape('images/ball33.gif')

                milestone_reached = True
        else:
            milestone_reached = False





    lives = score.lives  # Manage lives
    if lives < 1:
        score.game_over()




screen.exitonclick()
