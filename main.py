import turtle
import pandas

FONT = ("Arial", 10, "normal")

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

pen = turtle.Turtle()
pen.hideturtle()
pen.penup()

states_data = pandas.read_csv("50_states.csv")
correct_guesses = []
states_list = states_data.state.to_list()

while len(correct_guesses) != 50:
    if len(correct_guesses) == 0:
        answer_state = screen.textinput(title="Guess the State", prompt="What's a state's name?").title()
    else:
        answer_state = screen.textinput(title=f"{len(correct_guesses)}/50 States Correct",
                                        prompt="What's another state's name?").title()
    if answer_state == "Exit":
        missing_states = [state for state in states_list if state not in correct_guesses]
        data_missed_states = pandas.DataFrame(missing_states)
        data_missed_states.to_csv("missed_states.csv")
        break
    data = states_data[states_data.state == answer_state]
    if len(data) == 1 and (answer_state not in correct_guesses):
        x_coor = int(data.x)
        y_coor = int(data.y)
        pen.goto(x_coor, y_coor)
        pen.write(answer_state, align="center", font=FONT)
        correct_guesses.append(answer_state)


screen.exitonclick()
