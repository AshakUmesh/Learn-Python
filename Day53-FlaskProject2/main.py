from flask import Flask
import random
LOW_GIF = "https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif"
HIGH_GIF = "https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif"
CORRECT_GIF = "https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif"
app = Flask(__name__)


@app.route('/<int:choice>')
def higher_lower(choice):
    num = random.randint(0, 10)
    print(f"Generated number: {num}")  # server-side log

    if choice < num:
        message = f"You guessed {choice}. Too low!"
        gif_url = LOW_GIF
    elif choice > num:
        message = f"You guessed {choice}. Too high!"
        gif_url = HIGH_GIF
    else:
        message = f"🎉 Correct! It was {num}."
        gif_url = CORRECT_GIF  # celebrate on correct guess

    # Return HTML with dynamic message and GIF
    return f'''
        <h1 style="font-weight:bold">{message}</h1>
        <img src="{gif_url}">
        '''


@app.route('/')
def home():
    return '''
    <h1 style="font-weight:bold">Guess a number between 0 and 10</h1>
    <p>Use URL like /5 to guess "5"</p>
    <img src="https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif">
    '''

if __name__ == "__main__":
    app.run(debug=True)
