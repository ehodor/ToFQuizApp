#Created by Emma Hodor
from question_model import Question
from quiz_brain import QuizBrain
from ui import UI
import requests
question_bank = []

response = requests.get(url="https://opentdb.com/api.php?amount=10&type=boolean")
response.raise_for_status()
question_data = response.json()["results"]

for i in question_data:
    new_q = Question(i['question'], i['correct_answer'])
    question_bank.append(new_q)

quiz = QuizBrain(question_bank)
ui = UI(quiz)

'''while quiz.still_q():
    quiz.next_q()'''

print("You've completed the quiz!")
print(f"Your final score was: {quiz.score}/{len(question_bank)}")
