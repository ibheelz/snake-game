from turtle import Turtle


class Score:
    def __init__(self):
        self.player_score = 0
        self.score = Turtle()
        self.score.hideturtle()
        self.score.penup()
        self.score.goto(0, 270)
        self.score.color("white")
        self.refresh_score()

    def refresh_score(self):
        self.score.write(f"Score = {self.player_score}", align="center", font=('Courier', 18, 'normal'))


    def score_update(self):
        self.player_score += 1
        self.score.clear()  # Clear the previous score
        self.refresh_score()

    def game_over(self):
        self.score.goto(0, 0)
        self.score.write("GAME OVER", align="center", font=('Courier', 22, 'normal'))
