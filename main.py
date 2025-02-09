import turtle
import pandas as pd

screen = turtle.Screen()
screen.title("U.S. States Game")

#setting the background
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

#getting the CSV file
data = pd.read_csv("50_states.csv")
state_names = data["state"].to_list()

#setting the number of states guessed
states_guessed = []


while len(states_guessed) < 50:
    # getting input
    answer = screen.textinput(title=f"{len(states_guessed)}/50 States Guessed", prompt="Name a state")
    answer = answer.title()

    if answer == "Exit":
        missing_states = []
        for s in state_names:
            if s not in states_guessed:
                missing_states.append(s)
        learning_data = pd.DataFrame(missing_states)
        learning_data.to_csv("States_to_learn.csv")
        break

    if answer in state_names:
        if answer not in states_guessed:
            states_guessed.append(answer)
            t = turtle.Turtle()
            t.hideturtle()
            t.penup()

            row = data[data.state == answer]

            t.goto(row.x.item(), row.y.item())
            t.write(answer)

            #print(len(states_guessed))
    # else:
    #     print("Sorry! That's wrong")


if len(states_guessed) == 50:
    print("Great job! You got all the 50 states!")

screen.exitonclick()
