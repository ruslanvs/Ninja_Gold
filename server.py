import random
from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = "MyNinjaGoldSession"

@app.route( "/" )
def front_page():
    if "goldBalance" not in session:
        session["goldBalance"] = 0
    if "message" not in session:
        session["message"] = ""

    return render_template( "index.html", gold_balance = session["goldBalance"], activities = session["message"] )

@app.route( "/process_money", methods = ["POST"] )
def process_money():
    print "process money route"
    if request.form['place'] == "farm":
        attempt_outcome = random.randrange( 10, 21 )
        attempt_message = '<p class="green">Earned ' + str( attempt_outcome ) + ' golds from the farm!</p>'
    elif request.form['place'] == "cave":
        attempt_outcome = random.randrange( 5, 11 )
        attempt_message = '<p class="green">Earned ' + str( attempt_outcome ) + ' golds from the cave!</p>'
    elif request.form['place'] == "house":
        attempt_outcome = random.randrange( 2, 6 )
        attempt_message = '<p class="green">Earned ' + str( attempt_outcome ) + ' golds from the house!</p>'
    elif request.form['place'] == "casino":
        attempt_outcome = random.randrange( -50, 51 )
        if attempt_outcome > 0:
            attempt_message = '<p class="green">Went to the casino and won ' + str( attempt_outcome ) + ' golds!</p>'
        elif attempt_outcome < 0:
            attempt_message = '<p class="red">Went to the casino and lost ' + str( attempt_outcome ) + ' golds... Ouch..</p>'
        elif attempt_outcome == 0:
            attempt_message = '<p class="green">Went to the casino and broke even!</p>'

    session["goldBalance"] += attempt_outcome
    session["message"] = attempt_message + session["message"]

    return redirect( "/" )

@app.route( "/reset", methods = ["POST"] )
def reset():
    session.clear()
    return redirect( "/" )

app.run( debug = True )