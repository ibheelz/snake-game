from turtle import Turtle


class Score:
    def __init__(self):
        self.player_score = 0
        self.score = Turtle()
        self.score.hideturtle()
        self.score.penup()
        self.score.goto(0, 280)
        self.score.color("white")
        self.score.write(f"Score = {self.player_score}", align="center", font=('Poppins', 14, 'normal'))

    def score_update(self):
        self.player_score += 1
        self.score.clear()  # Clear the previous score
        self.score.write(f"Score = {self.player_score}", align="center", font=('Poppins', 14, 'normal'))
