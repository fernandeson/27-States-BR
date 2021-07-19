import turtle
import pandas as pd

screen = turtle.Screen()
screen.title("BR States Game")

# Add background image:
image = "mapa-brasil.gif"
screen.addshape(image)
turtle.shape(image)
guessed_states = []
df = pd.read_csv("27_states_br.csv")
state_names = df["name"].to_list()

while len(guessed_states) < len(state_names):
    user_answer = screen.textinput(title=f"{len(guessed_states)}/{len(state_names)} right states",
                                   prompt="Enter the name of a state from BR:").lower()
    if user_answer == "exit":
        states_to_learn = [state for state in state_names if state not in guessed_states]
        df_states_to_learn = pd.DataFrame(states_to_learn).to_csv("states_to_learn.csv", header=["missed_states"])
        break
    for state in state_names:
        if user_answer == state:
            guessed_states.append(state)
            index = state_names.index(state)
            state_x = df.loc[index, "x_value"]
            state_y = df.loc[index, "y_value"]
            tom = turtle.Turtle()
            tom.hideturtle()
            tom.penup()
            tom.goto(state_x, state_y)
            tom.write(state.title(), font=("Ranchers", 10, "normal"))
screen.exitonclick()
