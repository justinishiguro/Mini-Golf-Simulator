import re
from flask import Flask, render_template, request, jsonify, redirect, url_for
from flask_cors import CORS
import json

app = Flask(__name__)

# Enable Cross-Origin Resource Sharing (CORS) for requests from http://cpen291-2.ece.ubc.ca/
# Allowing requests from the specified origin to access resources on the server.
# This is useful when the client and server are hosted on different domains.
CORS(app, resources={r"/*": {"origins": "http://cpen291-2.ece.ubc.ca/"}})

# Render the start page when /start is accessed
@app.route("/start")
def homepage():
    return render_template("startPage.html")

# Render the start page when the root is accessed
@app.route("/")
def homepage2():
    return render_template("startPage.html")

# Render the game page when /game is accessed
@app.route("/game")
def gamepage():
    return render_template("gamePage.html")

# Reset the balls and render the end page when /end is accessed
@app.route("/end")
def endpage():
    global ball1, ball2, ball3, ball4, ball5, ball6
    ball1 = False
    ball2 = False
    ball3 = False
    ball4 = False
    ball5 = False
    ball6 = False
    return render_template("endPage.html")

# Handle requests made to /hole1
@app.route('/hole1', methods=['POST', 'GET'])
def handle_request():
    global ball1, ball2, ball3, ball4, ball5, ball6

    # Parse JSON data sent in the request body
    try:
        data = request.data.decode('utf-8')
        print(data)

        # Update ball variables based on the received data
        if "One True" in data:
            ball1 = True
        if "Two True" in data:
            ball2 = True
        if "Three True" in data:
            ball3 = True
        if "Four True" in data:
            ball4 = True
        if "Five True" in data:
            ball5 = True
        if "Six True" in data:
            ball6 = True 

        # Construct ball object from the updated ball variables
        ball_obj = {'ball1': ball1, 'ball2': ball2, 'ball3': ball3, 'ball4': ball4, 'ball5': ball5, 'ball6': ball6}

        # Send the ball object as a JSON response
        return jsonify(ball_obj)

    except Exception as e:
        # Handle other errors
        return jsonify({'error': str(e)})

# Reset the ball variables and redirect to the game page when /reset is accessed
@app.route('/reset')
def reset_balls():
    global ball1, ball2, ball3, ball4, ball5, ball6
    ball1 = False
    ball2 = False
    ball3 = False
    ball4 = False
    ball5 = False
    ball6 = False
    return redirect('http://cpen291-2.ece.ubc.ca/game')


# Initialize the ball variables to False and run the Flask app
if __name__ == "__main__":
    ball1 = False
    ball2 = False
    ball3 = False
    ball4 = False
    ball5 = False
    ball6 = False
    app.run(host = "0.0.0.0", debug=True)
