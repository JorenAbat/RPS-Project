from flask import Flask, render_template, request
import random

# Configure application
app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/play', methods=['POST'])
def play():
    choices = ['Rock', 'Paper', 'Scissors']
    user_choice = request.form['choice']
    computer_choice = random.choice(choices)

    user_img = "images/" + user_choice.lower() + ".png"
    computer_img = "images/" + computer_choice.lower() + ".png"

    # If no option is chosen
    if user_choice == 'None':
        return render_template('missing.html', selected=False)

    # Results
    if user_choice == computer_choice:
        result = 'It\'s a tie!'
        flavour_text = 'No one wins!'
        bg_colour = 'lightgoldenrodyellow'
    elif (user_choice == 'Rock' and computer_choice == 'Scissors') or \
         (user_choice == 'Paper' and computer_choice == 'Rock') or \
         (user_choice == 'Scissors' and computer_choice == 'Paper'):
        result = 'YOU WIN'
        bg_colour = 'lightgreen'
    else:
        result = 'YOU LOSE'
        bg_colour = 'indianred'

    # Flavour Text
    if (user_choice == 'Rock' and computer_choice == 'Paper'):
        flavour_text = 'You got covered!'
    elif (user_choice == 'Paper' and computer_choice == 'Scissors'):
        flavour_text = 'You got cut!'
    elif (user_choice == 'Scissors' and computer_choice == 'Rock'):
        flavour_text = 'You got crushed!'
    elif (user_choice == 'Rock' and computer_choice == 'Scissors'):
        flavour_text = 'You crushed them!'
    elif (user_choice == 'Paper' and computer_choice == 'Rock'):
        flavour_text = 'You covered them up!'
    elif (user_choice == 'Scissors' and computer_choice == 'Paper'):
        flavour_text = 'You cut them to shreds!'

    return render_template('result.html', user_choice=user_choice, computer_choice=computer_choice, result=result,
                           user_img=user_img, computer_img=computer_img, flavour_text=flavour_text, bg_colour=bg_colour)
