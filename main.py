import turtle as t
import pandas as pd

screen = t.Screen()
screen.title("US state game")
image = "blank_states_img.gif"
t.addshape(image)
t.shape(image)

data = pd.read_csv("50_states.csv")

state_list = data.state.to_list()
guessed_state = []
final_list = []
while len(guessed_state) < 50:
    answer = screen.textinput(title=f"{len(guessed_state)}/50 State Correct",
                              prompt="What's another states name?").title()

    if answer == "Exit":
        for state in state_list:
            if state not in guessed_state:
                final_list.append(state)

        df = pd.DataFrame(final_list)
        df.to_csv("remaining.csv")
        break
    if answer in state_list:
        guessed_state.append(answer)
        tim = t.Turtle()
        answer_row = data[data.state == answer]
        x = int(answer_row.x)
        y = int(answer_row.y)
        tim.hideturtle()
        tim.penup()
        tim.goto(x, y)
        tim.write(answer)
