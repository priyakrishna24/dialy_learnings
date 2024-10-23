from question_model import Question
from data import question_data 
from quiz_brain import QuizBrain

question_bank=[]

for question in question_data:
    question_text=question["text"]
    question_answer=question["answer"]
    question=Question(q_text=question_text,q_answer=question_answer)
    question_bank.append(question)
# print(question_bank)

quiz=QuizBrain(question_bank)

while quiz.still_has_questions():# if still has questions in list
    quiz.next_question()

print("You have completed the quiz!")
print(f"Your final score is:{quiz.score}/{quiz.question_number}")