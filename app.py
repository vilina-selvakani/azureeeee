from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to Flask Web Application!"

@app.route('/about')
def about():
    return "This is my Flask application."

if __name__ == '__main__':
    app.run(debug=True)
