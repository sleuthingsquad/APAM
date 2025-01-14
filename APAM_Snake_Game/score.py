from turtle import Turtle


class score_board(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.score = 0
        self.write(f"Score: {self.score}", move=False, align="center", font=('Courier', 12, 'normal'))

    def increase_score(self):
        self.score += 1
        self.clear()
        self.write(f"Score: {self.score}", move=False, align="center", font=('Courier', 12, 'normal'))

    def write_game_over(self):
        self.goto(0, 0)
        self.write("Game Over!", move=False, align="center", font=('Courier', 15, 'normal'))
