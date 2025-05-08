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
    "img":"/static/images/NA.png",
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
    "img":"/static/images/HA_serum.png",
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
    "options": ["Water Cleanser", "Oil Cleanser"],
    "correct": 0,
    "images": [
            {"src": "water_cleanser.png", "caption": "Water Cleanser"},
            {"src": "oil_cleanser.png", "caption": "Oil Cleanser"},
        ]
    },{
    "id":1,
    "question": "Pick a toner that best suits Amira",
    "options": ["Rose Water Toner", "Green Tea Toner", "Witchhazel Toner"],
    "correct": 2,
    "images": [
            {"src": "rosewater.png", "caption": "Rose Toner"},
            {"src": "green_tea_toner.png", "caption": "Green Tea Toner"},
            {"src": "witch_hazel.png", "caption": "Witchhazel Toner"},
        ]
    },{
    "id":2,
    "question": "Pick a serum that best suits Amira",
    "options": ["Hyalauronic Acid Serum", "Retinol", "Vitamin C Serum"],
    "correct": 0,
    "images": [
            {"src": "HA_serum.png", "caption": "Hyalauronic Acid Serum"},
            {"src": "retinol.png", "caption": "Retinol"},
            {"src": "vit_c.png", "caption": "Vitamin C Serum"},
        ]
    },{
    "id":3,
    "question": "Pick an eye cream that best suits Amira",
    "options": ["Retinol Eye Cream", "Caffeine Eye Cream", "Green Tea Eye Cream"],
    "correct": 1,
    "images": [
            {"src": "retinol_eye.png", "caption": "Retinol Eye Cream"},
            {"src": "caff_eye.png", "caption": "Caffeine Eye Cream"},
            {"src": "green_eye.png", "caption": "Green Tea Eye Cream"},
        ]
    },{
    "id":4,
    "question": "Pick a moisturizer that best suits Amira",
    "options": ["Niacinamide Moisturizer", "Lightweight Gel Moisturizer", "Hyalauronic Acid Moisturizer"],
    "correct": 1,
    "images": [
            {"src": "NA_cream.png", "caption": "Niacinamide Moisturizer"},
            {"src": "glycerin.png", "caption": "Lightweight Gel Moisturizer"},
            {"src": "HA_cream.png", "caption": "Hyalauronic Acid Moisturizer"},
        ]
    },{
    "id":5,
    "question": "Pick a sunscreen that best suits Amira",
    "options": ["Mineral Sunscreen", "Chemical Sunscreen"],
    "correct": 0,
    "images": [
            {"src": "mineral_sun.png", "caption": "Mineral Sunscreen"},
            {"src": "chemical_sun.png", "caption": "Chemical Sunscreen"},
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