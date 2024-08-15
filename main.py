from unittest.mock import sentinel
from flask import Flask, render_template, request

from qa_bot import get_answer


app = Flask(__name__)

# Home route to display the web interface
@app.route('/')
def home():
    return render_template('index.html')

# Route to handle the QA functionality
@app.route('/get_answer', methods=['POST'])
def get_answer_route():
    if request.method == 'POST':
        question = request.form['question']
        answer = get_answer(question, sentinel)
        return render_template('index.html', question=question, answer=answer)

if __name__ == "__main__":
    app.run(debug=True)
