from flask import Flask, render_template, session, request, redirect,flash
app = Flask(__name__)
app.secret_key = "ThisisSecret"

import random


@app.before_first_request
def random_number():
	session['winning_number'] = random.randrange(0,101)

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/compare', methods=['POST'])
def compare_numbers():
	session['user_number'] = int(request.form['userNumber'])
	if session['winning_number'] > session['user_number']: 
		flash("Sorry to low, try again",changecolor=red)
		return redirect('/')

	elif session['winning_number'] < session['user_number']:
		flash("Sorry to high, try again")
		return redirect('/')

	else:
		flash("Congrats you guessed correctly!!!")
		return redirect('/')

@app.route('/reset')
def reset ():
	session['winning_number'] = random.randrange(0,101)
	return redirect ('/')


app.run(debug=True)