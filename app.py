from flask import Flask, render_template, request, redirect, url_for
import json
import requests
import random
import re

app = Flask(__name__)

url = 'https://app.oxyapi.uk/v1/chat/completions'
headers = {
    'Content-Type': 'application/json',
    'Authorization': 'Bearer oxy-4afVoiDieVOKDjuRotiIm1XtZrD72fM77vF1vxpdQ3UKG'
}

with open("quiz.json", "r") as f:
    quiz_data = json.load(f)
    f.close()

#AI answer checker
def check_answer(question_msg, question_answer, student_answer):

    with open("data/prompt.txt", "r", encoding="utf-8") as f_prompt:
        prompt = f_prompt.read()

    combined = f'\nQuestion:{question_msg} Answer: {question_answer}\nStudent answer: {student_answer}'

    d_prompt = f"{prompt}\n\n{combined}\nAI:"

    data = {
        "model": "gpt-3.5-turbo",
        "messages":[{"role": "system", "content": prompt},
                    {"role": "user", "content": combined},],
        "temperature": 0.7
    }

    while True:    
        try:
            response = requests.post(url, json=data, headers=headers)
            response = response.json()
            return False if response["choices"][0]["message"]["content"] == "False" else True
        except:
            print("failed again :/")
            continue

@app.route('/')
def index():
    return render_template('index.html', books=quiz_data.keys())

@app.route('/select_lesson/<book_choice>', methods=['GET', 'POST'])
def select_lesson(book_choice):
    if request.method == 'POST':
        lesson_choice = request.form['lesson_choice']
        return redirect(url_for('quiz', book_choice=book_choice, lesson_choice=lesson_choice))

    return render_template('lessons.html', lessons=quiz_data[book_choice].keys(), book=book_choice)

@app.route('/quiz', methods=['POST'])
def quiz():
    book_choice = request.form.get("book")
    lesson_choice = request.form.getlist("lesson")
    num_q = int(request.form.get("num_q"))
    questions = []
    for l in lesson_choice:
        for q_name, q in quiz_data[book_choice][l].items():
            questions.append(tuple([book_choice, l, q_name, q["question_msg"]]))
    questions_list = get_questions(questions, num_q)
    return render_template('quiz.html', questions=questions_list, book=book_choice)

@app.route('/result', methods=['GET', 'POST'])
def result():
    book_choice = request.form.get("book")
    result = []
    for key, val in request.form.items():
        if key.startswith(book_choice):
            lesson, q_num = key.split(" ")[1:]
            user_ans = val
            ans = quiz_data[book_choice][lesson][q_num]["answer_msg"]
            question = quiz_data[book_choice][lesson][q_num]["question_msg"]
            is_correct = check_answer(question, ans, user_ans)
            result.append(tuple([question, user_ans, ans, is_correct]))
    percentage = round(len([i for i in result if i[3]])/len(result)*100, 2)
    
    return render_template('results.html', result=result, percentage=percentage)

def get_questions(questions, amount):
    return random.sample(questions, k=min(amount, len(questions)))

if __name__ == '__main__':
    app.run(debug=True, port=17432)