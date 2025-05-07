from flask import Flask
from flask import render_template
from flask import Response, request, jsonify
app = Flask(__name__)


quiz1arr = [
    {
    "id":"0",
    "img": "/static/images/combo_skin.png",
    "alt": "combination skin",
    "desc": "1. Choose a toner for combination skin:",
    "feeback":"",
    "correct":0
}, {
    "id":"1",
    "img": "/static/images/rosewater.png",
    "alt": "rosewater toner",
    "desc": "Rosewater toner",
    "feedback":"Correct! Rosewater is a great ingredient for combination skin because "
    "it  balances dry and oily areas.",
    "correct":1
}, {
    "id":"2",
    "img":"/static/images/aloe.png",
    "alt":"aloe toner",
    "desc":"Aloe toner",
    "feedback":"Incorrect! Aloe is a better ingredient for dry skin.",
    "correct":0
}, {
    "id":"3",
    "img":"/static/images/witch_hazel.png",
    "alt":"witch hazel toner",
    "desc":"Witch hazel toner",
    "feedback":"Incorrect! Witch hazel is a better ingredient for oily skin.",
    "correct":0
}, {
    "id":"4",
    "img":"/static/images/normal_skin.png",
    "alt":"normal skin",
    "desc":"2. Choose a serum for brightening:",
    "feedback":"",
    "correct":0
}, {
    "id":"5",
    "img":"/static/images/serum_nia.png",
    "alt":"niacinamide serum",
    "desc":"Niacinamide serum",
    "feedback":"Incorrect! Niacinamide is a better ingredient for acne concerns.",
    "correct":0
}, {
    "id":"6",
    "img":"/static/images/vit_c.png",
    "alt":"vitamin c serum",
    "desc":"Vitamin C serum",
    "feedback":"Correct! Vitamin C is a great ingredient for any brightening concerns.",
    "correct":1
}, {
    "id":"7",
    "img":"/static/images/serum_ha.png",
    "alt":"hyaluronic acid serum",
    "desc":"Hyaluronic acid serum",
    "feedback":"Incorrect! Hyaluronic acid is a better ingredient for hydration concerns",
    "correct":0
}, 
]

quiz1answers = [ 
    {
        "id":"0",
        "q1":"",
        "q2":"",
        "score":0,
    },
]

quiz2_questions = [
    {
    "id":0,
    "question": "Pick a cleanser that best suits Amira",
    "options": ["Gel-based with salicylic acid", "cleanser 2", "cleanser 2"],
    "correct": 0,
    "images": [
            {"src": "cleanser.png", "caption": "Cleanser 1"},
            {"src": "cleanser.png", "caption": "Cleanser 2"},
            {"src": "cleanser.png", "caption": "Cleanser 3"},
        ]
    },{
    "id":1,
    "question": "Pick a toner that best suits Amira",
    "options": ["toner 1", "toner 2", "Witch hazel to balance oil"],
    "correct": 2,
    "images": [
            {"src": "toner_rose.png", "caption": "Toner 1"},
            {"src": "toner_rose.png", "caption": "Toner 2"},
            {"src": "toner_rose.png", "caption": "Toner 3"},
        ]
    },{
    "id":2,
    "question": "Pick a serum that best suits Amira",
    "options": ["serum 1", "serum 2", "serum 3"],
    "correct": 0,
    "images": [
            {"src": "serum_nia.png", "caption": "Serum 1"},
            {"src": "serum_nia.png", "caption": "Serum 2"},
            {"src": "serum_nia.png", "caption": "Serum 3"},
        ]
    },{
    "id":3,
    "question": "Pick an eye cream that best suits Amira",
    "options": ["cream 1", "cream 2", "cream 3"],
    "correct": 1,
    "images": [
            {"src": "eye_cream.png", "caption": "Eye cream 1"},
            {"src": "eye_cream.png", "caption": "Eye cream 2"},
            {"src": "eye_cream.png", "caption": "Eye cream 3"},
        ]
    },{
    "id":4,
    "question": "Pick a moisturizer that best suits Amira",
    "options": ["moisturizer 1", "moisturizer 2", "moisturizer 3"],
    "correct": 1,
    "images": [
            {"src": "moisturizer.png", "caption": "Moisturizer 1"},
            {"src": "moisturizer.png", "caption": "Moisturizer 2"},
            {"src": "moisturizer.png", "caption": "Moisturizer 3"},
        ]
    },{
    "id":5,
    "question": "Pick a sunscreen that best suits Amira",
    "options": ["sunscreen 1", "sunscreen 2", "sunscreen 3"],
    "correct": 1,
    "images": [
            {"src": "sunscreen.png", "caption": "Sunscreen 1"},
            {"src": "sunscreen.png", "caption": "Sunscreen 2"},
            {"src": "sunscreen.png", "caption": "Sunscreen 3"},
        ]
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

@app.route('/quiz1_answers', methods=["GET", "POST"])
def quiz1_answers():
    answers = request.get_json()
    answers["id"] = len(quiz1answers)
    quiz1answers.append(answers)
    return jsonify(answer = answers)

@app.route("/quiz2")
def serve_quiz2():
    return render_template("quiz2.html", questions=quiz2_questions)

@app.route("/case-study")
def case_study():
    return render_template("case_study.html", questions=quiz2_questions)

@app.route("/quiz2/results", methods=["POST"])
def quiz2_results():
    user_answers = request.form.to_dict()
    score = 0
    total = len(quiz2_questions)
    results = []

    for q in quiz2_questions:
        question_id = q["id"]
        user_choice_str = user_answers.get(f"q{question_id}")
        
        if user_choice_str is not None:
            user_choice = int(user_choice_str)
            is_correct = user_choice == q["correct"]
            if is_correct:
                score += 1

            results.append({
                "question": q["question"],
                "is_correct": is_correct,
                "image": q["images"][user_choice],  # image is a dict with 'src' and 'caption'
            })

    return render_template("quiz2_results.html", score=score, total=total, results=results)

if __name__ == '__main__':
    app.run(debug=True, port=5001)