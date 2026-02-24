from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
import requests
import html
from ui import QuizInterface

url_param = {
    "amount": 10,
    "category": 15,
    "type": "boolean"
}

r = requests.get('https://opentdb.com/api.php', params=url_param)
data = r.json()

question_bank = []
for item in data["results"]:
    question_text = item["question"]
    question_answer = item["correct_answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)
quiz_ui = QuizInterface(quiz)

# while quiz.still_has_question():
#     quiz.next_question()

# print("\nYou've completed the quiz.")
# print(f"Your final score was: {quiz.score}/{quiz.question_number}")