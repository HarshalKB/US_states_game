import turtle
import pandas as pd

data = pd.read_csv('/home/harshal/Harshal/us-states-game-start/50_states.csv')
data['state'] = data['state'].str.lower()
all_state = data.state.to_list()

screen = turtle.Screen()
screen.title('U.S. States Game')
image = '/home/harshal/Harshal/us-states-game-start/blank_states_img.gif'
screen.addshape(image)
turtle.shape(image)

guessed_state = []
while len(guessed_state) < 50:
    answer_state = screen.textinput(title=f'{len(guessed_state)}/50 state', prompt="What's another state name?")

    if answer_state.lower() == 'exit':
        missing_state = []
        for state in all_state:
            if state not in guessed_state:
                missing_state.append(state)
        new_data = pd.DataFrame(missing_state)
        new_data.to_csv('/home/harshal/Harshal/us-states-game-start/Missing_States.csv')
        break
    if answer_state in all_state and answer_state not in guessed_state:
        guessed_state.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        xcor = state_data.x.iloc[0]
        ycor = state_data.y.iloc[0]
        t.goto(xcor, ycor)
        # t.write(state_data.state.iloc[0].capitalize())
        t.write(answer_state.capitalize())

