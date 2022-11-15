from boggle import Boggle
from flask import Flask, render_template, redirect, request, flash, session, jsonify
from flask_debugtoolbar import DebugToolbarExtension


app = Flask(__name__)
app.config['SECRET_KEY'] = 'cats'
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

boggle_game = Boggle()

@app.route("/")
def boggle_home():

    user_visits = session.get("visits", 0) 

    game = boggle_game.make_board()
    session["game_board"] = game
    games_played = session.get('visits', 0)
    highscore = session.get("highscore", 0)

    return render_template("home.html", game = game, highscore = highscore)

@app.route("/guess", methods =["POST"])
def handle_guess():
    current_board = session["game_board"]
    highscore = session.get("highscore", 0)

    user_guess = request.form["userGuess"].lower()
    app.logger.info(user_guess)
    app.logger.info(highscore)

    # score = request.json["score"]
    # session['highscore'] = max(score, highscore)

    guess_result = jsonify(result = boggle_game.check_valid_word(current_board, user_guess))
    
    return guess_result
    

    
    


