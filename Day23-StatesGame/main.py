import turtle
import pandas

screen = turtle.Screen()
screen.title("Indian states game")

img = "IndianMap.gif"
screen.addshape(img)
data = pandas.read_csv("29_states.csv")
state_list = data["state"].to_list()


map_turtle = turtle.Turtle()
map_turtle.shape(img)
map_turtle.penup()
map_turtle.goto(0, 0)

guess_state = []

while len(guess_state) < 29:
    users_input_state = screen.textinput(title=f"{len(guess_state)}/29 Correct State", prompt="Enter next state name").title()
    if users_input_state == "Exit":
        break
    if users_input_state in state_list:
        guess_state.append(users_input_state)
        t = turtle.Turtle()
        t.penup()
        state_data = data[data.state == users_input_state]
        t.goto(state_data.x.item(),state_data.y.item())
        t.write(users_input_state)


remaining_state = []
for state in state_list:
    if state in guess_state:
        continue
    else:
        remaining_state.append(state)

missing_state_name = pandas.DataFrame(remaining_state)
missing_state_name.to_csv("states_to_learn.csv")

screen.exitonclick()

