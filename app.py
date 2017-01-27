from flask import Flask, render_template, url_for
from models.compliment import Compliment
app = Flask(__name__)

@app.route('/', methods = ['GET'])
def index():
    return render_template('index.html', title="Flask is just so so", details="Something else", compliments=compliments)

@app.route('/about/')
def about():
    return "blah blah blah"

if __name__ == '__main__':
    app.run(debug = True)
