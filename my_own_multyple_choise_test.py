from my_own_questions import Question
questions_prompts = [
    "When do you get up?\n(a) At 5 a.m.\n(b) At 7 a.m.\n(c) At 9 a.m.\n\n",
    "When do you go to sleep?\n(a) At 9 p.m.\n(b) At 11 p.m.\n(c) At 1 a.m.\n\n",
    "What kind of programing do you?\n(a) Web-development\n(b) Software engineering\n(c) Data Science\n\n"
]

questions = [
    Question(questions_prompts[0], "b"),
    Question(questions_prompts[1], "b"),
    Question(questions_prompts[2], "c")
]

def run_test(questions):
    score = 0
    for question in questions:
        answer = input(question.prompt)
        if answer == question.answer:
            score +=1
    print("You got " + str(score) + "/" + str(len(questions)) + " correct")

run_test(questions)