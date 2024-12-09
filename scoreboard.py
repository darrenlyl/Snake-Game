from turtle import Turtle

ALIGHTNMENT = "center"
FONT = ("Arial", 24, "normal")

class Scoreboard(Turtle):
    
    def __init__(self):
        super().__init__()
        self.score = 0 
        self.color("white")
        self.penup()
        self.goto(0,260)
        self.write(f"Score: {self.score}", align=ALIGHTNMENT, font=FONT)
        self.hideturtle()
        
    
    def update_scoreboard(self):
        self.write(f"Score: {self.score}", align="center", font=("Arial", 24, "normal"))

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()

    def game_over(self):
        self.color("white")
        self.goto(0,0)
        self.write("GAME OVER", align = ALIGHTNMENT, font = FONT)
        