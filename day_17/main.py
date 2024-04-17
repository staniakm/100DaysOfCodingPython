from day_17.quiz_brain import QuizBrain

quiz = QuizBrain()

playing = True
while playing:
    a_continue = input("Do you want to continue?")
    if a_continue == "no":
        playing = False
    else:
        quiz.next_question()
        quiz.answer_question(input("Your answer:(True/False)"))
