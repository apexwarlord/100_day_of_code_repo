import turtle
import pandas

from text_turtle import TextTurtle

# Screen settings
screen = turtle.Screen()
screen.setup(width=730, height=490)
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)

turtle.shape(image)

# Import turtle to write on map
text_turtle = TextTurtle()

# Pandas to manage CSV
states_data = pandas.read_csv('50_states.csv')
all_states = states_data["state"].to_list()
# main loop
states_guessed = []
while len(states_guessed) < 50:
    answer = turtle.textinput(f"{len(states_guessed)}/50 States Guessed", "Name a state!")
    if answer.strip().title() in all_states and answer.title() not in states_guessed:
        states_guessed.append(answer.title())
        text_turtle.write_text(answer.title(),
                               int(states_data[states_data.state == answer.title()].x.item()),
                               int(states_data[states_data.state == answer.title()].y.item()))

    elif answer.strip().lower() == 'exit':
        states_missed = [state for state in all_states if state not in states_guessed]
        # print(len(states_missed))
        # for state in states_guessed:
        #     all_states.pop(all_states.index(state))
        if len(states_missed) > 0:
            string_for_txt = "Missed States:"
            with open('states_to_learn.txt', 'w') as f:
                for state in states_missed:
                    string_for_txt += f'\n{state}'
                f.write(string_for_txt)

            new_data = pandas.DataFrame(states_missed)
            new_data.to_csv('states_to_learn.csv')

        break
