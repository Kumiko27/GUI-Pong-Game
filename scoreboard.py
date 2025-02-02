from turtle import Turtle

ALIGNMENT = "center"
FONT = ('Courier', 50, 'normal')


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.l_score = 0
        self.r_score = 0
        self.color("white")
        self.penup()
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.goto(-100, 220)
        self.write(str(self.l_score), align=ALIGNMENT, font=FONT)
        self.goto(100, 220)
        self.write(str(self.r_score), align=ALIGNMENT, font=FONT)

    def l_point(self):
        self.l_score += 1
        self.clear()
        self.update_scoreboard()

    def r_point(self):
        self.r_score += 1
        self.clear()
        self.update_scoreboard()
