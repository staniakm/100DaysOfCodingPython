from day_17.data import question_data
from day_17.question_model import Question


class QuizBrain:
    question_number = 0
    question_list = []
    points = 0

    def __init__(self):
        for d in question_data:
            self.question_list.append(Question(d['text'], d['answer']))

    def next_question(self):
        question = self.question_list[self.question_number]
        print(question.question)

    def answer_question(self, answer):
        question = self.question_list[self.question_number]
        print(f"Answer is {question.answer}")
        result = answer == question.answer
        if result:
            self.points += 1
        print(f"Points {self.points}/{self.question_number + 1}")
        self.question_number += 1
