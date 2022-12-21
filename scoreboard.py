from turtle import Turtle

FONT = ("Courier", 20, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.lvl = 1
        self.hideturtle()
        self.goto(-290, 260)
        self.write(f"Level: {self.lvl}", align="left", font=FONT)

    def increase_score(self):
        self.clear()
        self.lvl += 1
        self.write(f"Level: {self.lvl}", align="left", font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align="center", font=FONT)