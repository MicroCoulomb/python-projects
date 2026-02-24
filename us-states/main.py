from turtle import Turtle, Screen
import pandas

screen = Screen()
screen.title("U.S. States Game")
screen.bgpic("blank_states_img.gif")
screen.setup(width=750, height=500)

us_data = pandas.read_csv("50_states.csv")
all_states = us_data.state.to_list()

guessed_states = []
total_states = 50

while len(guessed_states) < total_states:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/{total_states} States Correct", prompt="Name a U.S. state:").title()
    if answer_state == "Exit":
        missing_states = [state for state in all_states if state not in guessed_states]
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break

    if answer_state in all_states:
        state_name = Turtle()
        state_name.hideturtle()
        state_name.penup()
        state_xcor = us_data[us_data.state == answer_state].x.item()
        # print(state_xcor)
        state_ycor = us_data[us_data.state == answer_state].y.item()
        state_name.goto(state_xcor, state_ycor)
        state_name.write(answer_state, align="center", font=("Arial", 6, "bold"))
        guessed_states.append(answer_state)


screen.mainloop()