from quiz_brain import QuizBrain
from question_model import Question
from data import question_data

question_bank = []

for i in question_data:
    question = Question(i['text'], i['answer'])
    question_bank.append(question)


quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()


print("********************************************************")
print("You've complated the quiz!")
print(f"Your score is {quiz.score}/{quiz.question_number}")
print("********************************************************")
