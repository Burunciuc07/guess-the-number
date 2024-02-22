from flask import Flask, render_template, request
import random

app = Flask(__name__)

# Generate a random number when the application starts
secret_number = random.randint(1, 100)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/play', methods=['POST', 'GET'])
def play():
    global secret_number  # Use the global variable to store the secret number
    
    if request.method == 'POST':
        # Get the player's guess from the form
        player_guess = int(request.form['guess'])

        # Check if the guess is correct
        if player_guess == secret_number:
            return render_template('win.html', secret_number=secret_number)
        elif player_guess < secret_number:
            message = "Try again. The number is higher."
        else:
            message = "Try again. The number is lower."
        
        return render_template('play.html', message=message)

    return render_template('play.html')

if __name__ == '__main__':
    app.run(debug=True)
