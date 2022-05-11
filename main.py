import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")

image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

# Get the x and y coordinate on any point.
# def get_mouse_click_coor(x, y):
#     print(x, y)
#
# turtle.onscreenclick(get_mouse_click_coor)
#
# turtle.mainloop()
data = pandas.read_csv("50_states.csv")
states = data.state.to_list()

correct_states = []

while len(correct_states) < 50:
    answer_state = screen.textinput(title=f"{len(correct_states)}/50 Guess the state", prompt="What's another state's name?")
    if answer_state.lower() == 'exit':
        states_to_learn = [state for state in states if state not in correct_states]
        learn_states = pandas.DataFrame(states_to_learn)
        learn_states.to_csv("states_to_learn.csv")
        break
    guess = answer_state.title()
    if guess in states:
        correct_states.append(guess)
        position_x = int(data.x[data.state == guess])
        position_y = int(data.y[data.state == guess])
        position = (position_x, position_y)
        state_name = turtle.Turtle()
        state_name.hideturtle()
        state_name.pu()
        state_name.goto(position)
        state_name.write(guess, align="center", font=("Arial", 10, "normal"))


