from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        
        self.level = 1
        self.penup()
        self.hideturtle()
        self.goto(-200,250)
        self.update_score()
        

    def score_increment(self):
        self.level+=1
        self.update_score()


    def update_score(self):
        self.clear()
        self.write(f"level: {self.level}",align="center",font=("courier",30,"normal"))
    
    def game_over(self):
        self.goto(0,0)
        self.write(f"GAME OVER",align="center",font=("courier",30,"normal"))
    




    '''
    note: align

    "center" : object cha madhyabindu tya position war rahil
    "left" : position warun start hoil. means object cha left madhun tya position war rahil
    '''
