from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

question_bank = []

for questiom in question_data:
    question_bank.append(Question(questiom["text"], questiom["answer"]))

quiz = QuizBrain(question_bank)
while quiz.still_has_question():
    quiz.next_question()

print("You've completed the quiz")
print(f"Your final score was: {quiz.score}/{len(quiz.question_numbers)}")