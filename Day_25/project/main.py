import  turtle
import pandas

screen =  turtle.Screen()
screen.title("U.S. states Game")
screen.setup(700,600)

image = "Day_25/project/blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)




data = pandas.read_csv("Day_25/project/states.csv")
states = data.state.to_list()
guessed_states = []

score=0

while(score!=50):

    answer_state = screen.textinput(title=f'{score}/50 States Correct',prompt="What's another states's name?").title()

    if answer_state == "Exit":
        missing_states = [state for state in states if state not in guessed_states ]
        df = pandas.DataFrame(missing_states)
        df.to_csv(('Day_25/project/missing_states.csv'))
        break

    if answer_state in states:
        row = data[data['state']==answer_state]
        x_cor = row.x
        y_cor = row.y
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        t.goto(int(x_cor),int(y_cor))
        t.write(answer_state)
        guessed_states.append(answer_state)


screen.exitonclick()


