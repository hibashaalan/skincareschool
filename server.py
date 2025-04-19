from flask import Flask, render_template

app = Flask(__name__, static_folder='.')

@app.route('/')
def serve_home():
    return render_template('home.html')

@app.route('/skintype')
def serve_skintype():
    return render_template('skintype.html')

@app.route('/foundation')
def serve_foundation():
    return render_template('foundation.html')


if __name__ == '__main__':
    app.run(debug=True)