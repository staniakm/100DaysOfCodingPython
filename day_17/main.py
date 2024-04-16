from question_model import Question
from data import question_data

bank = []

for d in question_data:
    bank.append(Question(d['text'], bool(d['answer'])))


print(bank)