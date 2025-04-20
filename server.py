from flask import Flask
from flask import render_template
from flask import Response, request, jsonify
app = Flask(__name__)

quiz1arr = [
    {
    "id":"0",
    "img": "/static/images/combo_skin.png",
    "alt": "combination skin",
    "desc": "",
    "feeback":"",
    "correct":0
}, {
    "id":"1",
    "img": "/static/images/toner_rose.jpeg",
    "alt": "rosewater toner",
    "desc": "Rosewater toner",
    "feedback":"Correct! Rosewater is a great ingredient for combination skin because "
    "it  balances dry and oily areas.",
    "correct":1
}, {
    "id":"2",
    "img":"/static/images/toner_aloe.jpeg",
    "alt":"aloe toner",
    "desc":"Aloe toner",
    "feedback":"Incorrect! Aloe is a better ingredient for dry skin.",
    "correct":0
}, {
    "id":"3",
    "img":"/static/images/toner_witchhazel.jpeg",
    "alt":"witch hazel toner",
    "desc":"Witch hazel toner",
    "feedback":"Incorrect! Witch hazel is a better ingredient for oily skin.",
    "correct":0
}, 
]

@app.route('/')
def serve_home():
    return render_template('home.html')

@app.route('/skintype')
def serve_skintype():
    return render_template('skintype.html')

@app.route('/foundation')
def serve_foundation():
    return render_template('foundation.html')


@app.route('/quiz1')
def quiz1():
    return render_template('quiz1.html')

@app.route('/quiz1_questions')
def quiz1_questions():
    return jsonify(quiz1arr = quiz1arr)

if __name__ == '__main__':
    app.run(debug=True, port=5001)