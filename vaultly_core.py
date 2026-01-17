from flask import Flask, render_template, request, session, redirect
import random

app = Flask(__name__)
app.secret_key = 'vaultly_secret'

@app.route('/')
def home():
    if 'balance' not in session:
        session['balance'] = 1000  # Starting cash
    return render_template('index.html', balance=session['balance'])

@app.route('/gamble', methods=['POST'])
def gamble():
    bet = int(request.form.get('bet', 0))
    if 0 < bet <= session['balance']:
        if random.choice([True, False]):
            session['balance'] += bet
            msg = f"WINNER! You gained ${bet}!"
        else:
            session['balance'] -= bet
            msg = f"BUST! You lost ${bet}."
    else:
        msg = "Invalid bet!"
    return render_template('index.html', balance=session['balance'], message=msg)

if __name__ == '__main__':
    app.run(debug=True)
    
